# UA Marketing — bài tập thực hành

🇻🇳 **Tiếng Việt** · [🇬🇧 English](README.md)

Repo này là **bài tập học User Acquisition (UA)**, không phải sản phẩm, không phải báo cáo số liệu thị trường.
Mỗi bài nộp là **1 file Excel**, kèm **bản đọc `.html`** sinh ra từ chính file Excel đó.

- **Tác giả bài làm:** Long Phan
- **Khoá học:** [UA Insider Academy](https://academy.uainsider.io.vn/) — *UA Marketing thực chiến cho người làm mobile app*
- **Hiện có:** bài 2 — Unit Economics (UA cơ bản). Danh sách đầy đủ: bảng [Các bài đã làm](#lessons).

## Chỉ để học

- Số liệu trong bài là **ví dụ để học cách tính**, không dùng để trích dẫn, đầu tư hay ra quyết định kinh doanh.
- App dùng làm đề bài là app thật (**Home Workout – No Equipment**, Leap Fitness Group) nhưng các con số tài chính phần lớn là **giả định của người học**, không phải số nội bộ của app.
- Mỗi con số đều được dán nhãn, xem cột `Nguồn/Loại` trong file Excel:

| Nhãn | Nghĩa |
|---|---|
| 🟩 REAL | Số thật, lấy từ nguồn công khai (Google Play, bảng giá App Store…) — có ghi ngày lấy |
| 🟨 ASSUMED | Số giả định hợp lý của người học (benchmark ngành, kinh nghiệm) |
| 🟥 FAKE | Số bịa có chủ đích để dựng kịch bản / so sánh |

Vì vậy: đọc để hiểu **vòng tiền và cách lập luận**, đừng coi các con số là dữ kiện.

## Xem bài

Không cần cài gì, không cần internet:

1. Mở `index.html` (double-click) → trang tổng có dropdown chọn bài.
2. Trong trang bài: chuyển tab bằng thanh tab trên cùng, bấm vào **một ô số** để xem phép tính và các ô nguồn (vàng), nút **⤓ Tải .xlsx** ở góc phải thanh tab để tải file bài nộp.

## Cấu trúc

| File / thư mục | Là gì |
|---|---|
| `*.xlsx` | Bài nộp, mỗi bài 1 file — **nguồn duy nhất**, không sửa tay sau khi chốt |
| `index.html` | Trang tổng: header + dropdown chọn bài + `<iframe>` nạp trang bài |
| `unit-economics/`, `channel-plan/` | Bản đọc từng bài — **sinh tự động**, không sửa tay |
| `assets/app.css`, `assets/app.js` | CSS/JS dùng chung cho mọi bài |
| `build_html.py` | Sinh `.html` từ `.xlsx` + tự kiểm số liệu |
| `scripts/` | Kiểm layout bằng headless Chrome, script commit |
| `docs/` | Quy ước làm bài, hồ sơ từng bài, nhật ký quyết định, `manifest.txt` (md5 + bytes) |

**Luật của repo:** `.xlsx` là nguồn duy nhất; `.html` sinh ra từ script nên **không sửa tay** — muốn đổi số thì sửa `.xlsx` rồi build lại.

## Build & kiểm

```bash
cd ua
make ok     # build .html + kiểm số liệu + ghi docs/manifest.txt + kiểm 9 mục layout
```

Cần Python 3 với `openpyxl` và `formulas` (makefile mặc định dùng venv trong thư mục tạm; nếu báo thiếu module thì tạo venv mới và `pip install openpyxl formulas`).

Đạt khi in `KET QUA: DAT`, `thieu-id-dung=0`, `file=5/5`, `KIEM: 9/9 muc OK`.

Chi tiết quy ước: `docs/00-quy-uoc-chung.md` · bảng tính: `docs/01-bang-tinh.md` · trang đọc: `docs/02-ban-doc-html.md` · hồ sơ bài: `docs/03-du-an-01-unit-economics.md`.

## Ghi nhận

Đề bài, khung kiến thức và cách đánh giá thuộc về **UA Insider Academy** ([academy.uainsider.io.vn](https://academy.uainsider.io.vn/)).
Repo này chỉ chứa **bài làm của người học**, không chứa tài liệu khoá học — vui lòng không dùng lại nội dung khoá học từ đây.

---

<a id="lessons"></a>

## Các bài đã làm

Bài mới = **thêm 1 dòng**, và dòng đó phải **giống hệt** trong file này với `README.md` (`make ok` báo lỗi nếu 2 bảng lệch nhau).

| # | Bài · Lesson | Cấp · Level | File nộp · Workbook | Bản đọc · Reading page | Trạng thái · Status |
|---|---|---|---|---|---|
| 2 | Unit Economics | UA cơ bản · Basics | `Unit_Economics_Home_Workout_bt2.xlsx` | [`unit-economics/`](unit-economics/index.html) | ✅ xong · done |
| 3 | Channel Plan | Cấp 3 · Level 3 | `Channel_Plan_Home_Workout.xlsx` | [`channel-plan/`](channel-plan/index.html) | 🟨 có Excel, trang đọc trống · workbook only |
