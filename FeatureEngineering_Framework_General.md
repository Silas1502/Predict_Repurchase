# FEATURE ENGINEERING FRAMEWORK - TỔNG QUÁT CHO MỌI NGÀNH

## � MỤC LỤC

- [📚 GIỚI THIỆU](#-giới-thiệu)
- [📋 PHẦN I: FEATURE SUB-GROUPS (NHÓM ĐẶC TRƯNG CHÍNH)](#-phần-i-feature-sub-groups-nhóm-đặc-trưng-chính)
  - [1.1. TENURE / TIME ON PLATFORM — Thời gian gắn bó](#11-tenure--time-on-platform--thời-gian-gắn-bó)
  - [1.2. AVERAGE VALUE PER EVENT — Giá trị trung bình mỗi sự kiện](#12-average-value-per-event--giá-trị-trung-bình-mỗi-sự-kiện)
  - [1.3. BALANCE / CURRENT STATE — Trạng thái hiện tại](#13-balance--current-state--trạng-thái-hiện-tại)
  - [1.4. EVENT COUNT — Số lượng sự kiện](#14-event-count--số-lượng-sự-kiện)
  - [1.5. EVENT VALUE / TOTAL VALUE — Tổng giá trị sự kiện](#15-event-value--total-value--tổng-giá-trị-sự-kiện)
  - [1.6. ACTIVE PRODUCT / SERVICE COUNT — Số sản phẩm/dịch vụ đang sử dụng](#16-active-product--service-count--số-sản-phẩmdịch-vụ-đang-sử-dụng)
  - [1.7. ACTIVE PERIODS — Số kỳ có hoạt động](#17-active-periods--số-kỳ-có-hoạt-động)
  - [1.8. RECENCY — Thời gian kể từ lần hoạt động cuối](#18-recency--thời-gian-kể-từ-lần-hoạt-động-cuối)
  - [1.9. EVENT DIVERSITY — Độ đa dạng sự kiện](#19-event-diversity--độ-đa-dạng-sự-kiện)
  - [1.10. DEMOGRAPHICS / STATIC ATTRIBUTES — Thuộc tính tĩnh](#110-demographics--static-attributes--thuộc-tính-tĩnh)
- [📊 PHẦN II: 2 CHIỀU PHÂN TÍCH — \[Metric\] × \[Timeframe\]](#-phần-ii-2-chiều-phân-tích--metric--timeframe)
  - [🕒 CHIỀU 1: TIMEFRAME (Khung Thời Gian)](#-chiều-1-timeframe-khung-thời-gian)
    - [1.1. Timeframe Cơ Bản](#11-timeframe-cơ-bản)
    - [1.2. Timeframe So Sánh (Comparison Windows)](#12-timeframe-so-sánh-comparison-windows)
    - [1.3. Trend Features (Xu hướng)](#13-trend-features-xu-hướng)
  - [📐 CHIỀU 2: METRICS (Các Phép Tính Thống Kê)](#-chiều-2-metrics-các-phép-tính-thống-kê)
    - [2.1. Basic Aggregations — Các phép tính cơ bản](#21-basic-aggregations--các-phép-tính-cơ-bản)
    - [2.2. Advanced Metrics — Các phép tính nâng cao](#22-advanced-metrics--các-phép-tính-nâng-cao)
    - [2.3. Velocity Metrics — Tốc độ / Cường độ](#23-velocity-metrics--tốc-độ--cường-độ)
    - [2.4. Ratio Metrics — Các tỷ lệ](#24-ratio-metrics--các-tỷ-lệ)
- [🔢 PHẦN III: FEATURE COMBINATION MATRIX — MA TRẬN KẾT HỢP](#-phần-iii-feature-combination-matrix--ma-trận-kết-hợp)
  - [3.1. Feature Naming Convention](#31-feature-naming-convention)
  - [3.2. Ma Trận Kết Hợp Đầy Đủ](#32-ma-trận-kết-hợp-đầy-đủ)
  - [3.3. Ước Tính Tổng Số Features](#33-ước-tính-tổng-số-features)
- [📈 PHẦN IV: ADVANCED FEATURE ENGINEERING](#-phần-iv-advanced-feature-engineering)
  - [4.1. RFM Features (Recency, Frequency, Monetary)](#41-rfm-features-recency-frequency-monetary)
  - [4.2. Ratio & Percentage Features](#42-ratio--percentage-features)
  - [4.3. Trend & Velocity Features](#43-trend--velocity-features)
  - [4.4. Volatility & Anomaly Features](#44-volatility--anomaly-features)
  - [4.5. Interaction Features — Đặc trưng tương tác](#45-interaction-features--đặc-trưng-tương-tác)
- [🛠️ PHẦN V: PIPELINE TỔNG QUÁT](#️-phần-v-pipeline-tổng-quát)
  - [5.1. Template Code — Feature Engineering Pipeline](#51-template-code--feature-engineering-pipeline)
- [📊 PHẦN VI: FEATURE SELECTION & OPTIMIZATION](#-phần-vi-feature-selection--optimization)
  - [6.1. Bước 1 — Loại bỏ features ít biến động](#61-bước-1--loại-bỏ-features-ít-biến-động)
  - [6.2. Bước 2 — Loại bỏ features tương quan cao](#62-bước-2--loại-bỏ-features-tương-quan-cao-multicollinearity)
  - [6.3. Bước 3 — Feature Importance](#63-bước-3--feature-importance-chọn-features-quan-trọng)
  - [6.4. Bước 4 — Mutual Information](#64-bước-4--mutual-information-đo-lượng-thông-tin)
- [🎯 PHẦN VII: TỔNG KẾT & CHECKLIST](#-phần-vii-tổng-kết--checklist)
  - [7.1. Feature Engineering Checklist](#71-feature-engineering-checklist-áp-dụng-mọi-ngành)
  - [7.2. Best Practices](#72-best-practices)

---

## �📚 GIỚI THIỆU

Framework này là bộ hướng dẫn **tổng quát (industry-agnostic)** để xây dựng features cho bất kỳ bài toán Machine Learning nào, áp dụng được cho mọi lĩnh vực:

| Ngành | Ví dụ bài toán |
|-------|---------------|
| 🏦 Ngân hàng / Tài chính | Fraud Detection, Credit Scoring, Churn Prediction |
| 🛒 Bán lẻ / E-commerce | Customer Segmentation, Recommendation, Demand Forecasting |
| 🏥 Y tế | Disease Prediction, Patient Readmission, Treatment Outcome |
| 📡 Viễn thông | Churn Prediction, Network Anomaly, Usage Forecasting |
| 🏭 Sản xuất | Predictive Maintenance, Quality Control, Yield Optimization |
| 🚗 Vận tải / Logistics | Delivery ETA, Route Optimization, Fleet Maintenance |
| 🎮 Gaming / Entertainment | Player Churn, In-app Purchase, Content Recommendation |
| 📊 SaaS / Subscription | User Engagement, Churn, Upsell Prediction |

**Tư tưởng chính:**
> "Với mọi thực thể (entity), hãy cắt nhỏ dữ liệu theo mọi chiều có thể, theo nhiều khung thời gian, và tính nhiều chỉ số thống kê khác nhau."

**Framework 2 chiều:**
```
Feature = [Metric] × [Timeframe]
```

---

## 📋 PHẦN I: FEATURE SUB-GROUPS (NHÓM ĐẶC TRƯNG CHÍNH)

> Mỗi sub-group dưới đây được trình bày theo dạng **tổng quát**, kèm ví dụ cụ thể cho nhiều ngành khác nhau.

---

### 1.1. TENURE / TIME ON PLATFORM — Thời gian gắn bó

**Định nghĩa:** Thời gian kể từ khi entity (khách hàng, thiết bị, user, bệnh nhân…) bắt đầu tham gia hệ thống.

**Công thức tổng quát:**

```python
tenure_days = (snapshot_date - first_activity_date).days
tenure_months = tenure_days / 30
tenure_years = tenure_days / 365
```

**Áp dụng theo ngành:**

| Ngành | Feature | Ý nghĩa |
|-------|---------|---------|
| Ngân hàng | `account_mob` (Month on Book) | Số tháng mở tài khoản |
| E-commerce | `customer_tenure_months` | Số tháng kể từ đơn hàng đầu tiên |
| SaaS | `subscription_age_days` | Số ngày kể từ khi đăng ký |
| Viễn thông | `contract_tenure_months` | Số tháng sử dụng dịch vụ |
| Y tế | `patient_history_months` | Số tháng có hồ sơ bệnh án |
| Gaming | `player_age_days` | Số ngày kể từ lần đăng nhập đầu tiên |
| Sản xuất | `machine_age_months` | Tuổi thiết bị |

**Phân nhóm Tenure:**

```python
tenure_group = pd.cut(
    tenure_months,
    bins=[0, 3, 6, 12, 24, 60, float('inf')],
    labels=['0-3M', '3-6M', '6-12M', '1-2Y', '2-5Y', '5Y+']
)
```

**Ý nghĩa nghiệp vụ chung:**
- Tenure rất ngắn (< 3 tháng): Entity mới, rủi ro rời bỏ cao, chưa đủ data để phân tích sâu
- Tenure trung bình (6-24 tháng): Đang ổn định, có đủ data
- Tenure dài (> 5 năm): Entity trung thành, ít rủi ro churn

---

### 1.2. AVERAGE VALUE PER EVENT — Giá trị trung bình mỗi sự kiện

**Định nghĩa:** Giá trị trung bình của một đơn vị hành động/sự kiện (giao dịch, đơn hàng, lượt truy cập, ca khám…).

**Công thức tổng quát:**

```python
avg_value_per_event = total_value / event_count
```

**Áp dụng theo ngành:**

| Ngành | Feature | Công thức |
|-------|---------|-----------|
| Ngân hàng | `avg_ticket_size` | Tổng tiền GD / Số GD |
| E-commerce | `avg_order_value (AOV)` | Tổng doanh thu / Số đơn hàng |
| Viễn thông | `avg_call_duration` | Tổng phút gọi / Số cuộc gọi |
| Y tế | `avg_visit_cost` | Tổng chi phí / Số lần khám |
| SaaS | `avg_session_duration` | Tổng thời gian / Số phiên |
| Gaming | `avg_session_score` | Tổng điểm / Số phiên chơi |
| Sản xuất | `avg_batch_output` | Tổng sản lượng / Số lô sản xuất |

**Mở rộng — Percentiles:**

```python
value_p25 = np.percentile(event_values, 25)
value_p50 = np.percentile(event_values, 50)  # Median
value_p75 = np.percentile(event_values, 75)
value_p95 = np.percentile(event_values, 95)  # Phát hiện outlier
```

**Ý nghĩa:**
- Average value tăng đột ngột → Sự kiện bất thường (gian lận, lỗi, nhu cầu đặc biệt)
- Average value ổn định → Entity hành vi bình thường
- Phân phối (percentiles) cho biết hình dạng phân bố giá trị

---

### 1.3. BALANCE / CURRENT STATE — Trạng thái hiện tại

**Định nghĩa:** Giá trị hiện tại hoặc trạng thái snapshot mới nhất của entity.

**Áp dụng theo ngành:**

| Ngành | Feature | Ý nghĩa |
|-------|---------|---------|
| Ngân hàng | `account_balance`, `credit_limit_usage` | Số dư tài khoản, % sử dụng hạn mức |
| E-commerce | `cart_value`, `loyalty_points` | Giá trị giỏ hàng, điểm tích lũy |
| SaaS | `storage_usage_pct`, `active_users` | % dung lượng sử dụng, số user hoạt động |
| Viễn thông | `data_remaining_gb`, `balance_remaining` | Data còn lại, số dư tài khoản |
| Sản xuất | `inventory_level`, `machine_health_score` | Tồn kho, chỉ số sức khỏe máy |
| Gaming | `in_game_currency`, `level` | Tiền trong game, level hiện tại |

**Features phái sinh từ Balance:**

```python
# Giá trị tuyệt đối
current_value       # Giá trị hiện tại
avg_value           # Giá trị trung bình trong kỳ
min_value           # Giá trị thấp nhất
max_value           # Giá trị cao nhất

# Biến động
value_change = current_value - previous_value
value_growth_pct = (current_value - previous_value) / (abs(previous_value) + 1)

# Volatility
value_std = std(values_over_period)
value_cv = value_std / (avg_value + 1)  # Coefficient of Variation
```

---

### 1.4. EVENT COUNT — Số lượng sự kiện

**Định nghĩa:** Tổng số lần entity thực hiện một hành động trong kỳ quan sát.

**Áp dụng theo ngành:**

| Ngành | Feature | Ý nghĩa |
|-------|---------|---------|
| Ngân hàng | `transaction_count` | Số giao dịch |
| E-commerce | `order_count`, `return_count` | Số đơn hàng, số lần trả hàng |
| Viễn thông | `call_count`, `sms_count` | Số cuộc gọi, số SMS |
| Y tế | `visit_count`, `prescription_count` | Số lần khám, số đơn thuốc |
| SaaS | `login_count`, `feature_usage_count` | Số lần đăng nhập, số lần dùng tính năng |
| Gaming | `session_count`, `purchase_count` | Số phiên chơi, số lần mua |
| Sản xuất | `production_run_count`, `defect_count` | Số lượt sản xuất, số lỗi |

**Mở rộng — Phân loại event:**

```python
# Tổng quát
total_event_count
positive_event_count    # Sự kiện tích cực (mua, nạp, deposit)
negative_event_count    # Sự kiện tiêu cực (rút, trả, complaint)
neutral_event_count     # Sự kiện trung tính (đăng nhập, xem)

# Tỷ lệ
positive_event_ratio = positive_event_count / (total_event_count + 1)
negative_event_ratio = negative_event_count / (total_event_count + 1)
```

---

### 1.5. EVENT VALUE / TOTAL VALUE — Tổng giá trị sự kiện

**Định nghĩa:** Tổng giá trị tích lũy của tất cả sự kiện trong kỳ.

**Áp dụng theo ngành:**

| Ngành | Feature | Ý nghĩa |
|-------|---------|---------|
| Ngân hàng | `total_transaction_amount` | Tổng giao dịch |
| E-commerce | `total_revenue`, `total_discount_used` | Tổng doanh thu, tổng giảm giá |
| Viễn thông | `total_call_minutes`, `total_data_usage_gb` | Tổng phút gọi, tổng data sử dụng |
| Y tế | `total_medical_cost` | Tổng chi phí y tế |
| SaaS | `total_session_time_hours` | Tổng thời gian sử dụng |
| Sản xuất | `total_output_units`, `total_energy_kwh` | Tổng sản lượng, tổng năng lượng |

**Phân tách theo hướng (Direction):**

```python
# Inflow vs Outflow
total_inflow   # Giá trị đi vào (thu nhập, nạp tiền, nhập kho)
total_outflow  # Giá trị đi ra (chi tiêu, rút tiền, xuất kho)
net_value = total_inflow - total_outflow

# Tỷ lệ
inflow_outflow_ratio = total_inflow / (total_outflow + 1)
```

---

### 1.6. ACTIVE PRODUCT / SERVICE COUNT — Số sản phẩm/dịch vụ đang sử dụng

**Định nghĩa:** Số lượng sản phẩm, dịch vụ, subscription, hoặc module mà entity đang sử dụng.

**Áp dụng theo ngành:**

| Ngành | Feature | Ý nghĩa |
|-------|---------|---------|
| Ngân hàng | `active_product_count` (CASA, Loan, Card) | Số sản phẩm đang dùng |
| E-commerce | `active_category_count` | Số danh mục sản phẩm đã mua |
| SaaS | `active_module_count`, `active_integration_count` | Số module/integration đang dùng |
| Viễn thông | `active_service_count` (Voice, Data, TV) | Số dịch vụ đăng ký |
| Y tế | `active_treatment_count` | Số phác đồ điều trị đang thực hiện |

**Features phái sinh:**

```python
total_active_items = item_a_active + item_b_active + item_c_active

# Cross-sell index — Entity dùng càng nhiều sản phẩm, càng gắn bó
cross_sell_index = total_active_items

# Binary flags
has_product_a = 1 if product_a_count > 0 else 0
has_product_b = 1 if product_b_count > 0 else 0

# Product penetration
product_penetration = active_products / total_available_products
```

**Ý nghĩa:**
- Số sản phẩm càng nhiều → Khách hàng càng khó rời bỏ (switching cost cao)
- `cross_sell_index` cao → Entity "deep" trong hệ sinh thái

---

### 1.7. ACTIVE PERIODS — Số kỳ có hoạt động

**Định nghĩa:** Số kỳ (ngày/tuần/tháng) mà entity có ít nhất 1 sự kiện.

**Công thức tổng quát:**

```python
active_periods = COUNT(DISTINCT period WHERE event_count > 0)
activity_ratio = active_periods / total_periods
```

**Áp dụng theo ngành:**

| Ngành | Feature | Công thức |
|-------|---------|-----------|
| Ngân hàng | `active_months_l6m` | Số tháng có GD trong 6 tháng gần nhất |
| E-commerce | `active_weeks_l3m` | Số tuần có đơn hàng trong 3 tháng |
| SaaS | `active_days_l1m` | Số ngày đăng nhập trong tháng |
| Viễn thông | `active_months_l12m` | Số tháng có sử dụng dịch vụ |
| Gaming | `active_days_l1m` | Số ngày chơi trong tháng |

**Ý nghĩa:**
- `activity_ratio` = 1.0 → Entity hoạt động liên tục mỗi kỳ
- `activity_ratio` < 0.5 → Hoạt động không đều, có nguy cơ churn
- `activity_ratio` giảm dần → Xu hướng rời bỏ

---

### 1.8. RECENCY — Thời gian kể từ lần hoạt động cuối

**Định nghĩa:** Khoảng cách (ngày/tuần/tháng) từ snapshot hiện tại đến sự kiện gần nhất.

**Công thức tổng quát:**

```python
recency_days = (snapshot_date - last_event_date).days
recency_months = recency_days / 30
```

**Áp dụng theo ngành:**

| Ngành | Feature | Ý nghĩa |
|-------|---------|---------|
| Ngân hàng | `months_since_last_transaction` | Tháng kể từ GD cuối |
| E-commerce | `days_since_last_order` | Ngày kể từ đơn hàng cuối |
| SaaS | `days_since_last_login` | Ngày kể từ lần đăng nhập cuối |
| Viễn thông | `days_since_last_call` | Ngày kể từ cuộc gọi cuối |
| Gaming | `days_since_last_session` | Ngày kể từ phiên chơi cuối |
| Sản xuất | `days_since_last_maintenance` | Ngày kể từ lần bảo trì cuối |

**Phân nhóm Recency:**

```python
recency_group = pd.cut(
    recency_days,
    bins=[0, 7, 30, 90, 180, float('inf')],
    labels=['Active', '1W-1M', '1-3M', '3-6M', 'Inactive']
)

# Dormancy flags
is_dormant = 1 if recency_days > 90 else 0
is_highly_dormant = 1 if recency_days > 180 else 0
```

**Ý nghĩa:**
- Recency = 0: Đang hoạt động (hôm nay có sự kiện)
- Recency tăng dần → Entity đang rời xa
- Recency > ngưỡng → Coi như Inactive/Churned

---

### 1.9. EVENT DIVERSITY — Độ đa dạng sự kiện

**Định nghĩa:** Số loại sự kiện/danh mục khác nhau mà entity tham gia.

**Áp dụng theo ngành:**

| Ngành | Feature | Ý nghĩa |
|-------|---------|---------|
| Ngân hàng | `distinct_mcc_count` | Số ngành hàng chi tiêu |
| E-commerce | `distinct_category_count` | Số danh mục sản phẩm mua |
| Viễn thông | `distinct_service_type_count` | Số loại dịch vụ sử dụng |
| SaaS | `distinct_feature_used_count` | Số tính năng đã dùng |
| Gaming | `distinct_game_mode_count` | Số chế độ chơi đã thử |
| Y tế | `distinct_diagnosis_count` | Số loại chẩn đoán |

**Features phái sinh:**

```python
# Diversity count
distinct_event_types = COUNT(DISTINCT event_type)

# Concentration — Herfindahl-Hirschman Index (HHI)
hhi = SUM((value_type_i / total_value) ** 2)
# HHI gần 1 → Tập trung vào 1-2 loại (ít đa dạng)
# HHI gần 0 → Phân tán đều nhiều loại (rất đa dạng)

# Top category dominance
top_category_pct = value_top_category / total_value
top3_category_pct = value_top3_categories / total_value
```

**Ý nghĩa:**
- Diversity cao → Entity sử dụng đa dạng → Gắn bó hơn
- Diversity thấp + concentration cao → Phụ thuộc 1-2 loại → Dễ thay thế

---

### 1.10. DEMOGRAPHICS / STATIC ATTRIBUTES — Thuộc tính tĩnh

**Định nghĩa:** Các thuộc tính mô tả entity, ít thay đổi theo thời gian.

**Áp dụng theo ngành:**

| Ngành | Features | Ví dụ |
|-------|----------|-------|
| Mọi ngành (khách hàng) | `age`, `gender`, `location`, `income_level` | Nhân khẩu học |
| E-commerce | `account_type`, `membership_tier` | Loại tài khoản, hạng thành viên |
| Viễn thông | `plan_type`, `contract_type` | Gói cước, loại hợp đồng |
| Y tế | `blood_type`, `chronic_condition_flag` | Nhóm máu, bệnh mạn tính |
| Sản xuất | `machine_type`, `manufacturer`, `install_year` | Loại máy, năm lắp đặt |
| SaaS | `plan_tier`, `company_size` | Gói subscription, quy mô công ty |

**Encoding:**

```python
# Categorical → Numeric
# One-hot encoding cho low cardinality
pd.get_dummies(df, columns=['gender', 'location_group'])

# Label encoding cho ordinal
from sklearn.preprocessing import OrdinalEncoder
tier_order = ['Basic', 'Silver', 'Gold', 'Platinum']
encoder = OrdinalEncoder(categories=[tier_order])

# Binning cho continuous
age_group = pd.cut(age, bins=[0, 25, 35, 50, 65, 100],
                   labels=['18-25', '25-35', '35-50', '50-65', '65+'])
```

---

## 📊 PHẦN II: 2 CHIỀU PHÂN TÍCH — [Metric] × [Timeframe]

### Framework Kết Hợp 2 Chiều

```
Feature = [Metric] × [Timeframe]

Ví dụ:
- SUM_L3M_order_value         → Tổng giá trị đơn hàng 3 tháng gần nhất
- AVG_L6M_session_duration    → Thời gian phiên trung bình 6 tháng gần nhất
- STD_L12M_daily_usage        → Độ biến động sử dụng hàng ngày trong 12 tháng
- COUNT_L1M_login             → Số lần đăng nhập tháng gần nhất
- MAX_L3M_purchase_amount     → Giá trị đơn hàng lớn nhất trong 3 tháng
```

> Mọi feature trong Phần I đều được nhân với 2 chiều này để tạo ra bộ features đầy đủ.

---

## 🕒 CHIỀU 1: TIMEFRAME (Khung Thời Gian)

### 1.1. Timeframe Cơ Bản

| Timeframe | Ký hiệu | Mô tả | Use Case |
|-----------|---------|-------|----------|
| Last 1 Week | L1W | 7 ngày gần nhất | Hành vi tức thì (gaming, SaaS) |
| Last 1 Month | L1M | 30 ngày gần nhất | Hành vi hiện tại |
| Last 3 Months | L3M | 90 ngày gần nhất | Xu hướng ngắn hạn |
| Last 6 Months | L6M | 180 ngày gần nhất | Xu hướng trung hạn |
| Last 12 Months | L12M | 365 ngày gần nhất | Xu hướng dài hạn |
| Lifetime | LTD | Toàn bộ lịch sử | Tổng quan toàn diện |

> **Lưu ý:** Chọn timeframe phù hợp với tần suất dữ liệu. Nếu dữ liệu theo ngày (SaaS, Gaming) → dùng L1W, L1M. Nếu dữ liệu theo tháng (Ngân hàng, Viễn thông) → dùng L3M, L6M, L12M.

### 1.2. Timeframe So Sánh (Comparison Windows)

**Mục đích:** Phát hiện thay đổi hành vi — so sánh giai đoạn gần với giai đoạn trước đó.

| So sánh | Kỳ gần (Recent) | Kỳ trước (Previous) | Ý nghĩa |
|---------|-----------------|---------------------|---------|
| L1M vs P1M | Tháng 1 gần nhất | Tháng 2 (trước đó) | Thay đổi Month-over-Month |
| L3M vs P3M | 3 tháng gần nhất | 3 tháng trước đó | Thay đổi Quarter-over-Quarter |
| L6M vs P6M | 6 tháng gần nhất | 6 tháng trước đó | Thay đổi Half-over-Half |

```
Timeline:
                    P6M                          L6M
├──────────────────────────────┤──────────────────────────────┤
  6 tháng trước đó               6 tháng gần nhất          snapshot
                         P3M           L3M
              ├──────────────┤──────────────┤
              3 tháng trước    3 tháng gần    snapshot
```

**Ví dụ tính toán:**

```python
# === Tính features cho từng timeframe ===

def compute_features_for_period(df, entity_col, date_col, value_col, start_date, end_date, suffix):
    """
    Tính các metrics cho một khoảng thời gian.
    
    Parameters:
    - df: DataFrame chứa dữ liệu sự kiện
    - entity_col: tên cột entity (customer_id, user_id, machine_id,...)
    - date_col: tên cột ngày
    - value_col: tên cột giá trị
    - start_date, end_date: khoảng thời gian
    - suffix: hậu tố đặt tên feature (vd: 'L3M', 'P3M')
    """
    mask = (df[date_col] >= start_date) & (df[date_col] <= end_date)
    period_df = df[mask]
    
    result = period_df.groupby(entity_col).agg(
        **{
            f'sum_{suffix}': (value_col, 'sum'),
            f'avg_{suffix}': (value_col, 'mean'),
            f'min_{suffix}': (value_col, 'min'),
            f'max_{suffix}': (value_col, 'max'),
            f'std_{suffix}': (value_col, 'std'),
            f'count_{suffix}': (value_col, 'count'),
        }
    )
    return result


# === Tính comparison features ===
# L3M
features_l3m = compute_features_for_period(df, 'customer_id', 'event_date', 'amount',
                                            snapshot - pd.DateOffset(months=3), snapshot, 'L3M')
# P3M
features_p3m = compute_features_for_period(df, 'customer_id', 'event_date', 'amount',
                                            snapshot - pd.DateOffset(months=6),
                                            snapshot - pd.DateOffset(months=3), 'P3M')

# Merge
features = features_l3m.join(features_p3m, how='outer').fillna(0)
```

### 1.3. Trend Features (Xu hướng)

```python
# === Growth Rate — Tốc độ tăng trưởng ===
# So sánh kỳ gần với kỳ trước đó
growth_rate = (value_recent - value_previous) / (abs(value_previous) + 1)

# Ví dụ cụ thể
sum_growth_l3m_vs_p3m = (sum_L3M - sum_P3M) / (abs(sum_P3M) + 1)
count_growth_l3m_vs_p3m = (count_L3M - count_P3M) / (abs(count_P3M) + 1)
avg_growth_l6m_vs_p6m = (avg_L6M - avg_P6M) / (abs(avg_P6M) + 1)


# === Absolute Change — Thay đổi tuyệt đối ===
sum_change_l3m_vs_p3m = sum_L3M - sum_P3M
count_change_l3m_vs_p3m = count_L3M - count_P3M


# === Acceleration — Gia tốc (thay đổi của thay đổi) ===
# Nếu growth_rate đang tăng → Entity đang tăng tốc
# Nếu growth_rate đang giảm → Entity đang giảm tốc
acceleration = growth_l3m_vs_p3m - growth_p3m_vs_pp3m

# Cách tính đơn giản hơn:
spending_acceleration = (sum_L3M - sum_P3M) - (sum_P3M - sum_PP3M)
# PP3M = 3 tháng trước P3M (tháng 7-9 tính từ snapshot)
# Dương → Đang tăng tốc
# Âm → Đang giảm tốc


# === Volatility Change — Biến động thay đổi ===
volatility_change = std_L3M - std_L6M
# Dương → Biến động tăng (bất ổn hơn)
# Âm → Biến động giảm (ổn định hơn)
```

---

## 📐 CHIỀU 2: METRICS (Các Phép Tính Thống Kê)

### 2.1. Basic Aggregations — Các phép tính cơ bản

| Metric | Ký hiệu | Công thức | Ý nghĩa | Ví dụ Feature |
|--------|---------|-----------|---------|---------------|
| **SUM** | Tổng | `SUM(values)` | Tổng giá trị trong kỳ | `sum_L3M_spending` |
| **AVG** | Trung bình | `MEAN(values)` | Giá trị trung bình | `avg_L6M_order_value` |
| **MIN** | Nhỏ nhất | `MIN(values)` | Giá trị thấp nhất | `min_L12M_balance` |
| **MAX** | Lớn nhất | `MAX(values)` | Giá trị cao nhất | `max_L3M_purchase` |
| **STD** | Độ lệch chuẩn | `STD(values)` | Mức biến động | `std_L6M_daily_usage` |
| **COUNT** | Đếm | `COUNT(events)` | Số sự kiện | `count_L3M_transactions` |
| **COUNT_DISTINCT** | Đếm unique | `COUNT(DISTINCT x)` | Số loại khác nhau | `count_distinct_L6M_categories` |
| **MEDIAN** | Trung vị | `MEDIAN(values)` | Giá trị giữa | `median_L3M_amount` |

### 2.2. Advanced Metrics — Các phép tính nâng cao

```python
# === Percentiles (Phân vị) ===
p25 = np.percentile(values, 25)   # Quartile 1
p50 = np.percentile(values, 50)   # Median
p75 = np.percentile(values, 75)   # Quartile 3
p95 = np.percentile(values, 95)   # Phát hiện sự kiện lớn bất thường
iqr = p75 - p25                    # Inter-Quartile Range

# Ý nghĩa:
# P95 cao bất thường so với P50 → Có outlier (sự kiện bất thường)
# IQR lớn → Phân bố rộng, entity có hành vi đa dạng


# === Coefficient of Variation (CV) — Hệ số biến thiên ===
cv = std_value / (avg_value + 1)
# CV > 1 → Biến động rất lớn (hành vi không ổn định)
# CV < 0.5 → Tương đối ổn định
# CV ≈ 0 → Rất ổn định (pattern lặp lại)


# === Skewness (Độ lệch) ===
from scipy.stats import skew
skewness = skew(values)
# Skewness > 0: Phần lớn giá trị nhỏ, ít giá trị lớn (phân phối lệch phải)
# Skewness < 0: Phần lớn giá trị lớn, ít giá trị nhỏ (phân phối lệch trái)
# Skewness ≈ 0: Phân phối cân đối


# === Kurtosis (Độ nhọn) ===
from scipy.stats import kurtosis
kurt = kurtosis(values)
# Kurtosis cao → Có nhiều outlier (giá trị cực đoan)
# Kurtosis thấp → Phân phối phẳng, ít cực đoan


# === Range (Khoảng biến thiên) ===
value_range = max_value - min_value
# Range lớn → Hành vi dao động nhiều
```

### 2.3. Velocity Metrics — Tốc độ / Cường độ

```python
# === Tần suất sự kiện ===
events_per_day = total_event_count / days_in_period
events_per_week = total_event_count / weeks_in_period
events_per_month = total_event_count / months_in_period

# === Cường độ giá trị ===
value_per_day = total_value / days_in_period
value_per_event = total_value / (event_count + 1)

# === Active ratio ===
active_days = COUNT(DISTINCT event_date)
active_day_ratio = active_days / total_days_in_period
# Gần 1 → Hoạt động hằng ngày
# < 0.1 → Rất ít hoạt động

# === Burst detection — Phát hiện bùng nổ ===
max_events_single_day = MAX(daily_event_count)
burst_ratio = max_events_single_day / avg_events_per_day
# Burst ratio cao → Có ngày hoạt động bất thường (có thể là fraud hoặc event đặc biệt)
```

### 2.4. Ratio Metrics — Các tỷ lệ

```python
# === Direction ratios ===
inflow_outflow_ratio = total_inflow / (total_outflow + 1)
positive_negative_ratio = positive_events / (negative_events + 1)

# === Category ratios ===
top_category_pct = top_category_value / (total_value + 1)
secondary_category_pct = second_category_value / (total_value + 1)

# === Change ratios ===
value_change_pct = (current_value - previous_value) / (abs(previous_value) + 1)

# === Efficiency ratios ===
value_per_event = total_value / (event_count + 1)
success_rate = successful_events / (total_events + 1)
```

---

## 🔢 PHẦN III: FEATURE COMBINATION MATRIX — MA TRẬN KẾT HỢP

### 3.1. Feature Naming Convention

```
[METRIC]_[TIMEFRAME]_[FEATURE_GROUP]

Components:
- METRIC:     SUM, AVG, MIN, MAX, STD, COUNT, COUNT_DISTINCT, MEDIAN
- TIMEFRAME:  L1W, L1M, L3M, L6M, L12M, LTD
- FEATURE_GROUP: tên nhóm feature từ Phần I (vd: spending, login, order, usage)
```

**Ví dụ đặt tên theo ngành:**

```python
# ===== Ngân hàng =====
sum_L3M_transaction_amount
avg_L6M_ticket_size
count_L12M_transactions
std_L3M_balance
max_L3M_single_transaction

# ===== E-commerce =====
sum_L3M_order_value
avg_L6M_order_value
count_L3M_orders
count_distinct_L6M_categories
std_L3M_order_value

# ===== SaaS =====
sum_L1M_session_minutes
avg_L3M_session_duration
count_L1M_logins
count_distinct_L3M_features_used
std_L1M_daily_active_minutes

# ===== Viễn thông =====
sum_L3M_data_usage_gb
avg_L6M_call_duration
count_L3M_calls
std_L3M_monthly_bill

# ===== Sản xuất =====
sum_L3M_output_units
avg_L6M_defect_rate
count_L3M_maintenance_events
std_L3M_energy_consumption

# ===== Gaming =====
sum_L1M_playtime_hours
avg_L3M_session_score
count_L1M_sessions
count_distinct_L3M_game_modes
```

### 3.2. Ma Trận Kết Hợp Đầy Đủ

Bảng dưới đây minh họa cách kết hợp **tất cả metrics** × **tất cả timeframes** cho **một feature group**.

Ví dụ cho feature group `event_value` (giá trị sự kiện):

| | **L1M** | **L3M** | **L6M** | **L12M** |
|---|---|---|---|---|
| **SUM** | sum_L1M_value | sum_L3M_value | sum_L6M_value | sum_L12M_value |
| **AVG** | avg_L1M_value | avg_L3M_value | avg_L6M_value | avg_L12M_value |
| **MIN** | min_L1M_value | min_L3M_value | min_L6M_value | min_L12M_value |
| **MAX** | max_L1M_value | max_L3M_value | max_L6M_value | max_L12M_value |
| **STD** | std_L1M_value | std_L3M_value | std_L6M_value | std_L12M_value |
| **COUNT** | count_L1M_events | count_L3M_events | count_L6M_events | count_L12M_events |
| **MEDIAN** | median_L1M_value | median_L3M_value | median_L6M_value | median_L12M_value |

→ **7 metrics × 4 timeframes = 28 features** chỉ cho 1 feature group!

### 3.3. Ước Tính Tổng Số Features

```
Feature Count = [Metrics] × [Timeframes] × [Feature Sub-groups] + [Derived Features]

Ví dụ ước tính:
= 7 metrics (SUM, AVG, MIN, MAX, STD, COUNT, MEDIAN)
  × 4 timeframes (L1M, L3M, L6M, L12M)
  × 5 feature groups (value, count, balance, active_periods, diversity)
  + 30 derived features (ratios, trends, flags)

= 7 × 4 × 5 + 30
= 140 + 30
= 170 features (trước feature selection)

Sau feature selection: 30-80 features cho model
```

> Con số thực tế phụ thuộc vào domain. Ngân hàng (nhiều loại sản phẩm, kênh) → nhiều features hơn. SaaS/Gaming (ít chiều phân tích hơn) → ít features hơn.

---

## 📈 PHẦN IV: ADVANCED FEATURE ENGINEERING

### 4.1. RFM Features (Recency, Frequency, Monetary)

Áp dụng cho **bất kỳ** bài toán nào có entity + event + value.

```python
# === Recency ===
recency_days = (snapshot_date - last_event_date).days
recency_score = pd.cut(recency_days,
                       bins=[0, 7, 30, 90, 180, float('inf')],
                       labels=[5, 4, 3, 2, 1])

# === Frequency ===
frequency = event_count_l12m
frequency_score = pd.qcut(frequency, q=5, labels=[1, 2, 3, 4, 5])

# === Monetary ===
monetary = total_value_l12m
monetary_score = pd.qcut(monetary, q=5, labels=[1, 2, 3, 4, 5])

# === Combined RFM ===
rfm_score = recency_score.astype(int) * 100 + frequency_score.astype(int) * 10 + monetary_score.astype(int)
# 555 → Best entity (recent, frequent, high value)
# 111 → Worst entity (old, rare, low value)

rfm_segment = pd.cut(rfm_score, bins=[0, 222, 333, 444, 555],
                     labels=['At_Risk', 'Need_Attention', 'Potential', 'Champion'])
```

### 4.2. Ratio & Percentage Features

```python
# === Tỷ lệ hướng (Direction ratios) ===
inflow_outflow_ratio = total_inflow / (total_outflow + 1)
# > 1 → Entity nhận nhiều hơn chi
# < 1 → Entity chi nhiều hơn nhận

# === Tỷ lệ sản phẩm (Product ratios) ===
product_penetration = active_products / total_available_products
cross_sell_ratio = total_products / initial_products

# === Tỷ lệ hoạt động (Activity ratios) ===
active_period_ratio = active_periods / total_periods
dormant_period_ratio = dormant_periods / total_periods

# === Tỷ lệ sự kiện (Event ratios) ===
positive_event_pct = positive_events / (total_events + 1)
negative_event_pct = negative_events / (total_events + 1)
event_success_rate = successful_events / (total_events + 1)
```

### 4.3. Trend & Velocity Features

```python
# === Growth rates — Tốc độ tăng trưởng ===
value_growth_mom = (value_L1M - value_P1M) / (abs(value_P1M) + 1)   # Month-over-Month
value_growth_qoq = (value_L3M - value_P3M) / (abs(value_P3M) + 1)   # Quarter-over-Quarter
value_growth_yoy = (value_L12M - value_P12M) / (abs(value_P12M) + 1) # Year-over-Year

# === Velocity — Vận tốc ===
spending_velocity = value_L3M / 3   # Giá trị trung bình mỗi tháng (3 tháng gần)
spending_velocity_prev = value_P3M / 3
velocity_change = spending_velocity - spending_velocity_prev

# === Moving Average Distance ===
ma_3m = value_L3M / 3
ma_6m = value_L6M / 6
distance_from_ma = (ma_3m - ma_6m) / (abs(ma_6m) + 1)
# Dương → Gần đây cao hơn trung bình dài hạn (xu hướng tăng)
# Âm → Gần đây thấp hơn trung bình dài hạn (xu hướng giảm)
```

### 4.4. Volatility & Anomaly Features

```python
# === Volatility — Biến động ===
value_volatility = std_L3M_value
value_cv = std_L3M_value / (avg_L3M_value + 1)  # Coefficient of Variation

# === Z-Score — Phát hiện bất thường ===
z_score = (current_value - avg_historical) / (std_historical + 1)
# |z_score| > 2 → Bất thường vừa
# |z_score| > 3 → Bất thường nghiêm trọng (outlier)

is_anomaly = 1 if abs(z_score) > 3 else 0

# === IQR-based outlier ===
iqr = p75 - p25
lower_bound = p25 - 1.5 * iqr
upper_bound = p75 + 1.5 * iqr
is_outlier = 1 if (value < lower_bound) or (value > upper_bound) else 0
```

### 4.5. Interaction Features — Đặc trưng tương tác

```python
# === Kết hợp 2 features để tạo feature mới ===

# Tenure × Value
tenure_value_interaction = tenure_months * total_value_l12m
# Entity lâu năm + giá trị cao → VIP

# Age × Activity
age_activity_interaction = age * active_period_ratio
# Người trẻ + hoạt động nhiều → Segment khác biệt

# Product × Engagement
product_engagement = active_product_count * active_period_ratio
# Nhiều sản phẩm + hoạt động thường xuyên → Rất gắn bó

# Value × Frequency
value_frequency = avg_value_per_event * event_count_l3m
# Tương tự Monetary × Frequency trong RFM
```

---

## 🛠️ PHẦN V: PIPELINE TỔNG QUÁT

### 5.1. Template Code — Feature Engineering Pipeline

```python
import pandas as pd
import numpy as np
from datetime import datetime
from scipy.stats import skew, kurtosis


def build_features(df, entity_col, date_col, value_col, snapshot_date,
                   timeframes=None):
    """
    Feature Engineering Pipeline tổng quát.
    
    Parameters:
    -----------
    df : DataFrame
        Dữ liệu sự kiện (event log) với ít nhất 3 cột: entity, date, value
    entity_col : str
        Tên cột entity (customer_id, user_id, machine_id,...)
    date_col : str
        Tên cột ngày sự kiện
    value_col : str
        Tên cột giá trị sự kiện
    snapshot_date : datetime
        Ngày quan sát (thời điểm tạo features)
    timeframes : dict, optional
        Dict {tên: số ngày}. Mặc định: L1M=30, L3M=90, L6M=180, L12M=365
    
    Returns:
    --------
    DataFrame với entity_col là index và các features là columns.
    """
    
    if timeframes is None:
        timeframes = {
            'L1M': 30,
            'L3M': 90,
            'L6M': 180,
            'L12M': 365
        }
    
    # Convert date
    df[date_col] = pd.to_datetime(df[date_col])
    snapshot_date = pd.to_datetime(snapshot_date)
    
    all_features = pd.DataFrame(index=df[entity_col].unique())
    all_features.index.name = entity_col
    
    # ============================================================
    # 1. TENURE
    # ============================================================
    first_event = df.groupby(entity_col)[date_col].min()
    all_features['tenure_days'] = (snapshot_date - first_event).dt.days
    all_features['tenure_months'] = all_features['tenure_days'] / 30
    
    # ============================================================
    # 2. RECENCY
    # ============================================================
    last_event = df.groupby(entity_col)[date_col].max()
    all_features['recency_days'] = (snapshot_date - last_event).dt.days
    all_features['is_dormant'] = (all_features['recency_days'] > 90).astype(int)
    
    # ============================================================
    # 3. TIMEFRAME-BASED FEATURES: [Metric] × [Timeframe]
    # ============================================================
    for tf_name, tf_days in timeframes.items():
        start = snapshot_date - pd.Timedelta(days=tf_days)
        mask = (df[date_col] > start) & (df[date_col] <= snapshot_date)
        period_df = df[mask]
        
        grp = period_df.groupby(entity_col)[value_col]
        
        # Basic aggregations
        all_features[f'sum_{tf_name}'] = grp.sum()
        all_features[f'avg_{tf_name}'] = grp.mean()
        all_features[f'min_{tf_name}'] = grp.min()
        all_features[f'max_{tf_name}'] = grp.max()
        all_features[f'std_{tf_name}'] = grp.std()
        all_features[f'count_{tf_name}'] = grp.count()
        all_features[f'median_{tf_name}'] = grp.median()
        
        # Active periods (distinct months)
        if tf_days >= 30:
            active_months = (
                period_df
                .assign(month=period_df[date_col].dt.to_period('M'))
                .groupby(entity_col)['month']
                .nunique()
            )
            total_months = max(tf_days // 30, 1)
            all_features[f'active_months_{tf_name}'] = active_months
            all_features[f'activity_ratio_{tf_name}'] = active_months / total_months
        
        # Event diversity (distinct dates as proxy)
        active_days = period_df.groupby(entity_col)[date_col].nunique()
        all_features[f'active_days_{tf_name}'] = active_days
    
    # ============================================================
    # 4. COMPARISON / TREND FEATURES
    # ============================================================
    for tf_name, tf_days in timeframes.items():
        p_name = f'P{tf_name[1:]}'  # L3M → P3M
        
        # Previous period
        p_start = snapshot_date - pd.Timedelta(days=tf_days * 2)
        p_end = snapshot_date - pd.Timedelta(days=tf_days)
        mask_p = (df[date_col] > p_start) & (df[date_col] <= p_end)
        p_df = df[mask_p]
        
        grp_p = p_df.groupby(entity_col)[value_col]
        all_features[f'sum_{p_name}'] = grp_p.sum()
        all_features[f'count_{p_name}'] = grp_p.count()
        
        # Growth rates
        all_features[f'sum_growth_{tf_name}_vs_{p_name}'] = (
            (all_features[f'sum_{tf_name}'] - all_features[f'sum_{p_name}'])
            / (all_features[f'sum_{p_name}'].abs() + 1)
        )
        all_features[f'count_growth_{tf_name}_vs_{p_name}'] = (
            (all_features[f'count_{tf_name}'] - all_features[f'count_{p_name}'])
            / (all_features[f'count_{p_name}'].abs() + 1)
        )
        
        # Absolute change
        all_features[f'sum_change_{tf_name}_vs_{p_name}'] = (
            all_features[f'sum_{tf_name}'] - all_features[f'sum_{p_name}']
        )
    
    # ============================================================
    # 5. ADVANCED METRICS
    # ============================================================
    # Coefficient of Variation
    for tf_name in timeframes:
        all_features[f'cv_{tf_name}'] = (
            all_features[f'std_{tf_name}'] / (all_features[f'avg_{tf_name}'].abs() + 1)
        )
    
    # Average value per event (ticket size)
    for tf_name in timeframes:
        all_features[f'avg_per_event_{tf_name}'] = (
            all_features[f'sum_{tf_name}'] / (all_features[f'count_{tf_name}'] + 1)
        )
    
    # ============================================================
    # 6. FILL NaN
    # ============================================================
    # Count & Sum features: fill 0 (không có sự kiện = 0)
    fill_zero_cols = [c for c in all_features.columns
                      if c.startswith(('sum_', 'count_', 'active_'))]
    all_features[fill_zero_cols] = all_features[fill_zero_cols].fillna(0)
    
    # Other features: fill 0
    all_features = all_features.fillna(0)
    
    return all_features


# ============================================================
# USAGE EXAMPLE
# ============================================================
# # Banking
# features = build_features(transactions, 'customer_id', 'txn_date', 'amount', '2025-12-31')
#
# # E-commerce
# features = build_features(orders, 'user_id', 'order_date', 'order_value', '2025-12-31')
#
# # SaaS
# features = build_features(sessions, 'user_id', 'session_date', 'duration_min', '2025-12-31')
#
# # Manufacturing
# features = build_features(sensor_logs, 'machine_id', 'log_date', 'reading_value', '2025-12-31')
```

---

## 📊 PHẦN VI: FEATURE SELECTION & OPTIMIZATION

### 6.1. Bước 1 — Loại bỏ features ít biến động

```python
from sklearn.feature_selection import VarianceThreshold

selector = VarianceThreshold(threshold=0.01)
X_filtered = selector.fit_transform(X)
kept_features = X.columns[selector.get_support()].tolist()
print(f"Giữ lại {len(kept_features)} / {X.shape[1]} features")
```

### 6.2. Bước 2 — Loại bỏ features tương quan cao (Multicollinearity)

```python
corr_matrix = X[kept_features].corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [col for col in upper.columns if any(upper[col] > 0.95)]
X_reduced = X.drop(columns=to_drop)
print(f"Loại bỏ {len(to_drop)} features tương quan cao")
```

### 6.3. Bước 3 — Feature Importance (chọn features quan trọng)

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

importance_df = (
    pd.DataFrame({'feature': X_train.columns, 'importance': rf.feature_importances_})
    .sort_values('importance', ascending=False)
)

# Chọn top N features
top_n = 50
selected_features = importance_df.head(top_n)['feature'].tolist()
```

### 6.4. Bước 4 — Mutual Information (đo lượng thông tin)

```python
from sklearn.feature_selection import mutual_info_classif

mi_scores = mutual_info_classif(X_train, y_train, random_state=42)
mi_df = (
    pd.DataFrame({'feature': X_train.columns, 'mi_score': mi_scores})
    .sort_values('mi_score', ascending=False)
)

# Chọn features có MI > ngưỡng
selected = mi_df[mi_df['mi_score'] > 0.01]['feature'].tolist()
```

---

## 🎯 PHẦN VII: TỔNG KẾT & CHECKLIST

### 7.1. Feature Engineering Checklist (Áp dụng mọi ngành)

| # | Nhóm Feature | Câu hỏi cần trả lời | Đã tạo? |
|---|-------------|---------------------|---------|
| 1 | **Tenure** | Entity đã ở bao lâu? | ☐ |
| 2 | **Avg Value per Event** | Mỗi sự kiện có giá trị bao nhiêu? | ☐ |
| 3 | **Current State / Balance** | Trạng thái hiện tại là gì? | ☐ |
| 4 | **Event Count** | Có bao nhiêu sự kiện? | ☐ |
| 5 | **Event Value** | Tổng giá trị sự kiện? | ☐ |
| 6 | **Active Products / Services** | Đang dùng bao nhiêu sản phẩm? | ☐ |
| 7 | **Active Periods** | Bao nhiêu kỳ có hoạt động? | ☐ |
| 8 | **Recency** | Lần cuối hoạt động khi nào? | ☐ |
| 9 | **Event Diversity** | Hoạt động đa dạng hay tập trung? | ☐ |
| 10 | **Demographics / Static** | Thuộc tính tĩnh của entity? | ☐ |
| 11 | **Timeframe Aggregations** | Đã tính cho L1M, L3M, L6M, L12M? | ☐ |
| 12 | **Comparison Windows** | Đã so sánh L3M vs P3M, L6M vs P6M? | ☐ |
| 13 | **Growth Rates** | Tốc độ thay đổi? | ☐ |
| 14 | **Volatility** | Mức biến động (STD, CV)? | ☐ |
| 15 | **RFM Score** | Đã tính RFM? | ☐ |
| 16 | **Ratios** | Các tỷ lệ quan trọng? | ☐ |
| 17 | **Anomaly Flags** | Cờ cảnh báo bất thường? | ☐ |
| 18 | **Interaction Features** | Kết hợp giữa các features? | ☐ |

### 7.2. Best Practices

#### 1. Bắt đầu đơn giản, mở rộng dần

```
Step 1: Tạo features cơ bản (Tenure, Recency, Count, Sum)               → ~20 features
Step 2: Thêm timeframe variations (×4 timeframes)                        → ~80 features
Step 3: Thêm advanced metrics (STD, CV, Percentiles)                     → ~120 features
Step 4: Thêm comparison/trend features (growth, change)                  → ~160 features
Step 5: Thêm derived features (RFM, ratios, flags, interactions)         → ~200 features
Step 6: Feature selection → Giữ lại 30-80 features hữu ích cho model
```

#### 2. Xử lý Missing Values

```python
# Chiến lược theo loại feature:
fill_strategy = {
    'count_*':   0,        # Không có sự kiện = 0
    'sum_*':     0,        # Không có giá trị = 0
    'avg_*':     0,        # Hoặc median nếu cần
    'std_*':     0,        # Không có biến động = 0
    'ratio_*':   0,        # Hoặc -1 để đánh dấu missing
    'flag_*':    0,        # Không có cờ = 0
    'tenure_*':  median,   # Dùng median
}
```

#### 3. Đặt tên Feature rõ ràng

```python
# ✅ Tốt: tự mô tả, có cấu trúc
sum_L3M_order_value
avg_L6M_session_duration
count_growth_L3M_vs_P3M

# ❌ Tệ: không rõ nghĩa
f1, f2, f3
feature_x_1
data_col_new
```

#### 4. Luôn document features

```python
feature_dictionary = {
    'sum_L3M_order_value': {
        'description': 'Tổng giá trị đơn hàng trong 3 tháng gần nhất',
        'formula': 'SUM(order_value) WHERE date >= snapshot - 90 days',
        'type': 'numeric',
        'missing_strategy': 'fill 0',
        'business_meaning': 'Tổng chi tiêu ngắn hạn — chỉ số sức mua'
    },
}
```

---

**Course: Machine Learning for Data Analytics**
**Module: Feature Engineering Framework - General (Industry-Agnostic)**
