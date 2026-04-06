# Dự đoán khả năng khách hàng phát sinh mua hàng trong tháng tiếp theo trên website thương mại điện tử

# 1. Vấn đề 
- Trong thương mại điện tử, doanh nghiệp thường sở hữu lượng lớn dữ liệu lịch sử mua hàng của khách hàng theo thời gian. Tuy nhiên, không phải tất cả khách hàng đều có cùng khả năng quay lại mua hàng. Việc áp dụng chiến dịch marketing đồng nhất cho toàn bộ khách hàng dẫn đến lãng phí ngân sách, trong khi những khách hàng tiềm năng nhất lại không nhận được sự chú ý xứng đáng.

- Thách thức cốt lõi là xác định **nhóm khách hàng có xác suất mua lại tầm trung** - đây là nhóm mang lại cơ hội tăng trưởng lớn nhất. Những khách hàng này có tiềm năng nhưng cần thêm động lực để chuyển đổi thành khách hàng trung thành. Ngược lại, nhóm khách hàng có xác suất cực thấp nên được tối ưu hóa chi phí marketing, trong khi nhóm khách hàng có xác suất cao sẽ tự quay lại mua hàng mà không cần can thiệp nhiều.

- Nếu doanh nghiệp có thể dự đoán chính xác và phân loại khách hàng thành 3 nhóm theo xác suất mua lại, hệ thống có thể áp dụng chiến lược phù hợp:
  - **Nhóm Khách hàng Tự hành**: Tự động quay lại mua hàng, chỉ cần chương trình tri ân nhẹ, loyalty program cơ bản để duy trì.
  - **Nhóm Trọng tâm Tăng trưởng**: **Đây là nhóm mục tiêu chính** - cần tập trung ngân sách marketing để áp dụng voucher, ưu đãi đặc biệt, remarketing cá nhân hóa nhằm khuyến khích chuyển lên nhóm cao.
  - **Nhóm Tối ưu Hóa Chi phí**: Không nên chi nhiều ngân sách, có thể áp dụng chiến lược tiết kiệm hoặc bỏ qua.

- Việc tập trung vào nhóm **Trọng tâm Tăng trưởng** giúp doanh nghiệp tối đa hóa hiệu quả đầu tư marketing: Thay vì "cứu" khách hàng đã rời bỏ hoặc lãng phí tiền cho khách hàng tự quay lại, doanh nghiệp đẩy nhanh tốc độ chuyển đổi của nhóm khách hàng đang ở ngưỡng cửa quyết định.

# 2. Nội dung đề tài
Đề tài tập trung phân tích dữ liệu lịch sử mua sắm của khách hàng trên nền tảng thương mại điện tử, bao gồm thông tin về khách hàng, thời điểm đặt hàng, sản phẩm đã mua và giá trị đơn hàng. Trên cơ sở đó, xây dựng mô hình Machine Learning nhằm dự đoán khả năng khách hàng sẽ phát sinh mua hàng trong tháng tiếp theo, sau đó phân loại vào 3 nhóm tiềm năng để tối ưu chiến lược marketing: **tập trung ưu đãi cho nhóm tầm trung**, **tối ưu chi phí cho nhóm thấp**, và **giữ chân nhẹ nhàng cho nhóm cao**.

# 3. Nội Dung Cần Thực Hiện
1. Tạo và chuẩn bị dữ liệu
2. Phân tích dữ liệu
3. Tiền xử lý
4. Tạo file Snapshot data
5. Feature Engineering
6. Feature Selection
7. Xây dựng và đánh giá mô hình
8. Triển khai và báo cáo
9. Thiết kế và phát triển ứng dụng web

# 3.1 Tạo và chuẩn bị dữ liệu
Dự án sử dụng **bộ dữ liệu Online Retail II** từ Kaggle (sheet 2009-2010 và 2010-2011) với 1,067,371 dòng dữ liệu giao dịch.
 
Các bước xử lý dữ liệu gốc:
- Gộp 2 sheet dữ liệu và làm sạch (xóa dòng thiếu Customer ID, Description)
- Chuẩn hóa định dạng: Customer ID → string, InvoiceDate → datetime
- Xác định đơn hủy (`is_canceled`) dựa trên mã hóa đơn chứa 'C' hoặc Quantity < 0
- Phân loại sản phẩm vào 11 nhóm: fees_services, seasonal, kitchen_food, home_decor, stationery_craft, toys_gifts, storage_bags, accessories, garden_outdoor, furniture, design_vintage
- Tính giá trị thành tiền: `valid_spend = Quantity × unit_price`
- Groupby theo Customer_id, Invoice, InvoiceDate để tạo thành file transaction hoàn chỉnh.

