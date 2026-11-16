# Bản đọc `.html` — cách dựng và các mục đã CHỐT

> Áp dụng khi làm/sửa **trang đọc** của một bài tập. Hiện tại:
> `index.html` = trang tổng (header chung + iframe) nạp `unit-economics/index.html` (Cấp 2, sinh từ
> `Unit_Economics_Home_Workout_bt2.xlsx` bằng `build_html.py`); `channel-plan/index.html` (Cấp 3) là khung trống;
> CSS/JS dùng chung ở `assets/app.css` + `assets/app.js`.
>
> **Luật số 1: không sửa tay `.html`.** Sửa script → sinh lại → ghi md5 + số byte.
> **Luật số 2: không sửa `.xlsx` gốc** khi làm bản đọc.

## 1. Mục đích & sản phẩm

- **`index.html` = trang tổng**: chỉ có header chung (`HOME WORKOUT` + dropdown chọn bài) và 1 `<iframe>` nạp trang bài. Mặc định nạp `unit-economics/index.html`.
- **Mỗi bài = 1 thư mục có `index.html` riêng** (`unit-economics/`, `channel-plan/`), bên trong chứa thanh tab + nội dung. CSS/JS nằm ở `assets/` dùng chung. **Không cần internet**, double-click `index.html` là mở.
- Vì trang bài nằm trong iframe, trang tổng **không chép nội dung** bài → sửa 1 chỗ, không có 2 bản lệch số. Đây là lý do phải dùng iframe: file tĩnh không tự hiển thị nội dung file khác (`fetch` chết trên `file://`).
- Mọi đường dẫn là **tương đối và trỏ thẳng file** (`assets/app.css`, `../index.html`, `unit-economics/index.html`) để chạy được cả `file://` lẫn GitHub Pages. **Không** trỏ vào thư mục (`../channel-plan/`) — mở bằng `file://` sẽ ra danh sách thư mục, không tự nạp `index.html`. **Không** dùng `fetch()` để nạp nội dung — `fetch` chết trên `file://`.
- Số tính sẵn lúc build bằng thư viện `formulas` rồi nhúng vào HTML. **Không** nhúng engine công thức vào trình duyệt.
- Muốn đổi giả định: sửa sheet `D_Gia_Dinh` trong `.xlsx` → chạy lại 1 lệnh.
- Trang trả lời 1 câu hỏi của người học: "số này ở đâu ra, và nó được tính thế nào" — không phải mở Excel.

## 2. Bố cục

| Hạng mục | Chốt |
|---|---|
| Chia đôi | **6.5 : 3.5** (đo thật 936px : 504px ở 1440) — trái = bài làm, phải 35% = toàn bộ `C_Du_Lieu_That` + `D_Gia_Dinh`, luôn hiện, cuộn riêng |
| Tab | thứ tự file gốc: `Hướng dẫn` → các câu → `Tóm tắt` → `Kết luận` → `Nguồn`. Nằm **trong trang bài** (`unit-economics/index.html`), không nằm ở header tổng. Đổi tab ghi `#hash` của **iframe**; mở thẳng trang bài thì refresh vẫn đúng tab, còn refresh trang tổng thì về tab `Hướng dẫn` |
| Chọn bài | Dropdown **góc phải header tổng** (`Unit Economics` / `Channel Plan`) → đổi trang bằng `location.href`, không nạp nội dung bằng `fetch`. Mặc định `index.html` nạp `unit-economics/index.html` qua iframe. Bài chưa làm (`channel-plan/index.html`) chỉ có header tổng, `main` rỗng. Dropdown hiện **đúng bài đang mở** (`selected`) |
| Màn hẹp <1100px | cột phải thành drawer, nút `Dữ liệu ⇄`, `Esc` để đóng |
| Số | tính sẵn lúc build, nhúng thẳng vào HTML |

## 3. Bảng bài làm (bên trái)

