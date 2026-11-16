# -*- coding: utf-8 -*-
"""Sinh trang tong (index.html) + trang Channel Plan tu file xlsx (KHONG sua file goc).

Ra: index.html (mac dinh = bai Cấp 2), channel-plan/index.html,
    dung chung assets/app.css, assets/app.js
Chay:  ./venv3/bin/python build_html.py
Kiem:  ./venv3/bin/python build_html.py --check
"""
import hashlib
import html
import os
import re
import sys
import warnings

import openpyxl

warnings.filterwarnings("ignore")

SRC = "/Users/buzzlp./Downloads/ua/Unit_Economics_Home_Workout_bt2.xlsx"
ROOT = "/Users/buzzlp./Downloads/ua"
# Moi file build sinh ra. So do (md5 + bytes) ghi vao docs/manifest.txt, khong chep tay vao docs.
OUTPUTS = ["index.html", "unit-economics/index.html", "channel-plan/index.html",
           "assets/app.css", "assets/app.js"]
MANIFEST = f"{ROOT}/docs/manifest.txt"
# Trang tổng (index.html) mặc định là bài Cấp 2; dropdown đổi sang bài khác.
# Đường dẫn tính từ gốc repo. Thêm bài mới = thêm 1 dòng.
PAGES = [("index.html", "Unit Economics"), ("channel-plan/index.html", "Channel Plan")]

DATA_SHEETS = ("C_DU_LIEU_THAT", "D_GIA_DINH")
WORK_SHEETS = [
    ("A_Huong_Dan", "Hướng dẫn"),
    ("2.1_Monetization", "2.1"),
    ("2.2_CPI_CAC", "2.2"),
    ("2.3_eCPM", "2.3"),
    ("2.4_ROAS", "2.4"),
    ("2.5_LTV", "2.5"),
    ("2.6_pLTV", "2.6"),
    ("2.7_LTV_CAC", "2.7"),
    ("2.8_Phan_Tang", "2.8"),
    ("B_Tom_Tat", "Tóm tắt"),
    ("E_Ket_Luan", "Kết luận"),
    ("F_Nguon_Cong_Cu", "Nguồn"),
]
SHORT = {k: v for k, v in WORK_SHEETS}
NUM_SHEETS = len(WORK_SHEETS)

# ------------------------------------------------------------------ gia tri
REF_VAL = re.compile(r"\]'?([A-Za-z0-9_.\-]+)'?!([A-Z]+)(\d+)$")

# ------------------------------------------------------------------ cong thuc
STR_LIT = re.compile(r'"[^"]*"')
SHEET_REF = re.compile(
    r"(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_.\-]*))?!(\$?[A-Z]{1,3}\$?\d+)"
    r"(?::(\$?[A-Z]{1,3}\$?\d+))?"
)
LOCAL_REF = re.compile(r"(\$?[A-Z]{1,3}\$?\d+)(?::(\$?[A-Z]{1,3}\$?\d+))?")


def load_values():
    import formulas
    sol = formulas.ExcelModel().loads(SRC).finish().calculate()
    val = {}
    for k, v in sol.items():
        m = REF_VAL.search(k)
        if not m:
            continue
        try:
            val[(m.group(1).upper(), f"{m.group(2)}{m.group(3)}")] = v.value[0][0]
        except Exception:
            pass
    return val


def split_addr(a):
    m = re.match(r"\$?([A-Z]{1,3})\$?(\d+)", a)
    col = 0
    for ch in m.group(1):
        col = col * 26 + (ord(ch) - 64)
    return col, int(m.group(2))


def expand(a, b=None):
    c1, r1 = split_addr(a)
    if not b:
        return [(c1, r1)]
    c2, r2 = split_addr(b)
    out = []
    for r in range(min(r1, r2), max(r1, r2) + 1):
        for c in range(min(c1, c2), max(c1, c2) + 1):
            out.append((c, r))
            if len(out) > 400:
                return out
    return out


def refs_of(formula, sheet):
    body = STR_LIT.sub('""', formula)
    out = []
    for m in SHEET_REF.finditer(body):
        name = (m.group(1) or m.group(2) or "").upper()
        out += [(name, c, r) for c, r in expand(m.group(3), m.group(4))]
    body2 = SHEET_REF.sub(" S ", body)
    for m in LOCAL_REF.finditer(body2):
        out += [(sheet.upper(), c, r) for c, r in expand(m.group(1), m.group(2))]
    return out


class Model:
    def __init__(self):
        self.wb = openpyxl.load_workbook(SRC)
        self.by_up = {ws.title.upper(): ws for ws in self.wb}
        self.val = load_values()
        self.grid = {}
        for ws in self.wb:
            g = {}
            for row in ws.iter_rows(max_row=ws.max_row, max_col=ws.max_column):
                for c in row:
                    if c.value is not None:
                        g[(c.column, c.row)] = c.value
            self.grid[ws.title.upper()] = g
        self._memo = {}
        self._busy = set()

    def raw(self, sheet, col, row):
        return self.grid.get(sheet.upper(), {}).get((col, row))

    def sources(self, sheet, col, row, depth=0):
        key = (sheet.upper(), col, row)
        if key in self._memo:
            return self._memo[key]
        # vong lap / qua sau: tra rong nhung KHONG ghi memo (truoc day ghi
        # ([],[]) vao memo => o nao bi cham lan dau o tang sau bi rong vinh vien,
        # mat mui ten ↗ o cot phai)
        if key in self._busy or depth > 6:
            return ([], [])
        self._busy.add(key)
        try:
            raw = self.raw(sheet, col, row)
            if not isinstance(raw, str) or not raw.startswith("="):
                res = ([(sheet.upper(), row)] if sheet.upper() in DATA_SHEETS
                       else [], [(sheet.upper(), col, row)])
            else:
                data, selfref = [], []
                for s, c, r in refs_of(raw, sheet):
                    if s in DATA_SHEETS:
                        data.append((s, r))
                    else:
                        d2, s2 = self.sources(s, c, r, depth + 1)
                        data += d2
                        selfref += s2
                res = (list(dict.fromkeys(data)), list(dict.fromkeys(selfref)))
        finally:
            self._busy.discard(key)
        self._memo[key] = res
        return res


# ------------------------------------------------------------------ format so
NUMRE = re.compile(r"\d[\d.,]*\d|\d")


def vn_num(s):
    if not isinstance(s, str):
        return s

    def rep(m):
        t = m.group(0)
        if "." in t and "," in t:
            t = t.replace(",", "")
            head, _, dec = t.partition(".")
            return f"{int(head):,}".replace(",", ".") + "," + dec
        if "," in t:
            parts = t.split(",")
            if all(len(x) == 3 for x in parts[1:]):
                return t.replace(",", ".")
            return t
        if "." in t:
            parts = t.split(".")
            if all(len(x) == 3 for x in parts[1:]):
                return t
            return t.replace(".", ",")
        return t

    return NUMRE.sub(rep, s)


def fmt(v, nf):
    """Dinh dang so, ho tro chu bao quanh kieu Excel: 0.0" ngày" · "lệch "0.00"""
    pre = suf = ""
    num = v is not None and isinstance(v, (int, float)) and not isinstance(v, bool)
    if isinstance(nf, str) and num:
        m = re.match(r'^"([^"]*)"(.*)$', nf)
        if m:
            pre, nf = m.group(1), m.group(2)
        m = re.search(r'"([^"]*)"$', nf or "")
        if m:
            suf, nf = m.group(1), nf[:m.start()]
    return pre + fmt_core(v, nf) + suf


def fmt_core(v, nf):
    if v is None:
        return ""
    if isinstance(v, (int, float)) and not isinstance(v, bool) and v == 0:
        v = 0.0          # -0,00 -> 0,00 (bang chenh lech toan so 0 van hien dau tru)
    if isinstance(v, bool):
        return "CÓ" if v else "KHÔNG"
    if isinstance(v, str):
        return v
    if not isinstance(v, (int, float)):
        return str(v)
    nf = nf or "General"
    if "%" in nf:
        dec = len(nf.split(".")[1].split("%")[0]) if "." in nf else 0
        return vn_num(f"{v * 100:,.{dec}f}") + "%"
    if "$" in nf:
        dec = len(nf.split('.')[1].split('"')[0]) if "." in nf else 0
        return "$" + vn_num(f"{v:,.{dec}f}")
    if "#,##0" in nf:
        dec = len(nf.split(".")[1]) if "." in nf else 0
        return vn_num(f"{v:,.{dec}f}")
    m = re.match(r"^0(?:\.(0+))?$", nf)
    if m:
        dec = len(m.group(1) or "")
        return vn_num(f"{v:,.{dec}f}")
    if isinstance(v, float):
        return vn_num(f"{v:.2f}")
    return str(v)


def esc(s):
    return html.escape(str(s), quote=True)