Chi tiết các biến trong file:

| Cột                  | Ý nghĩa                                 
| -------------------- | --------------------------------------- | 
| Customer_id          | Mã định danh duy nhất của khách hàng    | 
| Order_id             | Mã hóa đơn (Invoice Number)             | 
| Order_date           | Thời điểm khách hàng giao dịch          | 
| Order_value          | Tổng giá trị hóa đơn (đã trừ trả hàng)  | 
| Order_n_lines        | Số lượng SKU khác nhau trong đơn        | 
| Order_n_categories   | Số lượng ngành hàng khác nhau           | 
| Total_item           | Tổng lượng sản phẩm                     | 
| Log_items            | Tổng lượng sản phẩm (đã xử lý Log)      |
| Country              | Quốc gia cư trú (UK/Quốc tế)            | 
| Is_canceled          | Đơn này bị hủy không? (0/1)             | 
| Canceled_value       | Giá trị tiền bị hủy trong đơn này       | 


Các biến này được sử dụng nhằm phản ánh:

- Lịch sử và thâm niên: Thời gian gắn bó và độ tươi mới của khách hàng.

- Hành vi chi tiêu: Mức chi tiêu trung bình (AOV) và cường độ đơn hàng gần nhất.

- Bản chất khách hàng: Phân biệt khách sỉ (mua chuyên sâu) và khách lẻ (mua dàn trải).

Cấu trúc dữ liệu:
- Transaction Data: Dữ liệu đã được tiền xử lý và tổng hợp về cấp độ Đơn hàng (Order Level).
- Modeling Dataset (Snapshot): Dữ liệu được tạo ra từ phương pháp Rolling Window để huấn luyện mô hình.

# a. Transaction data
Bảng Transaction được xây dựng dựa trên dữ liệu giao dịch bán lẻ trực tuyến, trong đó quá trình xử lý dữ liệu trải qua hai cấp độ chính:

- Dữ liệu gốc (Retail - Order Item level): Đây là nguồn dữ liệu chi tiết nhất, trong đó mỗi dòng đại diện cho một mã hàng (StockCode) được mua trong một hóa đơn (Invoice). Dữ liệu này chứa các thông tin về số lượng (Quantity), đơn giá (Price), và mô tả sản phẩm (Description).

- Dữ liệu tổng hợp (Transaction - Order level): Từ dữ liệu gốc, chúng tôi thực hiện gom nhóm (Group by) theo mã đơn hàng và mã khách hàng để tạo ra bảng Transaction. Tại đây, mỗi dòng đại diện cho một đơn hàng duy nhất của một khách hàng tại một thời điểm cụ thể.

Bảng này đóng vai trò là "xương sống" để xây dựng các đặc trưng hành vi (Feature Engineering). Các biến quan trọng như tổng giá trị đơn hàng (Order_value), độ rộng giỏ hàng (Order_n_lines) và các biến chiến lược như độ chuyên sâu ngành hàng (Diversity) đều được tính toán từ cấp độ này.


# 3.2 Phân tích dữ liệu
## 3.2.1 Thực hiện EDA (Exploratory Data Analysis) 
Mục tiêu của bước này là hiểu tổng quan cấu trúc dữ liệu và đặc điểm hành vi mua hàng của khách hàng trước khi xây dựng mô hình.
Các bước thực hiện:
- Kiểm tra tổng quan dataset (cấu trúc dữ liệu, kiểu dữ liệu, thống kê mô tả cơ bản)
- Kiểm tra số lượng các thực thể chính như số khách hàng, số đơn hàng, số sản phẩm và số danh mục sản phẩm
- Kiểm tra giá trị thiếu (missing values) trong dataset

