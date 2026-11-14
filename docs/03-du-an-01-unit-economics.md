# Dự án 01 — Unit Economics (Cấp 2) & Channel Plan (Cấp 3)

> Hồ sơ của bài đã làm: app nào, số nào, file nào, build bằng gì.
> Quy ước chung để làm bài mới nằm ở `01-bang-tinh.md` và `02-ban-doc-html.md`.

## 1. Sản phẩm

| # | File | Trạng thái |
|---|------|-----------|
| 1 | `Unit_Economics_Home_Workout_bt2.xlsx` — toàn bộ bài Cấp 2, 1 file duy nhất | ✅ 14 sheet · 0 công thức lỗi · 40/40 số kiểm tra khớp |
| 2 | `Channel_Plan_Home_Workout.xlsx` — Cấp 3 Channel Plan | ✅ 9 sheet · 2 vùng/sheet · 0 lỗi · 65/65 bảng có dòng `Công thức:` · 0 merge chồng · 0 bước thiếu panel |
| 3 | `Channel_Plan_Home_Workout.docx` — bản đọc/nộp Cấp 3, sinh từ file xlsx | ✅ 9 câu · 38 bước · 9 kết luận · 159 bảng |
| 4 | `Unit_Economics_Home_Workout.html` — bản đọc Cấp 2, sinh từ file xlsx bằng `build_html.py` | ✅ 12 tab · 515 ô nhảy phải · 556 ô có phép tính · 75 số bấm được · 31 nút `↗` · `415.685 bytes` · md5 `25f698e3ea524a4819c67671c701654e` |

Nguồn khoá: `Unit_Economics_Home_Workout_bt2.xlsx` md5 `47b1aad1d8d80906808274bf498add7a` — **không sửa**.

## 2. App & số thật (🟩 REAL, Google Play, 2026-11-03)

| Chỉ số | Giá trị |
|--------|---------|
| Tên app | Home Workout - No Equipment |
| Package | `homeworkout.homeworkouts.noequipment` |
| Developer | Leap Fitness Group |
| Category | Health & Fitness |
| Installs | 100,000,000+ |
| Rating | 4.86 (≈4.05M reviews) |
| Contains ads | Có |
| In-app purchases | Có, $2.99 – $69.99 / item |

URL: `https://play.google.com/store/apps/details?id=homeworkout.homeworkouts.noequipment&hl=en&gl=US`

Toàn bộ doanh thu, CPI, eCPM, retention, churn, payer rate, phân tầng user là **mô phỏng** (🟨 có benchmark / 🟥 bịa). Không dùng để ra quyết định thật.

## 3. Đề Cấp 2 — 8 câu

1. **Monetization (2.1):** IAP / IAA / Sub / Freemium / Hybrid + liệt kê đủ 100% nguồn doanh thu.
2. **CPI & CAC (2.2, 2.7):** CPI từ chi phí media; CAC thật = (media + non-media) ÷ install, rồi nhân gross margin sau phí sàn 15–30%.
3. **eCPM (2.3):** eCPM tổng + tách theo Geo và theo định dạng.
4. **ROAS curve (2.4):** bảng D0/D7/D30/D90, đánh dấu điểm hòa vốn; blended vs theo kênh.
5. **LTV (2.5):** Total LTV = IAP + IAA + Sub; kiểm chứng chéo bằng ARPU/Churn.
6. **pLTV (2.6):** tín hiệu 24h đầu + ngưỡng scale/pause trong 48h.
7. **LTV:CAC & payback (2.7):** tỷ lệ, payback period, phân loại (<1:1 cần cứu / ~3:1 khỏe / >4:1 scale).
8. **Phân tầng user (2.8):** whale/dolphin/minnow, tỷ trọng doanh thu, 1 chiến dịch tối ưu (tROAS hoặc Highest Value).

**Tiêu chí đạt:** 1 bảng tính + nhận định 200–300 từ trả lời "CAC tối đa được trả là bao nhiêu, hoàn vốn trong bao lâu?". Số liệu nhất quán, LTV ≥ CAC×3, payback < 12 tháng, ≥1 quyết định scale/pause có lập luận bằng pLTV.

## 4. Sheet map

### Cấp 2 — `Unit_Economics_Home_Workout_bt2.xlsx` (14 sheet)

