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
  document.querySelectorAll('.src.on').forEach(x => x.classList.remove('on'));
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
  const b = document.createElement('b'); b.textContent = td.dataset.hd || 'Số';
  h.append(b);
  if (td.dataset.lab) h.append(document.createTextNode(' · ' + td.dataset.lab));
  calc.append(h);
  const e = document.createElement('div'); e.className = 'cx'; e.textContent = td.dataset.calc;
  /* o chi chep lai 1 con so (khong co phep tinh) thi chi hien ket qua 1 lan */
  const norm = t => (t || '').replace(/\s/g, '');
  if (td.dataset.calc && norm(td.dataset.calc) !== norm(td.dataset.res)) calc.append(e);
  if (td.dataset.res) {
    const d = document.createElement('div'); d.className = 'cd'; d.textContent = '= ' + td.dataset.res; calc.append(d);
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
  const tg = e.target.closest('td[data-uses]');
  if (!cd && !s && !nu && !tg) { unmark(); calcHide(); dnote.innerHTML = HINT; }
  else {
    unmark();
    /* o co so cung tab -> to vang so do (doc ra ket qua ngay tren bang);
       chi to cot phai khi khong co o nao cung tab (so phai lay tu bang gia dinh) */
    const here = document.querySelector('.sheet.on').id.slice(2).toUpperCase();
    const same = !!(tg && (tg.dataset.uses || '').split(',')
      .some(k => k.slice(0, k.lastIndexOf(':')).toUpperCase() === here));
    if (s && !same && !s.dataset.nop) {
      s.classList.add('on');
      let first = null, n = 0;
      s.dataset.src.split(',').filter(Boolean).forEach(k => {
        const p = k.split(':'), el = document.getElementById('p-' + p[0] + '-' + p[1]);
        if (!el) return;
        el.classList.add('hl'); n++; if (!first) first = el;      /* giu vang, khong fad */
      });
      dnote.innerHTML = n ? ('← <b>' + s.dataset.lab + '</b> · ' + n + ' ô nguồn bên dưới') : HINT;
      if (first) first.scrollIntoView({ block: 'center' });
      if (innerWidth <= 1100) document.body.classList.add('datopen');
    } else if (!cd && !nu) {    /* co so cung tab: to vang cac o do */
      markUses(tg);
    }
    if (cd || nu) calcShow(cd || nu); else calcHide();
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
