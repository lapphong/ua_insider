# Kế hoạch: chuyển `Unit_Economics_Home_Workout_bt2.xlsx` thành 1 file `.html`

**Người review:** bạn. Mỗi mục dưới đây có dòng `✍️ Ghi chú:` — cứ viết thẳng vào đó, mình đọc rồi sửa plan.
**Trạng thái:** chờ bạn duyệt. Chưa viết code.

---

## 1. Vấn đề đang sửa

Học thì phải mở sheet `D_Gia_Dinh` / `C_Du_Lieu_That` để tra số, rồi nhảy lại sheet 2.x để làm bài. Excel không giữ được 2 chỗ cùng lúc → mỏi tay, mất mạch.

**Cách sửa:** một trang HTML chia đôi màn hình. Trái = bài làm. Phải = toàn bộ dữ liệu app + giả định, **luôn hiện**, có scroll riêng. Bấm vào số bên trái thì bên phải nhảy tới đúng dòng sinh ra số đó.

✍️ Ghi chú:

---

## 2. Sản phẩm

| Hạng mục | Chốt |
|---|---|
| File | `Unit_Economics_Home_Workout.html` — **1 file duy nhất**, không cần internet, double-click là mở |
| Số sheet | 11 tab, đúng thứ tự file gốc: `Hướng dẫn` → `2.1 … 2.8` → `Tóm tắt` → `Kết luận` → `Nguồn` |
| Sửa file gốc? | **Không.** `Unit_Economics_Home_Workout_bt2.xlsx` giữ nguyên |
| Số trong HTML | Tính sẵn từ xlsx (thư viện `formulas`), nhúng thẳng vào HTML. Không nhúng engine công thức vào trình duyệt |

✍️ Ghi chú:

---

## 3. Bố cục 6 : 4

```
┌────────────────────────────────────────────┬──────────────────────────┐
│ Hướng dẫn │ 2.1 │ 2.2 │ 2.3 │ … │ Nguồn     │ 📱 APP & GIẢ ĐỊNH        │ ← dính, luôn thấy
├────────────────────────────────────────────┼──────────────────────────┤
│ 2.2 — MUA 1 LƯỢT CÀI ĐẶT GIÁ BAO NHIÊU?     │ [App] [A] [B] [C] [D]…   │ ← chip nhảy mục
│                                             │                          │
│ ▸ Trả lời ngắn: CPI blended = …  (xanh)     │ A. PHÍ SÀN & NGƯỠNG      │
│                                             │ ┌──────────────────────┐ │
│ ┌ A. CPI và CAC thật theo kênh ───────────┐ │ │ Phí sàn IAP     30%  │ │
│ │ Công thức: CPI = Media ÷ Installs        │ │ │ 🟨 ASSUMED           │ │
│ │ Kênhⓘ  Mediaⓘ  Installsⓘ  CPIⓘ  CACⓘ   │ │ │ Store cắt 30%…       │ │
│ │ Meta   26.000   13.000    2,00   2,15   │ │ ├──────────────────────┤ │
│ │ Google 24.000   20.000    1,20   1,35   │ │ │ Phí sàn Sub     20%  │ │
│ │ …                                        │ │ │ 🟨 ASSUMED           │ │
│ └──────────────────────────────────────────┘ │ └──────────────────────┘ │
│ Số lấy từ đâu: …                             │ B. RETENTION COHORT      │
│                                             │ …                        │
│ 60% — cuộn dọc theo bài                     │ 40% — cuộn dọc riêng     │
└────────────────────────────────────────────┴──────────────────────────┘
```

- Cột phải: `width: 40%`, `min-width: 400px`, `position: sticky`, `height: 100vh`, `overflow-y: auto`. Hai cột cuộn độc lập, không kéo nhau.
- Dưới 1100px: cột phải thu thành drawer, có nút mở/đóng (không làm layout mobile riêng).

✍️ Ghi chú:

---

## 4. Bốn tính năng, làm đúng thứ tự này

### 4.1 Tab sheet (bấm 1 cái là đổi, không load lại)

Cả 11 sheet render sẵn trong DOM, chỉ `.active` được hiện. Đổi tab ghi vào `#hash` → refresh vẫn đúng chỗ, gửi link cho người khác cũng mở đúng câu.

### 4.2 Bấm số bên trái → bên phải nhảy tới nguồn

