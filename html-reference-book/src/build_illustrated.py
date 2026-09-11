"""Build the short illustrated edition: every HTML element -> what it does -> example -> picture of the result.

Output: ../HTML-Elements-Illustrated.pdf and ../HTML-Elements-Illustrated.html
"""
import base64
import html as htmlmod
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import elements_a_d, elements_e_h, elements_i_o, elements_p_s, elements_t_z  # noqa: E402
from data_attrs import INPUT_TYPES  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SHOTS = os.path.join(ROOT, "shots")
ELEMENTS = sorted(elements_a_d.ELEMENTS + elements_e_h.ELEMENTS + elements_i_o.ELEMENTS + elements_p_s.ELEMENTS + elements_t_z.ELEMENTS, key=lambda e: e["name"])
TITLE = "HTML Elements Illustrated"
SUBTITLE = "Every element: what it does, an example, and a picture of what the browser shows"


def shot_path(key):
    p = os.path.join(SHOTS, key + ".png")
    return p if os.path.exists(p) else None


def one_line(e):
    """First sentence of the description = what it does."""
    d = e["desc"][0]
    cut = d.find(". ")
    return d if cut < 0 else d[:cut + 1]


# ---------------------------------------------------------------- PDF
def build_pdf(path):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether, PageBreak, PageTemplate, Paragraph,
                                    Preformatted, Spacer, Table, TableStyle)
    from reportlab.platypus.flowables import Flowable
    from reportlab.platypus.tableofcontents import TableOfContents

    fdir = "/usr/share/fonts/truetype/dejavu/"
    pdfmetrics.registerFont(TTFont("Sans", fdir + "DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("SansB", fdir + "DejaVuSans-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Mono", fdir + "DejaVuSansMono.ttf"))
    PAGE = A4
    LM = RM = 18 * mm
    AVAIL = PAGE[0] - LM - RM
    BRAND = colors.HexColor("#b90000")
    INK = colors.HexColor("#1b2431")
    MUTED = colors.HexColor("#5b6472")
    LINE = colors.HexColor("#d9d2c3")
    CODEBG = colors.HexColor("#f4f1ea")
    S = {
        "title": ParagraphStyle("title", fontName="SansB", fontSize=30, leading=36, textColor=BRAND, alignment=1, spaceAfter=10),
        "sub": ParagraphStyle("sub", fontName="Sans", fontSize=13, leading=18, textColor=MUTED, alignment=1),
        "h1": ParagraphStyle("h1", fontName="SansB", fontSize=22, leading=27, textColor=BRAND, spaceAfter=4),
        "h2": ParagraphStyle("h2", fontName="SansB", fontSize=12, leading=15, textColor=INK, spaceBefore=8, spaceAfter=3),
        "body": ParagraphStyle("body", fontName="Sans", fontSize=10.5, leading=15, textColor=INK, spaceAfter=4),
        "meta": ParagraphStyle("meta", fontName="Sans", fontSize=9, leading=12, textColor=MUTED, spaceAfter=6),
        "code": ParagraphStyle("code", fontName="Mono", fontSize=8.6, leading=11, backColor=CODEBG, borderPadding=(5, 6, 5, 6), leftIndent=4, spaceBefore=3, spaceAfter=8),
        "toc0": ParagraphStyle("toc0", fontName="Sans", fontSize=9.5, leading=13),
    }
    esc = lambda t: htmlmod.escape(t, quote=False)
    P = lambda t, st="body": Paragraph(esc(t), S[st])

    class Bookmark(Flowable):
        def __init__(self, key, title):
            Flowable.__init__(self)
            self.key, self.title = key, title
            self.width = self.height = 0

        def draw(self):
            self.canv.bookmarkPage(self.key)
            self.canv.addOutlineEntry(self.title, self.key, level=0)

    class Doc(BaseDocTemplate):
        def afterFlowable(self, fl):
            if isinstance(fl, Bookmark):
                self.notify("TOCEntry", (0, esc(fl.title), self.page, fl.key))

    def picture(fp, maxh=120 * mm):
        iw, ih = ImageReader(fp).getSize()
        w = AVAIL
        h = ih * w / iw
        if h > maxh:
            h, w = maxh, iw * maxh / ih
        img = Image(fp, width=w, height=h)
        t = Table([[img]], colWidths=[w + 4])
        t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.6, LINE), ("LEFTPADDING", (0, 0), (-1, -1), 2), ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                               ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
        t.hAlign = "LEFT"
        return t

    story = [Spacer(1, 150), P(TITLE, "title"), P(SUBTITLE, "sub"), Spacer(1, 20),
             P("%d HTML elements and %d input types, each with: what it does, example code, and a real picture of what the browser shows." % (len(ELEMENTS), len(INPUT_TYPES)), "sub"),
             Spacer(1, 200), P("Companion to The Complete HTML Reference Book. Edition of September 2026.", "sub"), PageBreak()]
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"]]
    story += [P("Contents", "h1"), toc, PageBreak()]

    for e in ELEMENTS:
        story.append(Bookmark("el-" + e["name"], "<%s> - %s" % (e["name"], e["title"])))
        story.append(P("<%s>" % e["name"], "h1"))
        story.append(P("%s   |   %s   |   %s" % (e["title"], e["status"].upper(), e["versions"]), "meta"))
        story.append(P("What it does", "h2"))
        for d in e["desc"][:2]:
            story.append(P(d))
        story.append(P("How to write it", "h2"))
        story.append(Preformatted(e["syntax"], S["code"], maxLineLength=95))
        if e["attrs"]:
            story.append(P("Its attributes: " + ", ".join(a[0] for a in e["attrs"]) + ". Plus the global attributes (id, class, style, title, lang, dir, hidden, data-*, ...).", "meta"))
        else:
            story.append(P("Attributes: only the global attributes (id, class, style, title, lang, dir, hidden, data-*, ...).", "meta"))
        for i, (t, c, note) in enumerate(e["examples"]):
            items = [P("Example %d: %s" % (i + 1, t), "h2"), Preformatted(c, S["code"], maxLineLength=95)]
            fp = shot_path("ex-%s-%d" % (e["name"], i))
            if fp:
                items.append(P("What the browser shows:", "meta"))
                items.append(picture(fp))
            if note:
                items.append(Spacer(1, 4))
                items.append(P(note))
            story.append(KeepTogether(items))
        story.append(PageBreak())

    story.append(Bookmark("inputs", "<input> types"))
    story.append(P("<input> - every type", "h1"))
    story.append(P("The input element changes completely depending on its type attribute. Each type below: what it does, the code, and what the browser shows."))
    for (typ, ttl, since, desc, sattrs, ex, notes) in INPUT_TYPES:
        items = [P('<input type="%s">' % typ, "h2"), P("%s   |   since %s" % (ttl, since), "meta"), P(desc), Preformatted(ex, S["code"], maxLineLength=95)]
        fp = shot_path("input-" + typ)
        if fp:
            items.append(P("What the browser shows:", "meta"))
            items.append(picture(fp))
        if notes:
            items.append(P(notes))
        story.append(KeepTogether(items))
        story.append(Spacer(1, 10))

    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("Sans", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(LM, 10 * mm, TITLE)
        canvas.drawRightString(PAGE[0] - RM, 10 * mm, "Page %d" % doc.page)
        canvas.setStrokeColor(LINE)
        canvas.line(LM, 13.5 * mm, PAGE[0] - RM, 13.5 * mm)
        canvas.restoreState()

    doc = Doc(path, pagesize=PAGE, leftMargin=LM, rightMargin=RM, topMargin=16 * mm, bottomMargin=18 * mm, title=TITLE, subject=SUBTITLE)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="body", frames=[frame], onPage=on_page)])
    doc.multiBuild(story)


