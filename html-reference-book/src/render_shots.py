"""Render every element example (and attribute mini-example) in headless Chrome and save PNG screenshots.

Usage: python3 render_shots.py            (expects a Chrome DevTools endpoint on 127.0.0.1:9333;
       start one with start_chrome.sh)     writes into ../shots/ and shots/index.json)
"""
import base64
import hashlib
import json
import os
import re
import sys
import time
import urllib.request

import websocket

sys.path.insert(0, os.path.dirname(__file__))
import elements_a_d, elements_e_h, elements_i_o, elements_p_s, elements_t_z  # noqa: E402
from data_attrs import INPUT_TYPES  # noqa: E402

ELEMENTS = (elements_a_d.ELEMENTS + elements_e_h.ELEMENTS + elements_i_o.ELEMENTS + elements_p_s.ELEMENTS + elements_t_z.ELEMENTS)
OUT = os.path.join(os.path.dirname(__file__), "..", "shots")
CDP = "http://127.0.0.1:9333"
WIDTH = 520

# A small inline SVG used wherever an example refers to an image file that does not exist.
def placeholder(label, w=160, h=100, color="#7aa2c9"):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
           '<rect width="100%%" height="100%%" fill="%s"/><circle cx="%d" cy="%d" r="%d" fill="#ffe08a"/>'
           '<path d="M0 %d L%d %d L%d %d L%d %d L%d %d Z" fill="#4c7a4c"/>'
           '<text x="50%%" y="92%%" font-family="sans-serif" font-size="11" fill="#fff" text-anchor="middle">%s</text></svg>'
           % (w, h, w, h, color, w * 0.75, h * 0.3, h * 0.13, h * 0.8, w * 0.25, h * 0.45, w * 0.45, h * 0.65, w * 0.65, h * 0.5, w, h * 0.8, label))
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


FRAME_CSS = """
<style>
  html { background: #fff; overflow: hidden; }
  body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 15px; margin: 12px; color: #111; }
  img:not([src^='data:']) { background: #dde6f0; }
  iframe, video, embed, object { background: repeating-linear-gradient(45deg,#eef,#eef 8px,#dde 8px,#dde 16px); }
</style>
"""

SUBSTITUTE_JS = r"""
(() => {
  const ph = (l, w, h) => %s;
  document.querySelectorAll('img').forEach(img => {
    if (!img.src || img.src.startsWith('data:')) return;
    const w = parseInt(img.getAttribute('width')) || 160, h = parseInt(img.getAttribute('height')) || Math.round(w * 0.62);
    img.removeAttribute('srcset'); img.removeAttribute('sizes');
    img.src = ph((img.getAttribute('alt') || img.getAttribute('src') || 'image').slice(0, 24), Math.min(w, 480), Math.min(h, 300));
  });
  document.querySelectorAll('video').forEach(v => { v.removeAttribute('autoplay'); v.setAttribute('controls', ''); v.style.background = '#222'; v.style.minHeight = '90px'; v.style.width = v.style.width || '320px'; });
  document.querySelectorAll('audio').forEach(a => { a.setAttribute('controls', ''); a.removeAttribute('autoplay'); });
  document.querySelectorAll('iframe').forEach(f => { if (!f.hasAttribute('srcdoc')) { f.setAttribute('srcdoc', '<p style="font-family:sans-serif;color:#456;padding:10px">iframe: ' + (f.getAttribute('title') || f.getAttribute('src') || '') + '</p>'); } f.style.border = f.style.border || '1px solid #999'; });
  document.querySelectorAll('object,embed').forEach(o => { o.style.display = 'inline-block'; o.style.width = o.style.width || '200px'; o.style.height = o.style.height || '80px'; });
  document.querySelectorAll('dialog').forEach(d => { d.setAttribute('open', ''); });
  document.querySelectorAll('[popover]').forEach(p => { try { p.showPopover(); } catch (e) {} });
  document.querySelectorAll('details').forEach(d => d.setAttribute('open', ''));
  document.querySelectorAll('script').forEach(s => s.remove());
  document.querySelectorAll('template').forEach(t => { const n = document.createElement('div'); n.style.cssText = 'border:1px dashed #888;padding:6px;color:#666;font-size:12px'; n.textContent = '<template> content is not rendered'; t.after(n); });
  document.querySelectorAll('canvas').forEach(c => { c.style.border = '1px dashed #888'; const x = c.getContext && c.getContext('2d'); if (x) { x.fillStyle = '#b90000'; x.fillRect(10, 10, 60, 40); x.fillStyle = '#336'; x.font = '14px sans-serif'; x.fillText('canvas', 80, 35); } });
})();
""" % ("`data:image/svg+xml;base64,` + btoa(`<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"${w}\" height=\"${h}\"><rect width=\"100%\" height=\"100%\" fill=\"#7aa2c9\"/><circle cx=\"${w*0.75}\" cy=\"${h*0.3}\" r=\"${h*0.13}\" fill=\"#ffe08a\"/><path d=\"M0 ${h*0.8} L${w*0.25} ${h*0.45} L${w*0.45} ${h*0.65} L${w*0.65} ${h*0.5} L${w} ${h*0.8} L${w} ${h} L0 ${h} Z\" fill=\"#4c7a4c\"/><text x=\"50%\" y=\"92%\" font-family=\"sans-serif\" font-size=\"11\" fill=\"#fff\" text-anchor=\"middle\">${l.replace(/[<>&]/g,'')}</text></svg>`)")