Lúc build, mỗi ô trong 8 sheet 2.x được phân giải ngược về **ô gốc** ở `D_Gia_Dinh` / `C_Du_Lieu_That`:

- Ô có công thức trỏ thẳng sheet dữ liệu → đó là nguồn.
- Ô trỏ ô khác trong cùng sheet → đi tiếp, tối đa 6 tầng, tới khi gặp ô gốc.
- Ô nhập tay → chính nó là gốc.

Ví dụ thật (đã kiểm trong file):

| Bấm ô | Nguồn nó trỏ tới |
|---|---|
| `2.2!D7` (CPI Meta) | `D_Gia_Dinh!B69` + `C69` |
| `2.2!H10` (CAC blended) | `D_Gia_Dinh!B69:C71` (3 kênh) + `B81` (tổng non-media) |
| `2.7!K10` (CAC tối đa) | đi 3 tầng: `2.7!D10` → `2.5!G49` → `D_Gia_Dinh!` 12 ô |
| `2.3!E7` (eCPM) | **không có nguồn bên phải** — xem luật (b) dưới |

Ba trường hợp, xử lý khác nhau:

- **(a) Có nguồn ở cột phải** → nhảy + tô sáng như trên.
- **(b) Ô nhập tay ngay trong sheet bài** → không nhảy; hiện nhãn nhỏ `nhập tay · 🟨 ASSUMED` để không ai tưởng nó lấy từ `D_Gia_Dinh`. Ví dụ: impressions và doanh thu ở `2.3_eCPM` (dòng 7–16) là ô nhập, eCPM mới là công thức → bấm eCPM sẽ chỉ ra `C7` và `D7` cùng sheet.
- **(c) Chữ / tiêu đề / dòng ghi chú** → không bấm được, không có icon.

Hành vi khi bấm: cột phải cuộn tới nguồn đầu tiên, **tô sáng tất cả** nguồn liên quan 2 giây, và hiện dòng chữ nhỏ `← dùng ở 2.2 · bảng A · cột CPI`.

Ô nào bấm được thì có gạch chấm dưới số + con trỏ bàn tay. Ô không có nguồn (chữ, tiêu đề) thì để yên.

### 4.3 Thuật ngữ có ⓘ + công thức ngay dưới chữ

Mọi cột trong bảng mà tên là thuật ngữ UA sẽ thành:

```
CPI ⓘ
Media ÷ Installs
```

- `ⓘ` hover (hoặc click để ghim) → hộp giải thích 1–2 câu tiếng Việt.
- Dòng nhỏ dưới tên cột = công thức của chính cột đó, in mờ, luôn thấy, không phải hover.

Bộ thuật ngữ lấy từ **31 dòng từ điển ở sheet `A_Huong_Dan`** (dòng 13–43) — đã có sẵn câu chữ bạn viết. Bổ sung công thức cho từng cái:

| Thuật ngữ | Công thức hiện dưới chữ |
|---|---|
| CPI | Media ÷ Installs |
| CAC | (Media + Non-media) ÷ Installs |
| eCPM | Doanh thu ÷ Impressions × 1.000 |
| ARPDAU | Σ(Impressions/DAU × eCPM) ÷ 1.000 |
| ARPPU | Doanh thu ÷ số user có trả tiền |
| Payer rate | Số payer ÷ tổng installs |
| Retention Dn | User còn lại ngày n ÷ user ngày 0 |
| LTV | IAP + IAA + Subscription |
| Net LTV | Gross LTV × (1 − phí sàn) |
| pLTV | LTV dự báo từ tín hiệu 24h |
| ROAS | Doanh thu ÷ chi quảng cáo |
| tROAS | ROAS mục tiêu ÷ GM sau phí sàn |
| Payback | Ngày mà doanh thu tích lũy = CAC |
| LTV:CAC | Net LTV ÷ CAC |
| Phí sàn | Giá × 15–30% |
| Blended | Tổng ÷ tổng của cả 3 kênh |
| Quality index | Hệ số chất lượng user của kênh (1,0 = trung bình) |

### 4.4 Panel phải: dài nhưng không rối

Nội dung = **toàn bộ** `C_Du_Lieu_That` + `D_Gia_Dinh`, chia 9 mục:

`📱 Thông tin app (REAL)` · `A. Phí sàn & ngưỡng` · `B. Retention cohort` · `C. IAA (impressions)` · `D. IAP` · `E. Subscription` · `F. Đường cong doanh thu` · `G. Kênh mua user` · `H. Chi phí ngoài media`

