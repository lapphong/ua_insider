# Quy ước bảng tính (`.xlsx`)

> Áp dụng cho mọi bài tập. Bài đã làm cụ thể: `03-du-an-01-unit-economics.md`.
> Sản phẩm nộp là **file tính**; `.html` / `.docx` chỉ là bản đọc sinh ra từ nó.

## 1. Một file, nhiều sheet

- Nộp đúng **1 file `.xlsx`**. Nhận định 200–300 từ, nguồn, công cụ đều nằm trong sheet của cùng file đó.
- Không tạo file `.md` / `.csv` rời để "kèm theo".
- Mỗi file bài tập là **file mới**, không sửa file của bài trước (xem `AGENTS.md` mục luật cứng).

## 2. Tên sheet = số câu hỏi

- Sheet bài làm đặt theo **số câu của đề**: `2.1_Monetization`, `2.2_CPI_CAC`, …, hoặc `C1_Chon_Kenh` nếu đề đánh số 3.1–3.9 nhưng chỉ có 4 câu.
- Mục đích: mở tab là biết đang trả lời câu nào, đối chiếu đề không phải nhớ.
- Sheet phụ dùng **chữ cái** để không đụng số câu: `A_Huong_Dan`, `B_Tom_Tat`, `C_...` (số liệu), `D_...` (giả định), `E_Ket_Luan`, `F_Nguon_Cong_Cu`.
- Đề có 4 câu thì gộp thành **4 sheet bài làm**, mỗi sheet 1 câu — đừng 1 sheet/note lý thuyết (dễ lạc, khó đối chiếu).

## 3. Khung sheet tối thiểu

| Nhóm | Sheet | Nội dung |
|------|-------|----------|
| Hướng dẫn | `A_Huong_Dan` | thứ tự đọc, thuật ngữ, nhãn dữ liệu, mục lục, lưu ý |
| Tóm tắt | `B_Tom_Tat` | các số chốt + câu hỏi chốt + bản đọc 30 giây |
| Dữ liệu | `C_...`, `D_...` | số thật (có link) tách riêng khỏi toàn bộ giả định |
| Bài làm | theo số câu | mỗi sheet đúng 1 câu của đề |
| Chốt | `E_Ket_Luan` | nhận định 200–300 từ + checklist tiêu chí |
| Tra cứu | `F_Nguon_Cong_Cu` | công cụ thật + benchmark cho từng mục |

## 4. Dòng `Công thức:` — bắt buộc trên **mỗi bảng**

Ngay **phía trên dòng tiêu đề** của mọi bảng, có 1 dòng:

```
Công thức: <tên chỉ số> = <công thức> | <ghi chú ngắn>
```

- Mục đích: người đọc thấy công thức mà không phải click vào ô.
- Áp dụng cho **từng bảng**, không phải từng sheet. Một sheet 3 bảng → 3 dòng `Công thức:`.
- Kiểm bằng máy: đếm số bảng có dòng `Công thức:` ngay trên header (bài Cấp 3 đã đạt 65/65).

## 5. Hai kiểu trình bày bài làm

### 5.1 Câu trả lời gọn (Cấp 2 — 8 câu độc lập)

Trong mỗi sheet `2.x`:

1. Tiêu đề in **đúng câu hỏi của đề**.
2. Ô **"Trả lời ngắn"** nền xanh lá ngay dưới tiêu đề — công thức `TEXT()` sống, đọc 1 câu là trả lời được câu hỏi.
3. Các bảng dữ liệu + tính toán.
4. Dòng **"Số lấy từ đâu"** nền xanh nhạt ngay dưới mỗi bảng — hiện luôn giá trị + sheet/ô gốc.

Mục đích: không phải nhảy tab. Thêm `B_Tom_Tat` gom toàn bộ số chốt kèm ô gốc cho người chỉ muốn đọc kết quả.

### 5.2 Câu nhiều bước (Cấp 3 — 4 câu, mỗi câu 5–10 bước)

Chia **2 vùng trên 1 sheet**:

