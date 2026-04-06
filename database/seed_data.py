"""
==========================================
SCRIPT NẠP DỮ LIỆU VÀO SUPABASE
==========================================
Script này đọc file processed_data.csv và nạp vào bảng raw_transactions

Yêu cầu:
1. Cài đặt thư viện: pip install supabase pandas python-dotenv
2. Tạo file .env với SUPABASE_URL và SUPABASE_KEY
3. Chạy: python database/seed_data.py

Hướng dẫn VS Code + PostgreSQL Extension (D2-D5):
--------------------------------
1. Cài Extension PostgreSQL trong VS Code:
   - Mở VS Code → Extensions (Ctrl+Shift+X)
   - Tìm "PostgreSQL" cweijan hoặc "SQLTools"
   - Click Install

2. Kết nối Supabase Database:
   - Mở Command Palette (Ctrl+Shift+P) → PostgreSQL: Add Connection
   - Hoặc dùng SQLTools → Add New Connection → PostgreSQL
   - Nhập thông tin từ Supabase Dashboard:
     + Host: [project-ref].supabase.co
     + Port: 5432
     + Database: postgres
     + User: postgres
     + Password: [your-password]
     + SSL: Required

3. Chạy SQL Schema:
   - Copy nội dung database/schema.sql
   - Paste vào SQL Editor trong VS Code
   - Click Run (F5) hoặc Ctrl+Enter

4. Kiểm tra bảng:
   - Mở PostgreSQL Explorer sidebar
   - Expand connection → schemas → public → tables
   - Right-click table → Select Top 100

5. Chạy seed script:
   - Mở terminal: python database/seed_data.py
   - Kiểm tra kết quả trong Supabase Table Editor
==========================================
"""

import os
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import List, Dict
import time

# Load biến môi trường
load_dotenv()

# ==========================================
# CẤU HÌNH
# ==========================================
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
CSV_PATH = "./data/processed_data.csv"
BATCH_SIZE = 1000  # Số records mỗi batch để tránh timeout