| Nhóm | Sheet | Trả lời câu |
|------|-------|-------------|
| Hướng dẫn | `A_Huong_Dan` | — (thứ tự đọc, 30 thuật ngữ, nhãn dữ liệu, mục lục) |
| Tóm tắt | `B_Tom_Tat` | tất cả (26 số chốt + 3 câu hỏi chốt + bản 30 giây) |
| Dữ liệu | `C_Du_Lieu_That` · `D_Gia_Dinh` | — |
| Bài làm | `2.1_Monetization` · `2.2_CPI_CAC` · `2.3_eCPM` · `2.4_ROAS` · `2.5_LTV` · `2.6_pLTV` · `2.7_LTV_CAC` · `2.8_Phan_Tang` | đúng 2.1 → 2.8 |
| Chốt | `E_Ket_Luan` | nhận định 293 từ + checklist 7 tiêu chí |
| Tra cứu | `F_Nguon_Cong_Cu` | công cụ + benchmark cho từng mục |

Kiểu trình bày: **5.1 trong `01-bang-tinh.md`** (Trả lời ngắn + Số lấy từ đâu).

### Cấp 3 — `Channel_Plan_Home_Workout.xlsx` (9 sheet = 4 bài làm + 5 phụ)

| Nhóm | Sheet | Trả lời câu |
|------|-------|-------------|
| Hướng dẫn | `A_Huong_Dan` | — (31 thuật ngữ, quy ước ô) |
| Tóm tắt | `B_Tom_Tat` | 3 quyết định + ngân sách + KPI + timeline 90 ngày |
| Dữ liệu | `C_So_Lieu_Ke_Thua` · `D_Gia_Dinh` | số vay Cấp 2 + 8 số Google Play + giả định |
| Bài làm | `C1_Chon_Kenh` | Câu 1 = 3.1 (mục tiêu → so 5 kênh → chốt 3) |
| Bài làm | `C2_Setup_Kenh` | Câu 2 = 3.2 Google AC + 3.3 Meta AAC + 3.5 TikTok |
| Bài làm | `C3_Mo_Rong` | Câu 3 = 3.6 DSP + 3.7 Retargeting + 3.8 Web-to-app |
| Bài làm | `C4_Policy_Do_Luong` | Câu 4 = 3.9 Policy + đo lường (MMP, event, iOS) |
| Tra cứu | `F_Nguon_Cong_Cu` | công cụ + benchmark + 4 giả định dễ bị chất vấn |

Kiểu trình bày: **5.2 trong `01-bang-tinh.md`** (2 vùng, panel ngang hàng bước: C1→K, C2→H, C3→H, C4→G).

## 5. Quyết định riêng của dự án này

| Ngày | Quyết định | Lý do |
|------|-----------|-------|
| 2026-11-03 | App: **Home Workout – No Equipment** (Leap Fitness Group) | App thật, có Ads + IAP, 100M+ install, giá IAP $2.99–$69.99; fitness có benchmark CPI/retention công khai |
| 2026-11-03 | File `FitPal_Unit_Economics.xlsx` là **giả hoàn toàn**, chỉ học cấu trúc | Người học xác nhận |
| 2026-11-03 | **Không sửa app Notes** `User Acquisition 2` — chỉ đọc lấy câu chữ (cá voi/cá heo/cá con, "tỷ lệ vàng 3:1", "gồng lỗ", "kê cao gối ngủ") rồi viết lại trong xlsx | Người học yêu cầu đúng vậy |
| 2026-11-03 | tROAS D7 phải `÷ GM sau phí sàn` | Nền tảng chỉ thấy doanh thu GROSS, mốc 3:1 là chuyện NET. Thiếu GM ra 57.8%/11.9% — sai bản chất |
| 2026-11-04 | `2.3_eCPM`: impressions + doanh thu là **ô nhập**, eCPM là **cột công thức** `= D ÷ C × 1000`; nhãn 🟨 ASSUMED | Yêu cầu là "tính eCPM", không phải suy doanh thu từ eCPM |
| 2026-11-10 | Cấp 3: **3 kênh** Meta AAC + Google AC + TikTok | Thực tế tuyển UA cần 3 kênh; đề cho 2–3 |
| 2026-11-10 | Ngân sách **$6.000/tháng all-in** = media $5.000 + non-media 20% | Non-media phân bổ theo tỷ trọng media |
| 2026-11-10 | **ASA ngoài phạm vi** | Model Cấp 2 không tách dữ liệu iOS |
| 2026-11-10 | TikTok giữ theo đề: 3 hook UGC + validate-then-scale + cổng 14 ngày | Đề yêu cầu quy trình này; Cấp 2 đã pause TikTok nên đây là mở lại **có điều kiện**, không đảo kết luận |
| 2026-11-10 | 3.8 chọn **web-to-app** thay CTV | Đo được + né phí sàn |

