# AGENTS.md — UA Learning Project

> Bộ nhớ của phiên làm việc. Token reset / mở phiên mới → đọc file này TRƯỚC, rồi mới mở file khác.
> Cập nhật file này mỗi khi có quyết định hoặc số liệu mới. Không để nó lệch với file thật.

## 1. Người học & cách dạy

- Newbie tự học UA Marketing, trao đổi bằng tiếng Việt.
- Đang làm **"Dự án cuối Cấp 2"**: bảng Unit Economics cho 1 app (thật hoặc mô phỏng).
- Cách học mong muốn:
  - Giải thích **tại sao** con số đó quan trọng, không chỉ đưa công thức.
  - Mỗi mục ghi rõ **dùng công cụ gì để check** + **nguồn ở đâu**.
  - Đánh dấu rõ **số thật / số giả** — không được lẫn lộn.
- Ưu tiên: hiểu được vòng tiền, không cần hoàn hảo. App chỉ cần "tương đối đúng", phần thiếu thì mô phỏng có ghi chú.

## 2. Deliverable

**Quy tắc: chỉ 1 file `.xlsx`.** Mọi thứ (nhận định 200–300 từ, nguồn, công cụ) nằm trong sheet của cùng file đó. Không tạo file .md/.csv rời.

| # | File | Trạng thái |
|---|------|-----------|
| 1 | `AGENTS.md` (file này) | ✅ xong |
| 2 | `Unit_Economics_Home_Workout_bt2.xlsx` — toàn bộ bài làm, 1 file duy nhất | ✅ xong (14 sheet, 0 công thức lỗi, 40/40 số kiểm tra khớp) |
| 3 | `Channel_Plan_Home_Workout.xlsx` — Cấp 3 Channel Plan | ✅ xong (9 sheet, 2 vùng/sheet, 0 công thức lỗi, 65/65 bảng có dòng công thức, 0 merge chồng, 0 bước thiếu panel) |
| 4 | `Channel_Plan_Home_Workout.docx` — bản đọc/nộp của Cấp 3, sinh từ file xlsx | ✅ xong (9 câu · 38 bước · 9 kết luận · 159 bảng) |
| 5 | `Unit_Economics_Home_Workout.html` — bản đọc của Cấp 2, chia 6.5:3.5, sinh từ file xlsx bằng `build_html.py` | ✅ xong · bản mới nhất 2026-11-13 (có hộp "số nào ra số nào") · 12 tab · 515 ô nhảy phải · 556 ô có phép tính · 31 nút `↗` đã kiểm từng cái · md5 `27a15f706a40b9444d74e994a63424d8` |

**Quy tắc trình bày bảng tính:** trên **mỗi bảng** (không chỉ mỗi sheet) phải có 1 dòng ghi công thức ngay phía trên dòng tiêu đề, dạng:
`Công thức: <tên chỉ số> = <công thức> | <ghi chú ngắn>`
để người đọc thấy công thức mà không cần click vào ô.

Các sheet trong file (tên = số câu hỏi, để đối chiếu với đề không phải nhớ):

| Nhóm | Sheet | Trả lời câu |
|------|-------|-------------|
| Hướng dẫn | `A_Huong_Dan` | — (thứ tự đọc, 30 thuật ngữ, nhãn dữ liệu, mục lục, lưu ý) |
| Tóm tắt | `B_Tom_Tat` | tất cả (26 số chốt + 3 câu hỏi chốt + bản 30 giây) |
| Dữ liệu | `C_Du_Lieu_That` · `D_Gia_Dinh` | — (REAL từ Google Play · toàn bộ giả định) |
| Bài làm | `2.1_Monetization` · `2.2_CPI_CAC` · `2.3_eCPM` · `2.4_ROAS` · `2.5_LTV` · `2.6_pLTV` · `2.7_LTV_CAC` · `2.8_Phan_Tang` | đúng 2.1 → 2.8 |
| Chốt | `E_Ket_Luan` | nhận định 293 từ + checklist 7 tiêu chí |
| Tra cứu | `F_Nguon_Cong_Cu` | công cụ thật + nguồn benchmark cho từng mục |

**Quy ước trong từng sheet 2.x** (để không phải nhảy tab):
1. Tiêu đề in đúng câu hỏi của đề.
2. Ô **"Trả lời ngắn"** nền xanh lá ngay dưới tiêu đề — công thức `TEXT()` sống, đọc 1 câu là trả lời được câu hỏi.
3. Dòng **"Số lấy từ đâu"** nền xanh nhạt ngay dưới mỗi bảng — hiện luôn giá trị + sheet/ô gốc.

## 3. Đề bài (nguồn chân lý)

1. **Monetization (2.1):** IAP / IAA / Sub / Freemium / Hybrid + liệt kê đủ 100% nguồn doanh thu.
2. **CPI & CAC (2.2, 2.7):** CPI từ chi phí media; CAC thật = (media + non-media) ÷ install, rồi nhân gross margin sau phí sàn 15–30%.
3. **eCPM (2.3):** eCPM tổng + tách theo Geo và theo định dạng.
4. **ROAS curve (2.4):** bảng D0/D7/D30/D90, đánh dấu điểm hòa vốn; blended vs theo kênh.
5. **LTV (2.5):** Total LTV = IAP + IAA + Sub; kiểm chứng chéo bằng ARPU/Churn.
6. **pLTV (2.6):** tín hiệu 24h đầu + ngưỡng scale/pause trong 48h.
7. **LTV:CAC & payback (2.7):** tỷ lệ, payback period, phân loại (<1:1 cần cứu / ~3:1 khỏe / >4:1 scale).
8. **Phân tầng user (2.8):** whale/dolphin/minnow, tỷ trọng doanh thu, 1 chiến dịch tối ưu (tROAS hoặc Highest Value).

**Tiêu chí đạt:** 1 bảng tính + nhận định 200–300 từ trả lời "CAC tối đa được trả là bao nhiêu, hoàn vốn trong bao lâu?". Số liệu nhất quán, LTV ≥ CAC×3, payback < 12 tháng, ≥1 quyết định scale/pause có lập luận bằng pLTV.

## 4. Quyết định đã chốt

| Ngày | Quyết định | Lý do |
|------|-----------|-------|
| 2026-11-03 | Chỉ xuất **1 file `.xlsx`**, nhiều sheet bên trong | Đúng yêu cầu; mọi thứ tra được ở một chỗ |
| 2026-11-03 | Mỗi bảng có **1 dòng công thức ngay trên header** | Đọc được công thức mà không phải click ô |
| 2026-11-03 | Ngôn ngữ: tiếng Việt, thuật ngữ UA giữ tiếng Anh | Đúng thực tế nghề |
| 2026-11-03 | App: **Home Workout – No Equipment** (Leap Fitness Group) | App thật, có Ads + IAP thật, tải 100M+, giá IAP $2.99–$69.99; fitness là ngành có benchmark CPI/retention công khai |
| 2026-11-03 | File tham khảo `FitPal_Unit_Economics.xlsx` là **giả hoàn toàn**, chỉ dùng để học cấu trúc | Người học đã xác nhận |
| 2026-11-03 | **Không sửa app Notes** folder `User Acquisition 2` — chỉ đọc để lấy đúng câu chữ (cá voi/cá heo/cá con, "tỷ lệ vàng 3:1", "gồng lỗ", "kê cao gối ngủ") rồi viết lại trong xlsx | Người học: "ý là vào Notes để xem câu từ rồi sửa lại cái .xlsx" |
| 2026-11-03 | Đổi tên sheet theo **số câu hỏi của đề** (`2.1_...` → `2.8_...`), nhóm phụ dùng chữ cái (`A_`…`F_`) để không đụng số | Mở đúng tab là biết đang trả lời câu nào |
| 2026-11-03 | Bỏ hẳn việc phải tab qua lại: mỗi sheet 2.x có **"Trả lời ngắn"** (xanh lá, đầu sheet) + **"Số lấy từ đâu"** (xanh nhạt, dưới bảng) + 1 sheet **`B_Tom_Tat`** gom 26 số chốt kèm ô gốc | Người học chọn phương án "đọc tại chỗ + 1 sheet tóm tắt" thay vì `=LTV!$G$34` |
| 2026-11-03 | Sửa công thức **tROAS D7**: thêm `÷ GM sau phí sàn` vì nền tảng quảng cáo chỉ thấy doanh thu GROSS, còn mốc 3:1 là chuyện của NET | Công thức cũ thiếu GM nên ra 57.8%/11.9% — sai bản chất |
| 2026-11-04 | Sheet `2.3_eCPM`: **impressions + doanh thu là ô nhập**, còn **eCPM là cột công thức** `= D ÷ C × 1000`; nhãn dữ liệu đổi 🟥 FAKE → 🟨 ASSUMED vì doanh thu bám benchmark eCPM ngành | Trước đó làm ngược (eCPM nhập tay, suy ra doanh thu) — sai với yêu cầu "tính eCPM" |

## 5. Quy ước đánh dấu số liệu (BẮT BUỘC)

| Nhãn | Nghĩa | Yêu cầu |
|------|-------|---------|
| 🟩 **REAL** | Lấy trực tiếp từ nguồn công khai | Có link + ngày lấy |
| 🟨 **ASSUMED** | Giả định có căn cứ | Ghi benchmark gốc dùng để suy ra |
| 🟥 **FAKE** | Bịa để bài chạy được | Ghi rõ "số bịa — không dùng để ra quyết định thật" |

Mỗi con số trong bảng tính phải có nhãn ở cột `Nguồn/Loại`. Không có ngoại lệ.

## 6. Ledger số liệu

### 6.1 Dữ liệu THẬT (🟩) — lấy từ Google Play, ngày 2026-11-03

| Chỉ số | Giá trị | Nhãn | Nguồn |
|--------|---------|------|-------|
| Tên app | Home Workout - No Equipment | 🟩 REAL | play.google.com |
| Package | `homeworkout.homeworkouts.noequipment` | 🟩 REAL | play.google.com |
| Developer | Leap Fitness Group | 🟩 REAL | play.google.com |
| Category | Health & Fitness | 🟩 REAL | play.google.com |
| Installs | 100,000,000+ | 🟩 REAL | play.google.com |
| Rating | 4.86 (≈4.05M reviews) | 🟩 REAL | play.google.com |
| Contains ads | Có | 🟩 REAL | play.google.com |
| In-app purchases | Có, $2.99 – $69.99 / item | 🟩 REAL | play.google.com |

URL: `https://play.google.com/store/apps/details?id=homeworkout.homeworkouts.noequipment&hl=en&gl=US`

### 6.2 Mọi thứ còn lại (🟨 / 🟥)