## 3.2.2 Trực quan hóa dữ liệu và tìm hiểu mối quan hệ giữa các biến
Mục tiêu của bước này là phân tích hành vi mua hàng của khách hàng và khám phá các pattern quan trọng có thể ảnh hưởng đến khả năng mua lại trong tương lai.
Các phân tích chính bao gồm:
- Phân tích biến động doanh thu theo thời gian
- Phân tích phân phối Recency
- Phân tích phân phối Frequency
- Phân tích phân phối Monetary
- Phân tích tương quan giữa Tần suất và Giá trị đơn hàng
- Phân tích đóng góp doanh thu theo địa lý
- Khám phá đặc điểm phân bổ của các biến số
- Phân tích danh mục sản phẩm chủ lực
- Phân tích ma trận tương quan RFM

# 3.3 Tiền xử lý
- Xử lý giá trị outlier bằng phương pháp Capping (Chặn đầu dữ liệu): valid_spend, Quantity (Đối với giá trị dương)
- Áp dụng kỹ thuật Log Transform: Quantity (Đối với giá trị dương)
- Chuẩn hóa dữ liệu và định danh đơn hàng hợp lệ

# 3.4 Xây dựng Snapshot Dataset

## 3.4.1 Transaction Data

Bảng Transaction được xây dựng bằng GroupBy theo `Customer ID`, `Invoice`, `InvoiceDate` với các cột:
| Cột | Cách tính | Ý nghĩa |
|-----|-----------|---------|
| order_value | sum(valid_spend_capped) | Doanh thu thuần (đã trừ đơn hủy) |
| is_canceled | max(is_canceled) | 1 nếu có bất kỳ dòng nào bị hủy |
| total_items | sum(Quantity_capped) | Tổng số lượng sản phẩm |
| Order_n_lines | count(StockCode) | Số lượng sản phẩm khác nhau |
| Order_n_categories | count(category) | Số ngành hàng khác nhau |
| Log_items | sum(log_qty) | Tổng sản phẩm dạng Log |
| Canceled_value | sum(valid_spend where is_canceled=1) | Giá trị đơn hủy |
| items_per_cat | Order_n_lines / Order_n_categories | Tỷ lệ chuyên sâu/dàn trải |



Từ bảng transaction, tập dữ liệu modeling được xây dựng bằng phương pháp rolling snapshot theo thời gian.

Mỗi snapshot được xác định tại ngày cuối cùng của một tháng (cutoff date). Tại thời điểm này, dữ liệu giao dịch của khách hàng trong một khoảng thời gian quá khứ, gọi là Observation Window, được sử dụng để tính toán và gán nhãn:
- Số đơn hàng đã phát sinh
- Tổng giá trị chi tiêu
- Giá trị đơn hàng trung bình trong Observation Window
- Các biến này phản ánh mức độ hoạt động gần đây và mức độ gắn kết mua sắm của khách hàng.

Sau thời điểm snapshot, một khoảng thời gian tiếp theo (Performance Window) được sử dụng để xác định biến mục tiêu, thể hiện việc khách hàng có phát sinh giao dịch mua lại hay không.

Độ dài Observation Window được lựa chọn dựa trên phân tích trực quan dữ liệu nhằm phản ánh tốt nhất chu kỳ mua sắm điển hình của khách hàng.

Performance Window (Cửa sổ thực thi): Một khoảng thời gian tiếp theo sau Snapshot được sử dụng để xác định biến mục tiêu (Label). Khoảng thời gian này đủ dài để quan sát khả năng quay lại mua sắm của khách hàng trong một chu kỳ tiêu dùng tiêu chuẩn.

## Xác định biến mục tiêu
Biến mục tiêu được xây dựng bằng cách kiểm tra nếu khách hàng có AOV_Future > 0 và ratio (AOV tháng dự đoán/AOV_L5M) >= 0.5 thì sẽ được gán nhãn 1 (có mua lại). Các trường hợp còn lại sẽ gán là 0 (không mua lại).

Ràng buộc: Chỉ xét khách hàng trên 2 tháng hoạt động liên tục trong 5 tháng qua (đảm bảo đủ dữ liệu hành vi).

Tại mỗi thời điểm snapshot, tập dữ liệu modeling bao gồm toàn bộ khách hàng đã từng phát sinh giao dịch trong phạm vi Observation Window. Quy trình được lặp lại cho nhiều thời điểm cutoff khác nhau nhằm xây dựng tập dữ liệu theo cấu trúc thời gian để huấn luyện mô hình dự đoán khả năng khách hàng mua lại trong tháng tiếp theo.

