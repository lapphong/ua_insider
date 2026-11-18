# UA Marketing — practice workbook

🇬🇧 **English** · [🇻🇳 Tiếng Việt](README.vi.md)

This repo is a **User Acquisition (UA) learning workbook**, not a product and not a market-data report.
Each submission is **one Excel file**, plus a **reading page (`.html`)** generated from that very file.

- **Author of the work:** Long Phan
- **Course:** [UA Insider Academy](https://academy.uainsider.io.vn/) — *hands-on UA marketing for mobile app teams*
- **Included now:** lesson 2 — Unit Economics (UA basics). Full list: the [Lessons](#lessons) table.

## For learning only

- The numbers are **worked examples**, not citations. Do not invest or make business decisions from them.
- The app used as the case study is real (**Home Workout – No Equipment**, Leap Fitness Group), but most financial figures are **the learner's assumptions**, not the app's internal data.
- Every figure is labelled in the `Nguồn/Loại` (source/type) column of the Excel file:

| Label | Meaning |
|---|---|
| 🟩 REAL | Real figure from a public source (Google Play, App Store price list…), with the date it was taken |
| 🟨 ASSUMED | Reasonable assumption by the learner (industry benchmark, experience) |
| 🟥 FAKE | Deliberately made up to build a scenario or comparison |

So read it to understand the **money loop and the reasoning**, not to quote the numbers.

## Viewing the pages

Nothing to install, no internet needed:

1. Open `index.html` (double-click) → landing page with a lesson dropdown.
2. Inside a lesson: switch tabs with the top tab bar, click **any number cell** to see the calculation and the source cells (highlighted yellow), and use **⤓ Tải .xlsx** on the right of the tab bar to download the submitted workbook.

## Layout

| File / folder | What it is |
|---|---|
| `*.xlsx` | The submission, one file per lesson — **single source of truth**, never edited once locked |
| `index.html` | Landing page: header + lesson dropdown + `<iframe>` loading the lesson page |
| `unit-economics/`, `channel-plan/` | Per-lesson reading pages — **generated**, never hand-edited |
| `assets/app.css`, `assets/app.js` | Shared CSS/JS for every lesson |
| `build_html.py` | Generates the `.html` from the `.xlsx` and self-checks the numbers |
| `scripts/` | Headless-Chrome layout checks, commit helpers |
| `docs/` | Authoring rules, per-lesson records, decision log, `manifest.txt` (md5 + bytes) |

**Repo rule:** the `.xlsx` is the only source; the `.html` comes from the script, so **never edit it by hand** — change the `.xlsx` and rebuild.

## Build & verify

```bash
cd ua
make ok     # build .html + verify numbers + write docs/manifest.txt + run 9 layout checks
```

Requires Python 3 with `openpyxl` and `formulas` (the makefile uses a temp venv; if a module is missing, create a venv and `pip install openpyxl formulas`).

Passing output: `KET QUA: DAT`, `thieu-id-dung=0`, `file=5/5`, `KIEM: 9/9 muc OK`.

Rules: `docs/00-quy-uoc-chung.md` · spreadsheet: `docs/01-bang-tinh.md` · reading page: `docs/02-ban-doc-html.md` · lesson record: `docs/03-du-an-01-unit-economics.md`.

## Credits

The assignment, the curriculum and the grading belong to **UA Insider Academy** ([academy.uainsider.io.vn](https://academy.uainsider.io.vn/)).
This repo contains **the learner's own work only**, not course material — please do not reuse course content from here.

---

<a id="lessons"></a>

## Lessons

A new lesson = **one new row**, and the row must be identical in this file and `README.vi.md` (`make ok` fails if the two tables differ).

| # | Bài · Lesson | Cấp · Level | File nộp · Workbook | Bản đọc · Reading page | Trạng thái · Status |
|---|---|---|---|---|---|
| 2 | Unit Economics | UA cơ bản · Basics | `Unit_Economics_Home_Workout_bt2.xlsx` | [`unit-economics/`](unit-economics/index.html) | ✅ xong · done |
| 3 | Channel Plan | Cấp 3 · Level 3 | `Channel_Plan_Home_Workout.xlsx` | [`channel-plan/`](channel-plan/index.html) | 🟨 có Excel, trang đọc trống · workbook only |
