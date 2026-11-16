const tabs = [...document.querySelectorAll('.tab')], sheets = [...document.querySelectorAll('.sheet')];
const work = document.getElementById('work'), data = document.getElementById('data');
const dnote = document.getElementById('dnote'), HINT = dnote.innerHTML;
function show(id) {
  sheets.forEach(s => s.classList.toggle('on', s.id === 's-' + id));
  tabs.forEach(t => t.classList.toggle('on', t.dataset.t === id));
  work.scrollTop = 0;
  try { history.replaceState(null, '', '#s-' + id) } catch (e) { }
}
tabs.forEach(t => t.onclick = () => show(t.dataset.t));
let start = (location.hash || '').replace(/^#s/, '');
if (!sheets.some(s => s.id === 's-' + start)) start = sheets[0].id.slice(2);
show(start);

const tip = document.getElementById('tip');
function place(x, y) {
  const r = tip.getBoundingClientRect(); let L = x + 14, T = y + 14;
  if (L + r.width > innerWidth - 8) L = Math.max(8, x - r.width - 14);
  if (T + r.height > innerHeight - 8) T = Math.max(8, y - r.height - 14);
  tip.style.left = L + 'px'; tip.style.top = T + 'px';
}
function tipOn(el, x, y) { tip.innerHTML = el.dataset.tip; tip.classList.add('on'); place(x, y); }
document.addEventListener('mouseover', e => { const i = e.target.closest('.info'); if (i) tipOn(i, e.clientX, e.clientY); });
document.addEventListener('mousemove', e => { if (tip.classList.contains('on')) place(e.clientX, e.clientY); });
document.addEventListener('mouseout', e => { if (e.target.closest('.info')) tip.classList.remove('on'); });
document.addEventListener('focusin', e => {
  const i = e.target.closest('.info');
  if (i) { const r = i.getBoundingClientRect(); tipOn(i, r.left, r.bottom); }
});
document.addEventListener('focusout', e => { if (e.target.closest('.info')) tip.classList.remove('on'); });

const toast = document.getElementById('toast'); let tt;
function say(m) {
  toast.textContent = m; toast.classList.add('on'); clearTimeout(tt);
  tt = setTimeout(() => toast.classList.remove('on'), 2600);
}
/* to vang giu nguyen cho tới khi bam ra ngoai */
function unmark() {
  document.querySelectorAll('td.on,.src.on').forEach(x => x.classList.remove('on'));
  document.querySelectorAll('.use-on,.hl').forEach(x => x.classList.remove('use-on', 'hl'));
}

/* bam vao so -> hop nho: phep tinh bang so that + o nao duoc dung. Bam ra ngoai -> tat. */
const calc = document.getElementById('calc'); let cur = null, shownAt = 0;
function calcHide() { calc.classList.remove('on'); cur = null; }
function calcPlace() {
  if (!cur) return;
  const r = cur.getBoundingClientRect(), b = work.getBoundingClientRect();
  /* o bi cuon khuat -> tat (bo qua 0,7s dau: luc do con dang cuon chuong trinh) */
  if ((r.bottom < b.top + 4 || r.top > b.bottom - 4) && Date.now() - shownAt > 700) { calc.classList.remove('on'); return; }
  const cr = calc.getBoundingClientRect();
  let L = r.left, T = r.bottom + 6;
  if (L + cr.width > b.right - 8) L = b.right - 8 - cr.width;
  if (T + cr.height > b.bottom - 8) T = r.top - 6 - cr.height;      /* khong du cho duoi -> len tren */
  calc.style.left = Math.max(b.left + 6, L) + 'px';
  calc.style.top = Math.max(b.top + 6, T) + 'px';             /* ghim trong khung bai lam */
}
function markUses(td) {
  const here = document.querySelector('.sheet.on').id.slice(2), chips = [];
  let same = false;
  (td.dataset.uses || '').split(',').filter(Boolean).forEach(k => {
    const i = k.lastIndexOf(':'), sh = k.slice(0, i), ad = k.slice(i + 1);
    const el = document.getElementById('c-' + here + '-' + ad);
    if (sh === here.toUpperCase()) {
      if (el) { el.classList.add('use-on'); same = true; }
    } else {
      const tab = [...document.querySelectorAll('.tab')].find(t => t.dataset.t.toUpperCase() === sh);
      chips.push([tab ? tab.dataset.t : sh, ad]);
    }
  });
  return { chips, same };
}
function calcShow(td) {
  calc.textContent = '';
  const h = document.createElement('div'); h.className = 'ch';
  const b = document.createElement('b'); b.textContent = td.dataset.hd || td.dataset.lab || 'Số';
  h.append(b);
  /* không có tên chỉ số thì lấy nhãn làm tiêu đề, khỏi in lặp "Số · nhãn" */
  if (td.dataset.lab && td.dataset.hd) h.append(document.createTextNode(' · ' + td.dataset.lab));
  calc.append(h);
  const e = document.createElement('div'); e.className = 'cx'; e.textContent = td.dataset.calc;
  /* o chi chep lai 1 con so (khong co phep tinh) thi chi hien ket qua 1 lan */
  const norm = t => (t || '').replace(/\s/g, '');
  if (td.dataset.calc && norm(td.dataset.calc) !== norm(td.dataset.res)) calc.append(e);
  if (td.dataset.res) {
    const d = document.createElement('div'); d.className = 'cd'; d.textContent = '= ' + td.dataset.res; calc.append(d);
  } else if (!td.dataset.calc) {
    /* công thức không in được (SUMIFS/COUNTIF…): vẫn hiện hộp. Nếu các ô nó lấy số
       cộng lại đúng bằng kết quả thì in phép cộng, vd 2.3!C21 = 7.920.000 + 1.980.000 + 990.000 */
    const here = document.querySelector('.sheet.on').id.slice(2);
    const num = t => {
      const s = (t || '').replace(/[$\s\u00a0%]/g, '');
      if (!/^-?\d[\d.,]*$/.test(s)) return null;
      return parseFloat(s.replace(/\./g, '').replace(',', '.'));
    };
    const parts = (td.dataset.uses || '').split(',').filter(Boolean)
      .filter(k => k.slice(0, k.lastIndexOf(':')).toUpperCase() === here.toUpperCase())
      .map(k => document.getElementById('c-' + here + '-' + k.slice(k.lastIndexOf(':') + 1)))
      .filter(el => el && num(el.textContent) !== null);
    const tot = num(td.textContent);
    const sum = parts.reduce((a, el) => a + num(el.textContent), 0);
    if (parts.length > 1 && tot !== null && Math.abs(sum - tot) <= Math.max(0.011, Math.abs(tot) * 5e-5)) {
      const x = document.createElement('div'); x.className = 'cx';
      x.textContent = parts.map(el => el.textContent.trim()).join(' + ');
      calc.append(x);
    }
    const d = document.createElement('div'); d.className = 'cd';
    d.textContent = '= ' + td.textContent.trim(); calc.append(d);
  }
  const { chips, same } = markUses(td);
  if (same) {
    const s = document.createElement('div'); s.className = 'use-note'; s.textContent = 'ô vàng = số lấy vào phép tính này';
    calc.append(s);
  }
  if (chips.length) {
    const row = document.createElement('div'); row.className = 'cg';
    chips.forEach(([sh, ad]) => {
      /* data-uses ghi ten sheet bang CHU HOA (2.6_PLTV) con id tren trang la chu thuong
         (2.6_pLTV) -> phai lay dung data-t cua tab, khong ghep thang chuoi */
      const tab = [...document.querySelectorAll('.tab')].find(t => t.dataset.t.toUpperCase() === sh.toUpperCase());
      const key = tab ? tab.dataset.t : sh;
      const btn = document.createElement('button'); btn.className = 'gotab';
      btn.dataset.sheet = key; btn.dataset.cell = 'c-' + key + '-' + ad;
      btn.textContent = '↗ tab ' + (tab ? tab.textContent : sh);
      row.append(btn);
    });
    calc.append(row);
  }
  calc.classList.add('on'); cur = td; shownAt = Date.now(); calcPlace();
}
work.addEventListener('scroll', calcPlace);   /* cuon thi hop nho di theo o, khuat han thi tat */

document.addEventListener('click', e => {
  const go = e.target.closest('.gotab');
  if (go) {                                  /* nhay sang tab dang chua so do */
    unmark();
    show(go.dataset.sheet);
    const el = document.getElementById(go.dataset.cell);
    calcHide();
    if (el) { el.classList.add('use-on'); el.scrollIntoView({ block: 'center' }); }
    return;
  }
  if (e.target.closest('#calc')) return;      /* bam trong hop thi khong tat */
  const cd = e.target.closest('td.calc'), s = e.target.closest('.src'), nu = e.target.closest('.num');
  /* moi o so deu co id="c-<sheet>-<cell>" — kể cả số gõ tay (trước đây bấm vào không ăn gì) */
  const cell = cd || s || e.target.closest('.sheet td[id^="c-"]');
  const tg = e.target.closest('td[data-uses]');
  if (!cell && !nu) { unmark(); calcHide(); dnote.innerHTML = HINT; }
  else {
    unmark();
    const here = document.querySelector('.sheet.on').id.slice(2).toUpperCase();
    const same = !!(tg && (tg.dataset.uses || '').split(',')
      .some(k => k.slice(0, k.lastIndexOf(':')).toUpperCase() === here));
    /* Cột phải: tô dòng đang hiện ĐÚNG con số này — sánh từng chuỗi số
       (giữ "%" và số thập phân, bỏ "$") với số hạng trong phép tính đang hiện
       hoặc với kết quả. vd 2.3 ARPDAU "(8,0 × $0,52 + 2,0 × $7,43 + 1,0 × $10,70) ÷ 1000"
       -> tô Banner 8,0 · Interstitial 2,0 · Rewarded 1,0.
       Có data-src: chỉ xét các dòng đã truy nguồn (không khớp số nào thì tô hết,
       trừ ô data-nop / ô đã có nguồn cùng tab). Không có data-src (số gõ tay):
       xét cả cột phải. */
    const nrm = t => (t || '').replace(/[$\s\u00a0]/g, '');
    const pc = s || cd || cell;   /* ô gõ tay không có class .src nhưng vẫn phải đối chiếu cột phải */
    if (pc) pc.classList.add('on');            /* ô đang bấm: luôn vàng */
    let list = [];
    if (pc) {
      const toks = ((pc.dataset.calc || '').match(/-?\$?\d[\d.,]*%?/g) || []).concat([pc.textContent]);
      const want = new Set(toks.map(nrm));
      /* bảng mini cột phải trộn TIỀN ($26.000), SỐ LƯỢNG (13.000) và HỆ SỐ (1,20):
         riêng bảng mini phải giữ dấu $ trong khoá, không thì "CAC thật $1,20" (2.2)
         tô nhầm dòng "Quality index 1,20". Dòng .pr/.fact giữ luật cũ. */
      const mny = t => ((t || '').indexOf('$') >= 0 ? '$' : '') + nrm(t);
      const mwant = new Set(toks.map(mny));
      const hit = el => {
        /* dòng .pr/.fact có .v; dòng bảng mini thì số nằm trong td.n (quality index, giá gói…) */
        if (el.tagName === 'TR')
          return [...el.querySelectorAll('td.n')].some(td => mwant.has(mny(td.textContent))) ? [el] : [];
        return [...el.querySelectorAll('.v,.fv')].some(v => want.has(nrm(v.textContent))) ? [el] : [];
      };
      const nodes = pc.dataset.src
        ? pc.dataset.src.split(',').filter(Boolean).map(k => {
            const p = k.split(':');
            return document.getElementById('p-' + p[0] + '-' + p[1]);
          }).filter(Boolean)
        : [...document.querySelectorAll('#data .pr,#data .fact,#data table.mini tr[id]')];
      list = nodes.flatMap(hit);
      if (!list.length && pc.dataset.src && !pc.dataset.nop && !same) list = nodes;
    }
    if (list.length) {
      let first = null, n = 0;
      list.forEach(el => {
        el.classList.add('hl'); n++; if (!first) first = el;        /* giu vang, khong fad */
      });
      dnote.innerHTML = n ? ('← <b>' + (pc.dataset.lab || 'số nguồn') + '</b> · ' + n + ' ô nguồn bên dưới') : HINT;
      if (first) first.scrollIntoView({ block: 'center' });
      if (innerWidth <= 1100) document.body.classList.add('datopen');
    }
    if (tg) markUses(tg);       /* số dùng trong cùng tab: tô luôn, kể cả khi đã tô cột phải */
    if (cd || nu || tg) calcShow(cd || nu || tg); else calcHide();
  }
  const g = e.target.closest('[data-go]');
  if (g) {
    show(g.dataset.sheet);
    const el = document.getElementById(g.dataset.go);
    if (el) { el.classList.add('hl'); el.scrollIntoView({ block: 'center' }); }
    return;
  }
  const slf = e.target.closest('.self');
  if (slf) say('“' + slf.dataset.self + '” là ô nhập tay ngay trong bảng này · 🟨 ASSUMED');
});
document.getElementById('dtoggle').onclick = () => document.body.classList.toggle('datopen');
document.addEventListener('keydown', e => {
  if ((e.key === 'Enter' || e.key === ' ') && e.target.classList &&
    (e.target.classList.contains('calc') || e.target.classList.contains('num'))) {
    e.preventDefault(); unmark(); calcShow(e.target); return;
  }
  if (e.key === 'Escape') {
    document.body.classList.remove('datopen'); tip.classList.remove('on');
    calcHide(); unmark();
  }
});