# 3.5. Feature Engineering
Từ các feature ban đầu, thực hiện phái sinh ra nhiều feature theo cấu trúc: `{Metric}_{Feature}_{TimeFrame}`

| Nhóm (Group)     | Cột gốc                       | Metric (Hàm)                  | TimeFrame     | Tên feature                       | Giải thích ý nghĩa                                                          |
| ---------------- | ----------------------------- | ----------------------------- | ------------- | --------------------------------- | --------------------------------------------------------------------------- |
| Monetary         | Order_value                   | sum                           | L1M, L3M, L5M | sum_LxM_value                     | Tổng chi tiêu thực tế qua các mốc 1, 3, 5 tháng                             |
|                  | Order_value                   | mean                          | L1M, L3M, L5M | avg_LxM_value                     | Giá trị đơn hàng trung bình (AOV) từng thời kỳ                              |
|                  | Order_value                   | std                           | L1M, L3M, L5M | std_LxM_value                     | Chi tiêu đều đặn (std thấp) hay đột biến (std cao)                          |
|                  | Order_value                   | max                           | L1M, L3M, L5M | max_LxM_value                     | Giá trị đơn hàng lớn nhất - Phát hiện khách VIP tiềm năng                   |
|                  | Order_value                   | min                           | L1M, L3M, L5M | min_LxM_value                     | Giá trị đơn hàng nhỏ nhất - Phân biệt khách "test buy"                      |
|                  | Order_value                   | percentile(75)                | L1M, L3M, L5M | p75_LxM_value                     | Phân vị 75 - 75% đơn dưới ngưỡng nào                                        |
|                  | Order_value                   | percentile(95)                | L1M, L3M, L5M | p95_LxM_value                     | Phân vị 95 - Giá trị đơn cao cấp                                            |
|                  | Order_value                   | iqr (P75-P25)                 | L1M, L3M, L5M | iqr_LxM_value                     | Khoảng cách phân vị - Độ rộng phân bố                                       |
| Frequency        | Order_id                      | count                         | L1M, L3M, L5M | cnt_LxM_orders                    | Tần suất đặt đơn (Đo độ "nghiện" mua sắm)                                   |
| Recency          | Order_date                    | Snap − Max                    | History       | recency_days                      | Số ngày kể từ lần mua hàng cuối cùng                                        |
| Tenure           | Order_date                    | Snap − Min                    | History       | tenure_days                       | Thâm niên/Độ gắn bó của khách với sàn                                       |
| Basket Size      | Order_n_lines                 | mean                          | L1M, L3M, L5M | avg_LxM_skus                      | Độ rộng giỏ hàng (Số lượng trung bình sản phẩm unique)                      |
|                  | Order_n_lines                 | max                           | L1M, L3M, L5M | max_LxM_skus                      | Số SKU max trong 1 đơn - Đặc trưng khách sỉ vs lẻ                           |
|                  | Log_items                     | sum                           | L1M, L3M, L5M | sum_LxM_items_log                 | Tổng số lượng sản phẩm (dạng Log để khử nhiễu)                              |
|                  | Log_items                     | mean                          | L1M, L3M, L5M | avg_LxM_items_log                 | Quy mô sản phẩm trung bình mỗi đơn (dạng Log)                               |
| Category Stats   | Order_n_categories            | mean                          | L1M, L3M, L5M | avg_n_categories_LxM              | Số danh mục trung bình mỗi đơn                                              |
|                  | Order_n_categories            | sum                           | L1M, L3M, L5M | sum_n_categories_LxM              | Tổng số danh mục qua các đơn                                                |
| Diversity        | items_per_cat                 | mean                          | L1M, L3M, L5M | avg_items_per_cat_LxM             | Số sản phẩm trung bình trên mỗi danh mục (Order_n_lines/Order_n_categories) |
|                  | sum_n_categories / cnt_orders | formula                       | L1M, L3M, L5M | category_diversity_LxM            | Tỷ lệ đa dạng danh mục trên mỗi đơn                                         |
| Risk & Quality   | Is_canceled                   | sum                           | L1M, L3M, L5M | sum_LxM_canceled                  | Số lượng đơn hàng bị khách chủ động hủy                                     |
|                  | Is_canceled, Order_id         | sum / count                   | L1M, L3M, L5M | cancel_rate_LxM                   | Tỷ lệ đơn bị lỗi/hủy theo từng kỳ L1M/L3M/L5M                               |
|                  | Canceled_value, Order_value   | sum / sum                     | History       | global_cancel_val_ratio           | Tỉ lệ tiền hủy/tiền đặt lịch sử (Phát hiện VIP ảo)                          |
|                  | Is_canceled                   | last                          | History       | last_order_canceled               | Đơn gần nhất có bị hủy không?                                               |
| Intensity        | Order_value                   | last / global_aov             | Last Order    | last_order_intensity              | Cường độ đơn hàng gần nhất                                                  |
|                  | Order_value                   | last / avg_L3M                | Last Order    | relative_last_order               | Giá trị đơn cuối so với trung bình L3M                                      |
| Velocity         | Order_value                   | sum_L1M / (sum_L3M/3)         | Trend         | spend_velocity                    | Tốc độ chi tiêu đang nóng lên hay nguội đi                                  |
|                  | Order_value                   | (sum_L1M - sum_L3M/3) / (sum_L3M/3 + 1)   | Trend         | value_growth_L1M_vs_L3M           | Tốc độ tăng trưởng chi tiêu tháng gần nhất                                  |
|                  | Order_value                   | (sum_L3M - sum_L5M/5) / (sum_L5M/5 + 1) | Trend         | value_growth_L3M_vs_L5M           | Tốc độ tăng trưởng xu hướng dài hạn                                         |
|                  | Order_id                      | cnt_L1M / (cnt_L3M/3)         | Trend         | order_acceleration                | Gia tốc đặt đơn đang tăng hay giảm                                          |
|                  | Order_id                      | (cnt_L1M - cnt_L3M/3) / (cnt_L3M/3 + 1)   | Trend         | count_growth_L1M_vs_L3M           | Tốc độ tăng trưởng tần suất đặt đơn                                         |
|                  | Order_id                      | cnt_L5M / 5                   | L5M           | order_velocity                    | Tần suất mua hàng trung bình mỗi tháng                                      |
| Activity Density | Order_date                    | count(distinct day)           | L5M           | active_days_L5M                   | Số ngày duy nhất có giao dịch - Đo mức độ "chăm chỉ"                        |
|                  | Order_id, active_days         | cnt_L5M / active_days         | L5M           | orders_per_active_day             | Cường độ mua khi đã vào sàn                                                 |
|                  | Order_value, active_days      | sum_L5M / active_days         | L5M           | revenue_per_active_day            | Doanh thu/ngày hoạt động thực tế                                            |
|                  | Order_id                      | max_daily / avg_daily         | L5M           | burst_ratio_orders                | Tỷ lệ bùng nổ - Ngày mua nhiều bất thường                                   |
| Rhythm           | Order_date                    | mean(gap)                     | L5M           | avg_gap_L5M                       | Chu kỳ mua hàng trung bình                                                  |
|                  | Order_date                    | mode(dayofweek)               | L5M           | preferred_order_day               | Ngày trong tuần hay đặt hàng nhất                                           |
|                  | Order_date                    | count(weekend) / count(total) | L5M           | weekend_order_ratio               | Tỷ lệ đơn cuối tuần                                                         |
| Activity Pattern | Order_date                    | count(distinct month)         | L5M           | active_months_L5M                 | Số tháng mua thực tế trong 5 tháng                                          |
|                  | Order_date                    | max(date) - min(date)         | L5M           | days_between_first_last           | Khoảng thời gian giãn cách đơn đầu-cuối                                     |
|                  | Order_date                    | max consecutive months        | L5M           | consecutive_active_months         | Số tháng liên tiếp có mua                                                   |
|                  | Order_date                    | active_days / days_range      | L5M           | activity_density                  | Mật độ hoạt động                                                            |
| RFM              | recency, frequency, monetary  | RobustScaler transform        | L5M           | rf_value, fm_value, rfm_clv_proxy | R×F, F×M, R×F×M - Proxy cho CLV (dùng RobustScaler)                         |
| Geography        | Country                       | Binary (UK=1, Other=0)        | History       | is_UK                             | Phân loại hành vi khách nội địa vs. quốc tế                                 |