| Hạng mục | Đúng phải là |
|---|---|
| Đơn vị render | **1 bảng cho mỗi KHỐI** (tiêu đề / mục / dòng `Công thức:` cắt khối) → cột chỉ chịu ảnh hưởng của khối đó, không bị sheet 9 cột ép cả khối 4 cột vào 4 cột đầu |
| Cột | **Bỏ mọi cột không có dữ liệu** — chỉ tính cột mà một ô **có chữ bắt đầu** ở đó. Ô merge 5:8 **không** được kéo 8 cột vào bảng (đây là gốc của lỗi header `Sheet dùng nó` bị xuống dòng) |
| Bề ngang, khối ≤7 cột | `.grid.fixed` + `<col style="width:%">`, ước lượng `max(từ dài nhất × 6.8 + 18, header × 6.6 + 18, cả ô × 7.4 + 18, cap 240)`. Tổng ước lượng > 800px hoặc khối ≥8 cột → để **auto layout** (fixed sẽ cắt số) |
| Chia bề ngang | **"chia đều trước, cột nào cần hơn thì lấy đủ rồi chia lại"**. Không cộng phần dư theo tỷ lệ — cột chỉ chứa 1 chuỗi dài (vd cột Google ở 2.6) sẽ phình hơn hẳn 2 cột bên cạnh |
| Khối ≥8 cột | `.grid.wide` (11,5px, padding 6px) |
| Khối ≤3 cột | `.grid.narrow` = `width:auto;max-width:100%` + `padding:5px 15px` — rộng đúng bằng chữ nhưng chừa 15px hai bên. Kéo hết 100% thì cột nhãn phình, số nằm lơ lửng; padding 9px thì chữ dính mép |
| Căn cột | **theo cột, không theo ô**: cột nào **≥80% ô là số / chuỗi ≤12 ký tự** và có header thì cả cột (kể cả header) canh giữa; cột còn lại canh trái. Cột 1 luôn trái. Không `white-space:nowrap` cho ô `.n` |
| Bấm số | Tô **tất cả** ô nguồn liên quan, **không lọc** bớt panel — giữ nguyên ngữ cảnh để đối chiếu |
| Bảng 2–3 cột | Giữ cột nhãn **34%** (từng bị bóp còn 120px trong khi cột số trống 800px) |
| Công thức | **chỉ trong hover `ⓘ`**, không in dưới tên cột (chữ trong bảng phải gọn) |
| Thuật ngữ | từ điển lấy câu chữ từ sheet `A_Huong_Dan` → `ⓘ` hover hiện **giải thích + công thức**. Mục **không có công thức thì không in dòng `Công thức:`**. `info()` bỏ ghi chú <20 ký tự không có số (đỡ spam `ⓘ`) |

## 4. Cột phải — CHỐT (người học xác nhận "đã xong, không chỉnh sửa gì nữa")

Làm lại y như dưới đây, **đừng "cải tiến" thêm**:

| Hạng mục | Đúng phải là |
|---|---|
| Cấu trúc | **1 cột dài**, không chip, không tab con, không khối gập. Header dính trên, cuộn riêng |
| Header | `📱 APP & GIẢ ĐỊNH` — **chỉ chữ đó**, không phụ đề, không dòng hướng dẫn mặc định |
| Chú giải | `🟩 Số thật · 🟨 Giả định · 🟥 Bịa` là `.dlegend` `position:absolute; top:7px; right:10px` trong `.dhead` → **góc phải trên cùng**, đứng yên khi cuộn |
| Dòng hướng dẫn | Chỉ hiện **sau khi bấm một số**: `← <tên dòng> · n ô nguồn`. Bình thường `.dnote:empty` co về 0 (header cao 34px) |
| Dòng dữ liệu | `tên | số | ↗ | ô màu` — `grid-template-columns: minmax(0,1fr) auto 16px 16px`; **ô màu luôn là cột cuối**, `↗` ngay trước nó; `.pr .lbcell{grid-column:4}` để dòng không có nút vẫn thẳng cột màu. **Không bỏ `↗`** (người học đã kêu bỏ là sai) |
| Lề trong | Mọi dòng (`.pr` và `table.mini`) có **6px lề trái cho chữ, 6px lề phải cho ô màu** — `.pr{padding:3px 6px}`, `table.mini th,td{padding:3px 6px}`, `table.mini .lbh,.lbcell{padding:3px 6px 3px 0;width:22px}`, `th[scope=row]{padding-left:6px}`. Ô màu là `.lb{display:inline-block;width:16px}` nên mọi dấu 🟩🟨🟥 cùng 1 mép phải, không phụ thuộc emoji rộng 11 hay 17px |
| Thẳng hàng | Cả panel chỉ được có **1 toạ độ x cho ô màu** và **1 toạ độ x cho nút `↗`** (kể cả `table.mini`) — đo bằng `getBoundingClientRect().right` trong Chrome headless |
| `ⓘ` | Chỉ ở chỗ có gì để giải thích; `info()` bỏ ghi chú <20 ký tự không có số. **`SKIP_INFO = ("Tên app","Package ID","Khoảng giá IAP")` là không có icon** |
| Số thật từ store | Lưới 2 cột; `Contains ads` + `In-app purchases` nằm **chung 1 ô, 2 dòng** (`div.fact.two` + `div.frow`), nhãn rồi `Có` **sát nhau**, không đẩy ra mép |
| URL | `<a class="storelink" target="_blank" rel="noopener">`, tự thêm `https://` nếu thiếu, **gạch chân luôn** (`text-decoration:underline` trên chính `.storelink`), chữ xanh. **Không** để rule `.fv a{...}` đè (đã từng làm mất gạch chân) |
| Số giả định | Khối `A.`–`H.` mỗi mục 1 hàng `tên | số | ↗ | ô màu`; ghi chú/lý do đẩy vào `ⓘ`, không in ra |
| Chữ thừa | **Cấm** các câu: `luôn hiện, không phải đổi tab`, `Bấm một con số bên trái → nhảy tới ô sinh ra nó.`, `hover ⓘ để đọc lý do` |
| Nguồn | Chỉ lấy từ `C_Du_Lieu_That` + `D_Gia_Dinh`; anchor `p-<SHEET_UPPER>-<row>` |

## 5. Hộp "số nào ra số nào" (popover)

Bấm một ô **có phép tính** → hiện hộp nhỏ ngay dưới ô, 3 dòng: `tên cột · tên dòng` / **phép tính bằng số thật** / `= kết quả`. Bấm ra ngoài hoặc `Esc` thì tắt. Hộp nằm trong khung bài làm, không đè thanh tab.