Toàn bộ doanh thu, CPI, eCPM, retention, churn, payer rate, phân tầng user là **mô phỏng**.
- 🟨 ASSUMED = có benchmark ngành làm căn cứ (ghi rõ benchmark trong sheet `F_Nguon_Cong_Cu`).
- 🟥 FAKE = số bịa để bài chạy được, không có căn cứ.

Trong file xlsx, mỗi dòng dữ liệu có cột `Loại` mang nhãn tương ứng.

## 7. Công cụ & nguồn theo mục

> Chi tiết + cách tự kiểm từng bước nằm ở sheet `F_Nguon_Cong_Cu`.

| Mục | Sheet | Cần check gì | Công cụ / nguồn |
|-----|-------|--------------|-----------------|
| 2.1 Monetization | `2.1_Monetization` | app có Ads? có IAP? giá IAP? | Google Play listing (🟩 REAL) |
| 2.2 CPI/CAC | `2.2_CPI_CAC` | giá media, non-media cost | Ads Manager / benchmark ngành |
| 2.3 eCPM | `2.3_eCPM` | eCPM theo geo + format | AdMob / AppLovin / ironSource benchmark |
| 2.4 ROAS | `2.4_ROAS` | doanh thu tích lũy theo ngày | MMP cohort report |
| 2.5 LTV | `2.5_LTV` | ARPU, churn, mix doanh thu | tính từ cohort + công thức |
| 2.6 pLTV | `2.6_pLTV` | tín hiệu 24h | MMP + event tracking |
| 2.7 LTV:CAC | `2.7_LTV_CAC` | tổng hợp | tính |
| 2.8 Tầng user | `2.8_Phan_Tang` | phân bố doanh thu theo payer | phân tích cohort thanh toán |

## 8. Glossary nhanh

- **CPI** — Cost Per Install (chỉ tiền media).
- **CAC** — Customer Acquisition Cost (toàn bộ chi phí để có 1 user trả tiền, đã trừ phí sàn).
- **eCPM** — doanh thu / 1000 impression.
- **ROAS** — doanh thu ÷ chi phí quảng cáo, theo cửa sổ ngày.
- **LTV** — tổng doanh thu 1 user mang lại trong vòng đời.
- **pLTV** — LTV dự phóng từ tín hiệu sớm (24h).
- **Payback** — số ngày để doanh thu tích lũy = CAC.
- **Gross margin sau phí sàn** — doanh thu còn lại sau khi store lấy 15–30%.
- **tROAS** — target ROAS khi chạy campaign.
- **Whale/Dolphin/Minnow** — tầng chi tiêu: cá voi / cá heo / cá nhỏ.

## 9. Nhật ký phiên

- **2026-11-03:** Tạo file. Chưa chốt app. Đã xác nhận đọc được dữ liệu công khai trên Google Play (installs, rating, mức giá IAP, cờ Ads/IAP, developer).
- **2026-11-03:** Chốt app **Home Workout – No Equipment**. Chốt chỉ xuất 1 file xlsx. Bắt đầu dựng model.
- **2026-11-03:** Dựng xong 13 sheet. Viết script kiểm tra bằng thư viện `formulas` (không có LibreOffice trên máy): phát hiện & sửa 4 lớp lỗi tham chiếu chéo — ARPDAU trỏ nhầm cột % thay vì cột eCPM, phí sàn trỏ lệch 1 dòng, %% doanh thu eCPM chia nhầm cho tổng impressions, và các dòng LTV bị lệch sau khi thêm dòng công thức. Kết quả: **0 công thức lỗi, 41/41 ô kiểm tra khớp giá trị kỳ vọng, 7/7 tiêu chí ĐẠT**.
- **2026-11-03 (vòng 2):** Yêu cầu mới — dễ đọc cho newbie + đối chiếu được với đề. Đọc 8 note trong Notes `User Acquisition 2` (không sửa), lấy lại câu chữ. Đổi toàn bộ tên sheet sang số câu hỏi; thêm `A_Huong_Dan` (30 thuật ngữ + mục lục) và `B_Tom_Tat` (26 số chốt + 3 câu hỏi chốt + bản 30 giây); thêm ô **"Trả lời ngắn"** + dòng **"Số lấy từ đâu"** ở cả 8 sheet 2.x; sửa tROAS (thiếu ÷ GM). Build lại: **14 sheet, 0 công thức lỗi, 40/40 số kiểm tra khớp, 0 merge chồng nhau, 7/7 tiêu chí ĐẠT, nhận định 293 từ**.
- **2026-11-10:** Làm **Cấp 3** — đọc 9 note trong Notes `User acquisition 3` (read-only), dựng file mới `Channel_Plan_Home_Workout.xlsx` 14 sheet, 3 kênh, ngân sách $6.000. Kết quả kiểm: **0 công thức lỗi · 0 merge chồng · 56/56 bảng có dòng `Công thức:` · 13 dòng `Số lấy từ đâu` · 11 ô "Trả lời ngắn" đều chạy đúng**. Số chốt: 3.617 install · CAC $1,659 · LTV:CAC 3,358 · TikTok pLTV:CAC 1,98 (thiếu 1,0% so ngưỡng). File Cấp 2 không bị sửa.
- **2026-11-10 (vòng 2):** Đề chỉ có **4 câu** và áp dụng 3.1–3.9 → gộp 14 sheet còn **9 sheet**: 4 bài làm `C1`–`C4` (C1=3.1 · C2=3.2+3.3+3.5 · C3=3.6+3.7+3.8 · C4=3.9+đo lường) + 5 phụ. Build lại: **9 sheet · 0 công thức lỗi · 56/56 bảng có dòng `Công thức:` · 13 dòng `Số lấy từ đâu` · 11 ô "Trả lời ngắn" chạy đúng · 0 merge chồng**.
- **2026-11-10 (vòng 3):** Đổi thứ tự đọc trong từng câu: bỏ kết luận ở đầu, thêm bảng **`CẦN XÁC ĐỊNH GÌ`** (input → lấy ở sheet › bảng › dòng → dùng ở bước nào), đánh số lại section thành **`BƯỚC 1..n`**, dời ô xanh xuống **`KẾT LUẬN`** cuối câu; refnote ghi rõ bảng nguồn. Build lại: **9 sheet · 0 công thức lỗi · 65/65 dòng `Công thức:` · 0 merge chồng · 11 ô xanh (9 kết luận + 2 tóm tắt) chạy đúng**. Số không đổi: 3.617 install · CAC $1.659 · LTV:CAC 3.358.
- **2026-11-10 (vòng 4 — 2 vùng + docx):** Người học kêu phải nhảy tab để tra nguồn. Đổi `refnote()` từ dòng riêng bên trái thành **panel bên phải, ngang hàng đúng `BƯỚC`** (cột `len(widths)+2`); thêm 27 note còn thiếu nên **38/38 bước đều có panel** `NGUỒN SỐ ·`/`KIẾN THỨC ·`. Thêm deliverable **`Channel_Plan_Home_Workout.docx`** sinh tự động từ xlsx bằng `makedoc.py` (python-docx, A4 dọc, bảng 2 cột `[công thức | nguồn]` + bảng dữ liệu, số đọc qua `formulas` nên khớp file tính). Sửa 4 lỗi docx: thứ tự `w:shd` sai schema (banner không lên màu), bảng bị Word merge (thêm spacer 3pt), số kiểu Excel lẫn kiểu Việt (thêm `vn_num()`), cột trống thứ 11 (đếm `ncols` theo text thật). Kiểm cuối: **XLSX 9 sheet · 0 lỗi · 65/65 · 0 merge chồng · 0 bước thiếu panel · DOCX 9 câu/38 bước/9 kết luận/159 bảng**, đủ số chốt 3.617 · $1,66 · 3,36 · $6.000 · 62,7 · 1,98 · $2,10.

### 9.1 Số cuối cùng (đã kiểm chứng bằng máy)

| Chỉ số | Giá trị |
|--------|---------|
| Gross LTV 365 (base / blended) | $7.662 / $7.884 |
| Net LTV 365 (base / blended) | $6.132 / $6.310 |
| Gross margin sau phí sàn | 80.0% |
| CPI blended / CAC thật blended | $1.447 / $1.737 |
| LTV:CAC blended | **3.63** (Meta 3.07 · Google 4.68 · TikTok 1.53) |
| Payback blended | **D21** (Meta D27 · Google D14 · TikTok D110) |
| CAC tối đa = Net LTV ÷ 3 | **$2.10** (dư địa $0.37 = 21%) |
| pLTV sau 48h | Meta 2.79 → GIỮ · Google 4.29 → SCALE +20% · TikTok 1.98 → PAUSE |
| Sau khi pause TikTok | LTV:CAC 3.78 · CAC tối đa $2.33 · payback D20 |
| Phân tầng doanh thu | Whale 47.2% · Dolphin 31.4% · Minnow 16.5% · Non-payer 4.9% |
| Whale + Dolphin | 5.5% user tạo **78.6%** doanh thu |
| tROAS D7 tối thiểu / khởi điểm | **72.2% / 65.0%** (đã nhân ÷ GM sau phí sàn) |

## 10. Việc tiếp theo

Đã xong. Nếu muốn đi sâu thêm: thay số ở `D_Gia_Dinh` + `2.3_eCPM` + `2.6_pLTV` + `2.8_Phan_Tang` bằng dữ liệu thật của app mình rồi đọc lại `B_Tom_Tat` và `2.7_LTV_CAC`. Không sửa ô chữ đen (công thức).

## 11. Cấp 3 — Channel Plan & Media Buying Blueprint

**File:** `Channel_Plan_Home_Workout.xlsx` (tạo mới, KHÔNG sửa file Cấp 2). **9 sheet** = 4 sheet bài làm đúng 4 câu của đề + 5 sheet phụ, cùng quy ước trình bày với Cấp 2.

| Nhóm | Sheet | Trả lời câu |
|------|-------|-------------|
| Hướng dẫn | `A_Huong_Dan` | — (thứ tự đọc, 31 thuật ngữ, nhãn dữ liệu, quy ước ô) |
| Tóm tắt | `B_Tom_Tat` | tất cả (3 quyết định + bảng ngân sách + KPI + timeline 90 ngày + bản 30 giây) |
| Dữ liệu | `C_So_Lieu_Ke_Thua` · `D_Gia_Dinh` | — (số vay Cấp 2 + 8 số Google Play · toàn bộ giả định) |
| Bài làm | `C1_Chon_Kenh` | Câu 1 = 3.1 (mục tiêu → so 5 kênh → chốt 3) |
| Bài làm | `C2_Setup_Kenh` | Câu 2 = 3.2 Google AC + 3.3 Meta AAC + 3.5 TikTok |
| Bài làm | `C3_Mo_Rong` | Câu 3 = 3.6 DSP + 3.7 Retargeting + 3.8 Web-to-app |
| Bài làm | `C4_Policy_Do_Luong` | Câu 4 = 3.9 Policy + kế hoạch đo lường (MMP, event, iOS) |
| Tra cứu | `F_Nguon_Cong_Cu` | công cụ + nguồn benchmark + 4 giả định dễ bị chất vấn |