Sau khi thực hiện Feature Engineering, tổng số lượng các cột là 87 cột
                                     

# 3.6 Feature Selection
Sau khi thực hiện Feature Engineering, cần tiến hành lọc ra những feature phù hợp
- Chuẩn bị dữ liệu và xử lý giá trị thiếu
- Chia dữ liệu theo thời gian: chia theo trình tự thời gian (Time-based Split) với 80% dữ liệu thời gian đầu cho tập Train và 20% dữ liệu cuối cùng cho tập Test.
- Lọc biến dựa trên tương quan cao (trên 90%)
- Đánh giá tầm quan trọng bằng Random Forest và giữ lại 85% biến cốt lõi.
- Đo lường quan hệ phi tuyến bằng Mutual Information (MI) và loại bỏ 25% số biến có điểm MI thấp nhất
- Tổng hợp tập đặc trưng cuối cùng
- Lưu trữ tập dữ liệu huấn luyện

Tuy nhiên, cần giữ lại những biến mang giá trị cốt lõi cao mà đôi khi model đánh giá thấp:
- recency_days: Xác định khoảng cách từ giao dịch cuối để nhận diện khách hàng đang "nóng" hay đã rời bỏ.
- tenure_days: Phân biệt khách mới dễ biến động với khách cũ có độ trung thành cao hơn.
- active_months_L5M: Đo mức độ ổn định thói quen mua, tránh đánh giá sai khách mua thưa nhưng đều.
- cancel_rate_L5M: Loại bỏ nhiễu từ đơn hàng ảo và hành vi hủy đơn.
- success_rate_L5M: Tỷ lệ đơn thành công thực tế, giúp phân biệt khách hàng chất lượng cao dễ mua lại.
- spend_velocity: Phát hiện sớm xu hướng giảm chi tiêu trước khi khách rời bỏ hoàn toàn.
- avg_gap_L5M: Giúp model hiểu "nhịp điệu riêng" của từng khách thay vì áp chung một tiêu chuẩn cho tất cả.