def create_supabase_client() -> Client:
    """Tạo kết nối Supabase client"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError(
            "Thiếu SUPABASE_URL hoặc SUPABASE_KEY. "
            "Vui lòng tạo file .env với nội dung:\n"
            "SUPABASE_URL=https://ebbtgbisetdcxojimpoy.supabase.co\n"
            "SUPABASE_KEY=sb_publishable_ryoYbCIZlXTF5QqCijLPFA_Ne0W5za9"
        )
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def read_processed_data(csv_path: str) -> pd.DataFrame:
    """Đọc dữ liệu từ CSV"""
    print(f"📖 Đang đọc dữ liệu từ {csv_path}...")
    
    df = pd.read_csv(csv_path)
    
    # In thông tin cơ bản
    print(f"✅ Đọc thành công {len(df)} records")
    print(f"   - Các cột: {list(df.columns)}")
    
    # Online Retail columns
    customer_col = 'Customer_id' if 'Customer_id' in df.columns else 'CustomerID'
    date_col = 'Order_date' if 'Order_date' in df.columns else 'InvoiceDate'
    
    if customer_col in df.columns:
        print(f"   - Số customer unique: {df[customer_col].nunique()}")
    if date_col in df.columns:
        print(f"   - Khoảng thời gian: {df[date_col].min()} đến {df[date_col].max()}")
    
    return df


def prepare_records(df: pd.DataFrame) -> List[Dict]:
    """Chuẩn bị records để insert vào Supabase - cho Online Retail data"""
    
    # Map từ CSV columns (PascalCase) sang database columns (lowercase)
    csv_to_db_mapping = {
        'Customer_id': 'customer_id',
        'Order_id': 'order_id',
        'Total_items': 'total_items',
        'Log_items': 'log_items',
        'Order_date': 'order_date',
        'Order_value': 'order_value',
        'Canceled_value': 'canceled_value',
        'Order_n_categories': 'order_n_categories',
        'Order_n_lines': 'order_n_lines',
        'Is_canceled': 'is_canceled',
        'Country': 'country'
    }
    
    # Rename columns theo mapping
    df_clean = df.rename(columns=csv_to_db_mapping).copy()
    
    # Đảm bảo tất cả columns cần thiết đều tồn tại
    required_cols = ['customer_id', 'order_id', 'total_items', 'order_date', 'order_value', 'country']
    for col in required_cols:
        if col not in df_clean.columns:
            print(f"⚠️ Thiếu cột: {col}")
    
    # Xử lý NaN values
    for col in df_clean.columns:
        if df_clean[col].dtype in ['float64', 'int64']:
            df_clean[col] = df_clean[col].fillna(0)
        else:
            df_clean[col] = df_clean[col].fillna('')
    
    # Đảm bảo log_items được tính nếu thiếu
    if 'log_items' not in df_clean.columns and 'total_items' in df_clean.columns:
        import numpy as np
        def calculate_log_items(quantity, is_canceled):
            if is_canceled == 1 or quantity <= 0:
                return 0
            return np.log1p(quantity)
        
        df_clean['log_items'] = df_clean.apply(
            lambda row: calculate_log_items(row['total_items'], row.get('is_canceled', 0)), 
            axis=1
        )
    
    # Đảm bảo các cột có giá trị mặc định
    if 'order_n_categories' not in df_clean.columns:
        df_clean['order_n_categories'] = 1
    if 'order_n_lines' not in df_clean.columns:
        df_clean['order_n_lines'] = df_clean.get('total_items', 1)
    if 'is_canceled' not in df_clean.columns:
        df_clean['is_canceled'] = 0
    if 'canceled_value' not in df_clean.columns:
        df_clean['canceled_value'] = 0.0
    
    # Chỉ giữ các cột cần thiết
    final_cols = ['customer_id', 'order_id', 'total_items', 'log_items', 'order_date',
                  'order_value', 'canceled_value', 'order_n_categories', 'order_n_lines',
                  'is_canceled', 'country']
    df_clean = df_clean[[col for col in final_cols if col in df_clean.columns]]
    
    # Convert sang list of dicts
    records = df_clean.to_dict('records')
    
    return records


def batch_insert(supabase: Client, records: List[Dict], batch_size: int = 1000):
    """Insert dữ liệu theo batch để tránh timeout"""
    
    total = len(records)
    print(f"\n🚀 Bắt đầu nạp {total} records vào bảng raw_transactions...")
    
    for i in range(0, total, batch_size):
        batch = records[i:i + batch_size]
        
        try:
            # Insert batch
            result = supabase.table("raw_transactions").insert(batch).execute()
            
            print(f"   ✅ Batch {i//batch_size + 1}/{(total//batch_size)+1}: {len(batch)} records")
            
            # Delay nhỏ để tránh rate limit
            time.sleep(0.1)
            
        except Exception as e:
            print(f"   ❌ Lỗi batch {i//batch_size + 1}: {str(e)}")
            continue
    
    print(f"\n🎉 Hoàn tất! Đã nạp dữ liệu vào Supabase.")


def verify_data(supabase: Client):
    """Kiểm tra dữ liệu đã nạp"""
    print("\n🔍 Kiểm tra dữ liệu đã nạp...")
    
    # Đếm tổng số records
    result = supabase.table("raw_transactions").select("id", count="exact").execute()
    count = result.count if hasattr(result, 'count') else len(result.data)
    print(f"   - Tổng số records trong raw_transactions: {count}")
    
    # Lấy sample
    sample = supabase.table("raw_transactions").select("*").limit(3).execute()
    if sample.data:
        print(f"   - Sample record: {sample.data[0]}")
    
    # Đếm số customer unique
    result = supabase.table("raw_transactions") \
        .select("customer_id") \
        .execute()
    unique_customers = len(set([r['customer_id'] for r in result.data])) if result.data else 0
    print(f"   - Số customer unique: {unique_customers}")


def main():
    """Main function"""
    print("=" * 50)
    print("🗄️  SUPABASE SEED DATA SCRIPT")
    print("=" * 50)
    
    # 1. Tạo kết nối
    supabase = create_supabase_client()
    print("🔗 Đã kết nối Supabase thành công!")
    
    # 2. Đọc dữ liệu
    df = read_processed_data(CSV_PATH)
    
    # 3. Chuẩn bị records
    records = prepare_records(df)
    
    # 4. Insert dữ liệu
    batch_insert(supabase, records, BATCH_SIZE)
    
    # 5. Kiểm tra
    verify_data(supabase)
    
    print("\n" + "=" * 50)
    print("✅ SEED DATA HOÀN TẤT!")
    print("=" * 50)


if __name__ == "__main__":
    main()