# ------------------------------------------------------------------ tu dien
GLOSSARY = [
    ("pLTV:CAC", "Tỷ lệ dự báo: chia pLTV cho CAC. Đọc sau 48h để biết nên scale hay tắt.",
     "pLTV net 365 ÷ CAC thật"),
    ("LTV:CAC", "Tỷ lệ vàng: 1:1 là hòa tiền ads (vẫn lỗ) · 3:1 là khỏe · >4:1 nên scale.",
     "Net LTV ÷ CAC thật"),
    ("ARPPU", "Doanh thu ÷ số user CÓ trả tiền. Khác ARPU: ARPU chia cho mọi user.",
     "Revenue ÷ Payers"),
    ("ARPU", "Doanh thu ÷ toàn bộ user, tính cả người không trả đồng nào.", "Revenue ÷ Users"),
    ("ARPDAU", "Mỗi user đang dùng app kiếm được bao nhiêu tiền quảng cáo trong 1 ngày.",
     "Σ(Impr/DAU × eCPM) ÷ 1.000"),
    ("Retention", "Còn bao nhiêu % user quay lại vào ngày thứ n.", "User ngày n ÷ user ngày 0"),
    ("Cohort", "Nhóm user cùng ngày cài app, được theo dõi cùng nhau.", "—"),
    ("Churn", "% user trả tiền bỏ đi mỗi tháng.", "Số rời ÷ số đầu kỳ"),
    ("pLTV", "LTV dự đoán từ tín hiệu 24h đầu — quyết định sớm thay vì chờ 30 ngày.",
     "LTV net 365 × chỉ số tín hiệu 24h"),
    ("LTV", "Tổng tiền 1 user mang lại trong cả vòng đời.", "IAP + IAA + Subscription"),
    ("tROAS", "ROAS mục tiêu đặt cho máy học, để nó đi tìm user giống nhóm sinh lời.",
     "ROAS mục tiêu ÷ GM sau phí sàn"),
    ("ROAS", "Thu về bao nhiêu đồng trên mỗi 1 đồng chi quảng cáo.", "Doanh thu ÷ chi quảng cáo"),
    ("Payback", "Bao lâu thì tiền thu về bằng tiền đã bỏ ra mua user.",
     "Ngày mà doanh thu tích lũy = CAC"),
    ("Hòa vốn", "Điểm doanh thu tích lũy vừa bằng chi phí mua user.", "Ngày ROAS = 1"),
    ("eCPM", "Cứ 1.000 lượt quảng cáo hiện ra thì thu về bao nhiêu tiền.",
     "Doanh thu ÷ Impressions × 1.000"),
    ("Impressions", "1 lượt quảng cáo hiện ra trước mắt user.", "—"),
    ("CPI", "Giá mua 1 lượt cài đặt — CHỈ tính tiền quảng cáo.",
     "Media ÷ Installs"),
    ("CAC", "Giá THẬT của 1 user: cộng cả quảng cáo, creative, tool, lương team.",
     "(Media + Non-media) ÷ Installs"),
    ("Non-media", "Tiền tiêu cho UA nhưng không nạp vào nền tảng quảng cáo.",
     "Tổng non-media ÷ Installs"),
    ("Media", "Tiền nạp vào Facebook / Google / TikTok để chạy quảng cáo.", "—"),
    ("Installs", "1 lượt tải + cài app.", "—"),
    ("Payer rate", "% installs trở thành người trả tiền.", "Payers ÷ Installs"),
    ("Gross margin", "Phần doanh thu còn lại sau khi store lấy 15–30%.", "Net ÷ Gross"),
    ("Phí sàn", "Apple / Google cắt 15–30% mỗi giao dịch.", "Giá × 15–30%"),
    ("Blended", "Gộp cả 3 kênh thành 1 con số trung bình có trọng số.", "Tổng ÷ tổng"),
    ("Quality index", "Hệ số chất lượng user của từng kênh. 1,0 = trung bình.",
     "LTV kênh ÷ LTV base"),
    ("Whale", "Cá voi: user chi ≥ $100 trong 365 ngày.", "—"),
    ("Dolphin", "Cá heo: user chi $25–99 trong 365 ngày.", "—"),
    ("Minnow", "Cá con: user chi dưới $25 trong 365 ngày.", "—"),
    ("IAA", "Bán sự chú ý: cho user xem quảng cáo, mạng quảng cáo trả tiền.",
     "Impressions × eCPM ÷ 1.000"),
    ("IAP", "User mua lẻ trong app, trả 1 lần.", "Payer rate × ARPPU"),
    ("Subscription", "User trả tiền định kỳ (tuần / tháng / năm).",
     "Payer rate × ARPPU × số chu kỳ"),
    ("Hybrid", "Làm IAA + IAP + Subscription cùng lúc, trên nền Freemium.", "—"),
]
GLOSSARY.sort(key=lambda x: -len(x[0]))


def term_of(text):
    """Tim thuat ngu xuat hien som nhat trong tieu de cot."""
    low = text.lower()
    best = None
    for key, dec, f in GLOSSARY:
        i = low.find(key.lower())
        if i < 0:
            continue
        if best is None or i < best[1]:
            best = (key, i, dec, f)
    return best


# ------------------------------------------------------------------ bang tra cuu o
def cell_fill(c):
    try:
        rgb = c.fill.fgColor.rgb
        return str(rgb)[-6:].upper() if rgb and c.fill.patternType else ""
    except Exception:
        return ""


def cell_color(c):
    try:
        rgb = c.font.color.rgb
        return str(rgb)[-6:].upper() if rgb else ""
    except Exception:
        return ""


def merge_map(ws):
    spans, covered = {}, set()
    for m in ws.merged_cells.ranges:
        spans[(m.min_col, m.min_row)] = (m.max_row - m.min_row + 1, m.max_col - m.min_col + 1)
        for r in range(m.min_row, m.max_row + 1):
            for c in range(m.min_col, m.max_col + 1):
                if (c, r) != (m.min_col, m.min_row):
                    covered.add((c, r))
    return spans, covered


# o trong xlsx dat nham dinh dang % (hien "29.958.460,1%") - hien lai thanh tien
# + checklist Kết luận: so tho "3,63 / 1,00 / 0,00" khong co don vi nen doc khong ra
#   (0,00 la CHENH LECH chu khong phai doanh thu -> phai ghi "lệch 0,00")
FORMAT_FIX = {
    ("2.8_PHAN_TANG", "B20"): '"$"#,##0',
    ("E_KET_LUAN", "B11"): '0.00" : 1"',
    ("E_KET_LUAN", "B12"): '0.0" ngày"',
    ("E_KET_LUAN", "B13"): '0" quyết định"',
    ("E_KET_LUAN", "B14"): "0.0%",
    ("E_KET_LUAN", "B15"): '0" từ"',
    ("E_KET_LUAN", "B16"): '"lệch "0.00',
    ("E_KET_LUAN", "B17"): "0.0%",
}

# o CHU sua lai cho ro nghia (khong doi so)
TEXT_FIX = {
    ("E_KET_LUAN", "A9"): "Công thức: mỗi tiêu chí so sánh trực tiếp với ngưỡng trong "
                          "bảng giả định và trả về ĐẠT / KHÔNG ĐẠT",
    ("E_KET_LUAN", "A16"): "LTV cộng dồn khớp (IAA+IAP+Sub) — chênh lệch phải = 0",
}