Sau khi thực hiện Feature Selection, số lượng feature còn lại là 26 feature đủ để train model.
# 3.7 Train model

## 3.7.1 Chia tập dữ liệu
Chia dữ liệu thành tập train/val/test: 
- Time-based split: chia theo trình tự thời gian (Time-based Split) với tỷ lệ 80/20. Cụ thể, sử dụng 80% dữ liệu thời gian đầu để huấn luyện (Train) và 20% dữ liệu mới nhất để kiểm thử (Test).
- Tiếp theo đó, tập train được chia tiếp 80/20 thành train_main và validation.

## 3.7.2 Train model và đánh giá
Model sử dụng: XGBoost

- Mô hình sẽ được train với phương pháp đánh trọng số. 
- Sau khi train xong sẽ thực hiện kiểm tra Feature Importance để loại bỏ những feature có importance xấp xỉ 0. 
- Vẽ ma trận tương quan để xem và loại bỏ 1 trong 2 feature có độ tương quan cao (trên 90%). Sau đó sẽ thực hiện train lại model baseline. 
- Nếu kết quả sau khi train khá tốt thì tiến hành hyperparameter tuning. 
- Dựa vào kết quả sẽ chọn ra mô hình tốt nhất dựa vào PR-AUC, Precision và Recall. 
- Sau đó tiến hành chọn ngưỡng tối ưu bằng cách thử nghiệm các thresholds từ 0.3 đến 0.9.
- Đánh giá mô hình trên tập test.

## 3.8 Triển khai và báo cáo

Đề xuất Triển khai Thực tế

Dựa trên phân bố xác suất, đề xuất chiến lược 3 nhóm tối ưu ngân sách:

🔥 Nhóm Hot (Prob ≥ 0.60): ~15-20% khách
- Đặc điểm: Tự mua lại được, xác suất cao
- Hành động: Email nhẹ hoặc không ưu đãi
- Chi phí: Thấp (5-10K/khách)
- Lý do: Không cần ưu đãi sâu vẫn mua, tiết kiệm ngân sách

🌤️ Nhóm Warm (Prob 0.40 - 0.60): ~30-35% khách ⭐
- Đặc điểm: Cần đẩy mới mua, nhóm mục tiêu chính
- Hành động: Ưu đãi mạnh (Voucher 20-30% hoặc 50-100K)
- Chi phí: Cao (50-100K/khách)
- Lý do: Đây là "điểm bùng phát" - đúng lúc, đúng chỗ để kích hoạt mua lại
- Precision 51%: Chấp nhận 50% lãng phí để bắt đủ khách tiềm năng