| Hạng mục | Đúng phải là |
|---|---|
| Ô nào có hộp | **Chỉ ô có công thức** (`describe()` ra được chuỗi). Ô nhập tay / số gốc / số giả định **không có hộp** — vẫn toast `🟨 ASSUMED` và nhảy cột phải |
| Nội dung | **Số thật + phép tính**, không bao giờ in tên hàm Excel hay tên sheet. VD `$26.000 ÷ 13.000` `= $2,00` |
| `SUM(vùng)` | Bung thành `a + b + c` (tối đa 12 ô; hơn thì **không hiện hộp**) |
| `SUMPRODUCT(v1,v2)` | `a × b + c × d + …` |
| `ROUND/TEXT/TRUNC(x, …)` | Bỏ phần định dạng, chỉ lấy `x` |
| `MIN/MAX(vùng)` | `nhỏ nhất của (…)` / `lớn nhất của (…)` — chữ Việt, không phải tên hàm. Bỏ ô trống như Excel |
| `IF(đk, a, b)` | Chọn đúng nhánh đã chạy: 1 nhánh chuỗi + 1 nhánh số → lấy nhánh số; cùng loại → tính `đk` bằng số thật (`AND/OR/so sánh`, `truth()`) rồi chọn. Không chắc → **không hiện hộp** |
| Hàm khác (`SUMIFS`, `COUNTIF`, `LEN`, `SUBSTITUTE`…) | Không hiện hộp — thà im còn hơn in hàm lạ |
| Ngoặc | **Giữ nguyên** ngoặc của công thức: `(a + b + c) ÷ 1000` |
| Ô bấm vào phải vàng | **Mọi** ô số (mọi `td[id^="c-"]`, kể cả số gõ tay `Impressions`, `Doanh thu`, và ô Tổng nền xám) đều bấm được và **tự tô vàng** class `on` — CSS `td.on{background:#ffe8a3` **`!important`** vì nền `.tot`/`.key` đè mất. Bấm ô không có công thức thì chỉ vàng ô đó (không có hộp, không có gì để truy nguồn) |
| Số cùng tab | Ô nguồn (trong bài, không phải cột phải) được **tô vàng** `.use-on`; vàng giữ tới khi bấm ra ngoài. Ghi chú trong hộp: `ô vàng = số lấy vào phép tính này` |
| Ô chỉ chép lại 1 con số | `describe()` ra đúng bằng kết quả (vd `=E23` → `1,01`) → **chỉ hiện `= 1,01` một lần**, không in thêm dòng trùng |
| Ô công thức không đọc được | Vẫn **có hộp**: tiêu đề = tên chỉ số (`data-hd`) + nhãn nhóm (`data-lab`), rồi **phép cộng các ô nó lấy số** (lấy `textContent` từ `data-uses` cùng tab, chỉ ô số) khi cộng lại đúng bằng kết quả, cuối cùng dòng `= <kết quả ô>`; ghi chú `ô vàng = số lấy vào phép tính này`. vd `2.3!B21` → `7.920.000 + 1.980.000 + 990.000` → `= 10.890.000`. Cộng không khớp (SUMIFS có điều kiện lọc, hoặc công thức nhân/chia) thì **chỉ in** `= kết quả`, không bịa phép cộng |
| Tô cột phải — dòng nào | Bấm ô có số: tô **các dòng đang hiện ĐÚNG con số đó**. Sánh **chuỗi số** (bỏ `$`, giữ `%` và số thập phân) của từng số hạng trong `data-calc` + kết quả với `.v` của từng dòng. vd 2.3 ARPDAU `(8,0 × $0,52 + 2,0 × $7,43 + 1,0 × $10,70) ÷ 1000` → tô Banner `8,0` · Interstitial `2,0` · Rewarded `1,0`; 2.2 `$11.000` → tô "Tổng chi phí ngoài media". **Không** so theo trị số đã làm tròn (`1` ≠ `1,0`, `2,0%` ≠ `2,0`) — so trị số thì tô nhầm 20+ ô |
| Ô không có `data-src` (số gõ tay) | Tab 2.6/2.8 nhập tay `38,0%`, `20,0%`… nên không có đường truy nguồn: đối chiếu **cả** cột phải, không cần `data-src`. Ô gõ tay không có class `.src`, nên JS phải lấy `pc = s \|\| cd` (chỉ dùng `.src` là mất trắng 23 ô) |
| Số nằm trong **bảng mini** cột phải | Quality index, giá gói, chi phí media… không phải dòng `.pr` mà là `<tr id="p-…">` + `<td class="n">`. So `.v` là trượt hết; phải so `td.n` rồi tô **cả dòng** (`tr.hl`). vd 2.5 §3/§4 `× 1,20` → tô dòng Meta Ads. **Riêng bảng mini giữ dấu `$` trong khoá so** (tiền `$1,20` ≠ hệ số `1,20` ≠ số chu kỳ `0,10`): không thì `2.2!H9` CAC thật `$1,00 + $0,20` tô nhầm dòng Quality index `1,20`. Dòng `.pr`/`.fact` vẫn so bỏ `$` như cũ |
| Không dòng nào trùng số | Tô hết các dòng trong `data-src` — **trừ** ô `data-nop="1"` (số phải tính vòng qua tab khác: tô hết là loang, có ô 17 dòng) và ô đã có nguồn cùng tab |
| Ô dùng cả số trong tab và số cột phải | Tô **cả hai**: ô cùng tab (`.use-on`) **và** dòng cột phải (`.hl`). Cài đặt: `markUses(tg)` gọi vô điều kiện, phần tô panel tính độc lập (đừng quay lại `if(s&&!same&&!nop)`) |
| Cột phải | Dòng nguồn tô vàng `.hl` **giữ nguyên** (không fade theo thời gian), chỉ xoá khi bấm ra ngoài. Bấm `↗` ở cột phải cũng tô `.hl` dòng đích và cuộn tới |
| Note tiêu đề cột | Cột có ô lấy số từ tab khác → tooltip `ⓘ` thêm `Có dùng số của tab 2.5 · 2.2.` — **hết**, không thêm câu "bấm vào số để xem phép tính" |
| Ô định dạng sai trong xlsx | `2.8_Phan_Tang!B20` đặt nhầm `0.0%` nên Excel hiện `29.958.460,1%`; HTML hiện lại `$299.585` bằng `FORMAT_FIX`. **Nên sửa định dạng ô đó trong xlsx nếu mở lại file** |
| Số trong checklist | Cột `Giá trị` không được để số thô: `0,00` cạnh `ĐẠT` đọc như lỗi. Dùng `FORMAT_FIX` (định dạng Excel có chữ bao quanh, `fmt()` hiểu `pre`/`suf`): `3,63 : 1` · `21,1 ngày` · `2 quyết định` · `100,0%` · `293 từ` · `lệch 0,00`. Ô chữ sửa bằng `TEXT_FIX` |
| Chữ hiển thị | `plain()` đổi tên sheet khi in: `D_Gia_Dinh` → `bảng giả định`, `C_Du_Lieu_That` → `bảng số thật`, `2.5_LTV` → `tab 2.5`, `B_Tom_Tat` → `tab Tóm tắt`, bỏ `ô G43`. File HTML độc lập — người đọc không phải biết tên sheet Excel |
| Vị trí | `position:fixed` trong khung `#work`; không đủ chỗ dưới thì lật lên trên; ô bị cuộn khuất > 0,7s thì tự tắt |
| Nút `↗` ở cột phải | Mỗi dòng nguồn có số dùng thật thì có `↗`. Chọn đích: **(1)** ô dùng số đó trực tiếp, **(2)** ô đang hiện đúng giá trị đó, **(3)** `data-lab` khớp tên dòng, **(4)** thứ tự render. Không quay lại `items[0]` |
| `↗` tới ô chữ | Ô kết quả là **chữ** (vd `"ĐẠT"`) vẫn phải có `id` + `data-src` + class `.src` để làm đích; bấm vào nó chỉ tô nguồn, **không mở hộp** (không có `data-calc`) |
| Số trong "Trả lời ngắn" | Mỗi số là 1 `<span class="num">` (gạch chân chấm). Bấm → tô vàng ô nguồn **cùng tab** + hộp `Trả lời ngắn · ô D9` / `= $1.00`; số ở tab khác thì có nút `↗ tab X`. Cắt câu bằng `top_parts()` (**chỉ** cắt theo `&` ở cấp ngoài cùng), đọc **token số** bằng `NUM_HEAD`, chỉ bọc cụm **đúng là số** (`NUM_ONLY.fullmatch`) |
| Số trong đoạn nhận định | Ô chữ, không cắt theo `&` → dùng bảng `ANS_LINK[(sheet, ô)] = [(ngữ cảnh, số, sheet đích, ô, nhãn)]`, thay span vào **đúng cụm ngữ cảnh**; câu chữ đổi thì mục đó **im lặng** (không in sai chỗ). Span: `data-hd`, `data-lab`, `data-uses`, `data-res`; **không** `data-calc` → hộp chỉ hiện `Kết luận · <nhãn>` + dòng vàng `= <kết quả>` + nút `↗ tab X` |
| Nút `↗ tab` | `data-uses` là chữ HOA (`2.6_PLTV`), `id` là title case (`2.6_pLTV`). Phải tìm tab bằng **so sánh không phân biệt hoa/thường cả hai vế** (`t.dataset.t.toUpperCase()===sh.toUpperCase()`), rồi dùng `tab.dataset.t` cho `dataset.sheet`/`dataset.cell` và `tab.textContent` cho chữ trên nút → `↗ tab 2.8`, không in `2.8_Phan_Tang` |