# So trong phan NHAN DINH (tab Ket luan) bam duoc -> hop "so gi ra so nay" + nut nhay sang tab goc.
# (ngu canh trong cau, so can bam, sheet, o, nhan)
ANS_LINK = {
    ("E_KET_LUAN", "A5"): [
        ("khoảng $2.10 mỗi install", "$2.10", "2.7_LTV_CAC", "K10", "CAC tối đa được phép trả"),
        ("365 ngày $6.31", "$6.31", "2.5_LTV", "G49", "Net LTV365 blended"),
        ("là $1.74, gồm", "$1.74", "2.7_LTV_CAC", "B10", "CAC thật blended"),
        ("gồm CPI $1.45", "$1.45", "2.2_CPI_CAC", "D10", "CPI blended"),
        ("và $0.29 chi phí", "$0.29", "2.2_CPI_CAC", "G10", "Chi phí ngoài media / install"),
        ("khoảng $0.37", "$0.37", "2.7_LTV_CAC", "L10", "Dư địa CAC"),
        ("hoàn vốn quanh D21", "D21", "2.4_ROAS", "G35", "Payback blended (ngày)"),
        ("gross LTV $7.66", "$7.66", "2.5_LTV", "G29", "Gross LTV365 base"),
        ("gross margin 80%", "80%", "2.5_LTV", "G34", "Gross margin sau phí sàn"),
        ("là $2.17 —", "$2.17", "2.2_CPI_CAC", "D18", "CAC điều chỉnh theo gross"),
        ("khoảng 83% gross LTV", "83%", "2.5_LTV", "G61", "% Subscription trong gross LTV"),
        ("IAP 11%", "11%", "2.5_LTV", "G60", "% IAP trong gross LTV"),
        ("IAA 6%", "6%", "2.5_LTV", "G59", "% IAA trong gross LTV"),
        ("Google đạt 4.68:1", "4.68:1", "2.7_LTV_CAC", "E8", "LTV:CAC Google"),
        ("hoàn vốn D14", "D14", "2.7_LTV_CAC", "F8", "Payback Google (ngày)"),
        ("Meta 3.07:1", "3.07:1", "2.7_LTV_CAC", "E7", "LTV:CAC Meta"),
        ("hoàn vốn D27", "D27", "2.7_LTV_CAC", "F7", "Payback Meta (ngày)"),
        ("TikTok chỉ 1.53:1", "1.53:1", "2.7_LTV_CAC", "E9", "LTV:CAC TikTok"),
        ("hoàn vốn D110", "D110", "2.7_LTV_CAC", "F9", "Payback TikTok (ngày)"),
        ("trial start 1.6%", "1.6%", "2.6_PLTV", "F18", "Trial start 24h TikTok"),
        ("benchmark 14%", "14%", "2.6_PLTV", "C18", "Trial start benchmark"),
        ("D1 retention 17%", "17%", "2.6_PLTV", "F15", "D1 retention TikTok"),
        ("pLTV:CAC 1.98", "1.98", "2.6_PLTV", "D32", "pLTV:CAC TikTok"),
        ("ngưỡng pause 2.0", "2.0", "2.6_PLTV", "B8", "Ngưỡng pause"),
        ("Google đạt 4.29", "4.29", "2.6_PLTV", "C32", "pLTV:CAC Google"),
        ("ngưỡng scale 3.5", "3.5", "2.6_PLTV", "B7", "Ngưỡng scale"),
        ("tăng 20% budget", "20%", "2.6_PLTV", "B10", "Mức tăng budget khi scale"),
        ("Meta 2.79", "2.79", "2.6_PLTV", "B32", "pLTV:CAC Meta"),
        ("blended lên 3.78", "3.78", "2.7_LTV_CAC", "C20", "LTV:CAC sau khi pause TikTok"),
        ("chỉ 5.5% user", "5.5%", "2.8_PHAN_TANG", "B18", "Whale + Dolphin: % installs"),
        ("nhưng tạo 78.6% doanh thu", "78.6%", "2.8_PHAN_TANG", "B19", "Whale + Dolphin: % doanh thu"),
        ("tROAS D7 65%", "65%", "2.8_PHAN_TANG", "B31", "tROAS D7 khởi điểm"),
        ("tới ngưỡng 72%", "72%", "2.8_PHAN_TANG", "B28", "tROAS D7 tối thiểu"),
    ],
}


SHEET_WORD = {"D_GIA_DINH": "bảng giả định", "C_DU_LIEU_THAT": "bảng số thật"}


def plain(t):
    """Chu hien ra cho nguoi doc: khong de ten sheet kieu D_Gia_Dinh, 2.5_LTV, 'ô G43'."""
    if not isinstance(t, str):
        return t
    t = re.sub(r"(sheet\s+)?D_Gia_Dinh", "bảng giả định", t, flags=re.I)
    t = re.sub(r"(sheet\s+)?C_Du_Lieu_That", "bảng số thật", t, flags=re.I)
    t = re.sub(r"\b(A_Huong_Dan|B_Tom_Tat|E_Ket_Luan|F_Nguon_Cong_Cu)\b",
               lambda mm: "tab " + SHORT[mm.group(1)], t)
    t = re.sub(r"\b(\d\.\d)_[A-Za-z_0-9]+", r"tab \1", t)
    t = re.sub(r"\s*ô\s+\$?[A-Z]{1,3}\$?\d+", "", t)
    return t


def display(m, ws, col, row):
    """(text, is_number) cua 1 o, da tinh cong thuc."""
    c = ws.cell(row=row, column=col)
    v = c.value
    addr = f"{openpyxl.utils.get_column_letter(col)}{row}"
    nf = FORMAT_FIX.get((ws.title.upper(), addr), c.number_format)
    if v is None:
        return "", False
    if isinstance(v, str) and (ws.title.upper(), addr) in TEXT_FIX:
        return TEXT_FIX[(ws.title.upper(), addr)], False
    if isinstance(v, str) and v.startswith("="):
        got = m.val.get((ws.title.upper(), addr))
        if got is None:
            return "", False
        return plain(fmt(got, nf)), isinstance(got, (int, float))
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return fmt(v, nf), True
    return plain(str(v)), False


def row_kind(ws, r):
    f = cell_fill(ws.cell(row=r, column=1))
    if f == "1F3864":
        return "title" if (ws.cell(row=r, column=1).font.sz or 10) >= 14 else "head"
    return {"DEEAF6": "sec", "E2EFDA": "ans", "F2F2F2": "fml", "F1F7EF": "ref"}.get(f, "body")


def term_html(text, extra=""):
    hit = term_of(text)
    if hit:
        key, _i, dec, f = hit
        # muc khong co cong thuc thi khong in dong "Cong thuc: --"
        fml = f'<br><i>Công thức: {esc(f)}</i>' if f.strip() not in ("", "-", "--", "–", "—") else ""
        tip = f'<b>{esc(key)}</b><br>{esc(dec)}{fml}'
    elif extra:
        tip = ""
    else:
        return esc(text)
    if extra:
        tip += ("<br>" if tip else "") + esc(extra)
    return f'{esc(text)}<span class="info" tabindex="0" data-tip="{esc(tip)}">i</span>'


# ------------------------------------------------------------------ cot trai
def row_items(m, ws, spans, covered, r, maxc):
    items, c = [], 1
    while c <= maxc:
        if (c, r) in covered:
            c += 1
            continue
        rs, cs = spans.get((c, r), (1, 1))
        text, isnum = display(m, ws, c, r)
        items.append((c, cs, rs, text, isnum, ws.cell(row=r, column=c)))
        c += max(1, cs)
    return items


CALC_REF = re.compile(
    r"(?:(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_.\-]*))!)?"
    r"(\$?[A-Z]{1,3}\$?\d+)(?::(\$?[A-Z]{1,3}\$?\d+))?"
)
INNER_FN = re.compile(r"([A-Z][A-Z0-9\.]*)\(([^()]*)\)")
RANGE_RE = re.compile(r"^(?:(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_.\-]*))!)?"
                      r"\$?([A-Z]{1,3})\$?(\d+):\$?([A-Z]{1,3})\$?(\d+)$")
NUMBER_OK = re.compile(r"^[\d.eE+\-/*() ]+$")