❄️ Nhóm Cold (Prob < 0.40): ~45-50% khách
- Đặc điểm: Xác suất thấp, khó kích hoạt
- Hành động: Không ưu đãi, chỉ gửi email newsletter định kỳ
- Chi phí: Rất thấp (0-5K/khách)
- Lý do: Tránh lãng phí ngân sách cho nhóm khó convert

## 3.9 Thiết kế và phát triển ứng dụng web
### 3.9.1 Mô tả
Xây dựng một ứng dụng web fullstack hoàn chỉnh cho bài toán Online Retail Repurchase Prediction App. Ứng dụng cho phép người dùng nhập lịch sử giao dịch khách hàng trên sàn Online Retail, để dự báo khả năng quay lại mua hàng. hệ thống sẽ sử dụng mô hình Machine Learning để đánh giá và trả về kết quả.

### 3.9.2 Mục tiêu
- Áp dụng kiến thức ML để train và export model phục vụ production
- Xây dựng REST API backend bằng Python
- Xây dựng giao diện frontend hiện đại
- Kết nối database lưu trữ dữ liệu
- Deploy toàn bộ hệ thống lên cloud
- Hiểu quy trình phát triển phần mềm end-to-end

### 3.9.3 Yêu cầu kỹ thuật

| Layer | Công nghệ | Hosting |
|-------|-----------|---------|
| **ML Model** | XGBoost | File `.pkl` trong repo |
| **Backend** | FastAPI (Python) | Render.com |
| **Frontend** | Next.js 14+ | Vercel |
| **Database** | PostgreSQL | Supabase |
| **Version Control** | Git + GitHub | GitHub |

### 3.9.4 Kiến trúc bắt buộc

```
[User Browser]
      ↓ HTTPS
[Frontend - Vercel]
      ↓ REST API (JSON)
[Backend - Render]
      ↓ load model          ↓ SQL
[ML Model file]        [Supabase PostgreSQL]
```

---

### 3.9.5 Yêu cầu chức năng chi tiết
## A. Backend API

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

## B. Database

| STT | Yêu cầu                      | Chi tiết kỹ thuật (Dành cho SQL Editor)                                                                                                                                                                                                                                                                                    | Mức độ   |
| --- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| D1  | Tạo table `repurchase_logs`  | Lưu kết quả dự báo: - id: UUID (Primary Key) đại diện cho mã lượt dự báo. - Customer_id: String (Lấy từ customer_info). - input_data: JSONB (Chỉ lưu mảng transactions). - probability, is_repurchase, potential_level, top_reasons.                                                                                                                                                                                | Bắt buộc |
| D2  | Tạo table `raw_transactions` | Import dữ liệu từ file processed_data.csv vào bảng này. Dữ liệu được giữ nguyên định dạng thô (customer level) để phục vụ tính năng Smart Quick-fill. | Nâng cao |
| D3  | Primary key UUID             | Sử dụng `gen_random_uuid()` cho cả hai bảng để đảm bảo định danh duy nhất.                                                                                                                                                                                                                                                 | Bắt buộc |
| D4  | Bật RLS & Policy             | Cho phép `INSERT` vào `repurchase_logs` và `SELECT` từ `raw_transactions` để lấy dữ liệu mẫu.                                                                                                                                                                                                                              | Bắt buộc |
| D5  | Indexing chiến thuật         | Tạo Index trên `Customer_id` của bảng `raw_transactions` và  `repurchase_logs` để truy vấn lịch sử nhanh chóng.                                                                                                                                                                                                    | Nâng cao |

### C. Frontend


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

### 3.9.6 Deployment

| # | Yêu cầu | Mức độ |
|---|---------|--------|
| P1 | Backend deploy trên Render.com | Bắt buộc |
| P2 | Frontend deploy trên Vercel | Bắt buộc |
| P3 | Database trên Supabase (đã setup) | Bắt buộc |
| P4 | Environment variables cấu hình đúng trên cả Render + Vercel | Bắt buộc |
| P5 | CORS cấu hình đúng (backend allow domain frontend) | Bắt buộc |
| P6 | Auto-deploy khi push code lên GitHub | Nâng cao |