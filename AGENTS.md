# AGENTS.md — mục lục dự án UA

> Đọc file này **trước** mỗi phiên. Nó chỉ có luật cứng + bản đồ tài liệu.
> Chi tiết nằm ở `docs/` — **mở đúng 1 file cần dùng**, đừng đọc cả thư mục.
> Có quyết định/số liệu mới → sửa đúng file `docs/` liên quan, không nhồi vào đây.

## 1. Người học

- Newbie tự học UA Marketing, trao đổi **tiếng Việt**, thuật ngữ UA giữ tiếng Anh.
- Giải thích **tại sao** con số quan trọng, ghi **công cụ check** + **nguồn** cho từng mục.
- Số thật / số giả phải đánh dấu rõ. Ưu tiên hiểu vòng tiền, không cần hoàn hảo.
- Chi tiết cách dạy + nhãn 🟩🟨🟥 + từ điển + bảng công cụ: `docs/00-quy-uoc-chung.md`.

## 2. Luật cứng (không thoả hiệp)

1. Mỗi bài tập nộp **1 file `.xlsx`**; nhận định, nguồn, công cụ nằm trong sheet của chính file đó.
2. Trên **mỗi bảng** có dòng `Công thức: <chỉ số> = <công thức> | <ghi chú>` ngay phía trên header.
3. Mỗi con số có nhãn 🟩 REAL / 🟨 ASSUMED / 🟥 FAKE (cột `Nguồn/Loại`).
4. `.html` / `.docx` là **bản sinh ra từ script** — không sửa tay, không được lệch số với `.xlsx`.
5. File đã chốt **không sửa** khi làm bản đọc; mỗi bài là file mới.
6. Nói "xong" chỉ sau khi **chạy `make ok`** và báo số đo thật; số đo file lấy từ `docs/manifest.txt`, không chép tay.
7. Người học đã bác hướng nào thì không tự thêm lại; mục ghi **CHỐT** thì làm đúng bảng đó.

## 3. Bản đồ tài liệu

| Cần làm gì | Đọc |
|---|---|
| Hiểu người học, ngôn ngữ, nhãn số, thuật ngữ, công cụ/nguồn | `docs/00-quy-uoc-chung.md` |
| Dựng/sửa **bảng tính `.xlsx`** (sheet, dòng công thức, 2 vùng, máy kiểm) | `docs/01-bang-tinh.md` |
| Dựng/sửa **trang đọc `.html`** (bố cục, cột phải CHỐT, popover, nghiệm thu) | `docs/02-ban-doc-html.md` |
| Số liệu, quyết định, md5, lệnh build của **bài đang có** | `docs/03-du-an-01-unit-economics.md` |
| "Tại sao lại quyết định thế" — chỉ khi cần tra | `docs/04-nhat-ky.md` |

## 4. Sản phẩm hiện có

| File | Là gì | Trạng thái |
|---|---|---|
| `Unit_Economics_Home_Workout_bt2.xlsx` | Bài Cấp 2, nguồn khoá (md5 `47b1aad1…`) | ✅ 14 sheet · 0 lỗi · 40/40 khớp |
| `Channel_Plan_Home_Workout.xlsx` | Bài Cấp 3 | ✅ 9 sheet · 65/65 dòng công thức · 0 lỗi |
| `Channel_Plan_Home_Workout.docx` | Bản đọc Cấp 3 (sinh từ xlsx) | ✅ 9 câu · 38 bước · 159 bảng |
| `index.html` | Trang tổng: header chung (`HOME WORKOUT` + dropdown) + `<iframe>` nạp bài Cấp 2 | ✅ chưa tới 1 KB |
| `unit-economics/index.html` | Nội dung Cấp 2 (sinh bằng `build_html.py`), dùng chung `assets/app.css` + `assets/app.js` | ✅ 12 tab · 556 hộp phép tính · 75 số bấm được |
| `channel-plan/index.html` | Khung trang Cấp 3 (trống nội dung, chờ bài sau) | ✅ chỉ header tổng + dropdown chọn bài |

Số đo file (md5 + bytes) **không chép tay**: `make ok` ghi ra `docs/manifest.txt`.

Muốn đổi số: sửa `D_Gia_Dinh` trong `.xlsx` rồi sinh lại — **không** sửa tay `.html`.
Số chốt + quyết định chi tiết: `docs/03-du-an-01-unit-economics.md`.

## 5. Lệnh chạy

```bash
cd /Users/buzzlp./Downloads/ua
make ok     # build + kiểm số liệu + ghi docs/manifest.txt + kiểm 7 mục layout
```

Đạt khi in `KET QUA: DAT`, `thieu-id-dung=0`, `file=5/5`, `KIEM: 7/7 muc OK`. Chạy lẻ: `python3 scripts/browser_check.py`.

Build lại file Cấp 3 (script q1–q9 + `fix.py` + `makedoc.py`) và cách kiểm `.xlsx`: `docs/03-du-an-01-unit-economics.md` §7.

Commit: `make commit msg="…"` · `make amend` · `make push`.

## 6. Bắt đầu bài tập mới — 7 bước

1. Chốt đề bài + app/đề tài **thật** (có listing công khai) → lấy số 🟩 trước.
2. Tách đề thành **đúng số câu**; mỗi câu 1 sheet, tên sheet = số câu.
3. Dựng sheet số thật + sheet giả định **trước**; mọi sheet bài làm chỉ tham chiếu 2 sheet đó.
4. Trình bày theo `docs/01-bang-tinh.md`: dòng `Công thức:` mỗi bảng, `Trả lời ngắn` / `CẦN XÁC ĐỊNH GÌ` → `BƯỚC` → `KẾT LUẬN`, panel nguồn ngang hàng bước.
5. Chốt: nhận định 200–300 từ + checklist tiêu chí có đơn vị; sheet công cụ/nguồn.
6. Chạy máy kiểm (mục 7 của `01`) tới khi 0 lỗi → mới làm bản đọc `.html`/`.docx`.
7. Ghi hồ sơ bài mới vào `docs/03-…` (hoặc file `03-du-an-02-….md`) + nhật ký vào `docs/04-nhat-ky.md`.

## 7. Khi sửa tài liệu

- Quy tắc **đang áp dụng** → `docs/00`–`02`. Lịch sử + số đo → `docs/04`.
- Số liệu/file của một bài → `docs/03-…` của bài đó.
- Đừng để luật nằm 2 nơi: sửa ở file chuyên mục, `AGENTS.md` chỉ giữ 1 dòng trỏ tới.