## 6. Số cuối cùng (đã kiểm bằng máy)

### Cấp 2

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
| tROAS D7 tối thiểu / khởi điểm | **72.2% / 65.0%** (đã ÷ GM sau phí sàn) |

### Cấp 3

| Chỉ số | Giá trị |
|--------|---------|
| Media / non-media / all-in | $5.000 / $1.000 / **$6.000** |
| Installs/tháng | **3.617** (Meta 1.075 · Google 1.542 · TikTok 1.000) |
| CAC blended | **$1.659** (Meta $2,40 · Google $1,44 · TikTok $1,20) |
| Net LTV blended | **$5.570** |
| LTV:CAC blended | **3.358** (giảm từ 3,63 vì TikTok kéo xuống) |
| Meta trial start | 62,7/tuần → thoát learning; tối ưu Purchase cần $3.061/tháng (+$911) |
| Google | $61,7/ngày ≥ 50×CPI $60 · tCPA ~$4.320/tháng · tROAS ~42 ngày đủ 300 purchase |
| TikTok trial start | 58,3/tuần; pLTV:CAC **1,98** — thiếu 1,0% so ngưỡng 2,0 |
| DSP | **0/3 điều kiện** → chưa mở; mốc sớm nhất tháng thứ 10 |
| 3.9 | Publish 9 PASS + 1 kiểm lại (families); Misleading Ad 9 PASS + 1 sửa (before/after) |

## 7. Build

### Bản đọc Cấp 2 (`.html`)

```bash
cd /Users/buzzlp./Downloads/ua
/private/var/folders/7h/z4fmlq_j0rj59jbzkbht6y880000gn/T/opencode/venv3/bin/python build_html.py --check
```

### File Cấp 3 (`.xlsx` + `.docx`)

Script ở `/private/var/folders/7h/z4fmlq_j0rj59jbzkbht6y880000gn/T/opencode/` (q1–q9.py):

```bash
cat q1.py q2.py q3.py q4.py q5.py q6.py q7.py q8.py q9.py > build.py
./venv3/bin/python build.py
./venv3/bin/python fix.py       # bắt buộc: tính lại chiều cao ô "Kết luận"
./venv3/bin/python makedoc.py   # xuất .docx từ chính file xlsx vừa build
```

`addnotes.py` đã chạy 1 lần (chèn 27 panel còn thiếu) — **chạy lại sẽ nhân đôi, đừng chạy**.

## 8. Lỗi đã gặp khi build Cấp 3 (đừng lặp lại)

- `3.2_Google_AC` đọc nhầm `C_So_Lieu_Ke_Thua!B32/B33` (LTV:CAC, payback) thay vì `B40/B41` (tROAS). Nguyên nhân: dấu `\'` trong chuỗi Python làm lệnh replace trượt.
- Block `3.3`/`3.5` dùng row cứng (`C24`, `C32`…) nên khi append vào sheet gộp bị trỏ sai và crash `MergedCell`. Sửa bằng `base = r` + `f"=C{base+n}"`.
- 4 bảng thiếu dòng "Số lấy từ đâu" (`3.1` mục A, `3.2` mục A, `3.5` mục B, `3.8` mục C).

## 9. Việc tiếp theo

Bài đã xong. Nếu muốn đi sâu: thay số ở `D_Gia_Dinh` + `2.3_eCPM` + `2.6_pLTV` + `2.8_Phan_Tang` bằng dữ liệu thật của app mình rồi đọc lại `B_Tom_Tat` và `2.7_LTV_CAC`. Không sửa ô chữ đen (công thức).