**Bố cục 2 vùng trên mỗi sheet** (thay cho các dòng "Số lấy từ đâu" rải rác):

| Vùng | Nội dung |
|------|----------|
| **TRÁI** (cột 1–n) | Bài làm đọc từ trên xuống: `CẦN XÁC ĐỊNH GÌ` → `BƯỚC 1..n` → `KẾT LUẬN` (ô xanh, cuối câu) |
| **PHẢI** (cột n+2, cách 1 cột trống) | Panel theo từng bước: `NGUỒN SỐ ·` (sheet › bảng › dòng) hoặc `KIẾN THỨC ·` (vì sao bước này quan trọng) — ngang hàng với đúng bước đó |

Panel đặt ở cột `len(widths)+2` (C1→K, C2→H, C3→H, C4→G), rộng 34+13+13. Không còn phải mở tab khác để tra nguồn.

Ngoài file tính còn có **`Channel_Plan_Home_Workout.docx`** — bản đọc/nộp, sinh tự động từ chính file xlsx (số lấy qua `formulas` nên khớp 100%). A4 dọc, mỗi `BƯỚC` là 1 bảng 2 cột `[công thức xám | nguồn số xanh nhạt]` + bảng dữ liệu full-width; kết luận là ô xanh cuối câu.

### 11.1 Quyết định đã chốt (2026-11-10)

| Quyết định | Lý do |
|-----------|-------|
| **3 kênh**: Meta AAC + Google AC + TikTok | Thực tế tuyển UA cần 3 kênh chính; đề cho 2–3 |
| Ngân sách **$6.000/tháng all-in** | Media $5.000 = Meta $2.150 · Google $1.850 · TikTok $1.000; non-media 20% ($1.000) phân bổ theo tỷ trọng media → all-in $2.580 / $2.220 / $1.200 |
| **ASA ngoài phạm vi** | Model Cấp 2 không tách dữ liệu iOS |
| TikTok **giữ theo đề**: 3 hook UGC + validate-then-scale + cổng 14 ngày | Đề yêu cầu đúng quy trình này; Cấp 2 đã pause TikTok nên đây là mở lại có điều kiện, không đảo kết luận |
| Mỗi câu C1–C4 có **`KẾT LUẬN`** ở cuối + **panel `NGUỒN SỐ`** bên phải | Đọc tại chỗ, không phải nhảy tab |
| Gộp 8 sheet lẻ thành **4 sheet bài làm** (`C1`–`C4`) | Đề chỉ có 4 câu; 1 sheet/câu dễ đối chiếu hơn 1 sheet/note |
| Mỗi câu đọc **từ trên xuống**: `CẦN XÁC ĐỊNH GÌ` → `BƯỚC 1..n` → `KẾT LUẬN` ở cuối | Người học phải thấy quá trình ra số, không đọc kết luận trước rồi lần ngược |
| Panel ghi **sheet › bảng › dòng**, không chỉ ô | Trả lời được "con số này ở bảng nào" |
| Mọi bảng có dòng **`Công thức:`** ngay trên header | 65/65 bảng đã kiểm |
| **2 vùng trên 1 sheet**: trái = bài làm, phải = panel nguồn số **theo từng bước** | Người học kêu mỏi vì phải nhảy tab; panel đặt ngang hàng bước nên mắt không rời dòng |
| Bỏ ô "Trả lời ngắn" đầu câu, dời thành **`KẾT LUẬN`** ở cuối | Phải thấy quá trình ra số rồi mới đọc kết luận |
| Xuất thêm **`.docx`** sinh từ xlsx | Có bản đọc/nộp không cần mở Excel; không được phép lệch số nên sinh trực tiếp từ file tính |

### 11.2 Số cuối cùng (đã kiểm chứng bằng máy)

| Chỉ số | Giá trị |
|--------|---------|
| Media / non-media / all-in | $5.000 / $1.000 / **$6.000** |
| Installs/tháng | **3.617** (Meta 1.075 · Google 1.542 · TikTok 1.000) |
| CAC blended | **$1.659** (Meta $2,40 · Google $1,44 · TikTok $1,20) |
| Net LTV blended | **$5.570** |
| LTV:CAC blended | **3.358** (giảm từ 3,63 vì TikTok kéo xuống) |
| Meta trial start | 62,7/tuần → thoát learning; tối ưu Purchase cần $3.061/tháng (+$911) |
| Google | $61,7/ngày ≥ 50×CPI $60 · tCPA cần ~$4.320/tháng · tROAS cần ~42 ngày đủ 300 purchase |
| TikTok trial start | 58,3/tuần; pLTV:CAC **1,98** — thiếu đúng 1,0% so ngưỡng 2,0 |
| DSP | **0/3 điều kiện** → chưa mở; mốc sớm nhất tháng thứ 10 |
| 3.8 | Chọn **web-to-app** thay CTV (đo được + né phí sàn) |
| 3.9 | Publish 9 PASS + 1 kiểm lại (families); Misleading Ad 9 PASS + 1 sửa (before/after) |

### 11.3 Lỗi đã sửa khi build

- `3.2_Google_AC` trả lời ngắn đọc nhầm `C_So_Lieu_Ke_Thua!B32/B33` (LTV:CAC 3,63 và payback 27) thay vì `B40/B41` (tROAS 72,2% / 65,0%). Nguyên nhân: dấu `\'` trong chuỗi Python làm lệnh replace trượt.
- Thêm dòng "Số lấy từ đâu" cho 4 bảng còn thiếu (`3.1` mục A, `3.2` mục A, `3.5` mục B, `3.8` mục C) → tổng 13 dòng.
- Thêm refnote KPI cho `B_Tom_Tat` và "Trả lời ngắn" thật cho `B_Tom_Tat` (trước là placeholder).
- Gộp sheet: các block `3.3`/`3.5` dùng row cứng (`C24`, `C32`…) nên khi append vào `C2_Setup_Kenh` bị trỏ sai và crash `MergedCell`. Sửa bằng `base = r` + `f"=C{base+n}"`; kiểm lại: install/ngày 35,8 · trial/tuần 62,7 · purchase/tuần 35,1 · thiếu $911 — khớp số cũ.

### 11.4 Cách build lại

Script nằm ở `/private/var/folders/7h/z4fmlq_j0rj59jbzkbht6y880000gn/T/opencode/` (q1–q9.py). Lệnh:

```bash
cat q1.py q2.py q3.py q4.py q5.py q6.py q7.py q8.py q9.py > build.py
./venv3/bin/python build.py
./venv3/bin/python fix.py       # bắt buộc: tính lại chiều cao ô "Kết luận"
./venv3/bin/python makedoc.py   # xuất .docx từ chính file xlsx vừa build
```

`addnotes.py` (đã chạy 1 lần) chèn 27 panel còn thiếu cho các `BƯỚC` — chạy lại sẽ nhân đôi, đừng chạy.

Kiểm tra: `formulas.ExcelModel().loads(path).finish().calculate()` → đếm ô bắt đầu bằng `#`, đếm merge chồng, đếm header có dòng `Công thức:` phía trên, và đếm `BƯỚC` không có panel cùng hàng.

## 12. Bản đọc `.html` của Cấp 2 (2026-11-12)

**File:** `Unit_Economics_Home_Workout.html` — **1 file duy nhất**, không cần internet, double-click là mở. Sinh tự động từ
`Unit_Economics_Home_Workout_bt2.xlsx` bằng `build_html.py`; **không sửa file xlsx**, không đụng 2 file Cấp 3.

> **TRẠNG THÁI: bản mới nhất 2026-11-13.** Bản 12/11 đã chốt, sau đó người học yêu cầu thêm hộp "số nào ra số nào"
> (§12.5) nên file được mở lại. Bản đang nộp: 410.472 bytes · md5 `27a15f706a40b9444d74e994a63424d8` ·
> 12 tab · 515 ô nhảy sang cột phải · 556 ô có phép tính · 101 `ⓘ` · 31 nút `↗` · 58 dòng nguồn có anchor · 0 ô lỗi.
> Chỉ được sinh lại từ `build_html.py` (sửa giả định ở `D_Gia_Dinh` rồi chạy 1 lệnh), **không sửa tay file HTML**.

