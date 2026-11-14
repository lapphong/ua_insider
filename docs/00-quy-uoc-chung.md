# Quy ước chung — người học, ngôn ngữ, nhãn số

> Áp dụng cho **mọi bài tập** trong dự án này. Không phải quy ước riêng của bài 1.

## 1. Người học & cách dạy

- Newbie tự học UA Marketing, trao đổi bằng **tiếng Việt**. Thuật ngữ UA giữ **tiếng Anh** (CPI, CAC, eCPM, ROAS, LTV…).
- Giải thích **tại sao** con số đó quan trọng, không chỉ đưa công thức.
- Mỗi mục ghi rõ **dùng công cụ gì để check** + **nguồn ở đâu**.
- Đánh dấu rõ **số thật / số giả** — không được lẫn lộn. Đây là yêu cầu cứng, không phải trang trí.
- Ưu tiên hiểu **vòng tiền**, không cần hoàn hảo. App chỉ cần "tương đối đúng"; phần thiếu thì mô phỏng **có ghi chú**.
- Người học đọc bài bằng mắt trên bảng tính / trang đọc, không click từng ô Excel. Vì vậy công thức và nguồn phải **nhìn thấy được** ngay trên bảng.

## 2. Nhãn số liệu (BẮT BUỘC)

| Nhãn | Nghĩa | Yêu cầu |
|------|-------|---------|
| 🟩 **REAL** | Lấy trực tiếp từ nguồn công khai | Có link + ngày lấy |
| 🟨 **ASSUMED** | Giả định có căn cứ | Ghi benchmark gốc dùng để suy ra |
| 🟥 **FAKE** | Bịa để bài chạy được | Ghi rõ "số bịa — không dùng để ra quyết định thật" |

- Mỗi con số trong bảng tính có nhãn ở cột `Nguồn/Loại`. Không có ngoại lệ.
- Mọi thứ không lấy được từ nguồn công khai (doanh thu, CPI, eCPM, retention, churn, payer rate, phân tầng user) mặc định là **mô phỏng**: 🟨 nếu có benchmark ngành làm căn cứ, 🟥 nếu bịa thuần.
- Benchmark gốc phải ghi ở sheet tra cứu (`F_Nguon_Cong_Cu`), không chỉ nói "theo ngành".

## 3. Nguyên tắc chọn số

1. Số **thật** lấy trước (app store listing, báo cáo công khai) — có link + ngày.
2. Thiếu số thật → lấy **benchmark ngành** rồi suy ra, ghi rõ benchmark nào.
3. Vẫn thiếu → **bịa có ghi chú**, và số bịa không được dùng để ra kết luận quan trọng.
4. Không bao giờ để hai nguồn mâu thuẫn trong cùng file: một số chỉ có **một** ô gốc, chỗ khác tham chiếu tới.

## 4. Từ điển nhanh

- **CPI** — Cost Per Install (chỉ tiền media).
- **CAC** — Customer Acquisition Cost (toàn bộ chi phí để có 1 user trả tiền, đã trừ phí sàn).
- **eCPM** — doanh thu / 1000 impression.
- **ROAS** — doanh thu ÷ chi phí quảng cáo, theo cửa sổ ngày.
- **LTV** — tổng doanh thu 1 user mang lại trong vòng đời.
- **pLTV** — LTV dự phóng từ tín hiệu sớm (24h).
- **Payback** — số ngày để doanh thu tích lũy = CAC.
- **Gross margin sau phí sàn** — doanh thu còn lại sau khi store lấy 15–30%.
- **tROAS** — target ROAS khi chạy campaign.
- **Whale / Dolphin / Minnow** — tầng chi tiêu: cá voi / cá heo / cá nhỏ.

## 5. Công cụ & nguồn — mỗi chỉ số một chỗ check

| Chỉ số | Cần check gì | Công cụ / nguồn |
|--------|--------------|-----------------|
| Monetization | app có Ads? có IAP? giá IAP? | Google Play / App Store listing (🟩 REAL) |
| CPI / CAC | giá media, non-media cost | Ads Manager / benchmark ngành |
| eCPM | eCPM theo geo + format | AdMob / AppLovin / ironSource benchmark |
| ROAS | doanh thu tích lũy theo ngày | MMP cohort report |
| LTV | ARPU, churn, mix doanh thu | tính từ cohort + công thức |
| pLTV | tín hiệu 24h | MMP + event tracking |
| LTV:CAC | tổng hợp | tính |
| Phân tầng user | phân bố doanh thu theo payer | phân tích cohort thanh toán |

Chi tiết + cách tự kiểm từng bước nằm trong sheet `F_Nguon_Cong_Cu` của từng file bài làm.

## 6. Cách trao đổi trong phiên

- Người học hay yêu cầu **sửa giao diện** nhiều vòng. Mỗi vòng: sửa **script sinh ra file**, chạy máy kiểm, báo lại **số đo thật** (không nói "đã sửa xong" bằng mắt).
- Khi người học nói "đã chốt, không sửa nữa" → ghi vào docs thành mục **CHỐT**, lần sau làm đúng như bảng đó, không "cải tiến" thêm.
- Khi người học đã bác một hướng (ví dụ bỏ một nút, bỏ một câu chữ) → không tự thêm lại.
- Chỉ đọc đúng file docs liên quan tới việc đang làm; đừng đọc cả `docs/` mỗi phiên.
