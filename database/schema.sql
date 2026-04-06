-- ==========================================
-- SCHEMA SQL FOR ONLINE RETAIL REPURCHASE PREDICTION APP
-- Database: PostgreSQL (Supabase)
-- ==========================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==========================================
-- 1. BẢNG repurchase_logs - Lưu kết quả dự báo
-- ==========================================
CREATE TABLE IF NOT EXISTS repurchase_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id VARCHAR(255) NOT NULL,
    input_data JSONB NOT NULL,
    probability DECIMAL(5,4) NOT NULL,
    is_repurchase BOOLEAN NOT NULL,
    potential_level VARCHAR(50) NOT NULL,
    top_reasons JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index cho customer_id để truy vấn nhanh
CREATE INDEX IF NOT EXISTS idx_repurchase_logs_customer_id 
    ON repurchase_logs(customer_id);

-- Index cho created_at để sắp xếp lịch sử
CREATE INDEX IF NOT EXISTS idx_repurchase_logs_created_at 
    ON repurchase_logs(created_at DESC);

-- Migration: Tăng độ dài cột potential_level nếu đã tạo bảng trước đó với VARCHAR(20)
ALTER TABLE repurchase_logs ALTER COLUMN potential_level TYPE VARCHAR(50);

-- ==========================================
-- 2. BẢNG raw_transactions - Lưu dữ liệu giao dịch thô (Online Retail)
-- ==========================================
CREATE TABLE IF NOT EXISTS raw_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id VARCHAR(255) NOT NULL,
    order_id VARCHAR(255) NOT NULL,
    total_items INTEGER NOT NULL,
    log_items DECIMAL(10,4),
    order_date TIMESTAMP NOT NULL,
    order_value DECIMAL(10,2) NOT NULL,
    canceled_value DECIMAL(10,2) DEFAULT 0,
    order_n_categories INTEGER,
    order_n_lines INTEGER,
    is_canceled INTEGER DEFAULT 0,
    country VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index cho customer_id - QUAN TRỌNG cho tính năng Quick-fill
CREATE INDEX IF NOT EXISTS idx_raw_transactions_customer_id 
    ON raw_transactions(customer_id);

-- Index cho order_id
CREATE INDEX IF NOT EXISTS idx_raw_transactions_order_id 
    ON raw_transactions(order_id);

-- Index cho order_date để lọc theo thời gian
CREATE INDEX IF NOT EXISTS idx_raw_transactions_order_date 
    ON raw_transactions(order_date);

-- ==========================================
-- 3. ROW LEVEL SECURITY (RLS) POLICIES
-- ==========================================

-- Bật RLS cho cả 2 bảng
ALTER TABLE repurchase_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE raw_transactions ENABLE ROW LEVEL SECURITY;

-- Policy: Cho phép INSERT vào repurchase_logs (từ backend)
CREATE POLICY IF NOT EXISTS "Allow insert to repurchase_logs" 
    ON repurchase_logs FOR INSERT TO anon 
    WITH CHECK (true);

-- Policy: Cho phép SELECT từ repurchase_logs
CREATE POLICY IF NOT EXISTS "Allow select from repurchase_logs" 
    ON repurchase_logs FOR SELECT TO anon 
    USING (true);

-- Policy: Cho phép SELECT từ raw_transactions (cho tính năng Quick-fill)
CREATE POLICY IF NOT EXISTS "Allow select from raw_transactions" 
    ON raw_transactions FOR SELECT TO anon 
    USING (true);

-- Policy: Cho phép INSERT vào raw_transactions (cho seed data)
CREATE POLICY IF NOT EXISTS "Allow insert to raw_transactions" 
    ON raw_transactions FOR INSERT TO anon 
    WITH CHECK (true);

-- ==========================================
-- 4. COMMENTS
-- ==========================================
COMMENT ON TABLE repurchase_logs IS 'Lưu kết quả dự báo khả năng mua lại của khách hàng';
COMMENT ON TABLE raw_transactions IS 'Lưu dữ liệu giao dịch thô để phục vụ tính năng Quick-fill';
COMMENT ON COLUMN repurchase_logs.input_data IS 'JSON chứa mảng transactions input';
COMMENT ON COLUMN repurchase_logs.top_reasons IS 'JSON chứa top 3 lý do ảnh hưởng đến kết quả';