| Vùng | Nội dung |
|------|----------|
| **TRÁI** (cột 1–n) | đọc từ trên xuống: `CẦN XÁC ĐỊNH GÌ` → `BƯỚC 1..n` → `KẾT LUẬN` (ô xanh, **cuối** câu) |
| **PHẢI** (cột `n+2`, cách 1 cột trống) | panel **ngang hàng đúng bước**: `NGUỒN SỐ ·` (sheet › bảng › dòng) hoặc `KIẾN THỨC ·` (vì sao bước này quan trọng) |

Quy tắc:

- Panel đặt ở cột `len(widths)+2`, rộng 34 + 13 + 13. **38/38 bước phải có panel** — không có bước nào trống bên phải.
- `CẦN XÁC ĐỊNH GÌ` là bảng 3 cột: input → lấy ở **sheet › bảng › dòng** → dùng ở bước nào.
- Không đặt kết luận ở đầu. Người học phải thấy quá trình ra số rồi mới đọc kết luận.
- Panel ghi **sheet › bảng › dòng**, không chỉ địa chỉ ô — trả lời được "con số này ở bảng nào".

## 6. Số liệu phải nhất quán

- Một số chỉ có **một ô gốc**; mọi chỗ khác tham chiếu, không gõ lại.
- Trước khi nộp, kiểm chéo các số chốt giữa sheet bài làm ↔ `B_Tom_Tat` ↔ `E_Ket_Luan`.
- Nhận định 200–300 từ ở `E_Ket_Luan` phải trả lời đúng câu hỏi chốt của đề (bài 1: "CAC tối đa được trả là bao nhiêu, hoàn vốn trong bao lâu?") và **mọi số trong đó khớp file tính**.
- Checklist tiêu chí: mỗi dòng = 1 tiêu chí, 1 giá trị, 1 kết luận ĐẠT/KHÔNG. Ô số trong checklist phải có **đơn vị** (`3,63 : 1`, `21,1 ngày`), không để số thô `3,63` / `0,00` cạnh chữ ĐẠT.

## 7. Máy kiểm trước khi nộp

Máy không có LibreOffice → dùng thư viện `formulas` (Python) để tính lại toàn bộ file:

```python
from formulas import ExcelModel
m = ExcelModel().loads(path).finish()
m.calculate()
```

Đếm và phải bằng 0 / đủ:

| Kiểm | Ngưỡng đạt |
|------|-----------|
| Ô lỗi (`#REF!`, `#VALUE!`, `#DIV/0!`, `None`) | 0 |
| Merge chồng nhau | 0 |
| Bảng thiếu dòng `Công thức:` phía trên header | 0 |
| `BƯỚC` không có panel cùng hàng (kiểu 2 vùng) | 0 |
| Số kiểm tra khớp giá trị kỳ vọng | 100% |
| Tiêu chí trong checklist | đủ, tất cả ĐẠT |

## 8. Checklist khi làm **bài tập mới**

1. Chốt app/đề tài **thật** (có listing công khai) → lấy số 🟩 trước.
2. Đọc đề, tách **đúng số câu**; mỗi câu 1 sheet, tên = số câu.
3. Dựng `C_...` (số thật) + `D_...` (giả định) **trước** khi làm bài — mọi sheet bài làm chỉ tham chiếu 2 sheet này.
4. Mỗi bảng: dòng `Công thức:` → header → dữ liệu → dòng nguồn / panel.
5. Mỗi câu: `Trả lời ngắn` (Cấp 2) hoặc `CẦN XÁC ĐỊNH GÌ` → `BƯỚC` → `KẾT LUẬN` (Cấp 3).
6. `E_Ket_Luan`: nhận định 200–300 từ + checklist tiêu chí có đơn vị.
7. `F_Nguon_Cong_Cu`: mỗi chỉ số 1 dòng công cụ + nguồn benchmark.
8. Chạy máy kiểm mục 7, sửa tới khi 0 lỗi rồi mới báo xong.
