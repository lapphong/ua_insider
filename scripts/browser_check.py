# -*- coding: utf-8 -*-
"""Kiem 6 muc trong docs/02 §7 — thu `--check` khong bat duoc — bang 1 lan Chrome headless.

Chay: python3 scripts/browser_check.py     (hoac `make ok`)
In 1 dong / muc, sai muc nao thi exit 1.
"""
import html as H
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time

ROOT = (os.path.abspath(sys.argv[1]) if len(sys.argv) > 1
        else os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PROBE = """<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">
<iframe id="f" src="site/unit-economics/index.html" style="width:1200px;height:800px;border:0"></iframe>
<pre id="out">pending</pre>
<script>
const f = document.getElementById('f');
function run() {
  const d = f.contentDocument, res = [];
  const push = (name, bad, detail) => res.push([name, bad, detail]);
  const tabs = [...d.querySelectorAll('.tab')];
  const work = d.getElementById('work'), data = d.getElementById('data');

  /* 1. cac sheet chong nhau */
  const sheets = [...d.querySelectorAll('.sheet')];
  const shown = sheets.filter(s => getComputedStyle(s).display !== 'none');
  push('sheet chong nhau', shown.length === 1 ? 0 : shown.length,
       shown.length + '/' + sheets.length + ' hien');

  /* 2 + 3 + 4. duyet tung tab: tran ngang, o tran chu, header lech canh le */
  const tabOver = [], cellOver = [], mis = [];
  tabs.forEach(t => {
    t.click();
    const sh = d.querySelector('.sheet.on');
    if (work.scrollWidth > work.clientWidth + 1) tabOver.push(t.dataset.t);
    sh.querySelectorAll('td,th').forEach(e => {
      if (e.scrollWidth > e.clientWidth + 1)
        cellOver.push(t.dataset.t + ':' + (e.textContent || '').trim().slice(0, 12));
    });
    sh.querySelectorAll('table').forEach(tb => {
      if (!tb.rows.length) return;
      const ths = [...tb.rows[0].children];
      [...tb.rows].slice(1).forEach(row => {
        const cs = [...row.children];
        if (cs.length !== ths.length) return;
        cs.forEach((c, i) => {
          if (getComputedStyle(c).textAlign !== getComputedStyle(ths[i]).textAlign)
            mis.push(t.dataset.t + ':' + i);
        });
      });
    });
  });
  push('tab tran ngang', tabOver.length, tabOver.slice(0, 5).join(' '));
  push('o tran chu', cellOver.length, cellOver.slice(0, 5).join(' '));
  push('header lech canh le', mis.length, mis.slice(0, 5).join(' '));

  /* 5. panel phai tran */
  const pOver = [...data.querySelectorAll('.pr,.fact')]
    .filter(e => e.scrollWidth > e.clientWidth + 1).length;
  const dataOver = data.scrollWidth > data.clientWidth + 1 ? 1 : 0;
  push('panel phai tran', dataOver + pOver, dataOver ? 'ca panel' : pOver + ' dong');

  /* 6. nut ↗: dich ton tai, dung tab, o dich co data-src dung dong panel */
  const arrows = [];
  data.querySelectorAll('.use').forEach(b => {
    const go = d.getElementById(b.dataset.go);
    if (!go) { arrows.push('thieu-dich ' + b.dataset.go); return; }
    const m = go.id.match(/^c-(.+)-[A-Z]+\\d+$/);
    if ((b.dataset.sheet || '').toUpperCase() !== (m ? m[1] : '').toUpperCase())
      arrows.push('sai-tab ' + b.dataset.go);
    const pr = b.closest('[id^="p-"]');
    const row = pr ? pr.id.split('-').pop() : '';
    if (!row || (go.dataset.src || '').split(',').indexOf('D_GIA_DINH:' + row) < 0)
      arrows.push('thieu-nguon ' + b.dataset.go);
  });
  push('nut ↗ sai', arrows.length, arrows.slice(0, 5).join(' '));

  /* 7. popover: khong lo ten ham, bam hien / bam ra ngoai tat */
  const badCalc = [...d.querySelectorAll('[data-calc]')].filter(e =>
    /SUM|IF\\(|ROUND|TEXT\\(|MIN\\(|MAX\\(|ABS|COUNTIF|SUMPRODUCT|_LTV|_Gia_Dinh|!/.test(e.dataset.calc)).length;
  let ok = 0, why = [];
  let cell = null;
  for (const t of tabs) {                            /* tab dau co the khong co o cong thuc */
    t.click();
    cell = d.querySelector('.sheet.on td.calc[data-uses]');
    if (cell) break;
  }
  if (!cell) {
    ok = 1; why.push('khong tim thay o co cong thuc');
  } else {
    cell.click();
    const box = d.getElementById('calc');
    const on = box.classList.contains('on'), hl = d.querySelectorAll('.use-on, .src.on').length;
    d.body.click();
    const off = !box.classList.contains('on');
    ok = (on && hl > 0 && off) ? 0 : 1;
    why.push('hien=' + on + ' to=' + hl + ' tat=' + off);
  }
  /* ô công thức không in được phép tính (SUMIFS) vẫn phải có hộp, và phải in phép cộng:
     2.3!B21 = 7.920.000 + 1.980.000 + 990.000 = 10.890.000 */
  [...tabs].find(x => x.dataset.t === '2.3_eCPM').click();
  const nc = d.getElementById('c-2.3_eCPM-B21');
  if (!nc) { ok++; why.push('thieu B21'); }
  else {
    nc.click();
    const box = d.getElementById('calc'), tx = box.textContent;
    if (!box.classList.contains('on')) { ok++; why.push('B21 khong hop'); }
    else if (tx.indexOf('7.920.000 + 1.980.000 + 990.000') < 0 || tx.indexOf('10.890.000') < 0) {
      ok++; why.push('B21 thieu phep cong');
    }
    d.body.click();
  }
  push('popover', badCalc + ok, 'lo-ham=' + badCalc + ' ' + why.join(' '));

  /* 8. ô dùng số ở cột phải: bấm phải tô đúng dòng đang hiện con số đó
     (2.2 F10 = B81 → "Tổng chi phí ngoài media"; 2.3 B42 = 8,0/2,0/1,0 → Banner/Interstitial/Rewarded) */
  let pOk = 0, pWhy = [];
  [['2.2_CPI_CAC', 'c-2.2_CPI_CAC-F10', ['D_GIA_DINH-81']],
   ['2.3_eCPM', 'c-2.3_eCPM-B42',
    ['D_GIA_DINH-32', 'D_GIA_DINH-33', 'D_GIA_DINH-34']],
   ['2.5_LTV', 'c-2.5_LTV-B40', ['D_GIA_DINH-69']],
   ['2.2_CPI_CAC', 'c-2.2_CPI_CAC-H9', []]].forEach(([sh, id, want]) => {   /* H9: tiền $1,20 KHÔNG được tô index 1,20 */
    const t = [...tabs].find(x => x.dataset.t === sh);
    if (t) t.click();
    const c = d.getElementById(id);
    if (!c) { pOk++; pWhy.push('thieu-o ' + id); return; }
    c.click();
    const got = [...d.querySelectorAll('#data .hl')].map(e => e.id);   /* gồm cả dòng bảng mini (tr) */
    const miss = want.filter(w => got.indexOf('p-' + w) < 0);
    if (miss.length) { pOk++; pWhy.push(id + ' thieu ' + miss.join(',')); }
    if (!want.length && got.length) { pOk++; pWhy.push(id + ' to nham ' + got.length + ' dong'); }
    d.body.click();
  });
  push('to dung dong cot phai', pOk, pWhy.slice(0, 2).join(' '));

  /* 9. ô đang bấm phải vàng — kể cả ô số gõ tay (trước đây bấm vào không ăn gì) */
  let cOk = 0, cWhy = [];
  [['2.3_eCPM', 'c-2.3_eCPM-C7'],              /* Impressions: số gõ tay */
   ['2.3_eCPM', 'c-2.3_eCPM-B42'],             /* ô tính toán */
   ['2.5_LTV', 'c-2.5_LTV-D28']].forEach(([sh, id]) => {
    const t = [...tabs].find(x => x.dataset.t === sh);
    if (t) t.click();
    const c = d.getElementById(id);
    if (!c) { cOk++; cWhy.push('thieu-o ' + id); return; }
    c.click();
    if (!c.classList.contains('on')) { cOk++; cWhy.push(id + ' khong vang'); }
    d.body.click();
  });
  push('o bam to vang', cOk, cWhy.slice(0, 2).join(' '));
  tabs[0].click();                                   /* tra ve tab dau */
  document.getElementById('out').textContent = JSON.stringify(res);
}
f.onload = run;
if (f.contentDocument && f.contentDocument.readyState === 'complete') run();
</script></body></html>
"""


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def main():
    if not os.path.exists(CHROME):
        print("  BO QUA: khong thay Chrome")
        return 0
    tmp = tempfile.mkdtemp(prefix="ua_check_")
    os.symlink(ROOT, os.path.join(tmp, "site"))
    with open(os.path.join(tmp, "__probe.html"), "w", encoding="utf-8") as f:
        f.write(PROBE)
    port = free_port()
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port),
                            "--bind", "127.0.0.1"], cwd=tmp,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(100):
            try:
                socket.create_connection(("127.0.0.1", port), 0.2).close()
                break
            except OSError:
                time.sleep(0.05)
        out = subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-first-run",
             "--user-data-dir=" + os.path.join(tmp, "prof"),
             "--virtual-time-budget=8000", "--dump-dom",
             f"http://127.0.0.1:{port}/__probe.html"],
            capture_output=True, text=True, timeout=120).stdout
        m = re.search(r'<pre id="out">(.*?)</pre>', out, re.S)
        body = H.unescape(m.group(1)) if m else ""
        if not body.startswith("["):
            print("  LOI: Chrome khong tra ket qua:", body[:120] or "(rong)")
            return 1
        rows = json.loads(body)
        bad = 0
        for name, n, detail in rows:
            print(f"  {'OK ' if not n else 'LOI'}  {name:<22} {n:>4}  {detail}")
            bad += 1 if n else 0
        print(f"  KIEM: {len(rows) - bad}/{len(rows)} muc OK")
        return 1 if bad else 0
    finally:
        srv.terminate()
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