# Examples that only make sense inside head/frameset etc. get a visible note instead of a blank picture.
HEAD_ONLY = {"base", "head", "link", "meta", "style", "title", "script", "noscript", "frameset", "frame", "html", "body", "template", "slot", "noframes", "isindex", "nextid", "bgsound", "keygen", "command", "menuitem", "element", "shadow", "portal", "fencedframe", "rb", "rtc", "xmp", "listing", "plaintext"}


class Chrome:
    def __init__(self):
        t = json.load(urllib.request.urlopen(urllib.request.Request(CDP + "/json/new?about:blank", method="PUT")))
        self.tid = t["id"]
        self.ws = websocket.create_connection(t["webSocketDebuggerUrl"], timeout=30)
        self.n = 0
        self.call("Page.enable")
        self.call("Runtime.enable")
        self.frame = self.call("Page.getFrameTree")["frameTree"]["frame"]["id"]

    def call(self, method, **params):
        self.n += 1
        self.ws.send(json.dumps({"id": self.n, "method": method, "params": params}))
        while True:
            m = json.loads(self.ws.recv())
            if m.get("id") == self.n:
                return m.get("result", m)

    def shot(self, html, out):
        self.call("Emulation.setDeviceMetricsOverride", width=WIDTH, height=420, deviceScaleFactor=2, mobile=False)
        self.call("Page.setDocumentContent", frameId=self.frame, html=FRAME_CSS + html)
        self.call("Runtime.evaluate", expression=SUBSTITUTE_JS, awaitPromise=False)
        time.sleep(0.15)
        h = self.call("Runtime.evaluate", expression="(() => { let m = 0; for (const el of document.body.querySelectorAll('*')) { const r = el.getBoundingClientRect(); if (r.height) m = Math.max(m, r.bottom); } return Math.ceil(m) + window.scrollY; })()", returnByValue=True)["result"]["value"]
        h = max(40, min(int(h) + 16, 900))
        self.call("Emulation.setDeviceMetricsOverride", width=WIDTH, height=h, deviceScaleFactor=2, mobile=False)
        time.sleep(0.05)
        r = self.call("Page.captureScreenshot", format="png")
        data = base64.b64decode(r["data"])
        open(out, "wb").write(data)
        return h

    def close(self):
        self.ws.close()
        urllib.request.urlopen(CDP + "/json/close/" + self.tid)


def wrap(name, code):
    """Make an example renderable on its own: strip head-only wrappers, add a note for invisible elements."""
    c = code
    if "<html" in c or "<!DOCTYPE" in c.upper():
        # keep only body content (plus any <style>) so the frame CSS still applies
        m = re.search(r"<body[^>]*>(.*)</body>", c, re.S | re.I)
        styles = "".join(re.findall(r"<style[^>]*>.*?</style>", c, re.S | re.I))
        c = styles + (m.group(1) if m else re.sub(r"<head>.*?</head>", "", c, flags=re.S | re.I))
    if name in HEAD_ONLY and "<style" not in c and not re.search(r"<(p|div|h[1-6]|ul|ol|table|form|button|img|a|section|article|main|span|input|label|select|textarea|nav|header|footer|figure|video|audio|pre|blockquote|dl|iframe|canvas|svg|details|dialog|fieldset)\b", c, re.I):
        c = ('<div style="border:1px dashed #b90000;padding:8px 10px;font-size:13px;color:#555;background:#fff8f6">'
             '<b style="color:#b90000">&lt;%s&gt;</b> does not draw anything on the page by itself; the code below is shown as text. '
             'Its effect is described in the explanation.</div><pre style="font-size:12px;white-space:pre-wrap;background:#f4f1ea;padding:8px">%s</pre>'
             % (name, code.replace("&", "&amp;").replace("<", "&lt;")))
    return c


def main():
    os.makedirs(OUT, exist_ok=True)
    index = {}
    idx_path = os.path.join(OUT, "index.json")
    if os.path.exists(idx_path):
        index = json.load(open(idx_path))
    ch = Chrome()
    jobs = []
    for e in ELEMENTS:
        for i, (t, c, note) in enumerate(e["examples"]):
            jobs.append(("ex-%s-%d" % (e["name"], i), wrap(e["name"], c)))
    for (typ, ttl, since, desc, sattrs, ex, notes) in INPUT_TYPES:
        jobs.append(("input-%s" % typ, wrap("input", ex)))
    done = 0
    for key, html in jobs:
        h = hashlib.md5(html.encode()).hexdigest()[:10]
        fn = "%s.png" % key
        path = os.path.join(OUT, fn)
        if index.get(key, {}).get("hash") == h and os.path.exists(path):
            continue
        try:
            height = ch.shot(html, path)
            index[key] = {"file": fn, "hash": h, "h": height}
        except Exception as exc:  # noqa: BLE001
            print("FAILED", key, exc)
            try:
                ch.close()
            except Exception:  # noqa: BLE001
                pass
            ch = Chrome()
        done += 1
        if done % 50 == 0:
            print(done, "rendered")
            json.dump(index, open(idx_path, "w"), indent=0)
    json.dump(index, open(idx_path, "w"), indent=0)
    ch.close()
    print("total", len(jobs), "rendered", done, "-> ", OUT)


if __name__ == "__main__":
    main()