## 6. Quy tắc khi sửa bản HTML

1. **Chỉ sinh lại từ script**, không sửa tay `.html`. Sửa `build_html.py` (hoặc `assets/app.css` / `assets/app.js` nếu là CSS/JS) → chạy `make ok` → số đo file tự ghi vào `docs/manifest.txt` (**không** chép md5/bytes vào docs nữa). **Không** nhúng CSS/JS trở lại vào HTML.
2. **Phép tính phải là số thật.** Không in tên hàm Excel, không in tên sheet thô. Không chắc thì **không hiện hộp** (`describe()` trả `""`).
3. **Ô chỉ chép lại 1 con số → hiện kết quả 1 lần.**
4. **Mọi ô số phải có `id="c-<sheet>-<addr>"`**, kể cả ô không có dòng ở cột phải — thiếu id là không tô vàng được. `--check` in `thieu-id-dung=0`; khác 0 thì đừng nộp.
5. **Vàng chỉ mất khi bấm ra ngoài** (hoặc `Esc`). Không fade, không tự xoá khi đổi tab.
6. **Cột bảng ≤7 cột**: chia bề ngang kiểu *chia đều trước, cột nào cần hơn lấy đủ rồi chia lại*; canh giữa khi **≥80%** ô ngắn. Đừng quay lại cộng dư theo tỷ lệ hay đòi 100% ô ngắn.
7. **Đo header xuống dòng phải đo đúng**: clone `th` vào `div` ngoài màn hình, `position:absolute; white-space:nowrap`, so `getBoundingClientRect().width`. `Range.getClientRects()` trên node đã tách khỏi DOM ra 0 (tưởng "0 header xuống dòng"); đo trên node đang gắn thì `ⓘ` inline-flex làm sai số.
8. **Chấp nhận** ~27 header xuống dòng ở bảng 8–12 cột (`2.2`, `2.7`, `2.8`). Muốn hết phải giảm cỡ chữ/bỏ cột — **hỏi trước**.
9. Mọi thay đổi ghi vào `04-nhat-ky.md` kèm **số đo thật**, và cập nhật lại file này nếu quy tắc đổi.
10. **Không sửa**: `.xlsx` gốc, file của bài khác (với bài 1 là 2 file Cấp 3).
11. **`Model.sources()` không được memo hoá kết quả rỗng.** Chặn vòng lặp bằng `self._busy`, chỉ ghi `_memo` khi tính xong; ghi `([], [])` trước khi tính làm ô chạm lần đầu ở tầng sâu bị **rỗng vĩnh viễn** → mất `data-src` → mất `↗`.
12. **Kiểm `↗` bằng máy, đừng nhìn mắt**: mỗi nút phải (a) có ô đích tồn tại, (b) đúng tab, (c) ô đích có `data-src` chứa đúng dòng panel. Đừng thêm `↗` cho dòng không ai dùng, và **đừng bật `↗` cho cả bảng** khi người học chỉ xin vài dòng — tôn trọng `NO_ARROW`.
13. **`SUMIFS`/`SUMIF`/`COUNTIF` chỉ tô dòng KHỚP điều kiện**, không tô cả vùng (bấm `US` → chỉ dòng `US`). Dùng `crit_split()` theo cách tính "ô nào **được** lấy" rồi hợp các `SUMIF` — đừng tính "ô nào bị loại", vì ô có nhiều `SUMIF` trên cùng vùng sẽ bị loại sạch.
14. **Câu "Trả lời ngắn" phải bấm được từng số**: cắt theo `&` cấp ngoài cùng (`top_parts`), đọc số bằng token (`NUM_HEAD`), không dùng `text.find(literal)` (literal `"."` cắt ngang `72.2%`), và literal phải khớp **đúng vị trí** — lệch thì in thường cả ô.
15. **Số trong nhận định** dùng `ANS_LINK` (khớp **cụm ngữ cảnh**), và mọi nút `↗ tab` lấy `dataset.t` thật của tab. Muốn thêm số bấm được → thêm 1 dòng vào `ANS_LINK` (ngữ cảnh phải **đúng nguyên văn** câu trong ô chữ) rồi chạy lại `--check`.

