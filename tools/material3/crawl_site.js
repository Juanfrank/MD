const { chromium } = require('playwright');
const fs = require('fs');
const urls = fs.readFileSync('urls.txt','utf8').split('\n').filter(Boolean);
const CONC = 6;
const extract = () => {
  const root = document.querySelector('main') || document.body;
  const out = [];
  const skip = new Set(['SCRIPT','STYLE','NOSCRIPT','NAV','BUTTON','SVG']);
  const txt = n => n.innerText.replace(/\s+/g,' ').trim();
  const walk = n => {
    if (n.nodeType !== 1 || skip.has(n.tagName.toUpperCase())) return;
    const t = n.tagName;
    if (/^H[1-6]$/.test(t)) { const s = txt(n).replace(/\s*link\s*Copy link$/,''); if (s) out.push('#'.repeat(+t[1])+' '+s); return; }
    if (t === 'P') { const s = txt(n); if (s) out.push(s); return; }
    if (t === 'LI') { const s = txt(n); if (s) out.push('- '+s); return; }
    if (t === 'TABLE') {
      const rows = [...n.rows].map(r => [...r.cells].map(c => txt(c).replace(/\|/g,'/')));
      if (rows.length) { out.push('| '+rows[0].join(' | ')+' |'); out.push('|'+rows[0].map(()=>'---').join('|')+'|'); rows.slice(1).forEach(r=>out.push('| '+r.join(' | ')+' |')); }
      return;
    }
    if (t === 'IMG') { const a = n.getAttribute('alt'); if (a) out.push('[image: '+a+']'); return; }
    for (const c of n.children) walk(c);
  };
  walk(root);
  return { title: document.title, md: out.join('\n\n') };
};
(async () => {
  const b = await chromium.launch();
  let i = 0, done = 0, fail = [];
  const worker = async () => {
    const p = await b.newPage();
    while (i < urls.length) {
      const u = urls[i++];
      const slug = u.replace('https://m3.material.io','').replace(/^\/|\/$/g,'').replace(/\//g,'__') || 'home';
      const f = `out/${slug}.json`;
      if (fs.existsSync(f)) { done++; continue; }
      try {
        await p.goto(u, {waitUntil:'networkidle', timeout:60000});
        await p.waitForTimeout(1500);
        const r = await p.evaluate(extract);
        fs.writeFileSync(f, JSON.stringify({url:u, ...r}));
      } catch(e) { fail.push(u); }
      if (++done % 25 === 0) console.log(done, '/', urls.length);
    }
    await p.close();
  };
  await Promise.all(Array.from({length:CONC}, worker));
  console.log('done', done, 'fail', fail.length, fail.join('\n'));
  await b.close();
})();