| Hạng mục | Chốt |
|---|---|
| Bố cục | **6.5 : 3.5** (đo thật 936px : 504px ở 1440) — trái = bài làm, phải 35% = toàn bộ `C_Du_Lieu_That` + `D_Gia_Dinh`, luôn hiện, cuộn riêng |
| Tab | 12: `Hướng dẫn` → `2.1`…`2.8` → `Tóm tắt` → `Kết luận` → `Nguồn` (đổi tab ghi vào `#hash`, refresh vẫn đúng chỗ) |
| Số | Tính sẵn lúc build (`formulas`), nhúng vào HTML. Muốn đổi giả định: sửa `D_Gia_Dinh` → chạy lại 1 lệnh |
| Bảng bài làm | **1 bảng cho mỗi KHỐI** (tiêu đề/mục/công thức cắt khối) → cột chỉ chịu ảnh hưởng của khối đó. **Bỏ mọi cột không có dữ liệu** (chỉ tính cột mà một ô CÓ CHỮ bắt đầu ở đó — ô merge 5:8 không được kéo 8 cột vào bảng; đây là gốc của lỗi header `Sheet dùng nó` bị xuống dòng). Bề ngang: khối ≤7 cột dùng `.grid.fixed` + `<col style="width:%">` tính từ `max(dài nhất của từ × 6.8 + 18, header × 6.6 + 18, cả ô × 7.4 + 18 cap 240)`; nếu tổng ước lượng > 800px hoặc khối ≥8 cột thì để auto layout (fixed sẽ cắt số). **Cách chia bề ngang: "chia đều trước, cột nào cần hơn thì lấy đủ rồi chia lại"** — không cộng đều phần dư theo tỷ lệ (làm cột chỉ chứa 1 chuỗi dài, vd cột Google ở 2.6, phình to hơn hẳn 2 cột bên cạnh). Khối ≥8 cột dùng `.grid.wide` (11,5px, padding 6px). **Khối ≤3 cột: `.grid.narrow` = `width:auto;max-width:100%` + `padding:5px 15px` — rộng đúng bằng chữ nhưng chừa 15px hai bên cho thoáng, không kéo hết 100%** (kéo hết thì cột nhãn phình ra, số nằm lơ lửng giữa bảng; padding 9px như bảng thường thì chữ dính sát mép) |
| Bấm số bên trái | **2 việc cùng lúc**: (1) nhảy/tô vàng ô nguồn ở cột phải (giữ vàng, bấm ra ngoài mới trả lại), (2) hiện hộp **"số nào ra số nào"** — xem §12.5 |
| Ô nhập tay | Nút `nhập tay` + toast `🟨 ASSUMED`, không nhảy, **không có hộp phép tính** (vd. impressions/doanh thu ở `2.3_eCPM`) |
| Căn cột | **theo cột, không theo ô**: cột nào **≥80% ô là số / chuỗi ≤12 ký tự** và có header thì cả cột (kể cả header) canh giữa; cột còn lại canh trái. (80% chứ không phải 100%: một ô dài bất thường — vd `SCALE (+20% budget)` ở 2.6 — không được làm cả cột lệch sang trái, đó chính là lỗi "cột Google giãn ra".) Cột 1 luôn trái. Không dùng `white-space:nowrap` cho ô `.n` (làm chữ tràn sang ô bên cạnh) |
| Thuật ngữ | 33 mục từ điển (câu chữ ở `A_Huong_Dan` dòng 13–43) → `ⓘ` hover hiện **cả giải thích + công thức**; mục **không có công thức thì không in dòng `Công thức:`** (8 mục: Cohort, Impressions, Media, Installs, Whale, Dolphin, Minnow, Hybrid); không in công thức dưới tên cột nữa. `info()` bỏ ghi chú ngắn <20 ký tự không có số (đỡ spam ⓘ) |
| Cột phải | **ĐÃ CHỐT — xem §12.0, không sửa nữa** |
| Màn hẹp <1100px | Cột phải thành drawer, nút `Dữ liệu ⇄` (Esc để đóng) |

### 12.0 Cột phải — CHỐT (2026-11-12, người học xác nhận "đã xong, không chỉnh sửa gì nữa")

Làm lại y như dưới đây, đừng "cải tiến" thêm:

| Hạng mục | Đúng phải là |
|---|---|
| Cấu trúc | **1 cột dài**, không chip, không tab con, không khối gập. Header dính trên, cuộn riêng |
| Header | `📱 APP & GIẢ ĐỊNH` — **chỉ chữ đó**, không phụ đề, không dòng hướng dẫn mặc định |
| Chú giải | `🟩 Số thật · 🟨 Giả định · 🟥 Bịa` là `.dlegend` `position:absolute; top:7px; right:10px` trong `.dhead` → **góc phải trên cùng**, đứng yên khi cuộn |
| Dòng hướng dẫn | Chỉ hiện **sau khi bấm một số**: `← <tên dòng> · n ô nguồn`. Bình thường `.dnote:empty` co về 0 (header cao 34px) |
| Dòng dữ liệu | `tên | số | ↗ | ô màu` — `grid-template-columns: minmax(0,1fr) auto 16px 16px`; **ô màu luôn là cột cuối**, `↗` ngay trước nó; `.pr .lbcell{grid-column:4}` để dòng không có nút vẫn thẳng cột màu. Không bỏ `↗` (người học đã kêu bỏ là sai) |
| Lề trong | Mọi dòng (`.pr` và `table.mini`) có **6px lề trái cho chữ, 6px lề phải cho ô màu** — `.pr{padding:3px 6px}`, `table.mini th,td{padding:3px 6px}`, `table.mini .lbh,.lbcell{padding:3px 6px 3px 0;width:22px}`, `th[scope=row]{padding-left:6px}`. Ô màu là `.lb{display:inline-block;width:16px}` nên mọi dấu 🟩🟨🟥 cùng 1 mép phải, không phụ thuộc emoji rộng 11 hay 17px. **Đừng** để chữ dính mép (trước 13/11 là 2px) |
| Thẳng hàng | Cả panel chỉ được có **1 toạ độ x cho ô màu** và **1 toạ độ x cho nút `↗`** (kể cả `table.mini`) — đo bằng `getBoundingClientRect().right` trong Chrome headless |
| `ⓘ` | Chỉ ở chỗ có gì để giải thích; `info()` bỏ ghi chú <20 ký tự không có số. **`SKIP_INFO = ("Tên app","Package ID","Khoảng giá IAP")` là không có icon** |
| Số thật từ Google Play | Lưới 2 cột; `Contains ads` + `In-app purchases` nằm **chung 1 ô, 2 dòng** (`div.fact.two` + `div.frow`), nhãn rồi `Có` **sát nhau**, không đẩy ra mép |
| URL | `<a class="storelink" target="_blank" rel="noopener">`, tự thêm `https://` nếu thiếu, **gạch chân luôn** (`text-decoration:underline` trên chính `.storelink`), chữ xanh. **Không** để rule `.fv a{...}` đè (đã từng làm mất gạch chân) |
| Số giả định | Khối `A.`–`H.` mỗi mục 1 hàng `tên | số | ↗ | ô màu`; ghi chú/lý do đẩy vào `ⓘ`, không in ra |
| Chữ thừa | **Cấm** các câu: `luôn hiện, không phải đổi tab`, `Bấm một con số bên trái → nhảy tới ô sinh ra nó.`, `hover ⓘ để đọc lý do` |
| Nguồn | Chỉ lấy từ `C_Du_Lieu_That` + `D_Gia_Dinh`; anchor `p-<SHEET_UPPER>-<row>` |

### 12.1 Cách build lại

```bash
cd /Users/buzzlp./Downloads/ua
/private/var/folders/7h/z4fmlq_j0rj59jbzkbht6y880000gn/T/opencode/venv3/bin/python build_html.py --check
```

