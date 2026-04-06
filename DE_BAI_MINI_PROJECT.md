# 📋 ĐỀ BÀI MINI PROJECT: FullStack Credit Score Prediction App

> **Tác giả**: Nguyễn Quốc Huy (Rinez) — VTI Academy

---

## Outline

1. [Tổng quan đề bài](#1-tổng-quan-đề-bài)
2. [Yêu cầu kỹ thuật bắt buộc](#2-yêu-cầu-kỹ-thuật-bắt-buộc)
3. [Yêu cầu chức năng chi tiết](#3-yêu-cầu-chức-năng-chi-tiết)
4. [Sản phẩm nộp bài](#4-sản-phẩm-nộp-bài)
5. [Tiêu chí chấm điểm](#5-tiêu-chí-chấm-điểm)
6. [Tài liệu tham khảo](#6-tài-liệu-tham-khảo)
7. [Hình thức nộp](#hình-thức-nộp)
8. [Gợi ý tính năng](#8-gợi-ý-tính-năng)

---

## 1. Tổng quan đề bài

### Mô tả dự án

Xây dựng một ứng dụng web **fullstack** hoàn chỉnh cho bài toán **Online Retail Repurchase Prediction App**. Ứng dụng cho phép người dùng nhập lịch sử giao dịch khách hàng trên sàn Online Retail, để dự báo khả năng quay lại mua hàng. hệ thống sẽ sử dụng mô hình Machine Learning để đánh giá và trả về kết quả.

### Mục tiêu

- Áp dụng kiến thức ML để train và export model phục vụ production
- Xây dựng REST API backend bằng Python
- Xây dựng giao diện frontend hiện đại
- Kết nối database lưu trữ dữ liệu
- Deploy toàn bộ hệ thống lên cloud
- Hiểu quy trình phát triển phần mềm end-to-end

---

## 2. Yêu cầu kỹ thuật bắt buộc

### 2.1. Tech Stack quy định

| Layer | Công nghệ | Hosting |
|-------|-----------|---------|
| **ML Model** | LightGBM | File `.pkl` trong repo |
| **Backend** | FastAPI (Python) | Render.com |
| **Frontend** | Next.js 14+ (React) | Vercel |
| **Database** | PostgreSQL | Supabase |
| **Version Control** | Git + GitHub | GitHub |

### 2.2. Kiến trúc bắt buộc

```
┌─────────────────┐      ┌──────────────────┐     ┌─────────────────┐
│   Frontend      │────▶│   FastAPI        │────▶│   Supabase DB   │
│   (Next.js)     │◀────│   Backend        │◀────│   (PostgreSQL)  │
└─────────────────┘      └──────────────────┘     └─────────────────┘
        │                        │
        │              ┌─────────┴───────────┐
        │              │  Model Files (.pkl) │
        │              │  • best_model.pkl   │
        │              │  • preprocessor.pkl │
        │              │  • optimal_threshold│
        │              └─────────────────────┘
        │
   Người dùng nhập
   Customer ID + Giao dịch
```

---

## 3. Yêu cầu chức năng chi tiết
### 3.1 Cấu trúc thư mục
```
MOCK PROJECT/
├── 📂 backend/                # [B1-B11] Source code FastAPI
│   ├── 📂 models/             # Chứa preprocessor.pkl và lgbm_model.pkl
│   │   ├── preprocessor.pkl
│   │   ├── best_model.pkl
│   │   ├── feature_importance.csv
│   │   ├── optimal_threshold.pkl
│   ├── 📂 app/
│   │   ├── main.py            # Logic API chính
│   │   ├── schemas.py         # Định nghĩa Pydantic (Bảng nhập liệu thô)
│   │   ├── preprocess_utils.py# Class OlistPreprocessor để giải nén pkl
│   │   └── database.py        # Kết nối Supabase SDK
│   └── requirements.txt       # fastapi, pandas, joblib, supabase, etc.
│
├── 📂 frontend/               # [F1-F12] Source code Next.js 14+
│   ├── 📂 src/
│   │   ├── 📂 app/            # App Router (Pages & Layouts)
│   │   │   ├── 📂 apply/      
│   │   │   │   └── page.tsx   # Trang nhập liệu dự báo (Form + Table)
│   │   │   ├── 📂 history/    
│   │   │   │   └── page.tsx   # Trang hiển thị lịch sử từ database
│   │   │   ├── layout.tsx     # Bọc Navbar, Footer và các Providers
│   │   │   └── page.tsx       # [F1] Landing page giới thiệu dự án
│   │   ├── 📂 components/     # UI Components tách rời
│   │   │   ├── 📂 predict/    # Components riêng cho tính năng dự báo
│   │   │   │   ├── TransactionTable.tsx # Bảng nhập liệu động (Thêm/Xóa dòng)
│   │   │   │   ├── PredictResult.tsx    # Hiển thị Gauge Chart & Level
│   │   │   │   └── QuickFillButton.tsx  # Nút lấy data thô từ DB
│   │   │   ├── 📂 layout/     # Navbar.tsx, Footer.tsx
│   │   │   └── 📂 ui/         # Button.tsx, Input.tsx, Badge.tsx, Card.tsx
│   │   ├── 📂 services/       # Hàm gọi API (Axios/Fetch)
│   │   │   ├── api.ts         # Gọi POST /predict, GET /applications
│   │   │   └── customer.ts    # Gọi GET /customers/{id}/history
│   │   └── 📂 types/          # TypeScript Definitions
│   │       └── index.ts       # Interface cho Transaction, PredictResponse...
│   ├── .env.local             # Biến môi trường (NEXT_PUBLIC_API_URL)
│   ├── package.json           # Scripts & Dependencies
│   └── tailwind.config.ts     # Cấu hình giao diện (Colors, Fonts)
│
│
├── 📂 database/               # [D1-D6] Quản lý cấu trúc dữ liệu
│   ├── schema.sql             # Chứa lệnh CREATE TABLE cho repurchase_logs và raw_transactions
│   ├── seed_data.py           # Script Python để đẩy dữ liệu từ CSV vào raw_transactions
│   └── policies.sql           # Chứa các lệnh thiết lập RLS & Policies
│
├── 📂 notebooks/              # Các file nghiên cứu .ipynb
│   ├── 1_Data_Generation.ipynb
│   ├── 2_Exploratory_Data_Analysis.ipynb
│   └── 3_Model_Building.ipynb
│
├── 📂 data/                   # File CSV gốc (Để local, không push lên GitHub)
│   ├── synthetic_data.csv
│   └── processed_data.csv
│   └── derived_features.csv
|   └── feature_data.csv
│   └── olist_customers_dataset.csv
|   └── olist_geolocation_dataset.csv
|   └── olist_order_items_dataset.csv
|   └── olist_order_payments_dataset.csv
|   └── olist_order_reviews_dataset.csv
|   └── olist_orders_dataset.csv
|   └── olist_products_dataset.csv
|   └── olist_sellers_dataset.csv
|
|
│
├── .gitignore                 # Chặn thư mục data/, __pycache__/, .env
├── DE_BAI_MINI_PROJECT.md     # Đề bài đã sửa theo bài toán Repurchase
└── README.md                  # Hướng dẫn cài đặt tổng thể
```
### 3.2. Backend API

| # | Yêu cầu | Mức độ |
|---|---------|--------|
| B1 | Tạo FastAPI app với Swagger UI tự động (`/docs`) | Bắt buộc |
| B2 | Endpoint `GET /health` — health check (trả trạng thái model + DB) | Bắt buộc |
| B3 | Endpoint POST /predict: 1. Nhận input JSON thô (Transaction level). 2. Khai báo lại Class OnlineRetailPreprocessor trong Backend để giải nén file preprocessor.pkl. 3. Gọi hàm __init__, transform(transactions, snapshot_date), transform_api_input để biến dữ liệu thô thành 26 feature. 4. Đưa kết quả qua best_model.pkl để trả về xác suất mua lại.. | Bắt buộc |
| B4 | Validate input bằng Pydantic: Cấu trúc dữ liệu: API nhận một Object `customer_info` chứa Customer_id (str) và snapshot_date (datetime) và một danh sách (List) các giao dịch thô transactions: chứa dữ liệu thô (Customer_id, Order_id, Order_date, Order_value, Is_canceled, Total_items, Log_items, Order_n_lines, Order_n_categories, Country, Canceled_value). Logic thời gian: Cho phép nhập toàn bộ lịch sử giao dịch. "Máy lọc" (preprocessor.pkl) sẽ tự động dựa vào snapshot_date để lọc và tính toán các đặc trưng trong phạm vi 5 tháng gần nhất (L1M, L3M, L5M).Ràng buộc: Order_date của tất cả đơn hàng phải $\le$ snapshot_date. Các biến lịch sử thì tính trên toàn bộ lịch sử giao dịch của file transaction, không giới hạn thời gian. | Bắt buộc |
| B5 | Response phải bao gồm: probability (xác suất mua), is_repurchase (bool), potential_level: Mức độ tiềm năng, top_reasons (từ Feature Importance). Logic phân loại Potential Level (Dựa trên Probability): High: Probability >= 60% (Khách hàng cực kỳ tiềm năng), Medium: 40% $\le$ Probability $\le$ 60% (Khách hàng cần chăm sóc), Low: Probability < 40% (Khách hàng ít khả năng quay lại) | Bắt buộc |
| B6 | Kết nối Supabase để lưu kết quả mỗi lần predict | Bắt buộc |
| B7 | Endpoint `GET /applications` — lấy lịch sử (có pagination) | Bắt buộc |
| B8 | CORS middleware cho phép frontend gọi API | Bắt buộc |
| B9 | Graceful degradation: API vẫn hoạt động khi DB không kết nối được | Nâng cao |
| B10 | Endpoint `GET /applications/{id}` — chi tiết 1 record | Nâng cao |
| B11 | Endpoint GET /model-info: Trả về thông tin phiên bản Model, ngày huấn luyện và ngưỡng threshold | Bonus |

Cấu trúc Input bắt buộc cho /predict:
Dữ liệu được chia thành 2 phần để tối ưu hóa giao diện nhập liệu dạng bảng:

A. Thông tin định danh (Client Header - Nhập 1 lần)

| Field              | Type           | Mô tả (Nguyên liệu thô)                                      |
| ------------------ | -------------- | ------------------------------------------------------------ |
| Customer_id | str            | ID định danh khách hàng  |
| snapshot_date      | str / datetime | Ngày chốt dữ liệu để dự báo (Ví dụ: "2010-09-30")            |

B. Danh sách giao dịch (Dynamic Table Body - Nhập nhiều dòng)
Mỗi dòng trong bảng (tương ứng với một order_id) phải chứa đầy đủ các thông tin sau để "máy lọc" có thể tính toán chính xác:

| Field                    | Type           | Mô tả                                                           |
| ------------------------ | -------------- | --------------------------------------------------------------- |
| Order_id                 | str            | Mã đơn hàng (Dùng để xác định tính duy nhất của đơn)            |
| Total_items               | int            | Tổng số lượng sản phẩm trong đơn                            |
| Log_items               | float            | Logarithm của tổng số lượng sản phẩm trong đơn                            |
| Order_date | datetime | Ngày mua hàng           |
| Order_value       | float          | Số tiền thanh toán (bao gồm giá trị âm đối với đơn bị hủy) |
| Canceled_value             | float    | Số tiền bị hủy (0 nếu đơn hàng không bị hủy)                    |
| Order_n_categories              | int            | Số danh mục sản phẩm trong đơn                 |
| Order_n_lines              | int            | Số dòng sản phẩm trong đơn                 |
| Is_canceled           | int            | Cờ hủy đơn hàng (0 hoặc 1)            |
| Country           | str            | Tên quốc gia              |


### 3.3. Database

| STT | Yêu cầu                      | Chi tiết kỹ thuật (Dành cho SQL Editor)                                                                                                                                                                                                                                                                                    | Mức độ   |
| --- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| D1  | Tạo table `repurchase_logs`  | Lưu kết quả dự báo: - id: UUID (Primary Key) đại diện cho mã lượt dự báo. - Customer_id: String (Lấy từ customer_info). - input_data: JSONB (Chỉ lưu mảng transactions). - probability, is_repurchase, potential_level, top_reasons.                                                                                                                                                                                | Bắt buộc |
| D2  | Tạo table `raw_transactions` | Import dữ liệu từ file processed_data.csv vào bảng này. Dữ liệu được giữ nguyên định dạng thô (customer level) để phục vụ tính năng Smart Quick-fill. | Nâng cao |
| D3  | Primary key UUID             | Sử dụng `gen_random_uuid()` cho cả hai bảng để đảm bảo định danh duy nhất.                                                                                                                                                                                                                                                 | Bắt buộc |
| D4  | Bật RLS & Policy             | Cho phép `INSERT` vào `repurchase_logs` và `SELECT` từ `raw_transactions` để lấy dữ liệu mẫu.                                                                                                                                                                                                                              | Bắt buộc |
| D5  | Indexing chiến thuật         | Tạo Index trên `customer_unique_id` của bảng `raw_transactions` và  `repurchase_logs` để truy vấn lịch sử nhanh chóng.                                                                                                                                                                                                    | Nâng cao |



### 3.4. Frontend


| # | Yêu cầu | Mức độ |
|---|---------|--------|
| F1 | Trang chủ `/` — giới thiệu ứng dụng | Bắt buộc |
| F2 | Trang `/apply` — Giao diện nhập liệu: Sử dụng Bảng nhập liệu động (Dynamic Table) thay vì các ô input cố định. Chức năng: Cho phép người dùng nhấn nút [+ Thêm đơn hàng] để nhập nhiều giao dịch cùng lúc cho một khách hàng. Yêu cầu dữ liệu: Khuyến khích nhập đủ lịch sử giao dịch trong 5 tháng để Model đạt độ chính xác cao nhất. | Bắt buộc |
| F3 | Hiển thị kết quả sau khi submit: Hiển thị: Probability (%), is_repurchase: Badge trạng thái (Khả năng mua lại: cao, trung bình, thấp), potential_level: Mức độ tiềm năng, top_reasons: Danh sách các đặc trưng ảnh hưởng nhất | Bắt buộc |
| F4 | Trang `/history` — bảng lịch sử các đơn đã submit | Bắt buộc |
| F5 | Responsive design (hiển thị tốt trên mobile + desktop) | Bắt buộc |
| F6 | Loading state khi chờ API respond | Bắt buộc |
| F7 | Error handling: hiển thị thông báo khi API lỗi | Bắt buộc |
| F8 | Form validation: không cho submit nếu thiếu thông tin | Bắt buộc |
| F9 | Top Reasons: Hiển thị 3 lý do chính dẫn đến kết quả | Nâng cao |
| F10 | Biểu đồ hoặc gauge hiển thị score trực quan | Nâng cao |
| F11 | Quick-fill: Cho phép người dùng nhanh chóng trải nghiệm hệ thống bằng cách sử dụng dữ liệu thật từ tập transaction. Thay vì nhập thủ công từng dòng Order_id, hệ thống cung cấp cơ chế: Khi người dùng nhập một Customer_id hợp lệ vào ô Input. Nhấn nút "Lấy lịch sử" (Fetch History). Hệ thống gọi API để lấy toàn bộ danh sách Order_id của khách hàng đó từ Database và tự động đổ (render) vào bảng nhập liệu. | Nâng cao |
| F12 | Thống kê tổng hợp trên trang history (tổng lượt test, % mua lại) | Bonus |

### 3.5. Deployment

| # | Yêu cầu | Mức độ |
|---|---------|--------|
| P1 | Backend deploy trên Render.com | Bắt buộc |
| P2 | Frontend deploy trên Vercel | Bắt buộc |
| P3 | Database trên Supabase (đã setup) | Bắt buộc |
| P4 | Environment variables cấu hình đúng trên cả Render + Vercel | Bắt buộc |
| P5 | CORS cấu hình đúng (backend allow domain frontend) | Bắt buộc |
| P6 | Auto-deploy khi push code lên GitHub | Nâng cao |

---

## 4. Sản phẩm nộp bài

### 4.1. Source code (GitHub)

Nộp **2 GitHub repositories** (hoặc 1 monorepo):

| Repo | Nội dung |
|------|---------|
| `credit-score-backend` | Code backend + model files + notebook |
| `credit-score-frontend` | Code frontend Next.js |

**Mỗi repo phải có:**
- `README.md` — hướng dẫn cài đặt và chạy local
- `.gitignore` — không push `node_modules/`, `venv/`, `.env`, `__pycache__/`
- Code sạch, có comment ở những chỗ quan trọng

### 4.2. URLs production

| Service | URL |
|---------|-----|
| Frontend (Vercel) | `https://your-app.vercel.app` |
| Backend API (Render) | `https://your-api.onrender.com` |
| Swagger UI | `https://your-api.onrender.com/docs` |

### 4.3. Demo

- Trình bày demo ứng dụng hoạt động trên production (Vercel URL)
- Thao tác: nhập đơn → xem kết quả → xem lịch sử
- Giải thích luồng hoạt động: Frontend → Backend → Model → Database

---

## 5. Tiêu chí chấm điểm

### Bảng điểm (Tổng: 100 điểm)

| Hạng mục | Điểm | Chi tiết |
|---------|------|---------|
| **ML Model** | **15** | |
| - Train model chạy được, export thành công | 8 | Notebook chạy đầy đủ, model predict được |
| - EDA + Evaluation đầy đủ | 5 | Có biểu đồ, metrics rõ ràng |
| - So sánh models / Feature Importance | 2 | Bonus |
| **Backend API** | **25** | |
| - `/predict` hoạt động đúng | 10 | Nhận input → trả score, approved, risk_level |
| - Pydantic validation | 5 | Input sai → trả lỗi rõ ràng |
| - `/health` + `/applications` | 5 | Health check + lịch sử hoạt động |
| - Kết nối Supabase lưu data | 5 | Mỗi predict lưu vào DB thành công |
| **Database** | **10** | |
| - Table schema đúng + RLS | 6 | Table tạo đúng, RLS bật, policies đúng |
| - Data lưu đúng + query được | 4 | Verify data trong Supabase Dashboard |
| **Frontend** | **25** | |
| - Form nhập đơn (≥10 fields) | 8 | Form hiển thị đúng, đủ fields |
| - Hiển thị kết quả score | 7 | Score, approved/rejected, risk level |
| - Trang lịch sử | 5 | Bảng hiển thị đúng data |
| - UI/UX + Responsive | 5 | Giao diện sạch, dùng được trên mobile |
| **Deployment** | **15** | |
| - Backend live trên Render | 5 | URL hoạt động, `/docs` mở được |
| - Frontend live trên Vercel | 5 | URL hoạt động, 3 trang hiển thị |
| - End-to-end test thành công | 5 | Submit trên Vercel → Data lưu vào Supabase |
| **Code Quality** | **10** | |
| - README.md rõ ràng | 3 | Hướng dẫn setup local đầy đủ |
| - Code có cấu trúc, comment | 4 | Tách file hợp lý, comment chỗ quan trọng |
| - .gitignore đúng, không push secrets | 3 | Không push `.env`, `node_modules`, `venv` |

---

## 6. Tài liệu tham khảo

### Tài liệu dự án (đã cung cấp sẵn)

| File | Mô tả |
|------|--------|
| `FULL_SETUP_GUIDE.md` | Hướng dẫn setup từ Step 1 → Step 5 |
| `Step01_Train_Model/` | Notebook mẫu + sample data |
| `Step02_Backend/` | Code backend mẫu |
| `Step03_Database/` | SQL schema + seed data |
| `Step04_Frontend/` | Code frontend mẫu |
| `Step05_Deployment/` | Hướng dẫn deploy từng platform |

### Documentation chính thức

| Công nghệ | Link |
|-----------|------|
| FastAPI | https://fastapi.tiangolo.com |
| Next.js | https://nextjs.org/docs |
| Supabase | https://supabase.com/docs |
| XGBoost | https://xgboost.readthedocs.io |
| Tailwind CSS | https://tailwindcss.com/docs |
| Render | https://docs.render.com |
| Vercel | https://vercel.com/docs |

---

### Hình thức nộp

1. **Link GitHub**: 2 repo (backend + frontend)
2. **Link production**: URL Vercel + URL Render
3. **Demo trực tiếp**: trình bày trước lớp (5-10 phút / nhóm)

---

## 8. Gợi ý tính năng

| # | Tính năng |
|---|----------|
| 1 | Thêm **authentication** (Supabase Auth: đăng ký / đăng nhập) |
| 2 | Thêm **dashboard** thống kê (biểu đồ chart.js hoặc recharts) |
| 3 | **Batch prediction**: upload file CSV → predict nhiều hồ sơ |
| 4 | **So sánh 2+ models**: cho user chọn model để predict |
| 5 | **Export PDF**: xuất kết quả ra file PDF |
| 6 | **Dark mode**: toggle giao diện sáng/tối |
| 7 | **Animation**: hiệu ứng khi hiển thị kết quả (gauge quay, score đếm lên) |
| 8 | Tự tìm **dataset thật** trên Kaggle thay vì dùng sample data |
| 9 | Viết **unit test** cho backend (pytest) |
| 10 | Thêm **CI/CD pipeline** (GitHub Actions) |

---

*Credit Score Prediction — FullStack VibeCoding Mini Project*

> **Tác giả**: Nguyễn Quốc Huy (Rinez) — VTI Academy