def split_args(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch in ",;" and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [a.strip() for a in out]


def is_lit(s):
    s = s.strip()
    return len(s) > 1 and s[0] == '"' and s[-1] == '"'


def cell_value(m, sheet, addr):
    """So da dinh dang cua 1 o; None neu khong co / la chuoi dai."""
    addr = addr.replace("$", "")
    got, ws = m.val.get((sheet.upper(), addr)), m.by_up.get(sheet.upper())
    if got is None or ws is None:
        return None
    c, r = split_addr(addr)
    nf = FORMAT_FIX.get((sheet.upper(), addr), ws.cell(row=r, column=c).number_format)
    s = fmt(got, nf)
    return s if len(s) <= 24 else None


def range_cells(arg, sheet):
    """[(sheet, col, row)] cua 1 vung; [] neu khong phai vung."""
    mm = RANGE_RE.match(arg.strip())
    if not mm:
        return []
    up = (mm.group(1) or mm.group(2) or sheet).upper()
    cells = expand(f"{mm.group(3)}{mm.group(4)}", f"{mm.group(5)}{mm.group(6)}")
    return [(up, c, r) for c, r in cells]


SUMIF_RE = re.compile(r"\b(SUMIFS?|COUNTIFS?)\(([^()]*)\)")


def _crit(m, sheet, crit):
    """Nguong so sanh cua dieu kien: (op, value) hoac None neu khong chac."""
    c = crit.strip()
    op = "="
    for o in (">=", "<=", "<>", ">", "<", "="):
        if c.startswith(o):
            op, c = o, c[len(o):].strip()
            break
    if is_lit(c):
        return op, c[1:-1]
    if re.match(r"^-?\d+(\.\d+)?$", c):
        return op, float(c)
    cells = range_cells(c, sheet)
    if not cells:
        mm = CALC_REF.fullmatch(c)
        if mm:      # dieu kien la 1 O don (vd A21) chu khong phai vung
            up = (mm.group(1) or mm.group(2) or sheet).upper()
            cells = [(up,) + split_addr(mm.group(3))]
    if len(cells) == 1:
        s, col, r = cells[0]
        v = m.val.get((s.upper(), f"{openpyxl.utils.get_column_letter(col)}{r}"))
        if isinstance(v, (int, float, str)) and not isinstance(v, bool):
            return op, v
    return None


def _hit(op, want, v):
    """True/False/None (khong chac) khi so sanh 1 o voi dieu kien."""
    if isinstance(want, str):
        if not isinstance(v, str):
            return None
        return {"=": v == want, "<>": v != want}.get(op)
    if not isinstance(v, (int, float)) or isinstance(v, bool):
        return None
    return {">=": v >= want, "<=": v <= want, ">": v > want, "<": v < want,
            "=": abs(v - want) < 1e-9, "<>": abs(v - want) >= 1e-9}.get(op)


def crit_split(m, sheet, formula):
    """SUMIFS/SUMIF: (o thuoc vung dieu kien, o THAT SU duoc lay) -> chi to o thu 2.
    Vd 2.3 bang B: bam US chi to 3 dong US cua bang Geo, khong to EU/SEA."""
    covered, used = set(), set()
    for mm in SUMIF_RE.finditer(formula):
        name, args = mm.group(1).upper(), split_args(mm.group(2))
        if name.startswith("SUMIFS") or name.startswith("COUNTIFS"):
            if len(args) < 3:
                continue
            got = range_cells(args[0], sheet)
            pairs = [(range_cells(args[i], sheet), args[i + 1])
                     for i in range(1, len(args) - 1, 2)]
        else:
            if len(args) < 2:
                continue
            got = range_cells(args[2], sheet) if len(args) > 2 else range_cells(args[0], sheet)
            pairs = [(range_cells(args[0], sheet), args[1])]
        if not got:
            continue
        keep = [True] * len(got)
        marked = []
        for crit_cells, cond in pairs:
            cv = _crit(m, sheet, cond)
            hits = [None] * len(crit_cells) if cv is None else [
                _hit(cv[0], cv[1],
                     m.val.get((s.upper(), f"{openpyxl.utils.get_column_letter(c)}{r}")))
                for s, c, r in crit_cells]
            covered |= set(crit_cells)
            marked.append((crit_cells, hits))
            if len(crit_cells) == len(got):
                for i, hit in enumerate(hits):
                    if hit is False:
                        keep[i] = False
        covered |= set(got)
        used |= {cell for cell, ok in zip(got, keep) if ok}
        for crit_cells, hits in marked:
            used |= {cell for cell, hit in zip(crit_cells, hits) if hit is not False}
    return covered, used


def subst_number(m, sheet, expr):
    """Gia tri so cua 1 bieu thuc so sanh don gian (co the thay o). None neu khong chac."""
    ok = [True]

    def rep(mm):
        up = (mm.group(1) or mm.group(2) or sheet).upper()
        got = m.val.get((up, mm.group(3).replace("$", "")))
        if not isinstance(got, (int, float)) or isinstance(got, bool):
            ok[0] = False
            return "0"
        return repr(float(got))

    s = CALC_REF.sub(rep, expr)
    if not ok[0] or not NUMBER_OK.match(s):
        return None
    try:
        return eval(s, {"__builtins__": {}}, {})      # chi con so va + - * / ()
    except Exception:
        return None


def truth(m, sheet, cond):
    """True / False / None (khong chac) cho dieu kien AND/OR/so sanh."""
    c = cond.strip()
    mm = re.match(r"^(AND|OR)\((.*)\)$", c, re.I)
    if mm:
        vals = [truth(m, sheet, a) for a in split_args(mm.group(2))]
        if mm.group(1).upper() == "AND":
            return False if False in vals else (True if all(v is True for v in vals) else None)
        return True if True in vals else (False if all(v is False for v in vals) else None)
    mm = re.match(r"^(.+?)(>=|<=|<>|>|<|=)(.+)$", c)
    if mm:
        l, r = subst_number(m, sheet, mm.group(1)), subst_number(m, sheet, mm.group(3))
        if l is None or r is None:
            return None
        return {">=": l >= r, "<=": l <= r, ">": l > r, "<": l < r,
                "=": abs(l - r) < 1e-9, "<>": abs(l - r) >= 1e-9}[mm.group(2)]
    return None


def _fn(m, sheet, name, inner):
    """Doi 1 ham thanh phep tinh bang chu/số. None = khong biet -> khong hien hop."""
    args = split_args(inner)

    def values(a):
        """So trong 1 vung, bo o trong (Excel cung bo qua o trong khi tinh)."""
        cells = range_cells(a, sheet)
        if not cells or len(cells) > 12:
            return None
        vs = [cell_value(m, s, f"{openpyxl.utils.get_column_letter(c)}{r}")
              for s, c, r in cells]
        vs = [v for v in vs if v not in (None, "")]
        return vs or None

    if name in ("SUM", "MIN", "MAX"):
        vals = []
        for a in args:
            vs = values(a)
            if vs is None:
                return None
            vals += vs
        if name == "SUM":
            return "(" + " + ".join(vals) + ")"
        word = "nhỏ nhất của " if name == "MIN" else "lớn nhất của "
        return word + "(" + ", ".join(vals) + ")"
    if name == "SUMPRODUCT":
        r1, r2 = range_cells(args[0], sheet), range_cells(args[1], sheet)
        if not r1 or len(r1) != len(r2):
            return None
        vs = [(cell_value(m, s1, f"{openpyxl.utils.get_column_letter(c1)}{r1_}")
               , cell_value(m, s2, f"{openpyxl.utils.get_column_letter(c2)}{r2_}"))
              for (s1, c1, r1_), (s2, c2, r2_) in zip(r1, r2)]
        if any(a in (None, "") or b in (None, "") for a, b in vs):
            return None
        return "(" + " + ".join(f"{a} × {b}" for a, b in vs) + ")"
    if name in ("ROUND", "TEXT", "TRUNC"):
        return args[0]
    return None


def describe(m, sheet, formula, depth=0):
    """Cau phep tinh bang SO that: '$26.000 ÷ 13.000'. Khong in ten ham Excel.
    '' = khong mo ta duoc (o nhap tay, ham la, ...) -> khong hien hop."""
    if not (isinstance(formula, str) and formula.startswith("=")) or depth > 5:
        return ""
    body = formula[1:].strip()
    if re.match(r"^IF\(", body, re.I) and body.endswith(")"):
        args = split_args(body[3:-1])
        if len(args) == 3:
            a, b = args[1], args[2]
            if is_lit(a) != is_lit(b):
                pick = b if is_lit(a) else a
            else:
                got = truth(m, sheet, args[0])
                if got is None:
                    return ""
                pick = a if got else b
            return describe(m, sheet, "=" + pick, depth + 1)
        return ""
    s = body
    for _ in range(12):
        mm = INNER_FN.search(s)
        if not mm:
            break
        rep = _fn(m, sheet, mm.group(1).upper(), mm.group(2))
        if rep is None:
            return ""
        s = s[:mm.start()] + rep + s[mm.end():]

    def sub_ref(mm):
        up = (mm.group(1) or mm.group(2) or sheet).upper()
        return cell_value(m, up, mm.group(3)) or mm.group(0)
    s = CALC_REF.sub(sub_ref, s)
    if re.search(r"[A-Za-z]", re.sub(r"(nhỏ nhất|lớn nhất) của", "", s)):
        return ""                              # con ten ham / dia chi o -> khong hieu
    s = s.replace("*", " × ").replace("/", " ÷ ")
    s = re.sub(r"(?<=[\w)%])\s*([+-])\s*(?=[\w$(])", r" \1 ", s)
    s = re.sub(r"\s+", " ", s).strip()
    if is_lit(s):                              # chi la chuoi hang: "Đủ" -> Đủ (de JS so voi ket qua)
        s = s[1:-1]
    return (s[:170] + "…") if len(s) > 170 else s


def internal_uses(m, sheet, formula, limit=24):
    """Cac o TRONG BAI (tab khac hoac bang khac) ma o nay lay so, de to vang + nhay tab."""
    if not (isinstance(formula, str) and formula.startswith("=")):
        return []
    out = []
    covered, used = crit_split(m, sheet, formula)
    for s, c, r in refs_of(formula, sheet):
        if s in DATA_SHEETS:
            continue
        if (s, c, r) in covered and (s, c, r) not in used:
            continue        # dong khong khop dieu kien SUMIFS -> khong to
        ws = m.by_up.get(s)
        if ws is None:
            continue
        raw = ws.cell(row=r, column=c).value
        # o trong (khong in ra bang) thi khong to duoc -> bo
        if raw is None or (isinstance(raw, str) and raw.startswith("=") and m.val.get((s, f"{openpyxl.utils.get_column_letter(c)}{r}")) in (None, "")):
            continue
        addr = f"{openpyxl.utils.get_column_letter(c)}{r}"
        if (s, addr) not in out:
            out.append((s, addr))
    return out[:limit]


def top_parts(body):
    """Cat cong thuc theo dau & o cap NGOAI CUNG -> [('t', chuoi), ('x', bieu thuc)].
    Chuoi nam trong ham (vd "0.0%" cua TEXT) khong phai chu hien ra nen bo qua."""
    segs, depth, cur, i, n = [], 0, "", 0, len(body)
    while i < n:
        ch = body[i]
        if ch == '"':
            j, buf = i + 1, ""
            while j < n:
                if body[j] == '"':
                    if j + 1 < n and body[j + 1] == '"':
                        buf += '"'
                        j += 2
                        continue
                    break
                buf += body[j]
                j += 1
            if depth == 0:
                if cur.strip("& "):
                    segs.append(("x", cur))
                cur = ""
                segs.append(("t", buf))
            i = j + 1
            continue
        depth += 1 if ch == "(" else (-1 if ch == ")" else 0)
        cur += ch
        i += 1
    if cur.strip("& "):
        segs.append(("x", cur))
    return segs


def same_num(a, b):
    """'$3.63' va '3,63' la cung 1 con so (chi khac kieu dinh dang)."""
    key = lambda s: re.sub(r"[^\d]", "", s or "")
    return key(a) == key(b) != ""


NUM_HEAD = re.compile(r"\$?-?\d+(?:[.,]\d+)*%?")
NUM_ONLY = re.compile(r"\$?-?\d+(?:[.,]\d+)*%?")


def num_span(m, sheet, expr, chunk):
    """1 con so trong cau 'Tra loi ngan' -> bam duoc: to o nguon + hop phep tinh."""
    if not NUM_ONLY.fullmatch(chunk):
        return esc(chunk)                    # "Meta Ads", "SCALE (+20% budget)"... khong phai so
    f = "=" + expr.strip().strip("&").strip()
    uses = internal_uses(m, sheet, f)
    if not uses:
        return esc(chunk)
    bits = ['class="num"', 'data-hd="Trả lời ngắn"', 'data-res="%s"' % esc(chunk),
            'data-uses="%s"' % esc(",".join("%s:%s" % (s, a) for s, a in uses)),
            'tabindex="0"']
    if len(uses) == 1:
        bits.append('data-lab="ô %s"' % esc(uses[0][1]))
    ex = describe(m, sheet, f)
    if ex and not same_num(ex, chunk):     # '$3.63' va '3,63' la 1 so -> khong in 2 lan
        bits.append('data-calc="%s"' % esc(ex))
    return f'<span {" ".join(bits)}>{esc(chunk)}</span>'


def links_html(m, sheet, addr, text):
    """So trong phan nhan dinh: hop chi hien KET QUA (= so) + nut nhay tab goc, khong in phep tinh."""
    h = esc(text)
    for ctx, num, sh, ad, lab in ANS_LINK.get((sheet.upper(), addr), []):
        got = cell_value(m, sh, ad)
        if m.by_up.get(sh) is None or got is None:
            continue
        span = ('<span class="num" data-hd="Kết luận" data-lab="%s" data-uses="%s:%s" '
                'data-res="%s" tabindex="0">%s</span>' % (esc(lab), sh, ad, esc(got), esc(num)))
        h = h.replace(esc(ctx), esc(ctx).replace(esc(num), span, 1), 1)
    return h


def ans_html(m, sheet, formula, text):
    """Cau 'Tra loi ngan': moi con so thanh 1 nut -> bam la biet so ay lay tu dau."""
    if not (isinstance(formula, str) and formula.startswith("=")):
        return esc(text)
    segs = top_parts(formula[1:])
    if not any(k == "t" for k, _ in segs):
        return esc(text)
    out, cur = [], 0
    for i, (kind, val) in enumerate(segs):
        if kind == "t":
            if not text.startswith(val, cur):
                return esc(text)             # khong khop chu -> in thuong, khong doan bua
            out.append(esc(val))
            cur += len(val)
            continue
        mm = NUM_HEAD.match(text, cur) if "TEXT(" in val.upper() else None
        if mm:
            end = mm.end()                   # TEXT() luon ra 1 so -> doc dung token so
        else:
            nxt = next((v for k, v in segs[i + 1:] if k == "t" and v), "")
            end = text.find(nxt, cur) if nxt else len(text)
            if end < 0:
                return esc(text)
        out.append(num_span(m, sheet, val, text[cur:end]))
        cur = end
    if cur < len(text):
        out.append(esc(text[cur:]))
    return "".join(out)


def label_of(ws, row, text=""):
    got = []
    for c in range(1, 5):
        v = ws.cell(row=row, column=c).value
        if isinstance(v, str) and not v.startswith("=") and len(v.strip()) > 1:
            if v.strip() not in got:
                got.append(v.strip())
        if len(got) == 2:
            break
    return (" · ".join(got) if got else text.strip())[:34]


def render_sheet(m, name, usage):
    ws = m.wb[name]
    maxc = ws.max_column
    spans, covered = merge_map(ws)
    short = SHORT[name]
    out = [f'<article class="sheet" id="s-{name}">']
    block = []

    def flush():
        """1 bang cho 1 khoi lien tuc: cot chi chiu anh huong cua chinh khoi do."""
        if not block:
            return
        # bo cot khong co du lieu: chi tinh cot ma mot o CO CHU bat dau o do.
        # (o merge trai 5:8 khong duoc keo 8 cot vao bang -> cot trong lam header bi xuong dong)
        used = set()
        for _k, cells in block:
            for c in cells:
                if c["text"]:
                    used.add(c["c0"])
        pos = {col: i + 1 for i, col in enumerate(sorted(used))}
        rows = []
        for kind, cells in block:
            kept = []
            for c in cells:
                cols = [pos[k] for k in range(c["c0"], c["end"] + 1) if k in pos]
                if not cols:
                    continue
                kept.append(dict(c, c0=cols[0], cs=cols[-1] - cols[0] + 1,
                                 end=cols[-1]))
            if kept:
                rows.append((kind, kept))
        block.clear()
        if not rows:
            return
        ncol = max(c["end"] for _k, cells in rows for c in cells)
        # ten cot (de popover ghi "CPI ($) · Meta Ads")
        hd = {}
        for kind, cells in rows:
            if kind == "head":
                for c in cells:
                    for k in range(c["c0"], c["end"] + 1):
                        hd.setdefault(k, c["text"])
        # cot nao co lay so tu TAB khac -> note vao icon info cua tieu de cot
        xtab = {}
        for kind, cells in rows:
            if kind != "body":
                continue
            for c in cells:
                raw = c["cell"].value if c["cell"] is not None else None
                for sh, _a in internal_uses(m, name, raw):
                    if sh != name.upper() and sh not in xtab.setdefault(c["c0"], []):
                        xtab[c["c0"]].append(sh)
        # cot nao TOAN so / chuoi ngan thi ca cot (ke ca header) canh giua
        flags, longest, hlen, word = {}, {}, {}, {}
        for kind, cells in rows:
            for c in cells:
                if kind == "body" and c["text"] and c["cs"] == 1:
                    flags.setdefault(c["c0"], []).append(c["isnum"] or len(c["text"]) <= 12)
                if c["text"] and c["cs"] == 1:
                    longest[c["c0"]] = max(longest.get(c["c0"], 0), len(c["text"]))
                    w = max(len(t) for t in c["text"].split())
                    word[c["c0"]] = max(word.get(c["c0"], 0), w)
                    if kind == "head":
                        hlen[c["c0"]] = max(hlen.get(c["c0"], 0), len(c["text"]))
        # chi canh giua khi ca cot ngan VA cot do co header (cot ghi chu khong header thi de trai)
        # 80% o ngan la du: 1 o dai bat thuong (vd "SCALE (+20% budget)") khong lam ca cot lech trai
        centred = {c for c, v in flags.items() if c in hlen and sum(v) >= 0.8 * len(v)}
        # chia be ngang THEO DO DAI CHU cua tung cot (khong de trinh duyet tu doan):
        # cot nao nhieu chu thi rong, cot so thi hep -> khong cot nao bi bop xuong dong vo ly
        # uoc luong px can thiet: tu khong duoc be (word), header nen 1 dong, chu dai thi uu tien rong
        # bang it cot: chia be ngang theo uoc luong px (auto layout day het cho trong vao cot dau
        # -> cot nhan "hu vo ra"); bang 8+ cot thi de trinh duyet tu co, fixed se lam so bi cat
        need = {c: max(word.get(c, 1) * 6.8 + 18, hlen.get(c, 0) * 6.6 + 18,
                       min(longest.get(c, 1) * 7.4 + 18, 240), 20)
                for c in range(1, ncol + 1)}
        tot = sum(need.values())
        # tong be > cho trong -> de trinh duyet tu co (fixed se be tu giua tu)
        fixed = ncol <= 7 and tot <= 800
        narrow = ncol <= 3
        if narrow:
            cg = ""
        elif fixed:
            # cot nao CAN nhieu hon muc chia deu thi lay du muc do, con lai chia DEU
            # (cong deu phan du theo ty le se lam cot chi chua 1 chuoi dai phi to, vd 2.6 cot Google)
            left, rest, weight = 828.0, list(range(1, ncol + 1)), {}
            while rest:
                share = left / len(rest)
                tight = [c for c in rest if need[c] > share]
                if not tight:
                    for c in rest:
                        weight[c] = share
                    break
                for c in tight:
                    weight[c] = need[c]
                    left -= need[c]
                    rest.remove(c)
            tot = sum(weight.values())
            cg = "".join('<col style="width:%.2f%%">' % (100.0 * weight[i] / tot)
                         for i in range(1, ncol + 1))
        else:
            cg = "<col>" * ncol
        wide = " wide" if ncol >= 8 else ""
        if narrow:
            out.append('<table class="grid narrow">')
        else:
            out.append(f'<table class="grid{wide}{" fixed" if fixed else ""}">'
                       f'<colgroup>{cg}</colgroup>')
        for kind, cells in rows:
            tag = "th" if kind == "head" else "td"
            cls_row = {"head": "r-head", "body": "r-body"}.get(kind, "r-" + kind)
            end = max(c["end"] for c in cells)
            if end < ncol:
                cells[-1]["cs"] += ncol - end
            tds = []
            for x in cells:
                text, isnum, cell, cs, rs = (x["text"], x["isnum"], x["cell"],
                                             x["cs"], x["rs"])
                if not text:
                    tds.append(f'<{tag}{" class=\"n\"" if x["c0"] in centred else ""}'
                               f' colspan="{cs}" rowspan="{rs}"></{tag}>')
                    continue
                fill, color = cell_fill(cell), cell_color(cell)
                cls = ["tot"] if fill == "D9D9D9" else []
                if fill == "FFF2CC":
                    cls.append("key")
                if color == "0000CC":
                    cls.append("inp")
                if color == "007A33":
                    cls.append("rf")
                # canh giua theo COT (khong theo tung o) de ca cot thang mot kieu
                mid = cs == 1 and x["c0"] > 1 and x["c0"] in centred
                if (kind == "body" and mid) or (kind == "head" and (cs > 1 or mid)):
                    cls.append("n")
                inner = esc(text)
                if kind == "head":
                    used = []
                    for k in range(x["c0"], x["end"] + 1):
                        for sh in xtab.get(k, []):
                            if sh not in used:
                                used.append(sh)
                    extra = ("Có dùng số của tab " + " · ".join(SHORT.get(s, s) for s in used)
                             + ".") if used else ""
                    inner = term_html(text, extra)
                attr = ""
                if isnum:
                    addr = f"{openpyxl.utils.get_column_letter(x['c0'])}{x['r']}"
                    data, selfref = m.sources(name, x["c0"], x["r"])
                    lab = label_of(ws, x["r"], text)
                    raw = x["cell"].value if x["cell"] is not None else None
                    ex = describe(m, name, raw)
                    bits = ['id="c-%s-%s"' % (name, addr)]   # moi o so deu co id: o dung chung tab to vang duoc
                    is_fml = isinstance(raw, str) and raw.startswith("=")
                    uses = internal_uses(m, name, raw)
                    if ex:      # chi o TINH TOAN moi co hop "so gi ra so nay"; so nhap tay / so goc thi thoi
                        cls.append("calc")
                        bits += ['data-calc="%s"' % esc(ex), 'data-res="%s"' % esc(text),
                                 'data-hd="%s"' % esc(hd.get(x["c0"], ""))]
                    if uses:
                        # o TINH TOAN ma khong in duoc phep tinh (SUMIFS/COUNTIF...) van phai to
                        # duoc cac o no lay so, vd 2.3 muc B lay tu bang Geo phia tren
                        cls.append("uses")
                        bits.append('data-uses="%s"'
                                    % esc(",".join("%s:%s" % (s, a) for s, a in uses)))
                    if data:
                        cls.append("src")
                        bits += ['data-src="%s"' % ",".join("%s:%d" % (s, rr) for s, rr in data[:40])]
                        direct = {(s, rr) for s, _c, rr in refs_of(raw, name)
                                  if s in DATA_SHEETS} if isinstance(raw, str) else set()
                        if not direct:      # so phai tinh qua tab khac -> to het cot phai la sai
                            bits.append('data-nop="1"')
                        for s, rr in data:
                            usage.setdefault((s, rr), {})[f"c-{name}-{addr}"] = (
                                short, name, addr, lab, (s, rr) in direct, text)
                    elif selfref and not is_fml:   # o nhap tay that su (khong phai cong thuc)
                        cls.append("self")
                        bits += ['data-self="%s"' % esc(lab),
                                 'title="Ô nhập tay trong chính bảng này"']
                    if ex or data or selfref or uses:
                        bits += ['data-lab="%s"' % esc(lab), 'tabindex="0"']
                        if not ex:      # công thức không in được: vẫn có tên chỉ số cho hộp
                            bits.append('data-hd="%s"' % esc(hd.get(x["c0"], "")))
                    attr = (" " + " ".join(bits)) if bits else ""
                elif isinstance(x["cell"].value if x["cell"] is not None else None, str) \
                        and x["cell"].value.startswith("="):
                    # o CHU co cong thuc (vd "ĐẠT"): khong co hop phep tinh nhung van la
                    # dich de mui ten ↗ -> thieu cai nay thi dong nguon khong co ↗
                    addr = f"{openpyxl.utils.get_column_letter(x['c0'])}{x['r']}"
                    data, _sf = m.sources(name, x["c0"], x["r"])
                    raw = x["cell"].value
                    uses = internal_uses(m, name, raw)
                    attr = ' id="c-%s-%s"' % (name, addr)
                    if uses:      # "chưa/ĐẠT" phai to vang dung 2 o no so sanh (vd B7 + B15)
                        cls.append("uses")
                        attr += ' data-uses="%s"' % esc(",".join("%s:%s" % (s, a) for s, a in uses))
                    if data:
                        lab = label_of(ws, x["r"], text)
                        cls.append("src")
                        direct = {(s, rr) for s, _c, rr in refs_of(raw, name)
                                  if s in DATA_SHEETS}
                        attr += (' data-lab="%s" tabindex="0" data-src="%s"'
                                 % (esc(lab),
                                    ",".join("%s:%d" % (s, rr) for s, rr in data[:40])))
                        if not direct:
                            attr += ' data-nop="1"'
                        for s, rr in data:
                            usage.setdefault((s, rr), {})[f"c-{name}-{addr}"] = (
                                short, name, addr, lab, (s, rr) in direct, text)
                else:
                    # o chu thuong (nhãn Geo/định dạng...): van can id de o khac to vang duoc
                    attr = (' id="c-%s-%s"'
                            % (name, f"{openpyxl.utils.get_column_letter(x['c0'])}{x['r']}")) \
                        if kind == "body" else ""
                tds.append(f'<{tag}{attr} colspan="{cs}" rowspan="{rs}" class="{" ".join(cls)}">{inner}</{tag}>')
            out.append(f'<tr class="{cls_row}">' + "".join(tds) + "</tr>")
        out.append("</table>")

    for r in range(1, ws.max_row + 1):
        kind = row_kind(ws, r)
        items = row_items(m, ws, spans, covered, r, maxc)
        filled = [x for x in items if x[3]]
        if not filled:
            continue

        # dong ke chuyen / tieu de: 1 o trai het chieu ngang
        if len(filled) == 1 and (kind != "body" or filled[0][1] >= maxc):
            flush()
            text = filled[0][3]
            cls = {"title": "r-title", "sec": "r-sec", "ans": "r-ans", "fml": "r-fml",
                   "ref": "r-ref"}.get(kind, "r-note")
            cid = ""
            if kind == "body" and filled[0][2] is not None:
                cid = ' id="c-%s-%s"' % (name, f"{openpyxl.utils.get_column_letter(filled[0][0])}{r}")
            inner = (ans_html(m, name, filled[0][5].value, text)
                     if kind == "ans" and filled[0][5] is not None else esc(text))
            kaddr = f"{openpyxl.utils.get_column_letter(filled[0][0])}{r}"
            if (name.upper(), kaddr) in ANS_LINK:
                inner = links_html(m, name, kaddr, text)
            out.append(f'<table class="grid"><tr class="{cls}"><td{cid}>{inner}</td></tr></table>')
            continue

        bystart = {x[0]: x for x in items}
        cells, c = [], 1
        while c <= maxc:
            x = bystart.get(c)
            if not x:
                if (c, r) not in covered:
                    cells.append({"c0": c, "cs": 1, "rs": 1, "text": "", "isnum": False,
                                  "cell": None, "r": r, "end": c})
                c += 1
                continue
            c0, cs, rs, text, isnum, cell = x
            cs = max(1, cs)
            cells.append({"c0": c0, "cs": cs, "rs": rs, "text": text, "isnum": isnum,
                          "cell": cell, "r": r, "end": c0 + cs - 1})
            c += cs
        block.append((kind, cells))

    flush()
    out.append("</article>")
    return "\n".join(out)


# ------------------------------------------------------------------ cot phai
SHEET_NAMES = {"C_DU_LIEU_THAT": "C_Du_Lieu_That", "D_GIA_DINH": "D_Gia_Dinh"}
LV = {"REAL": ("🟩", "số thật, lấy từ Google Play"),
      "ASSUMED": ("🟨", "giả định có benchmark ngành làm căn cứ"),
      "FAKE": ("🟥", "số bịa để bài chạy được — đừng dùng ra quyết định thật")}
SKIP_COLS = ("Loại", "Ghi chú", "Vì sao", "Ngày lấy")
SKIP_INFO = ("Tên app", "Package ID", "Khoảng giá IAP")  # ⓘ khong can thiet
# nguoi hoc chi xin them ↗ cho D7/D30 o bang retention, khong phai moi dong
NO_ARROW = {("D_GIA_DINH", 20), ("D_GIA_DINH", 22), ("D_GIA_DINH", 24)}  # D3 · D14 · D60


def chip(txt):
    for k, (e, why) in LV.items():
        if k in txt.upper():
            return f'<span class="lb" title="{esc(why)}">{e}</span>'
    return ""


def info(tip):
    """Chi hien ⓘ khi that su co gi de noi (bo ghi chu ngan khong co so lieu)."""
    if not tip or (len(tip) < 20 and not any(c.isdigit() for c in tip)):
        return ""
    return f'<span class="info" tabindex="0" data-tip="{esc(tip)}">i</span>' 


def use_btn(usage, upper, r, nm="", vm=""):
    hits = usage.get((upper, r))
    if not hits:
        return ""
    items = list(hits.items())
    key = (nm or "").strip().lower()
    # chon dich: (1) o dung truc tiep so nay, (2) hien dung gia tri dang xem,
    # (3) ten dong khop, (4) thu tu xuat hien
    # -> truoc day lay items[0] nen Banner/Interstitial/Rewarded deu nhay ve cung 1 o
    def score(it):
        _cid, v = it
        direct = v[4] if len(v) > 4 else False
        same = bool(vm) and len(v) > 5 and (v[5] or "").strip() == vm.strip()
        lab = (v[3] or "").lower()
        return (0 if direct else 1, 0 if same else 1,
                0 if key and lab.startswith(key) else 1)
    best = sorted(items, key=score)[0]
    first = best[1]
    tags = list(dict.fromkeys(f"{v[0]} {v[3]}" for _k, v in items))
    why = " · ".join(tags[:4]) + (f" +{len(tags) - 4}" if len(tags) > 4 else "")
    return (f'<button class="use" data-go="{best[0]}" data-sheet="{first[1]}"'
            f' title="dùng ở: {esc(why)}">↗</button>')


def section_rows(m, ws, spans, covered, maxc):
    """-> [(row, kind, filled)] cua 1 sheet."""
    out = []
    for r in range(1, ws.max_row + 1):
        items = row_items(m, ws, spans, covered, r, maxc)
        filled = [x for x in items if x[3]]
        if filled:
            out.append((r, row_kind(ws, r), filled))
    return out


def build_panel(m, usage):
    out = ['<h3 class="pblk">Số thật từ Google Play <span>lấy 2026-11-03</span></h3>']

    # ---------- khoi so that
    up = "C_DU_LIEU_THAT"
    ws = m.wb[SHEET_NAMES[up]]
    maxc = ws.max_column
    spans, covered = merge_map(ws)
    facts, real, fake, steps = [], [], [], []
    cur, ads = "", ""
    for r, kind, filled in section_rows(m, ws, spans, covered, maxc):
        if kind == "title":
            continue
        if kind == "sec":
            cur = filled[0][3]
            continue
        if kind in ("fml", "head"):
            continue
        if len(filled) == 1:
            (steps if cur.startswith("C.") else []).append(filled[0][3])
            continue
        vals = [(x[0], x[3]) for x in filled]
        nm = next((v for c, v in vals if c == 1), "")
        if cur.startswith("A."):
            val = next((v for c, v in vals if c == 2), "")
            note = " · ".join(v for c, v in vals if c == 4)  # bo cot "Ngay lay"
            if nm == "Contains ads":       # giu lai, in chung o duoi
                ads = val
                continue
            if nm == "In-app purchases":   # 1 o, 2 dong
                facts.append(f'<div class="fact two" id="p-{up}-{r}">'
                             f'<div class="frow"><span>Contains ads</span><b>{esc(ads)}</b></div>'
                             f'<div class="frow"><span>In-app purchases</span><b>{esc(val)}</b></div></div>')
                continue
            href = val if "://" in val else "https://" + val
            body = (f'<a class="storelink" href="{esc(href)}" target="_blank" '
                    f'rel="noopener">{esc(val)}</a>' if nm == "URL" else esc(val))
            show = "" if nm in SKIP_INFO else info(note)
            facts.append(f'<div class="fact" id="p-{up}-{r}">'
                         f'<div class="fk">{esc(nm)}{show}</div>'
                         f'<div class="fv">{body}</div></div>')
        elif cur.startswith("B."):
            verdict = next((v for c, v in vals if c == 2), "")
            (real if "THẬT" in verdict.upper() else fake).append(nm)

    out.append('<div class="facts">' + "".join(facts) + "</div>")
    if steps:
        out.append('<details class="phow"><summary>Cách tự kiểm lại số thật (4 bước)</summary><ol>'
                   + "".join(f"<li>{esc(x)}</li>" for x in steps) + "</ol></details>")

    # ---------- khoi gia dinh
    out.append('<h3 class="pblk">Số giả định của model</h3>')
    up = "D_GIA_DINH"
    ws = m.wb[SHEET_NAMES[up]]
    maxc = ws.max_column
    spans, covered = merge_map(ws)
    secs, sec, header = [], None, {}
    for r, kind, filled in section_rows(m, ws, spans, covered, maxc):
        if kind == "title":
            continue
        if kind == "sec":
            sec = {"title": filled[0][3], "formula": "", "rows": [], "wrows": [],
                   "table": False, "note": "", "header": {}}
            secs.append(sec)
            header = {}
            continue
        if not sec:
            continue
        if kind == "fml":
            sec["formula"] = filled[0][3]
            continue
        if kind == "head":
            header = {x[0]: x[3] for x in filled}
            sec["header"] = header
            sec["table"] = sum(1 for c, v in header.items()
                               if c != 1 and v not in SKIP_COLS) >= 2
            continue
        if len(filled) == 1 and (filled[0][0] != 1 or filled[0][1] >= maxc):
            sec["note"] = (sec["note"] + " " + filled[0][3]).strip()
            continue
        if sec["table"]:
            sec["wrows"].append(r)
            continue
        vals = [(x[0], x[3]) for x in filled]
        nm = next((v for c, v in vals if c == 1), "")
        if header.get(1, "").startswith("Ngày"):
            nm = f"D{nm}"
        val = next((v for c, v in vals if header.get(c) == "Giá trị"), "")
        rest = [(c, v) for c, v in vals if c != 1 and header.get(c) != "Giá trị"]
        if not val and rest:
            val = rest[0][1]
            rest = rest[1:]
        notes = [v for c, v in rest if header.get(c) in ("Ghi chú", "Vì sao")]
        notes += [f"{header[c]}: {v}" for c, v in rest if header.get(c) not in SKIP_COLS]
        loai = next((v for c, v in rest if chip(v)), "")
        sec["rows"].append({"r": r, "nm": nm, "val": val,
                            "loai": chip(loai), "note": " · ".join(notes)})

    for s in secs:
        out.append(f'<div class="ps"><h4>{esc(s["title"])}{info(s["formula"])}</h4>')
        if s["table"]:
            out.append(render_wide(m, ws, up, s, usage))
        for row in s["rows"]:
            out.append(f'<div class="pr" id="p-{up}-{row["r"]}">'
                       f'<span class="k">{esc(row["nm"])}{info(row["note"])}</span>'
                       f'<span class="v">{esc(row["val"])}</span>'
                       f'{(use_btn(usage, up, row["r"], row["nm"], row["val"]) if (up, row["r"]) not in NO_ARROW else "")}'
                       f'<span class="lbcell">{row["loai"]}</span></div>')
        if s["note"]:
            out.append(f'<div class="pnote">{esc(s["note"])}</div>')
        out.append("</div>")
    return "\n".join(out)


def render_wide(m, ws, up, sec, usage):
    cols = [c for c in sorted(sec["header"]) if c > 1 and sec["header"][c] not in SKIP_COLS]
    loai_c = next((c for c, v in sec["header"].items() if v == "Loại"), None)
    fallback = chip(sec["note"])
    head = "".join(f'<th>{esc(sec["header"][c])}</th>' for c in cols)
    out = [f'<table class="mini"><tr><th>{esc(sec["header"].get(1, ""))}</th>{head}'
           f'<th class="lbh"></th></tr>']
    for r in sec["wrows"]:
        name_v, tds, loai = "", [], ""
        for i, c in enumerate(sorted(sec["header"])):
            text, isnum = display(m, ws, c, r)
            if c == loai_c:
                loai = chip(text)
                continue
            if i == 0:
                name_v = text
                continue
            if c not in cols:
                continue
            tds.append(f'<td class="n">{esc(text)}</td>' if isnum else f"<td>{esc(text)}</td>")
        out.append(f'<tr id="p-{up}-{r}"><th scope="row">{esc(name_v)}</th>'
                   + "".join(tds) + f'<td class="lbcell">{loai or fallback}</td></tr>')
    out.append("</table>")
    return "".join(out)


# ------------------------------------------------------------------ vo trang
def picker(current, up):
    opts = "".join(
        f'<option value="{up}{k}"{" selected" if k == current else ""}>{esc(v)}</option>'
        for k, v in PAGES)
    return ('<div class="picker"><select aria-label="Chọn bài" '
            f'onchange="location.href=this.value">{opts}</select></div>')


# Trang tong: header chung + iframe nap trang bai. Sua noi dung = sua trang bai, khong dung vao day.
SHELL = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<link rel="stylesheet" href="%(css)s">
</head>
<body>
<header class="top">
  <div class="brand">HOME WORKOUT<span>%(sub)s</span></div>
  %(picker)s
</header>
<main class="frame">%(main)s</main>
</body>
</html>
"""

# Trang bai (nam trong iframe): khong co header tong, chi thanh tab + noi dung
PAGE = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Unit Economics · Cấp 2</title>
<link rel="stylesheet" href="../assets/app.css">
</head>
<body>
<div class="pagebar">
  <nav class="tabs" id="tabs">%(tabs)s</nav>
  <button class="dt" id="dtoggle">Dữ liệu ⇄</button>
</div>
<main class="split">
  <section id="work">%(sheets)s</section>
  <aside id="data">
    <div class="dhead">
      <div class="dtit">📱 APP &amp; GIẢ ĐỊNH</div>
      <div class="dlegend">
        <span class="lg" title="số thật lấy từ Google Play">🟩 Số thật</span>
        <span class="lg" title="giả định có benchmark ngành làm căn cứ">🟨 Giả định</span>
        <span class="lg" title="số bịa để bài chạy được — đừng dùng ra quyết định thật">🟥 Bịa</span>
      </div>
      <div class="dnote" id="dnote"></div>
    </div>
    <div class="dbody">%(panel)s</div>
  </aside>
</main>
<div id="tip"></div>
<div id="calc"></div>
<div id="toast"></div>
<script src="../assets/app.js"></script>
</body>
</html>
"""


def put(rel, text):
    path = f"{ROOT}/{rel}"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def build():
    m = Model()
    usage = {}
    sheets_html = "\n".join(render_sheet(m, n, usage) for n, _ in WORK_SHEETS)
    panel = build_panel(m, usage)
    tabs = "".join(f'<button class="tab" data-t="{n}">{esc(s)}</button>' for n, s in WORK_SHEETS)
    doc = PAGE % {"tabs": tabs, "sheets": sheets_html, "panel": panel}
    put("unit-economics/index.html", doc)
    frame = '<iframe src="unit-economics/index.html" title="Unit Economics · Cấp 2"></iframe>'
    put("index.html", SHELL % {
        "title": "Home Workout — Unit Economics · Cấp 2", "sub": "Unit Economics · Cấp 2",
        "css": "assets/app.css", "picker": picker("index.html", ""), "main": frame})
    put("channel-plan/index.html", SHELL % {
        "title": "Home Workout — Channel Plan · Cấp 3", "sub": "Channel Plan · Cấp 3",
        "css": "../assets/app.css", "picker": picker("channel-plan/index.html", "../"), "main": ""})
    return doc, m, usage


def check(doc, m, usage):
    ok = True
    css = open(f"{ROOT}/assets/app.css", encoding="utf-8").read()
    js = open(f"{ROOT}/assets/app.js", encoding="utf-8").read()
    need = OUTPUTS
    miss_files = [f for f in need if not os.path.exists(f"{ROOT}/{f}")]
    if miss_files:
        print("  THIEU FILE:", ", ".join(miss_files))
        ok = False
    stale = [f for f in ("Unit_Economics_Home_Workout.html",)
             if os.path.exists(f"{ROOT}/{f}")]
    if stale:
        print("  FILE CU CON SOT (xoa di):", ", ".join(stale))
        ok = False
    n_src = len(re.findall(r'class="[^"]*\bsrc\b', doc))
    n_self = len(re.findall(r'class="[^"]*\bself\b', doc))
    n_calc = len(re.findall(r'class="[^"]*\bcalc\b', doc))
    no_calc = sum(1 for tag in re.findall(r"<td[^>]*>", doc)
                  if re.search(r'class="[^"]*\bcalc\b', tag) and "data-calc=" not in tag)
    ids = set(re.findall(r'id="(p-[A-Z_0-9]+-\d+)"', doc))
    missing = sum(1 for k in usage if f"p-{k[0]}-{k[1]}" not in ids)
    # moi o trong data-uses phai co id de to vang duoc
    have = set()
    for i in re.findall(r'id="c-([^"]+)"', doc):
        head, _, ad = i.rpartition("-")
        have.add((head.upper(), ad))
    miss_use = 0
    for tag in re.findall(r'<(?:td|span)[^>]*data-uses="[^"]*"[^>]*>', doc):
        for k in re.search(r'data-uses="([^"]*)"', tag).group(1).split(","):
            sh, _, ad = k.rpartition(":")
            if (sh.upper(), ad) not in have:
                miss_use += 1
    bad = sum(doc.count(x) for x in ("#REF!", "#VALUE!", "#DIV/0!", "None<", "nan"))
    print(f"  tab={doc.count('class=\"tab\"')} sheet={doc.count('class=\"sheet\"')} "
          f"o-bam-duoc={n_src} o-nhap-tay={n_self}")
    print(f"  tooltip={doc.count('class=\"info\"')} nut-nguoc={doc.count('class=\"use\"')} "
          f"dong-nguon={len(ids)} thieu-anchor={missing} loi-o={bad}")
    print(f"  o-bam-so={n_calc} (chi o co cong thuc) thieu-data-calc={no_calc} "
          f"o-nhay-phai={n_src} thieu-id-dung={miss_use} "
          f"so-trong-cau={doc.count('class=\"num\"')}")
    if doc.count('class="tab"') != NUM_SHEETS or doc.count('class="sheet"') != NUM_SHEETS or missing or bad:
        ok = False
    if no_calc or not n_calc or miss_use:
        print("  LOI popover: o so thieu data-calc hoac o dung thieu id")
        ok = False
    if ".sheet{display:none}" not in re.sub(r"\s+", "", css) or \
       ".sheet.on{display:block}" not in re.sub(r"\s+", "", css):
        print("  THIEU CSS an sheet (.sheet{display:none})")
        ok = False
    print(f"  file={len(need) - len(miss_files)}/{len(need)} css={len(css)}B js={len(js)}B")
    shell = open(f"{ROOT}/index.html", encoding="utf-8").read() if not miss_files else ""
    ch = open(f"{ROOT}/channel-plan/index.html", encoding="utf-8").read() if not miss_files else ""
    checks = [("trang bai tro assets", 'href="../assets/app.css"' in doc and 'src="../assets/app.js"' in doc),
              ("trang tong tro assets", 'href="assets/app.css"' in shell),
              ("trang tong nap bai", '<iframe src="unit-economics/index.html"' in shell),
              ("dropdown chi bai dang mo",
               'value="index.html" selected' in shell and
               'value="../channel-plan/index.html" selected' in ch)]
    for name, good in checks:
        if not good:
            print(f"  LOI: {name}")
            ok = False
    print("  KET QUA:", "DAT" if ok else "LOI")
    return ok


def write_manifest():
    """Mot cho duy nhat ghi so do file — docs chi tro toi day."""
    rows = []
    for rel in OUTPUTS:
        data = open(f"{ROOT}/{rel}", "rb").read()
        rows.append(f"{hashlib.md5(data).hexdigest()}  {len(data):>8}  {rel}")
    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write("\n".join(rows) + "\n")
    return rows


if __name__ == "__main__":
    doc, m, usage = build()
    for rel in OUTPUTS:
        print(f"  ghi {rel} ({os.path.getsize(f'{ROOT}/{rel}')} B)")
    if "--check" in sys.argv:
        if not check(doc, m, usage):
            sys.exit(1)
        for row in write_manifest():      # chi ghi so do khi kiem da dat
            print("  " + row)