# ---------------------------------------------------------------- HTML
def build_html(path):
    E = htmlmod.escape

    def img(key, alt):
        fp = shot_path(key)
        if not fp:
            return ""
        return '<figure><figcaption>What the browser shows</figcaption><img src="data:image/png;base64,%s" alt="%s" loading="lazy"></figure>' % (
            base64.b64encode(open(fp, "rb").read()).decode(), E(alt))

    secs = []
    nav = []
    for e in ELEMENTS:
        nav.append('<a href="#el-%s">&lt;%s&gt;</a>' % (e["name"], e["name"]))
        b = ['<section class="el" id="el-%s" data-name="%s %s">' % (e["name"], E(e["name"]), E(e["title"].lower()))]
        b.append("<h2>&lt;%s&gt; <small>%s</small></h2>" % (e["name"], E(e["title"])))
        b.append('<p class="meta">%s &middot; %s</p>' % (E(e["status"].upper()), E(e["versions"])))
        b.append("<h3>What it does</h3>" + "".join("<p>%s</p>" % E(d) for d in e["desc"][:2]))
        b.append("<h3>How to write it</h3><pre><code>%s</code></pre>" % E(e["syntax"]))
        b.append('<p class="meta">Attributes: %s</p>' % (E(", ".join(a[0] for a in e["attrs"])) + " + global attributes" if e["attrs"] else "global attributes only"))
        for i, (t, c, note) in enumerate(e["examples"]):
            b.append("<h3>Example %d: %s</h3><pre><code>%s</code></pre>%s%s" % (i + 1, E(t), E(c), img("ex-%s-%d" % (e["name"], i), "Browser result for " + e["name"]), ("<p>%s</p>" % E(note)) if note else ""))
        b.append("</section>")
        secs.append("".join(b))
    inputs = ['<section class="el" id="inputs" data-name="input types">', "<h2>&lt;input&gt; <small>every type</small></h2>"]
    for (typ, ttl, since, desc, sattrs, ex, notes) in INPUT_TYPES:
        inputs.append('<h3 id="input-%s">&lt;input type="%s"&gt; - %s</h3><p class="meta">since %s</p><p>%s</p><pre><code>%s</code></pre>%s%s' % (
            typ, typ, E(ttl), E(since), E(desc), E(ex), img("input-" + typ, "Browser result for input type " + typ), ("<p>%s</p>" % E(notes)) if notes else ""))
    inputs.append("</section>")
    secs.append("".join(inputs))
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>
:root { --brand:#b90000; --ink:#1b2431; --muted:#5b6472; --line:#d9d2c3; --bg:#faf8f3; --code:#f4f1ea; }
body { margin:0; font-family: system-ui, "Segoe UI", Arial, sans-serif; color:var(--ink); background:var(--bg); line-height:1.5; }
header { position: sticky; top:0; background:#fff; border-bottom:2px solid var(--brand); padding:.7rem 1rem; display:flex; gap:1rem; align-items:center; flex-wrap:wrap; z-index:2; }
header h1 { font-size:1.1rem; margin:0; color:var(--brand); }
header input { flex:1; min-width:14rem; padding:.5rem .8rem; border:1px solid #bbb; border-radius:999px; font:inherit; }
nav { padding:.6rem 1rem; display:flex; flex-wrap:wrap; gap:.3rem .6rem; font-size:.85rem; background:#fff; border-bottom:1px solid var(--line); }
nav a { color:var(--brand); text-decoration:none; font-family: monospace; }
main { max-width: 60rem; margin: 0 auto; padding: 1rem; }
.el { background:#fff; border:1px solid var(--line); border-radius:12px; padding:1rem 1.4rem; margin:1rem 0; }
.el[hidden] { display:none; }
h2 { color:var(--brand); margin:.2rem 0; font-family: monospace; font-size:1.6rem; }
h2 small { font-family: system-ui, sans-serif; font-size: 1rem; color: var(--muted); font-weight: 400; }
h3 { margin:1rem 0 .3rem; font-size:1rem; }
.meta { color:var(--muted); font-size:.85rem; }
pre { background:var(--code); padding:.7rem .9rem; border-radius:8px; overflow:auto; font-size:.85rem; }
figure { margin:.5rem 0 .8rem; }
figure img { max-width:100%%; border:1px solid var(--line); border-radius:6px; background:#fff; }
figcaption { font-size:.8rem; color:var(--muted); margin-bottom:.2rem; }
</style>
</head>
<body>
<header><h1>%(title)s</h1><input id="q" type="search" placeholder="Search an element, e.g. table, img, form" autofocus></header>
<nav>%(nav)s</nav>
<main>%(secs)s</main>
<script>
const q = document.getElementById('q'), els = [...document.querySelectorAll('.el')];
q.addEventListener('input', () => { const v = q.value.trim().toLowerCase(); els.forEach(s => { s.hidden = v && !s.dataset.name.includes(v); }); });
</script>
</body>
</html>""" % dict(title=E(TITLE), nav="".join(nav), secs="".join(secs))
    open(path, "w", encoding="utf-8").write(page)


if __name__ == "__main__":
    build_html(os.path.join(ROOT, "HTML-Elements-Illustrated.html"))
    print("HTML written")
    build_pdf(os.path.join(ROOT, "HTML-Elements-Illustrated.pdf"))
    print("PDF written")