## 7. Nghiệm thu — 9 mục `--check` không bắt được (đã có script)

`python3 scripts/browser_check.py` (hoặc `make ok`) chạy 1 lần Chrome headless, in 1 dòng/mục, sai mục nào exit 1:

| Lỗi | Cách bắt |
|---|---|
| Các sheet chồng lên nhau (thiếu `.sheet{display:none}`) | `getComputedStyle` từng `.sheet`, đúng 1 cái `display:block` |
| Tab tràn ngang | `#work.scrollWidth > clientWidth` sau khi bấm **từng** tab |
| Ô tràn chữ | so `scrollWidth` vs `clientWidth` của từng `td`/`th` |
| Header lệch canh lề với body | so `textAlign` của `th` với `td` cùng cột, chỉ khi `row.children.length === ths.length` |
| Panel phải tràn | `#data` scrollWidth vs clientWidth, và `scrollWidth` từng `.pr`/`.fact` |
| Nút `↗` trỏ sai / thiếu | duyệt **mọi** `#data .use`: `getElementById(data-go)` phải tồn tại, đúng `data-sheet`, và `data-src` của ô đích chứa `D_GIA_DINH:<dòng panel>` |
| Popover | `data-calc` không chứa tên hàm; bấm 1 ô → hộp hiện + ô nguồn vàng; bấm ra ngoài → tắt hết. Bấm `2.3!B21` (SUMIFS, không có `data-calc`) → hộp phải in `7.920.000 + 1.980.000 + 990.000` và `= 10.890.000` |
| Tô đúng dòng cột phải | Bấm `2.2!F10` → dòng "Tổng chi phí ngoài media" vàng; bấm `2.3!B42` → đúng 3 dòng Banner/Interstitial/Rewarded vàng (so chuỗi số, xem bảng §5) |
| Ô bấm phải vàng | Bấm `2.3!C7` (Impressions, **số gõ tay**), `2.3!B42` (ô tính toán), `2.5!D28` → ô đang bấm phải có class `on` = vàng |

Đo tay chỉ khi cần **nhìn** (màu, khoảng cách): Chrome headless `--window-size=1440,300 --screenshot=…`. Cần số chính xác thì dùng probe in text, đừng đọc ảnh.

## 8. Lệnh build & kiểm

```bash
cd /Users/buzzlp./Downloads/ua
make ok
```

Phải in `KET QUA: DAT`, **0 ô lỗi**, `thieu-id-dung=0`, `file=5/5`, `KIEM: 7/7 muc OK`. Build ghi 5 file:

| File | Vai trò |
|---|---|
| `index.html` | trang tổng: header chung + `<iframe>` nạp bài Cấp 2 |
| `unit-economics/index.html` | nội dung Cấp 2: thanh tab + bảng + panel phải |
| `assets/app.css`, `assets/app.js` | dùng chung mọi bài |
| `channel-plan/index.html` | khung Cấp 3, `main` rỗng |

`--check` còn báo `FILE CU CON SOT` nếu còn `Unit_Economics_Home_Workout.html` — xoá đi, đừng để 2 bản trùng nội dung.

Số đo file nằm ở `docs/manifest.txt` (5 dòng: md5 + bytes + đường dẫn). Không chép tay vào docs — lần build sau sẽ lệch.