Để 40% màn hình vẫn đọc được (không nhồi 5 cột vào 570px), mỗi dòng đổi thành **2 tầng**:

```
Phí sàn IAP                                    30%   🟨
Store cắt 30%; 15% chỉ khi doanh thu < $1M/năm
```

- Dòng 1: tên + giá trị (căn phải) + nhãn màu.
- Dòng 2: ghi chú, chữ nhỏ, xám.
- Chip `[App][A][B]…[H]` **dính trên đầu cột phải** → bấm là nhảy mục, không phải lăn chuột tìm.
- Mỗi mục thu gọn/mở được (mặc định mở hết; nhớ trạng thái trong 1 phiên).
- Mỗi dòng nguồn có chip ngược: `↗ dùng ở 2.2 · 2.7` → bấm là nhảy về bài làm đúng bảng.

✍️ Ghi chú:

---

## 5. KHÔNG làm (để khỏi phình)

- **Không** cho sửa số trong trình duyệt. Muốn đổi giả định: sửa `D_Gia_Dinh` trong Excel → chạy lại 1 lệnh → HTML mới. (Nhúng engine công thức kiểu HyperFormula là ~500KB + cả buổi sửa bug, không đáng.)
- Không in PDF, không export, không mobile layout riêng.
- Không sửa file xlsx, không sửa 2 file Cấp 3 đã xong.

✍️ Ghi chú:

---

## 6. Cách làm (6 bước, mỗi bước có kiểm chứng)

Script build nằm ở thư mục tạm `…/T/opencode/gen_html.py` (giống các script Cấp 2/3 trước). Chỉ file `.html` ra thư mục dự án.

| # | Việc | Kiểm chứng |
|---|---|---|
| 1 | Đọc xlsx: lấy giá trị đã tính (`formulas`) + cấu trúc ô/merge/định dạng (openpyxl) | In ra 14 sheet, đếm đúng số bảng |
| 2 | Dựng đồ thị phụ thuộc ô → phân giải về ô gốc (tối đa 6 tầng) | Đếm 3 nhóm: có nguồn phải / ô nhập trong sheet / không có; **0 ô rơi vào nhóm "không rõ"** |
| 3 | Render cột trái: 8 sheet bài làm, giữ nguyên tiêu đề / `Công thức:` / `Trả lời ngắn` / `Số lấy từ đâu` | 8 sheet, đủ câu 2.1→2.8, 0 ô `#REF!` / `NaN` |
| 4 | Render cột phải + chip + nhãn màu + chip "dùng ở" | 9 mục, đủ 100% dòng của `C_Du_Lieu_That` + `D_Gia_Dinh` |
| 5 | Gắn ⓘ + công thức dưới tên cột; gắn link cho ô có nguồn | Đếm cột có tooltip / đếm ô bấm được; soát 17 thuật ngữ ở mục 4.3 có mặt đủ |
| 6 | Mở bằng trình duyệt, thử tay | Đổi 11 tab · bấm 5 ô ngẫu nhiên → panel phải nhảy đúng · tooltip hiện không bị cắt · 2 cột cuộn độc lập |

Nghiệm thu cuối (mình tự chạy trước khi đưa):
`11 tab · 0 nguồn không phân giải · 0 lỗi công thức · đủ 8 câu bài làm · 17/17 thuật ngữ có công thức · bấm thử 5 ô đều đúng`.

---

## 7. Cần bạn chốt (mình đã chọn sẵn, bạn chỉ cần nói "OK" hoặc sửa)

1. **Số chốt cứng** (không sửa trong trình duyệt), đổi giả định thì build lại — OK?
2. **Panel phải 1 cột dài + chip nhảy mục**, không tách 2 tab "Thật / Giả" — OK?
3. Bấm số → **tô sáng tất cả nguồn** liên quan (không lọc, không ẩn bớt panel) — OK?
4. Tooltip **hover + click để ghim**; dòng công thức dưới tên cột **luôn hiện** — OK?
5. Tên file `Unit_Economics_Home_Workout.html`, để cùng thư mục `/Downloads/ua` — OK?

✍️ Ghi chú:

---

## 8. Sau khi duyệt

Bạn duyệt plan (hoặc sửa thẳng vào file này) → đổi sang agent code → mình build theo đúng 6 bước, đưa bạn 1 file `.html` + ảnh chụp màn hình để soát bố cục.