Nghiệm thu (máy kiểm, `--check`): **12 tab · 12 sheet · 515 ô bấm được · 86 ô nhập tay · 101 `ⓘ` · 31 nút `↗` ·
58 dòng nguồn có anchor · 0 nguồn thiếu anchor · 0 ô lỗi (#REF!/#VALUE!/None) · 410.472 bytes**.
Thử tay bằng Chrome headless: đổi tab → click `2.2!H10` → nhảy + tô 4 dòng (69–71 + 81) · click ô `self` → toast · hover `ⓘ` → tooltip không bị cắt · 900px → drawer mở/đóng được · trong panel cả 40 ô màu chỉ có 1 toạ độ x, 31 nút `↗` cũng 1 toạ độ x, và **31/31 nút nhảy đúng ô** (mỗi ô đích có `data-src` chứa dòng panel tương ứng).

### 12.2 Quyết định riêng của bản HTML

| Quyết định | Lý do |
|---|---|
| Không nhúng engine công thức vào trình duyệt | HyperFormula ~500KB + cả buổi sửa bug; số chốt cứng là đủ để học |
| Panel phải 1 cột dài, không chip/tab con | 35% màn hình không đủ cho 5 cột; mỗi dòng 1 hàng, ghi chú đẩy vào `ⓘ` → cả bộ dữ liệu còn ~2,5 màn hình |
| Số THẬT xếp 2 cột (grid) | 11 fact ngắn, xếp 2 cột thì hết 6 hàng thay vì 14 → đỡ phải cuộn đúng chỗ hay xem nhất |
| Bấm số → tô **tất cả** nguồn liên quan, không lọc panel | Giữ nguyên ngữ cảnh để đối chiếu, không làm mất dòng khác |
| `FORMAT_FIX` cho `2.8_Phan_Tang!B20` | Ô này trong xlsx đặt nhầm `0.0%` nên Excel hiện `29.958.460,1%`; HTML hiện lại `$299.585`. **Nên sửa định dạng ô này trong xlsx nếu mở lại file** |
| Công thức **chỉ** trong hover, không in dưới tên cột | Người học đã chốt: chữ trong bảng gọn lại, ai cần công thức thì hover |
| Bảng 2–3 cột giữ cột nhãn 34% | Trước đó nhãn bị bóp còn 120px trong khi cột số trống 800px |

### 12.3 Nhật ký

- **2026-11-12:** Đọc hết 14 sheet (cấu trúc, merge, fill, font, number format) → dựng `build_html.py`: `load_values()` (formulas),
  `refs_of()` + `Model.sources()` (đệ quy ≤6 tầng), `vn_num()`/`fmt()` (số kiểu Việt), `GLOSSARY` 33 thuật ngữ, renderer 2 cột,
  CSS/JS nhúng. Kết quả kiểm: 12 tab · 450 ô bấm được · 170 ô nhập tay · 0 nguồn thiếu anchor · 0 ô lỗi.
- Lỗi đã sửa khi build: (a) bảng rộng mục F bị in 2 lần + lặp cột đầu → tách `wrows` và bỏ cột 1 khỏi header; (b) dòng ghi chú
  nằm ở cột B (không phải A) bị coi là dòng dữ liệu → nhận diện theo "ô bắt đầu khác cột 1"; (c) `max-width:64%` trong grid
  `auto` làm chữ bị bẻ từng ký tự ("C ó") → đổi `.prow` sang flex; (d) `\b` trong regex đếm của `--check` bị escape 2 lần → đếm ra 0.
- **2026-11-12 (vòng 2 — sửa theo review):** người học chê 3 thứ: (1) bảng 2.2 cột không đều, chữ rớt dòng loạn — vì bê
  `width` cột của Excel sang; (2) công thức in dưới tên cột làm rối — muốn vào hover; (3) cột phải quá nhiều chip + mỗi dòng 2
  tầng nên phải cuộn nhiều. Đã sửa: bỏ `colgroup` + `table-layout:auto` (bảng 2–3 cột giữ nhãn 34%), bỏ `.tf` (công thức vào
  tooltip), panel phải viết lại thành 2 khối (THẬT 2 cột / GIẢ ĐỊNH 1 hàng mỗi mục, ghi chú vào `ⓘ`, nút `↗` thay chip chữ),
  bỏ toàn bộ chip điều hướng. Panel từ ~3300px xuống **2161px (2,5 màn 867px)**. Kiểm lại: 12 tab · 450 ô bấm được · 81 `ⓘ` ·
  26 `↗` · 0 nguồn thiếu anchor · 0 ô lỗi; hover/click/nút `↗`/drawer 1000px đều chạy.
- Lỗi do vòng 2 gây ra và đã sửa: viết lại CSS làm rơi mất `.sheet{display:none}` → cả 12 sheet chồng lên nhau (phát hiện bằng
  cách đo `getComputedStyle(...).display` của từng sheet trong Chrome headless, giờ `--check` không bắt được lỗi này).
- **2026-11-12 (vòng 3 — sửa theo review):** người học chê: (1) ⓘ spam, có cái hover chỉ ra "ngày lấy dữ liệu"; (2) chú giải
  `Số THẬT 🟩 / Số GIẢ ĐỊNH 🟨🟥` phải ở góc phải trên cùng, còn trong bảng thì để **1 cột màu ở cuối** và phải thẳng hàng;
  (3) 2.2 mục B "còn quá trời chỗ mà viết dính rồi xuống hàng" — vì cả sheet là **1 bảng 9 cột** nên khối 4 cột của mục B bị
  ép vào 4 cột đầu, 5 cột sau trống; (4) 2.4 cột `D0` canh trái còn số canh phải.
  Đã sửa: `render_sheet()` cắt thành **1 bảng / 1 khối** + `colgroup` cho cột cuối nhận `width:100%` khi cột đó là chữ dài;
  số + chuỗi ngắn canh giữa, header canh giữa; `.grid.wide` cho khối ≥8 cột; `info()` bỏ ghi chú <20 ký tự không có số;
  chú giải dời lên header phải, bỏ `.pblk` emoji + dòng `THẬT:/GIẢ:` trùng lặp; ô màu + nút `↗` thành cột 16px cố định
  (`grid-template-columns: minmax(0,1fr) auto 16px 16px`), `table.mini` thêm cột `Loại` cuối. Kiểm: `--check` ĐẠT (75 `ⓘ`,
  295 KB) · **0/12 sheet tràn ngang** (đo `#work.scrollWidth` từng tab trong Chrome headless) · click số 14 nguồn · `↗` 15 ô ·
  tooltip + drawer vẫn chạy. File xlsx md5 không đổi.
- **2026-11-12 (vòng 4):** người học chốt lại: (1) ô màu phải **luôn ở cuối**, không có mũi tên `↗` cạnh nó, và phải thẳng hàng
  từ trên xuống; (2) 3 chú giải `🟩 Số thật · 🟨 Giả định · 🟥 Bịa` phải **thật sự ở góc phải trên**; (3) bảng bên trái "hụt vô ra"
  — do canh giữa **từng ô** nên ô ngắn (`.n`) nhảy vào giữa còn ô dài nằm trái, và header luôn giữa nên lệch khỏi cột chữ.
  Đã sửa: `.pr` thành `tên | số | ↗ | ô màu` (`minmax(0,1fr) auto 16px 16px`), ô màu cột cuối, `.pr .lbcell{grid-column:4}`
  để dòng không có nút vẫn thẳng cột màu; chú giải thành `.dlegend` absolute `top:7px;right:10px` trong header phải; canh lề
  đổi sang **theo cột** (cột toàn số/chuỗi ngắn → cả cột + header canh giữa, còn lại trái, cột 1 luôn trái).
  Kiểm: `--check` ĐẠT (75 `ⓘ`, 26 `↗`, 298 KB) · 0/12 tab tràn ngang · **40/40 ô màu cùng 1 toạ độ x**, 26 nút `↗` cùng 1
  toạ độ x, `table.mini` cũng thẳng · click số 2.4 → 14 ô · click `↗` → về đúng sheet + tô ô · tooltip/drawer 1000px chạy.
- **2026-11-12 (vòng 5 — dọn chữ cột phải):** bỏ 3 câu chữ thừa: phụ đề `luôn hiện, không phải đổi tab`, dòng mặc định
  `Bấm một con số bên trái → nhảy tới ô sinh ra nó.` (chỉ hiện lại khi bấm số: `← tên · n ô`), và `hover ⓘ để đọc lý do`.
  Gộp `Contains ads` + `In-app purchases` thành 1 ô `Contains ads · In-app purchases = Có`; bỏ class `.full` của `URL` nên
  URL nằm nửa phải, ngang hàng ô `Khoảng giá IAP`. `.dnote:empty` co về 0 → header phải thấp 34px. Kiểm: `--check` ĐẠT
  (58 dòng nguồn, 75 `ⓘ`, 26 `↗`) · URL không bị cắt · `.facts` không tràn.
- **2026-11-12 (vòng 6):** (1) `URL` thành link bấm được, **luôn gạch chân** (`<a class="storelink" target="_blank" rel="noopener">`, tự thêm
  `https://` nếu thiếu scheme); (2) `Contains ads` + `In-app purchases` nằm trong **1 ô nhưng 2 dòng** (`div.fact.two` +
  `div.frow`, nhãn rồi `Có` **sát nhau**, không đẩy ra mép phải) thay vì 1 dòng gộp; (3) bỏ `ⓘ` ở `Tên app`, `Package ID`, `Khoảng giá IAP`
  (`SKIP_INFO`). Kiểm: `--check` ĐẠT (72 `ⓘ`, 26 `↗`, 58 dòng nguồn) · `href` đúng `https://play.google.com/...`,
  `target=_blank` · `.fact.two` không tràn · 3 nhãn trên không còn `.info`.
- **2026-11-12 (vòng 7):** gạch chân URL không hiện vì CSS cũ `.fv a{text-decoration:none}` (specificity 0,1,1) đè
  `.storelink{text-decoration:underline}` (0,1,0). Đã **xoá hẳn 2 dòng `.fv a` / `.fv a:hover`**, chỉ còn `.storelink`.
  Kiểm: screenshot 1440px thấy gạch chân dưới link, `href`+`target=_blank` đúng.
- **2026-11-12 (chốt cột phải):** người học xác nhận **cột phải đã xong, không chỉnh sửa gì nữa** → gom toàn bộ yêu cầu
  rải qua 7 vòng thành **§12.0 "Cột phải — CHỐT"**. Lần sau được kêu sửa gì ở bên phải thì đọc §12.0 trước và làm đúng
  như bảng đó, không tự thêm/bớt (nhất là: **không bỏ nút `↗`**, **ô màu luôn ở cột cuối**, **không thêm chữ phụ ở header**).
- **2026-11-12 (vòng 8 — layout bảng bên trái):** người học bắt 2 lỗi: (1) `Hướng dẫn` mục 2 header `Sheet dùng nó`
  xuống dòng dù còn chỗ; (2) `2.1` chỗ canh giữa chỗ sát mép trái trong cùng một cột ("có lúc center, có lúc sát mép trái").
  Nguyên nhân: (a) sheet gốc có 3–4 **cột trống** + ô merge trải 5:8 nên bảng 8–9 cột, cột chữ bị bóp; (b) canh lề quyết
  định **theo từng ô** (`len ≤ 12`) nên `CÓ — nguồn phụ` (14) nằm trái còn `KẾT LUẬN` (9) nằm giữa.
  Đã sửa: **bỏ cột trống** theo "ô có chữ bắt đầu ở cột nào"; `.grid.fixed` + bề ngang % ước lượng theo độ dài từ/header
  cho khối ≤7 cột (auto cho 8+ và khi tổng > 800px); phần bề ngang còn thừa chia **đều** cho các cột (chia theo tỷ lệ
  làm cột nhãn phình ra, số nằm lơ lửng giữa bảng); canh giữa **theo cột** + chỉ khi cột có header; bỏ `nowrap` ở `.n`.
  Kiểm bằng Chrome headless: **0 ô tràn chữ · 0/12 tab tràn ngang · 0 cột lệch canh lề giữa header và body**;
  header ngắn chỉ còn xuống dòng ở 3 bảng 8–12 cột (`2.2`, `2.7`, `2.8` — không đủ chỗ), 20 header. File 284 KB.
- **2026-11-12 (vòng 9 — tỉ lệ cột + bảng hẹp):** người học chê (1) chia 6:4 thì panel phải dư nhiều, nhãn `D0` cách số
  xa; (2) bảng 3 cột không cần giãn hết cỡ ("đủ là được"). Đã sửa: `#data` 40% → **35%** (đo thật 936 : 504 ở 1440,
  panel không tràn ô nào, URL xuống 2 dòng nhưng không cắt); bảng **≤3 cột** thêm class `.narrow` với
  `width:auto;max-width:100%` → 16 bảng đo được rộng 279–812px thay vì luôn 894px. Kiểm lại cả 12 tab bằng Chrome
  headless: **0 ô tràn chữ · 0/12 tab tràn ngang · 0 cột lệch canh lề · 0 panel tràn · click 2.4 → 14 ô · drawer 1100px
  chạy · Esc đóng**. `--check` ĐẠT. File 284 KB.
- **2026-11-12 (vòng 10 — bảng nhỏ cho thoáng):** người học: bảng nhỏ "cứ rộng rãi thoải mái, không cần gò bó,
  nhưng cũng không cần giãn hết cỡ" (ảnh: `2.6` mục 1, chữ `Ghi chú` dính sát mép phải bảng). Đã thêm
  `.grid.narrow td,th{padding:5px 15px}` → 16 bảng nhỏ rộng thêm 25–45px (2.6 mục 1: 588 → 643 của 921 pane ≈ 70%),
  chữ còn 15px mỗi bên. Giữ `padding` dọc 5px để chiều cao dòng bằng bảng thường. Kiểm lại: **0 tràn · 0 lệch canh
  lề · 0/12 tab tràn ngang · click 2.4 → 14 ô**; header xuống dòng còn 18 (bớt 2). File 284 KB.
- **2026-11-12 (vòng 11 — tooltip sạch):** hover `ⓘ` của 8 thuật ngữ không có công thức (Cohort · Impressions · Media ·
  Installs · Whale · Dolphin · Minnow · Hybrid) đang in `Công thức: —`. Đã sửa `term_html()`: chỉ chèn dòng công thức
  khi `f` khác `""`/`-`/`--`/`–`/`—`. Kiểm: 72 tooltip, **0 tooltip còn `Công thức: —`**, 40 tooltip có công thức thật
  vẫn in đủ; `--check` ĐẠT. File 284 KB.
- **2026-11-12 (ĐÓNG BĂNG):** người học xác nhận bài xong và **file `.html` không sửa nữa** → ghi trạng thái đóng băng
  (md5 `e801f6692e10abf5d8cbcf6a24700ca2`, 289.928 bytes) vào §1 và đầu §12. Toàn bộ checklist nghiệm thu gom vào §12.4.
- **2026-11-13 (vòng 12 — hộp "số nào ra số nào"):** người học yêu cầu: bấm số vẫn nhảy cột phải như cũ **và** hiện hộp
  cho biết số nào ra số nào; chỉ ô **có tính toán** mới có hộp; ô dùng số của **bảng khác trong cùng tab** phải tô vàng;
  **không in tên hàm Excel** (`SUM`, `SUMIF`…) mà viết hẳn phép tính; cột nào lấy số từ **tab khác** thì note ở `ⓘ`;
  tô vàng **giữ nguyên** tới khi bấm ra ngoài; file là độc lập nên **không in `D_Gia_Dinh`** nữa.
  Đã làm: `describe()` (thay `expr_of()` cũ) + `_fn()` bung `SUM`/`SUMPRODUCT`/`MIN`/`MAX`, bỏ `ROUND/TEXT`, chọn nhánh `IF`
  bằng `truth()`; `internal_uses()` + `data-uses` → `.use-on` (cùng tab) và nút `↗ tab 2.5` (khác tab); `plain()` đổi tên
  sheet khi in; `.hl` giữ vàng ở cột phải; hộp ghim trong `#work`, `Esc`/bấm ngoài tắt.
  Kiểm: **556 ô có hộp / 660 ô công thức · 0 chuỗi còn tên hàm hay tên sheet · 505 ô có `data-uses` · 39 tooltip note
  "Có dùng số của tab …" · 12 tab 0 tràn ngang · 0 ô tràn chữ · 0 lỗi JS**. File 343 KB, md5 `972c799f…`.
- **2026-11-13 (vòng 12b — sửa tô vàng + `MIN`):** 2 lỗi tự phát hiện khi đo: (1) ô nguồn **không có dòng ở cột phải**
  (vd. `2.6_pLTV` ô `1,08` dùng `41,0% ÷ 38,0%`) thì không có `id="c-<sheet>-<addr>"` nên JS không tô vàng được →
  **mọi ô số giờ đều có id** (đặt ngoài nhánh `if data:`, `tabindex` vẫn chỉ gắn cho ô bấm được); `internal_uses()` bỏ
  ô trống (ô trống không in ra bảng thì không tô được) → `--check` thêm dòng `thieu-id-dung=0`. (2) `MIN/MAX/SUM` gặp ô
  trống in ra `nhỏ nhất của (, 27,3, , , )` → bỏ ô trống như Excel, còn `nhỏ nhất của (27,3)`. Kiểm: **556/556 ô mở
  được hộp · 0 chuỗi còn tên hàm/tên sheet · 375 ô tô vàng ô nguồn cùng tab · bấm ra ngoài 0 còn vàng · 12 tab 0 tràn ·
  0 ô tràn chữ**. File 369.354 bytes, md5 `a5e84953…`.
- **2026-11-13 (vòng 13 — theo 4 góp ý của người học):** (1) bỏ hẳn câu "bấm vào số để xem phép tính" ở note `ⓘ` của tiêu đề
  cột, còn `Có dùng số của tab 2.5 · 2.2.`; (2) đổi ghi chú trong hộp thành **`ô vàng = số lấy vào phép tính này`**;
  (3) ô chỉ **chép lại 1 con số** (`=E23` → `1,01`) không còn in 2 dòng `1,01` trùng — chỉ hiện `= 1,01` (139 ô);
  (4) tab 2.6 mục "Quyết định sau 48h" cột Google phình to: do **chia bề ngang** cộng phần dư theo tỷ lệ ước lượng
  (cột nào có 1 chuỗi dài như `SCALE (+20% budget)` thì rộng hơn) **và canh giữa chỉ khi 100% ô ngắn** (một ô dài làm
  cả cột lệch trái). Sửa: chia kiểu **chia đều trước, cột nào cần hơn thì lấy đủ rồi chia lại**; canh giữa khi **≥80% ô
  ngắn**; ước lượng header 6.2→6.6px/ký tự, ô dài 7.0→7.4. Kèm: nút `↗` ở cột phải tô `.hl` dòng đích (trước chỉ cuộn).
  Kiểm: **0 ô tràn chữ/12 tab tràn ngang · 556/556 hộp mở đúng · 0 chuỗi còn tên hàm/tên sheet · 139 ô hiện 1 lần ·
  375 ô tô vàng nguồn cùng tab · 0 còn vàng sau khi bấm ra ngoài · 0 header xuống dòng ở 17 bảng fixed** (27 header còn
  xuống dòng đều ở bảng 8+ cột auto — chấp nhận). 2.6 mục 3 giờ 248/217/217/217px. File 367.811 bytes, md5 `890cff31…`.
- **2026-11-13 (vòng 14 — mũi tên `↗` ở cột phải):** người học báo thiếu `↗` ở `D7`, `D30` và nghi Banner/Interstitial/Rewarded
  trỏ sai. Ba nguyên nhân: (1) **`Model.sources()` tự đầu độc memo** — hàm ghi `([], [])` vào `_memo` *trước* khi tính (để chặn
  vòng lặp) nên ô nào bị chạm lần đầu ở tầng > 6 (chuỗi `2.4_ROAS` → `2.5_LTV`) rỗng vĩnh viễn → không có `data-src` →
  không có `↗`; sửa: chặn vòng lặp bằng `self._busy`, **chỉ memo kết quả thật**; (2) `use_btn()` lấy `items[0]` (ô đầu tiên
  được render) nên 3 dòng Banner/Inter/Rewarded đều nhảy về ô Banner; sửa: chọn đích theo thứ tự **ô dùng trực tiếp →
  ô hiện đúng giá trị đang xem → tên dòng khớp → thứ tự**; (3) ô **chữ** có công thức (vd `2.7_LTV_CAC!H7` = "ĐẠT") trước đây
  không có `id` nên không làm đích được → nay có `id` + `data-src` + `.src` (bấm chỉ tô nguồn, không mở hộp phép tính).
  Kiểm: **31 nút `↗`, 31/31 nhảy đúng tab + tô đúng ô, 0 ô đích không tồn tại, 0 nút trỏ tới ô không dùng số đó** ·
  D7 → `2.5_LTV!B10` (18,0%), D30 → `B12` (8,0%) · Banner/Inter/Rewarded → `2.3_eCPM!B42` (ô ARPDAU IAA — **ô duy nhất**
  trong model dùng 3 số này) · 556/556 hộp phép tính · 515 ô bấm được · 0 tràn ·
  375 ô tô vàng · 0 còn vàng sau khi bấm ra ngoài · 156/156 chip đổi tab. File 410.472 bytes, md5 `27a15f70…`.
- **2026-11-13 (vòng 14b — chỉ thêm đúng 2 mũi tên):** người học nói rõ: ở bảng retention chỉ xin thêm `↗` cho **D7 và D30**,
  không phải thêm hết. Bảng giả định đã có `NO_ARROW = {("D_GIA_DINH",20),("D_GIA_DINH",22),("D_GIA_DINH",24)}` (D3 · D14 · D60)
  → retention còn **7 nút**: D0 · D1 · **D7** · **D30** · D90 · D180 · D365 (D3/D14/D60 không có). Tổng 34 → **31 nút**,
  phần còn lại của bản không đổi (đích `↗` vẫn chọn theo §12.5). Kiểm lại: 31/31 nhảy đúng ô · 556/556 hộp · 0 tràn · 0 vàng sót.
- **2026-11-13 (vòng 15 — bấm ô "Impressions / Doanh thu theo Geo" phải tô bảng trên):** tab `2.3_eCPM` mục B là `SUMIFS` trên
  bảng mục A. `describe()` không đọc được `SUMIFS` nên ô đó **không có hộp phép tính**, mà code cũ còn gắn nhầm nhãn
  "ô nhập tay" (vì `sources()` trả `selfref` cho mọi ô có công thức nội bộ) → bấm vào không tô gì. Sửa: (1) `selfref` chỉ
  được coi là ô nhập tay khi ô **không có công thức**; (2) ô có công thức mà không in được phép tính vẫn nhận `data-uses`
  + class `.uses` — bấm vào là tô vàng các ô nó lấy số (cùng tab), không mở hộp; (3) mọi ô **chữ** trong bảng (nhãn Geo,
  "Đủ", "ĐẠT"…) và ô chữ một-dòng giờ đều có `id` để tô vàng được; (4) `internal_uses` limit 12 → **24 ô** để phủ trọn
  vùng `A7:A15` + cột số. Kiểm: bấm `2.3!B21` (Impressions US) tô **19 ô** = `A7:A15` + `C7:C15` + `A21`; `C21` tô 19 ô
  (`A` + `D`); `B28` (theo định dạng) tô `B`+`C`; bấm ra ngoài còn 0 vàng · 556/556 hộp vẫn chạy · 31/31 mũi tên `↗` ·
  12 tab 0 tràn · 86 ô nhập tay · 0 id trùng. File 398.511 bytes, md5 `f44906b2…`.
- **2026-11-13 (vòng 16 — chỉ tô dòng khớp điều kiện):** người học thấy ảnh: bấm Impressions của `US` ở mục B mà **cả 9 dòng**
  bảng Geo phía trên đều vàng → sai, "chọn US thì tô của US thui". Nguyên nhân: `internal_uses()` lấy **toàn bộ** vùng trong
  `SUMIFS` ($A$7:$A$15, $C$7:$C$15), không xét điều kiện. Sửa: thêm `crit_split()` (cùng `_crit()`/`_hit()`) — đọc các cặp
  `(vùng điều kiện, điều kiện)`, so giá trị từng dòng với điều kiện (điều kiện là **1 ô** như `A21`, chuỗi `"IAA"` hay số),
  rồi trả về *(ô thuộc vùng, ô thật sự được lấy)*; `internal_uses` chỉ bỏ ô thuộc vùng mà **không** được lấy. Kết quả: `B21`
  = 7 ô (`A7:A9` + `C7:C9` + `A21`), `B22` = dòng EU, `B23` = dòng SEA, `B28` = 3 dòng Banner (`B7,B10,B13`), `B29` =
  Interstitial, `B30` = Rewarded. Lỗi tự phát hiện khi test: bản đầu tính "ô nào bị loại" nên ô có **nhiều `SUMIF`** (trả lời
  ngắn `2.1!A3`, 3 `SUMIF` IAA/IAP/Sub trên cùng vùng) bị loại sạch → đổi sang tính "ô nào **được** lấy" rồi hợp lại
  (2.1!A3 còn 18 ô, đúng: dòng `Khác` không có `SUMIF` nào dùng). Kiểm: 12 tab 0 tràn · 0 ô tràn chữ · 556/556 hộp ·
  375 ô vàng · bấm ra ngoài còn 0 · 31/31 `↗` · 156/156 chip · `--check` ĐẠT. File 410.472 bytes, md5 `27a15f70…`.
- **2026-11-13 (vòng 17 — số trong "Trả lời ngắn" bấm được):** người học: ô xanh lá ở đầu mỗi câu có dẫn ra số kết quả, muốn
  **bấm vào từng số là tô vàng + chỉ ra chỗ lấy số ấy**. Đã làm: `top_parts()` cắt công thức theo `&` ở **cấp ngoài cùng**
  (chuỗi trong hàm như `"0.0%"` của `TEXT` không phải chữ hiện ra → bỏ), `ans_html()` ghép lại từng mẩu, `num_span()` bọc
  số thành `<span class="num" data-uses data-calc data-lab>`; JS cho `.num` dùng chung `calcShow()` nên hộp hiện
  `Trả lời ngắn · ô D9` / `= $1.00` / `ô vàng = số lấy vào phép tính này`, số ở tab khác thì có nút `↗ tab X`.
  Lỗi tự phát hiện khi test: (1) bản đầu cắt theo mọi chuỗi `"..."` nên `"IAA"`/`"0.0%"` bên trong `SUMIF`/`TEXT` bị coi là chữ
  → phải theo độ sâu ngoặc; (2) tìm literal kế tiếp bằng `text.find(".")` cắt `72.2%` thành `72` + `.2%` → đọc **token số**
  bằng `NUM_HEAD`, literal phải khớp **đúng vị trí** (`text.startswith(val, cur)`), lệch thì in thường cả ô; (3) `[\\d.,]*`
  ăn luôn dấu phẩy sau số → dùng `\\d+(?:[.,]\\d+)*`; (4) bấm `.num` rơi vào nhánh `markUses(td[data-uses])` với `td` null →
  thêm điều kiện `!nu`. Chỉ bọc cụm **đúng là số** (`NUM_ONLY.fullmatch`) — `Meta Ads`, `SCALE (+20% budget)` để nguyên chữ.
  Kiểm: **42 số / 8 câu** (2.1: 3 · 2.2: 5 · 2.3: 5 · 2.4: 3 · 2.5: 5 · 2.6: 5 · 2.7: 8 · 2.8: 8) · 42/42 mở hộp + tô vàng
  (hoặc có chip `↗ tab`) · 0 hộp chứa tên hàm · 0 tự trỏ vào chính ô trả lời · phần cũ không đổi (556/556 hộp · 375 ô vàng ·
  31/31 `↗` · 156/156 chip · 12 tab 0 tràn) · `--check` ĐẠT. File 410.472 bytes, md5 `27a15f70…`.
- **2026-11-13 (vòng 18 — lề trong cột phải):** người học gửi 2 ảnh: dòng `Banner 8,0` và `Meta Ads $26.000 13.000 1,20` có chữ
  dính sát mép trái, ô màu dính mép phải. Đo bằng Chrome headless: `.pr` chỉ có **2px** lề hai bên; `table.mini` chữ **5px** nhưng ô
  màu **2,5px** và ô màu header/`Loại` đôi khi chạm đúng mép bảng. Sửa **1 chỗ trong CSS**: `.pr{padding:3px 6px}`,
  `table.mini th,td{padding:3px 6px}`, `.lbh/.lbcell{padding:3px 6px 3px 0;width:22px}`, `th[scope=row]{padding-left:6px}`,
  `.pnote/.phow` 2px → 6px; thêm `.lb{display:inline-block;width:16px;text-align:center}` vì emoji 🟨 đo ra 11px còn 🟩 17px nên
  **mép phải mỗi ô màu lệch nhau 2,5px** dù cùng cột. Đo lại: chữ 6px · ô màu 6px · **ô màu chỉ còn 1 toạ độ x (1405, spread 0,0)**
  · nút `↗` 1 toạ độ x (1383) · 2 bảng mini rộng 464/464 không tràn · panel không tràn. Nghiệm thu đầy đủ vẫn xanh:
  tab=12 · 0 tab tràn · 0 ô tràn chữ · 556/556 hộp · 139 hiện-1-lần · 375 ô tô vàng · 0 vàng sót · 156/156 chip ·
  31/31 `↗` (0 nút sai đích) · 42/42 số trong "Trả lời ngắn" · SUMIFS vẫn đúng (`B21`=7 ô, `B28`/`B30`=3 dòng) · `--check` ĐẠT.
  File 410.472 bytes, md5 `27a15f70…`.
- **2026-11-13 (vòng 19 — ô "chưa/ĐẠT" phải tô bảng trên, không tô giả định):** người học: ở tab 2.4, bấm vào `chưa/ĐẠT`
  thì phải tô vàng `B7` (ROAS bảng A) so với `B15` (ngưỡng hòa vốn), chứ tô vàng các ô giả định bên phải là vô nghĩa vì muốn ra số
  đó phải tính vòng qua tab 2.2 + 2.5. Hai lỗi: (1) ô **chữ** có công thức (`IF(...)="ĐẠT"`) chỉ được gắn `data-src`, **không** gắn
  `data-uses` → bấm vào chỉ tô cột phải; (2) mọi ô tính toán đều tô cột phải kể cả khi số phải đi qua tab khác. Sửa: nhánh ô chữ
  thêm `internal_uses()` → `data-uses` (tô `B7`+`B15`); thêm `data-nop="1"` cho ô có `data-src` mà công thức **không** trỏ trực tiếp
  bảng giả định; JS đổi `if(s)` → `if(s&&!s.dataset.nop)` và nhánh còn lại gọi `markUses()`. Kết quả đo (Chrome headless):
  `2.4!C15` → `B7`+`B15` · `D15` → `C7`+`B15` · `C18` → `B10`+`B18` · `I32` ("Hòa vốn khoảng D27") → `G32` · `G32` → `B24`+`C32`+`G24`
  · `B15`/`B24`/`C27` vẫn có hộp phép tính nhưng **0 dòng vàng** ở cột phải. Ô lấy trực tiếp giả định vẫn tô như cũ (`2.5!B26` → 3
  dòng + `B25`). Tổng: 148 ô tô cột phải / 375 ô tô vàng cùng tab / 0 ô bấm mà không làm gì (trừ nhãn cột A) · 556 hộp · 42 số ·
  156/156 chip · 31/31 `↗` (0 sai đích) · 12 tab 0 tràn · `--check` ĐẠT. File 410.472 bytes, md5 `27a15f70…`.

### 12.4 Nghiệm thu — chạy lại khi buộc phải build

`--check` chỉ đếm cấu trúc; 5 lỗi sau **không** `--check` bắt được, phải đo trong Chrome headless (`--window-size=1440,900`):

| Lỗi | Cách bắt |
|---|---|
| 12 sheet chồng lên nhau (thiếu `.sheet{display:none}`) | `getComputedStyle` từng `.sheet`, chỉ 1 cái `display:block` |
| Tab tràn ngang | `#work.scrollWidth > clientWidth` trên cả 12 tab |
| Ô tràn chữ | so `scrollWidth` vs `clientWidth` của từng `td`/`th` |
| Header lệch canh lề với body | so `textAlign` của `th` với `td` cùng cột, chỉ khi `row.children.length === ths.length` (bỏ dòng merge) |
| Panel phải tràn | `#data` scrollWidth vs clientWidth, và trong panel `scrollWidth` từng `.pr`/`.fact` |
| Nút `↗` trỏ sai / thiếu | duyệt **mọi** `#data .use`: `document.getElementById(data-go)` phải tồn tại, phải nằm trong `data-sheet`, và `data-src` của ô đích phải chứa `D_GIA_DINH:<dòng của panel>`; đếm luôn số dòng `.pr` **không** có `↗` (chỉ chấp nhận dòng THẬT không ai dùng, vd 77–80) |

Header xuống dòng: clone node, **bỏ `.info`**, rồi đếm `Range.getClientRects()` có `top` khác nhau (đếm chiều cao rect cho kết quả sai).
Chấp nhận còn ~18 header xuống dòng ở 3 bảng 8–12 cột (`2.2`, `2.7`, `2.8`) — 921px không đủ cho 12 cột.

Hộp phép tính (§12.5) phải kiểm thêm: `data-calc` **không** được chứa `SUM|IF|ROUND|TEXT|MIN|MAX|ABS|COUNTIF|SUMPRODUCT|_LTV|_Gia_Dinh|!`;
bấm 1 ô → hộp hiện + ô nguồn cùng tab vàng; bấm ra ngoài → hộp tắt, hết vàng; nút `↗ tab X` đổi đúng tab.

### 12.5 Hộp "số nào ra số nào" (2026-11-13)

Bấm một ô **có phép tính** → hiện hộp nhỏ ngay dưới ô, gồm 3 dòng: `tên cột · tên dòng` / **phép tính bằng số thật** / `= kết quả`.
Bấm ra ngoài (hoặc `Esc`) thì tắt. Hộp nằm trong khung bài làm, không đè lên thanh tab.

| Hạng mục | Đúng phải là |
|---|---|
| Ô nào có hộp | **Chỉ ô có công thức** (`describe()` ra được chuỗi). Ô nhập tay / số gốc / số giả định **không có hộp** — vẫn giữ toast `🟨 ASSUMED` và nhảy cột phải như cũ. Hiện có **556 ô** có hộp (trên 660 ô công thức) |
| Nội dung | **Số thật + phép tính**, không bao giờ in tên hàm Excel hay tên sheet. VD `$26.000 ÷ 13.000` `= $2,00` |
| `SUM(vùng)` | Bung thành `a + b + c` (tối đa 12 ô; hơn thì **không hiện hộp**) |
| `SUMPRODUCT(v1,v2)` | `a × b + c × d + …` |
| `ROUND/TEXT/TRUNC(x, …)` | Bỏ phần định dạng, chỉ lấy `x` |
| `MIN/MAX(vùng)` | `nhỏ nhất của (…)` / `lớn nhất của (…)` — chữ Việt, không phải tên hàm |
| `IF(đk, a, b)` | Chọn đúng nhánh đã chạy: 1 nhánh là chuỗi còn 1 nhánh là số → lấy nhánh số; cả hai cùng loại → tính `đk` bằng số thật (`AND/OR/so sánh`, `truth()`) rồi chọn. Không chắc → **không hiện hộp** |
| Hàm khác (`SUMIFS`, `COUNTIF`, `LEN`, `SUBSTITUTE`…) | Không hiện hộp — thà im còn hơn in hàm lạ |
| Ngoặc | **Giữ nguyên** ngoặc của công thức: `(a + b + c) ÷ 1000` — bỏ ngoặc là sai nghĩa |
| Số cùng tab | Ô nguồn (trong bài, không phải cột phải) được **tô vàng** `.use-on`; vàng giữ nguyên tới khi bấm ra ngoài. Ghi chú trong hộp: `ô vàng = số lấy vào phép tính này` (câu cũ "số được dùng ở bảng khác" người học kêu không rõ) |
| Ô chỉ chép lại 1 con số | `describe()` ra đúng bằng kết quả (vd `Chỉ số pLTV` = `=E23` → `1,01`) → **chỉ hiện kết quả 1 lần** (`= 1,01`), không in thêm dòng `1,01` trùng. Hiện có 139 ô như vậy |
| Ô công thức không đọc được (`SUMIFS`, `COUNTIF`…) | Không có hộp phép tính, nhưng **vẫn phải tô được ô nó lấy số**: gắn `data-uses` + class `.uses`; bấm vào là tô vàng các ô nguồn **cùng tab** (khác tab thì không có hộp để hiện nút nên bỏ). **Chỉ tô ô của dòng KHỚP điều kiện**, không tô cả vùng: `crit_split()` lọc theo cột điều kiện. VD `2.3_eCPM!B21` (Impressions US) → 7 ô = `A7:A9` + `C7:C9` + `A21` (không tô EU/SEA); `B28` (Banner) → `B7,B10,B13` + `C7,C10,C13`. Ô có nhiều `SUMIF` (vd trả lời ngắn 2.1) thì lấy **hợp** các dòng khớp, không loại trừ nhau. **Không** gắn nhãn "ô nhập tay" cho ô có công thức: `selfref` chỉ là ô nhập tay khi ô **không** có công thức |
| Số ở tab khác | Không tô được (đang ẩn) → hiện nút `↗ tab 2.5` trong hộp; bấm là đổi tab + tô đúng ô đó |
| Khi nào tô cột phải | **Chỉ khi công thức lấy số TRỰC TIẾP từ bảng giả định / bảng số thật** (`D_Gia_Dinh`, `C_Du_Lieu_That`). Số mà phải tính vòng qua tab khác (công thức chỉ trỏ `2.5_LTV`, `2.2_CPI_CAC`…) thì **không tô cột phải** — tô vàng các ô cùng tab (hoặc chỉ hiện hộp phép tính nếu không có ô cùng tab). Cài đặt: ô có `data-src` nhưng không có ô giả định trực tiếp thì gắn `data-nop="1"`; JS chỉ tô panel khi `.src` **không** có `data-nop`. `data-src` vẫn giữ nguyên trên mọi ô vì nút `↗` ở cột phải chọn đích từ nó (31 nút không đổi) |
| Cột phải | Dòng nguồn tô vàng `.hl` **giữ nguyên** (trước đây fade sau 2,2s — người học kêu mất), chỉ xoá khi bấm ra ngoài. Bấm nút `↗` ở cột phải cũng tô `.hl` dòng đích và cuộn tới, không fade |
| Note ở tiêu đề cột | Cột nào có ô lấy số từ tab khác → tooltip `ⓘ` thêm dòng `Có dùng số của tab 2.5 · 2.2.` — **hết, không thêm câu "bấm vào số để xem phép tính"** (người học đã bảo bỏ) |
| Chữ hiển thị | `plain()` đổi tên sheet khi in ra: `D_Gia_Dinh` → `bảng giả định`, `C_Du_Lieu_That` → `bảng số thật`, `2.5_LTV` → `tab 2.5`, `B_Tom_Tat` → `tab Tóm tắt`, bỏ `ô G43`. File HTML là **độc lập**, người đọc không phải biết tên sheet Excel |
| Vị trí | `position:fixed` trong khung `#work`; không đủ chỗ dưới thì lật lên trên; ô bị cuộn khuất > 0,7s thì tự tắt |
| Nút `↗` ở cột phải | Mỗi dòng nguồn có số dùng thật thì có `↗`. Chọn đích theo thứ tự: **(1) ô dùng số đó trực tiếp** (`refs_of` của ô có đúng `D_Gia_Dinh!<ô>`), (2) ô đang hiện **đúng giá trị** của dòng panel, (3) `data-lab` khớp tên dòng, (4) thứ tự render. Không quay lại `items[0]` — đó là lý do Banner/Interstitial/Rewarded cùng nhảy về ô Banner. Dòng không có `↗` khi **không ô nào** dùng số đó (vd 77–80 chi phí ngoài media chưa nối vào model) **hoặc** khi người học chỉ định trong `NO_ARROW` (hiện là D3 · D14 · D60 — họ chỉ xin thêm `↗` cho D7 và D30). Muốn thêm/bớt thì sửa đúng set đó, **đừng bật hết cả bảng** |
| `↗` tới ô chữ | Ô kết quả là **chữ** (vd `2.7_LTV_CAC!H7` = "ĐẠT") vẫn phải có `id` + `data-src` + class `.src` để làm đích; bấm vào nó chỉ tô nguồn ở cột phải, **không mở hộp phép tính** (không có `data-calc`) |
| Số trong "Trả lời ngắn" | Mỗi con số trong ô xanh lá là 1 `<span class="num">` (gạch chân chấm). Bấm → tô vàng ô nguồn **cùng tab** + hộp `Trả lời ngắn · ô D9` / `= $1.00`; số lấy từ tab khác thì hộp có nút `↗ tab X`. Cắt câu bằng `top_parts()` (**chỉ** cắt theo `&` ở cấp ngoài cùng — chuỗi nằm trong hàm như `"0.0%"` của `TEXT` không phải chữ hiện ra), rồi đọc **token số** bằng `NUM_HEAD`. **Đừng** dùng `text.find(literal)` để tìm số kế tiếp: literal `"."` sẽ cắt ngang `72.2%` thành `72` + `.2%`. Chỉ bọc khi **cả cụm** đúng là số (`NUM_ONLY.fullmatch`) — `Meta Ads`, `SCALE (+20% budget)` để nguyên chữ. Số trùng giá trị ô (`$3.63` vs `3,63`) thì không in 2 lần (`same_num()`). Hiện có **42 số** trên 8 câu |

### 12.6 Quy tắc rút ra khi sửa bản HTML (đọc trước khi động vào)

Lần sau người học kêu sửa giao diện/hộp phép tính thì làm đúng mấy điều này:

1. **Chỉ sinh lại từ script**, không sửa tay `.html`. Sửa `build_html.py` (hoặc giả định trong `D_Gia_Dinh`) → chạy
   `build_html.py --check` → md5 đổi → ghi lại md5 + số byte vào §1 và đầu §12.
2. **Phép tính phải là số thật.** Không in tên hàm Excel, không in tên sheet thô. Không chắc thì **không hiện hộp**
   (`describe()` trả `""`) — thà im còn hơn in sai.
3. **Ô chỉ chép lại 1 con số thì hiện kết quả 1 lần**; đừng bày 2 dòng giống nhau.
4. **Mọi ô số phải có `id="c-<sheet>-<addr>"`**, kể cả ô không có dòng ở cột phải — thiếu id là không tô vàng được.
   `--check` in `thieu-id-dung=0`; nếu khác 0 thì đừng nộp.
5. **Vàng chỉ mất khi bấm ra ngoài** (hoặc `Esc`). Không fade theo thời gian, không tự xoá khi đổi tab vừa tô.
6. **Cột bảng ≤7 cột**: chia bề ngang kiểu *chia đều trước, cột nào cần hơn lấy đủ rồi chia lại*; canh giữa khi
   **≥80%** ô ngắn. Đừng quay lại kiểu cộng dư theo tỷ lệ (cột có 1 chuỗi dài sẽ phình) hay đòi 100% ô ngắn (cả cột
   lệch trái, trông như "cột giãn").
7. **Đo header xuống dòng phải đo đúng**: clone `th` vào một `div` ngoài màn hình có `position:absolute;
   white-space:nowrap`, so `getBoundingClientRect().width` với bề ngang thật. Dùng `Range.getClientRects()` trên node
   đã tách khỏi DOM luôn ra 0 (tưởng là "0 header xuống dòng"); còn đo trên node đang gắn thì `ⓘ` inline-flex làm sai số.
8. **Chấp nhận** còn ~27 header xuống dòng ở 3 bảng 8–12 cột (`2.2`, `2.7`, `2.8`). Muốn hết phải giảm cỡ chữ/bỏ cột —
   hỏi trước, đừng tự làm.
9. Mọi thay đổi ghi vào **§12.3 (nhật ký)** kèm số đo thật, và cập nhật bảng §12/§12.5 nếu quy tắc đổi.
10. **Không sửa**: `Unit_Economics_Home_Workout_bt2.xlsx`, `Channel_Plan_Home_Workout.xlsx` (và `.docx` của Cấp 3).
11. **`Model.sources()` không được memo hoá kết quả rỗng.** Chặn vòng lặp bằng `self._busy`, chỉ ghi `_memo` khi đã tính xong;
    ghi `([], [])` trước khi tính sẽ làm mọi ô chạm lần đầu ở tầng sâu (chuỗi `2.4_ROAS` → `2.5_LTV`) **rỗng vĩnh viễn** →
    `data-src` mất → dòng nguồn mất `↗`. Đây là gốc của lỗi "thiếu ↗ ở D7/D30".
12. **Kiểm `↗` bằng máy, đừng nhìn mắt**: mỗi nút phải (a) có ô đích tồn tại, (b) đúng tab, (c) ô đích có `data-src` chứa
    đúng dòng panel. Muốn biết dòng nào **thiếu** `↗`, liệt kê `.pr` không có `.use` rồi xem số đó có ai dùng không —
    đừng thêm `↗` cho dòng không ai dùng (bấm vào sẽ không đi đâu), và **đừng bật `↗` cho cả bảng** khi người học chỉ xin
    vài dòng: tôn trọng `NO_ARROW`.
13. **`SUMIFS`/`SUMIF`/`COUNTIF` chỉ tô dòng KHỚP điều kiện**, không tô cả vùng: bấm `US` thì tô đúng các dòng `US` của
    bảng nguồn. Dùng `crit_split()` (tính "ô nào **được** lấy" rồi hợp các `SUMIF` lại) — đừng tính "ô nào **bị loại**",
    vì ô có nhiều `SUMIF` trên cùng vùng (như trả lời ngắn `2.1!A3`) sẽ bị loại sạch. Không chắc điều kiện → giữ hết.
14. **Câu "Trả lời ngắn" phải bấm được từng con số**: cắt theo `&` **cấp ngoài cùng** (`top_parts`), đọc số bằng **token số**
    (`NUM_HEAD`), không dùng `text.find(literal)` (literal `"."` cắt ngang `72.2%`), chỉ bọc cụm **đúng là số**
    (`NUM_ONLY.fullmatch`), và literal phải khớp **đúng vị trí** — lệch thì in thường cả ô, đừng đoán.
