# -*- coding: utf-8 -*-
"""Build the HTML Reference Book as a PDF and as a searchable single-page HTML file.

Usage:  python3 build.py
Output: ../HTML-Reference-Book.pdf  and  ../HTML-Reference-Book.html
"""
import html as htmlmod
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from data_intro import HOW_TO_USE, HISTORY, FUNDAMENTALS
from data_attrs import GLOBAL_ATTRS, EVENT_ATTRS, INPUT_TYPES
from data_css import CSS_INTRO, CSS_SELECTORS, CSS_PROPERTIES, CSS_HTML_STYLING_GUIDE, CSS_LISTS_TABLES
from data_refs import (LINK_TYPES, META_NAMES, AUTOCOMPLETE_TOKENS, MIME_TYPES, URL_SCHEMES,
                       COLOR_NAMES, ENTITIES, GUIDES, GLOSSARY)
from data_course import COURSE
import elements_a_d, elements_e_h, elements_i_o, elements_p_s, elements_t_z

ELEMENTS = (elements_a_d.ELEMENTS + elements_e_h.ELEMENTS + elements_i_o.ELEMENTS
            + elements_p_s.ELEMENTS + elements_t_z.ELEMENTS)
ELEMENTS.sort(key=lambda e: e["name"])

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TITLE = "The Complete HTML Reference Book"
SUBTITLE = "Every element and attribute from HTML 1 (1991) to the HTML Living Standard, with CSS"

# ----------------------------------------------------------------------------
# Validation of the data
# ----------------------------------------------------------------------------
def validate():
    names = [e["name"] for e in ELEMENTS]
    dupes = {n for n in names if names.count(n) > 1}
    assert not dupes, "duplicate elements: %s" % dupes
    for e in ELEMENTS:
        for key in ("name", "title", "cat", "versions", "status", "desc", "syntax", "categories",
                    "content", "parents", "omission", "dom", "attrs", "examples", "a11y", "mistakes", "related", "css"):
            assert key in e, "%s missing %s" % (e["name"], key)
        for a in e["attrs"]:
            assert len(a) == 4, "%s attr %r" % (e["name"], a)
        for ex in e["examples"]:
            assert len(ex) == 3, "%s example %r" % (e["name"], ex)
    known = set(names) | {"h2", "h3", "h4", "h5", "h6"}
    for e in ELEMENTS:
        for r in e["related"]:
            assert r in known, "%s related unknown %s" % (e["name"], r)


# ----------------------------------------------------------------------------
# Attribute index (which elements accept which attribute)
# ----------------------------------------------------------------------------
def attribute_index():
    idx = {}
    for e in ELEMENTS:
        for (name, values, desc, ver) in e["attrs"]:
            for part in re.split(r"\s*[/,]\s*", name):
                part = part.strip()
                if not part or " " in part or part.startswith("Any") or part.startswith("on") and "," in name:
                    continue
                idx.setdefault(part, []).append((e["name"], values, desc, ver))
    return dict(sorted(idx.items()))



def sample_value(values):
    """Pick a plausible sample value from a 'values' description string."""
    v = values.strip()
    low = v.lower()
    if low.startswith("boolean") or low == "(boolean)" or "boolean attribute" in low:
        return None
    if low.startswith("url"):
        return "https://example.com/page.html"
    if "integer" in low or "number" in low or low.startswith("pixels"):
        return "3"
    if "id of" in low or low.startswith("id "):
        return "my-id"
    if low.startswith("text") or "any text" in low or low.startswith("string"):
        return "value"
    if "language" in low:
        return "en"
    if "mime" in low:
        return "text/plain"
    if "color" in low or "colour" in low:
        return "#336699"
    m = re.split(r"\s*[|,/]\s*| or ", v)
    tok = m[0].strip().strip("\"'()")
    tok = re.sub(r"\s*\(.*$", "", tok)
    if not tok or " " in tok.strip() and len(tok) > 24:
        return "value"
    return tok.strip()


VERSIONS = [
    ("HTML 1", "HTML 1.0 (1991-1993)", ["HTML 1"],
     "The first HTML, described in Tim Berners-Lee's 'HTML Tags' document (1991) and the 1993 IETF draft by Berners-Lee and "
     "Dan Connolly. It had about 20 elements: headings, paragraphs, anchors, lists, addresses, preformatted text, plus a few "
     "editor hints. There were no images (the <img> tag was added by Mosaic in 1993), no tables and no forms."),
    ("HTML 2", "HTML 2.0 (RFC 1866, 1995)", ["HTML 2", "RFC 1866"],
     "HTML 2.0 was the first official standard, published by the IETF in November 1995. It documented what browsers "
     "already supported: images, forms (input, select, textarea), the <head>/<body> split and character entities for "
     "Latin-1."),
    ("HTML 3", "HTML 3.2 (W3C, January 1997)", ["HTML 3", "3.2"],
     "HTML 3.2 (code name 'Wilbur') was the first W3C Recommendation. It absorbed the popular Netscape and Internet Explorer "
     "extensions: tables, applets, text flow around images, subscripts and superscripts, and the presentational <font>, "
     "<center> and <u> elements together with attributes such as bgcolor and align. Most of that presentational markup is "
     "obsolete today, replaced by CSS."),
    ("HTML 4", "HTML 4.0 and 4.01 (1997-1999)", ["HTML 4", "4.01", "4.0"],
     "HTML 4 separated structure from presentation, introduced style sheets, scripting, frames, richer tables (thead, tbody, "
     "tfoot, colgroup), richer forms (button, fieldset, legend, label, optgroup), internationalisation (dir, lang, bdo) "
     "and accessibility features. It came in Strict, Transitional and Frameset flavours. XHTML 1.0 (2000) was HTML 4.01 "
     "re-expressed in XML."),
    ("HTML5", "HTML5 (WHATWG 2004 onwards, W3C Recommendation 2014)", ["HTML5", "HTML 5"],
     "HTML5 added semantic sectioning (header, footer, nav, main, article, section, aside), native audio and video, canvas, "
     "new form controls and input types with built-in validation, and it defined precisely how browsers must parse even "
     "broken markup. It also removed the presentational and frame elements."),
    ("Living", "The HTML Living Standard (2014-today)", ["Living", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"],
     "Since 2019 the WHATWG Living Standard is the single HTML specification; there will be no 'HTML6'. Features are added "
     "continuously once two browser engines ship them: <dialog>, <template>, <slot>, <picture>, <search>, the popover "
     "attribute, lazy loading, customisable select and more."),
]


def elements_for_version(keys):
    out = []
    for e in ELEMENTS:
        v = e["versions"]
        if any(k.lower() in v.lower() for k in keys):
            out.append(e)
    return out

# ============================================================================
# PDF
# ============================================================================
def build_pdf(path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A5
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, NextPageTemplate, PageBreak,
                                    PageTemplate, Paragraph, Preformatted, Spacer, Table, TableStyle)
    from reportlab.platypus.tableofcontents import TableOfContents
    from reportlab.platypus.flowables import Flowable

    fdir = "/usr/share/fonts/truetype/dejavu/"
    pdfmetrics.registerFont(TTFont("Sans", fdir + "DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("Sans-Bold", fdir + "DejaVuSans-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Serif", fdir + "DejaVuSerif.ttf"))
    pdfmetrics.registerFont(TTFont("Serif-Bold", fdir + "DejaVuSerif-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Mono", fdir + "DejaVuSansMono.ttf"))
    pdfmetrics.registerFont(TTFont("Mono-Bold", fdir + "DejaVuSansMono-Bold.ttf"))
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold")
    registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif", boldItalic="Serif-Bold")
    registerFontFamily("Mono", normal="Mono", bold="Mono-Bold", italic="Mono", boldItalic="Mono-Bold")

    PAGE = A5
    LM = RM = 13 * mm
    AVAIL = PAGE[0] - LM - RM
    BRAND = colors.HexColor("#b90000")
    INK = colors.HexColor("#1b2431")
    MUTED = colors.HexColor("#5b6472")
    LINE = colors.HexColor("#d9d2c3")
    CODEBG = colors.HexColor("#f4f1ea")
    HEADBG = colors.HexColor("#f0e9dc")

    S = {}
    S["title"] = ParagraphStyle("title", fontName="Serif-Bold", fontSize=24, leading=30, textColor=BRAND, alignment=TA_CENTER, spaceAfter=10)
    S["subtitle"] = ParagraphStyle("subtitle", fontName="Serif", fontSize=14, leading=20, textColor=INK, alignment=TA_CENTER, spaceAfter=6)
    S["center"] = ParagraphStyle("center", fontName="Sans", fontSize=10, leading=14, textColor=MUTED, alignment=TA_CENTER)
    S["part"] = ParagraphStyle("part", fontName="Serif-Bold", fontSize=22, leading=28, textColor=BRAND, spaceBefore=90, spaceAfter=14)
    S["partsub"] = ParagraphStyle("partsub", fontName="Serif", fontSize=13, leading=19, textColor=INK)
    S["h1"] = ParagraphStyle("h1", fontName="Serif-Bold", fontSize=19, leading=24, textColor=BRAND, spaceBefore=6, spaceAfter=8)
    S["h2"] = ParagraphStyle("h2", fontName="Sans-Bold", fontSize=13, leading=17, textColor=INK, spaceBefore=12, spaceAfter=5)
    S["h3"] = ParagraphStyle("h3", fontName="Sans-Bold", fontSize=11, leading=14, textColor=BRAND, spaceBefore=9, spaceAfter=3)
    S["p"] = ParagraphStyle("p", fontName="Serif", fontSize=10.5, leading=16, textColor=INK, spaceAfter=5)
    S["small"] = ParagraphStyle("small", fontName="Sans", fontSize=8.8, leading=12.5, textColor=INK)
    S["smallb"] = ParagraphStyle("smallb", fontName="Sans-Bold", fontSize=8.8, leading=12.5, textColor=INK)
    S["meta"] = ParagraphStyle("meta", fontName="Sans", fontSize=8.6, leading=12, textColor=MUTED, spaceAfter=2)
    S["li"] = ParagraphStyle("li", parent=S["p"], leftIndent=12, bulletIndent=2, spaceAfter=2)
    S["code"] = ParagraphStyle("code", fontName="Mono", fontSize=7.4, leading=10, textColor=INK, backColor=CODEBG,
                               borderColor=LINE, borderWidth=0.5, borderPadding=5, leftIndent=3, rightIndent=3, spaceBefore=3, spaceAfter=8)
    S["note"] = ParagraphStyle("note", parent=S["p"], backColor=colors.HexColor("#fff8e1"), borderColor=colors.HexColor("#e6c65c"),
                               borderWidth=0.6, borderPadding=6, leftIndent=4, rightIndent=4, spaceBefore=4, spaceAfter=10)
    S["caption"] = ParagraphStyle("caption", fontName="Sans", fontSize=8.2, leading=11, textColor=MUTED, spaceAfter=8)
    S["toc0"] = ParagraphStyle("toc0", fontName="Sans-Bold", fontSize=10.5, leading=15, spaceBefore=6)
    S["toc1"] = ParagraphStyle("toc1", fontName="Sans", fontSize=9, leading=12.5, leftIndent=14)
    S["idx"] = ParagraphStyle("idx", fontName="Sans", fontSize=8.2, leading=11)

    def esc(t):
        return htmlmod.escape(str(t), quote=False)

    def P(text, style="p"):
        return Paragraph(esc(text), S[style])

    def code_block(text):
        return Preformatted(text, S["code"], maxLineLength=70)

    def rl_table(rows, col_widths=None, head=True, font=None):
        data = []
        for i, r in enumerate(rows):
            st = S["smallb"] if (head and i == 0) else S["small"]
            data.append([Paragraph(esc(c), st) for c in r])
        ncol = max(len(r) for r in rows)
        avail = AVAIL
        if col_widths is None:
            if ncol == 2:
                col_widths = [avail * 0.3, avail * 0.7]
            elif ncol == 3:
                col_widths = [avail * 0.24, avail * 0.26, avail * 0.5]
            elif ncol == 4:
                col_widths = [avail * 0.17, avail * 0.2, avail * 0.45, avail * 0.18]
            else:
                col_widths = [avail / ncol] * ncol
        t = Table(data, colWidths=col_widths, repeatRows=1 if head else 0, hAlign="LEFT")
        style = [("GRID", (0, 0), (-1, -1), 0.4, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                 ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                 ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
        if head:
            style.append(("BACKGROUND", (0, 0), (-1, 0), HEADBG))
        for i in range(1, len(rows)):
            if i % 2 == 0:
                style.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#faf8f3")))
        t.setStyle(TableStyle(style))
        return [t, Spacer(1, 8)]

    def blocks(seq):
        out = []
        for kind, val in seq:
            if kind == "h2":
                out.append(P(val, "h2"))
            elif kind == "h3":
                out.append(P(val, "h3"))
            elif kind == "p":
                out.append(P(val))
            elif kind == "code":
                out.append(code_block(val))
            elif kind == "ul":
                for it in val:
                    out.append(Paragraph(esc(it), S["li"], bulletText="\u2022"))
                out.append(Spacer(1, 4))
            elif kind == "table":
                out.extend(rl_table(val))
            elif kind == "note":
                out.append(P(val, "note"))
        return out

    class Bookmark(Flowable):
        def __init__(self, key, title, level):
            Flowable.__init__(self)
            self.key, self.title, self.level = key, title, level
            self.width = self.height = 0

        def draw(self):
            c = self.canv
            c.bookmarkPage(self.key)
            c.addOutlineEntry(self.title, self.key, level=self.level, closed=(self.level == 0))

    class Doc(BaseDocTemplate):
        def afterFlowable(self, fl):
            if isinstance(fl, Bookmark):
                self.notify("TOCEntry", (fl.level, htmlmod.escape(fl.title, quote=False), self.page, fl.key))

    def heading(text, level, key):
        return [Bookmark(key, text, level), P(text, "h1" if level == 0 else "h2")]

    story = []
    # ----- Cover
    story += [Spacer(1, 90), P(TITLE, "title"), P(SUBTITLE, "subtitle"), Spacer(1, 20),
              P("HTML 1 \u2022 HTML 2.0 \u2022 HTML 3.2 \u2022 HTML 4.01 \u2022 XHTML \u2022 HTML5 \u2022 Living Standard", "center"),
              Spacer(1, 10), P("Elements \u2022 Attributes \u2022 Global attributes \u2022 Events \u2022 Input types \u2022 CSS \u2022 Entities \u2022 Guides", "center"),
              Spacer(1, 120), P("Compiled from the HTML Living Standard, MDN Web Docs, htmlreference.io, codeshack.io and the W3Schools HTML and CSS tutorial.", "center"),
              P("Edition of September 2026", "center"), PageBreak()]
    # ----- TOC
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"]]
    story += [P("Contents", "h1"), toc, NextPageTemplate("body"), PageBreak()]

    def part(num, title, sub):
        return [Bookmark("part%d" % num, "Part %d: %s" % (num, title), 0), P("Part %d" % num, "partsub"), P(title, "part"), P(sub, "partsub"), PageBreak()]

    # ----- Front matter
    story += heading("How to use this book", 0, "howto") + blocks(HOW_TO_USE) + [PageBreak()]
    story += part(1, "The History of HTML", "From Tim Berners-Lee's 18 tags to the Living Standard.")
    story += heading("A short history of HTML", 0, "history") + blocks(HISTORY) + [PageBreak()]
    story += part(2, "HTML Fundamentals", "Syntax, structure, nesting rules, content categories and entities.")
    story += heading("HTML fundamentals", 0, "fund") + blocks(FUNDAMENTALS) + [PageBreak()]

    # ----- Version by version
    story += part(3, "HTML Version by Version", "Which elements each version of HTML introduced, from HTML 1 to the Living Standard.")
    story += heading("How to read this part", 0, "verintro")
    story.append(P("Each chapter lists the elements whose history mentions that version of HTML, with a one-paragraph summary. "
                   "An element can appear in more than one chapter (for example when HTML 4 changed it and HTML5 changed it again). "
                   "Elements marked OBSOLETE are documented for reading old pages only; use the modern replacement named in the "
                   "element's full entry in Part 6."))
    story.append(PageBreak())
    for (vk, vtitle, keys, vintro) in VERSIONS:
        els = elements_for_version(keys)
        story += heading(vtitle, 1, "ver-" + vk.replace(" ", ""))
        story.append(P(vintro))
        story.append(P("Elements in this chapter: %d" % len(els), "meta"))
        story.extend(rl_table([["Element", "Meaning", "Status today"]] + [["<%s>" % e["name"], e["title"], e["status"]] for e in els]))
        for e in els:
            story.append(KeepTogether([P("<%s> \u2014 %s" % (e["name"], e["title"]), "h3"),
                                       P("Status: %s   |   Versions: %s" % (e["status"].upper(), e["versions"]), "meta"),
                                       P(e["desc"][0]), code_block(e["syntax"])]))
        story.append(PageBreak())

    # ----- Global attributes
    story += part(4, "Global Attributes", "Attributes that can be used on any HTML element.")
    story += heading("Global attributes", 0, "globals")
    story.append(P("The attributes in this part are 'global': they may be specified on every HTML element, even those where "
                   "they have no obvious effect. They are listed alphabetically. Event handler attributes (on*) are in Part 5."))
    story.extend(rl_table([["Attribute", "Values"]] + [[a[0], a[1]] for a in GLOBAL_ATTRS]))
    story.append(PageBreak())
    for (name, values, desc, ver, ex) in GLOBAL_ATTRS:
        story += [Bookmark("ga-" + re.sub(r"\W", "", name), name, 1), P("Global attribute: " + name, "h1"),
                  P("Values: %s   |   Since: %s" % (values, ver), "meta"), P("Description", "h3"), P(desc),
                  P("Example", "h3"), code_block(ex),
                  P("Where it can be used", "h3"),
                  P("On every HTML element, including <html>, <head> and <body>, and on elements inside <template> and shadow trees. "
                    "Elements where the attribute has no practical effect (for example tabindex on <meta>) still accept it without a validation error, "
                    "but such use should be avoided."),
                  P("Checklist", "h3")]
        for it in ["Write the name in lower case: %s." % name,
                   "Put the value in double quotes unless it is a boolean attribute.",
                   "Do not repeat the same attribute twice on one start tag; browsers keep the first one only.",
                   "In JavaScript read it with element.getAttribute('%s') or, for most global attributes, a property of the same name." % name]:
            story.append(Paragraph(esc(it), S["li"], bulletText="\u2022"))
        story.append(PageBreak())

    # ----- Events
    story += part(5, "Event Handler Attributes", "Every on* attribute and the event that triggers it.")
    story += heading("Event handler attributes", 0, "events")
    story.append(P("Every HTML element accepts event handler content attributes whose value is JavaScript code run when the "
                   "event fires. The attribute name is 'on' followed by the event name. In modern code it is better to attach "
                   "handlers with element.addEventListener('click', fn) in a script, which keeps behaviour out of the markup and "
                   "allows several handlers per event, but the attributes remain valid and are useful for quick prototypes."))
    story.append(code_block("<!-- attribute style -->\n<button onclick=\"alert('Hi')\">Say hi</button>\n\n<!-- script style (preferred) -->\n<button id=\"hi\">Say hi</button>\n<script>\n  document.getElementById('hi').addEventListener('click', () => alert('Hi'));\n</script>"))
    story.extend(rl_table([["Attribute", "Event", "Applies to"]] + [[a[0], a[1], a[3]] for a in EVENT_ATTRS],
                          col_widths=[AVAIL * 0.34, AVAIL * 0.3, AVAIL * 0.36]))
    story.append(PageBreak())
    for (aname, evname, fires, applies, extra) in EVENT_ATTRS:
        story += [Bookmark("ev-" + aname, aname, 1), P("Event attribute: " + aname, "h1"),
                  P("Event name: %s   |   Applies to: %s" % (evname, applies), "meta"),
                  P("Fires when", "h3"), P(fires + ((" " + extra) if extra else "")),
                  P("Attribute form", "h3"), code_block('<div %s="console.log(\'%s fired\', event)">...</div>' % (aname, evname)),
                  P("Script form (recommended)", "h3"),
                  code_block("element.addEventListener('%s', function (event) {\n  console.log('%s fired on', event.target);\n});" % (evname, evname)),
                  P("Notes", "h3")]
        for it in ["Inside the attribute value, the variable 'event' refers to the Event object and 'this' refers to the element.",
                   "Returning false from the attribute code cancels the default action (same as event.preventDefault()).",
                   "The attribute value is compiled as the body of a function, so a syntax error is reported only when the event first fires.",
                   "Content Security Policy (CSP) headers that forbid inline scripts also block attribute handlers; addEventListener is unaffected."]:
            story.append(Paragraph(esc(it), S["li"], bulletText="\u2022"))
        story.append(PageBreak())

    # ----- Element reference
    story += part(6, "Element Reference", "One complete entry for each of the %d HTML elements, alphabetically." % len(ELEMENTS))
    story += heading("Element index", 0, "elindex")
    rows = [["Element", "Meaning", "Status", "Since"]]
    for e in ELEMENTS:
        rows.append(["<%s>" % e["name"], e["title"], e["status"], e["versions"].split(",")[0].split(";")[0]])
    story.extend(rl_table(rows, col_widths=[AVAIL * 0.16, AVAIL * 0.4, AVAIL * 0.14, AVAIL * 0.3]))
    story.append(PageBreak())

    cats = {}
    for e in ELEMENTS:
        cats.setdefault(e["cat"], []).append(e["name"])
    story += heading("Elements by category", 0, "elcats")
    story.extend(rl_table([["Category", "Elements"]] + [[c, ", ".join("<%s>" % n for n in cats[c])] for c in sorted(cats)]))
    story.append(PageBreak())

    for e in ELEMENTS:
        key = "el-" + e["name"]
        title = "<%s> \u2014 %s" % (e["name"], e["title"])
        story += [Bookmark(key, "<%s> %s" % (e["name"], e["title"]), 1)]
        story.append(P("Quick card: <%s>" % e["name"], "h1"))
        story.append(P(e["title"], "partsub"))
        story.append(Spacer(1, 6))
        story.append(P(e["desc"][0]))
        story.append(P("At a glance", "h3"))
        story.extend(rl_table([
            ["", ""],
            ["Status", e["status"].upper()],
            ["Versions", e["versions"]],
            ["Category", e["cat"]],
            ["Closing tag", "None (void element)" if e["void"] else "Required unless noted under Tag omission"],
            ["Display", e["display"]],
            ["Own attributes", ", ".join(re.split(r"\s*[/,]\s*", a[0])[0] for a in e["attrs"]) or "None (global attributes only)"],
            ["Related", ", ".join("<%s>" % r for r in e["related"]) or "-"],
        ], col_widths=[AVAIL * 0.26, AVAIL * 0.74], head=False))
        story.append(P("Minimal example", "h3"))
        story.append(code_block(e["examples"][0][1] if e["examples"] else e["syntax"]))
        if e["mistakes"]:
            story.append(P("Most common mistake", "h3"))
            story.append(P(e["mistakes"][0]))
        story.append(PageBreak())
        story.append(P(title, "h1"))
        status = e["status"].upper()
        story.append(P("Category: %s   |   Status: %s   |   Versions: %s" % (e["cat"], status, e["versions"]), "meta"))
        if e.get("aliases"):
            story.append(P("This entry also covers: " + ", ".join("<%s>" % a for a in e["aliases"]), "meta"))
        story.append(Spacer(1, 4))
        story.append(P("Description", "h3"))
        for d in e["desc"]:
            story.append(P(d))
        story.append(P("Syntax", "h3"))
        story.append(code_block(e["syntax"]))
        story.append(P("Technical summary", "h3"))
        story.extend(rl_table([
            ["Property", "Value"],
            ["Void element", "Yes (no closing tag)" if e["void"] else "No"],
            ["Default display", e["display"]],
            ["Content categories", e["categories"]],
            ["Permitted content", e["content"]],
            ["Permitted parents", e["parents"]],
            ["Tag omission", e["omission"]],
            ["DOM interface", e["dom"]],
        ], col_widths=[AVAIL * 0.24, AVAIL * 0.76]))
        story.append(P("Attributes", "h3"))
        if e["attrs"]:
            story.append(P("In addition to the global attributes (Part 4) and event handler attributes (Part 5), this element supports the following:", "caption"))
            story.extend(rl_table([["Attribute", "Values", "Description", "Since"]] + [list(a) for a in e["attrs"]],
                                  col_widths=[AVAIL * 0.17, AVAIL * 0.2, AVAIL * 0.47, AVAIL * 0.16]))
        else:
            story.append(P("This element supports only the global attributes (Part 4) and event handler attributes (Part 5)."))
        if e["attrs"]:
            story.append(PageBreak())
            story.append(P("<%s>: attribute by attribute" % e["name"], "h2"))
            story.append(P("Each attribute of <%s> explained in detail, with a minimal example you can copy." % e["name"], "caption"))
            for (an, av, ad, aver) in e["attrs"]:
                sv = sample_value(av)
                first = re.split(r"\s*[/,]\s*", an)[0].strip()
                if sv is None:
                    attr_txt = first
                    how = "Boolean attribute: write only the name to switch it on; leave it out to switch it off."
                else:
                    attr_txt = '%s="%s"' % (first, sv)
                    how = "Write %s=\"...\" inside the start tag. Quote the value; several attributes are separated by spaces." % first
                ex = ("<%s %s>" % (e["name"], attr_txt)) if e["void"] else ("<%s %s>...</%s>" % (e["name"], attr_txt, e["name"]))
                story.append(KeepTogether([P(an, "h3"), P("Values: %s   |   Since: %s" % (av, aver), "meta"), P(ad), P(how, "caption"), code_block(ex)]))
        story.append(PageBreak())
        story.append(P("<%s>: worked examples" % e["name"], "h2"))
        for (t, c, note) in e["examples"]:
            items = [P(t, "smallb"), code_block(c)]
            if note:
                items.append(P(note, "caption"))
            story.append(KeepTogether(items))
        if e["css"]:
            story.append(P("Default browser CSS", "h3"))
            story.append(code_block(e["css"]))
        if e["a11y"]:
            story.append(P("Accessibility", "h3"))
            for a in e["a11y"]:
                story.append(Paragraph(esc(a), S["li"], bulletText="\u2022"))
        if e["mistakes"]:
            story.append(P("Common mistakes", "h3"))
            for m in e["mistakes"]:
                story.append(Paragraph(esc(m), S["li"], bulletText="\u2022"))
        if e["related"]:
            story.append(P("See also", "h3"))
            story.append(P(", ".join("<%s>" % r for r in e["related"])))
        story.append(PageBreak())

    # ----- Input types
    story += part(7, "The input Element in Depth", "Every value of the type attribute with its own entry.")
    story += heading("Input types overview", 0, "inputs")
    story.extend(rl_table([["type", "Control", "Since"]] + [[t[0], t[1], t[2]] for t in INPUT_TYPES]))
    story.append(PageBreak())
    for (typ, ttl, since, desc, sattrs, ex, notes) in INPUT_TYPES:
        story += [Bookmark("in-" + typ, "input type=%s" % typ, 1), P("<input type=\"%s\"> \u2014 %s" % (typ, ttl), "h1"),
                  P("Since: %s" % since, "meta"), P(desc)]
        story.append(P("Type-specific attributes", "h3"))
        story.extend(rl_table([["Attribute", "Note"]] + [list(a) for a in sattrs]))
        story.append(P("Example", "h3"))
        story.append(code_block(ex))
        if notes:
            story.append(P(notes, "caption"))
        story.append(P("Also accepted: the common input attributes name, value, disabled, form, autofocus, required (where meaningful), and all global attributes.", "caption"))
        story.append(PageBreak())
    story.append(PageBreak())

    # ----- Obsolete
    story += part(8, "Obsolete and Deprecated Features", "Old elements and attributes you may meet, with modern replacements.")
    story += heading("Obsolete elements", 0, "obsolete")
    story.append(P("These elements appeared in HTML 1, 2.0, 3.2, 4.01 or as browser extensions and are no longer part of the standard. "
                   "Browsers still render most of them for compatibility with old pages, but they must not be used in new documents. "
                   "Each has a full entry in Part 6; this table summarises the replacements."))
    obs = [e for e in ELEMENTS if e["status"] in ("obsolete", "deprecated", "experimental")]
    story.extend(rl_table([["Element", "Status", "Was used for", "Use instead"]] + [
        ["<%s>" % e["name"], e["status"], e["title"], ", ".join("<%s>" % r for r in e["related"]) or "CSS"] for e in obs],
        col_widths=[AVAIL * 0.16, AVAIL * 0.14, AVAIL * 0.4, AVAIL * 0.3]))
    story += heading("Obsolete attributes", 1, "obsattrs")
    story.append(P("Presentational attributes were the HTML 3.2 way to control appearance. All of them are replaced by CSS."))
    story.extend(rl_table([["Attribute", "Was on", "CSS replacement"],
        ["align", "div, p, h1-h6, table, tr, td, th, img, hr, caption, legend, iframe, object", "text-align, float, vertical-align, margin"],
        ["bgcolor", "body, table, tr, td, th", "background-color"], ["background", "body, table, td", "background-image"],
        ["border", "img, table, object", "border"], ["cellpadding / cellspacing", "table", "padding on cells / border-spacing, border-collapse"],
        ["width / height", "table, td, th, hr, pre, applet", "width, height"], ["hspace / vspace", "img, object, applet", "margin"],
        ["valign", "tr, td, th, col, tbody, thead, tfoot", "vertical-align"], ["nowrap", "td, th", "white-space: nowrap"],
        ["clear", "br", "clear"], ["color / face / size", "font, basefont", "color, font-family, font-size"], ["size / noshade", "hr", "height, border"],
        ["text / link / vlink / alink", "body", "color, a:link, a:visited, a:active"], ["type", "ul, li", "list-style-type"], ["compact", "dl, ol, ul, dir, menu", "margin, line-height"],
        ["frameborder / marginwidth / marginheight / scrolling", "iframe, frame", "border, padding, overflow"], ["language", "script", "type (or omit)"],
        ["name", "a, img, form (as id)", "id"], ["longdesc", "img, iframe", "a link or aria-describedby"], ["summary", "table", "caption, aria-describedby"],
        ["charset", "a, link, script", "HTTP headers"], ["rev", "a, link", "rel"], ["scheme", "meta", "-"], ["manifest", "html", "Service workers"],
        ["accept", "form", "accept on input"], ["archive, classid, codebase, codetype, declare, standby", "object", "-"],
    ]))
    story.append(PageBreak())

    # ----- Attribute index
    story += part(9, "Attribute Reference", "Every element-specific attribute listed alphabetically with the elements that accept it.")
    story += heading("Alphabetical attribute index", 0, "attrindex")
    story.append(P("Global attributes are in Part 4 and event attributes in Part 5. This index covers attributes specific to particular elements. "
                   "Look up the attribute, find the element, then read the full entry in Part 6."))
    idx = attribute_index()
    story.extend(rl_table([["Attribute", "Used on"]] + [[name, ", ".join(sorted({"<%s>" % u[0] for u in uses}))] for name, uses in idx.items()]))
    story.append(PageBreak())
    for name, uses in idx.items():
        story += [Bookmark("ai-" + re.sub(r"\W", "", name), name, 1), P("Attribute: " + name, "h1")]
        story.append(P("Accepted by %d element%s. Each use is described on the following pages." % (len(uses), "" if len(uses) == 1 else "s"), "meta"))
        rows = [["Element", "Values", "Since"]] + [["<%s>" % u[0], u[1], u[3]] for u in uses]
        story.extend(rl_table(rows, col_widths=[AVAIL * 0.22, AVAIL * 0.56, AVAIL * 0.22]))
        for (el, values, desc, ver) in uses:
            eobj = next(x for x in ELEMENTS if x["name"] == el)
            story.append(P("%s on <%s>" % (name, el), "h2"))
            story.append(P("Element: <%s> (%s)   |   Since: %s" % (el, eobj["title"], ver), "meta"))
            story.append(P("Description", "h3"))
            story.append(P(desc))
            story.append(P("Accepted values", "h3"))
            story.append(P(values))
            story.append(P("How to write it", "h3"))
            sv = sample_value(values)
            if sv is None:
                story.append(P("This is a boolean attribute: its presence switches the feature on, its absence switches it off. Write just the name (or name=\"\" / name=\"%s\" in XHTML style). Never write %s=\"false\"; that still counts as present." % (name, name)))
                attr_txt = name
            else:
                story.append(P("Write the attribute inside the start tag, followed by an equals sign and the value in double quotes."))
                attr_txt = '%s="%s"' % (name, sv)
            if eobj["void"]:
                story.append(code_block("<%s %s>" % (el, attr_txt)))
            else:
                story.append(code_block("<%s %s>...</%s>" % (el, attr_txt, el)))
            others = sorted({u2[0] for u2 in uses if u2[0] != el})
            if others:
                story.append(P("The same attribute on other elements", "h3"))
                story.append(P(", ".join("<%s>" % o for o in others) + ". The meaning is similar but check each entry, because accepted values can differ."))
            story.append(P("Remember", "h3"))
            story.append(P("All global attributes (Part 4) and event handler attributes (Part 5) may be combined with this one on <%s>. Full details of the element are in Part 6." % el))
            story.append(PageBreak())

    # ----- Value references
    story += part(10, "Value References", "Link types, meta names, autocomplete tokens, MIME types, URL schemes, colours and entities.")
    story += heading("Link relationship types (rel)", 0, "rels") + rl_table([["Value", "Allowed on", "Meaning"]] + [list(l) for l in LINK_TYPES]) + [PageBreak()]
    story += heading("Standard meta names", 0, "metanames") + rl_table([["Name", "Meaning"]] + [list(m) for m in META_NAMES]) + [PageBreak()]
    story += heading("Autocomplete tokens", 0, "autocomplete") + [P("Values for the autocomplete attribute on input, select and textarea. Combine a section, shipping/billing prefix, contact type and field: autocomplete=\"section-guest billing work tel\".")] + rl_table([["Token", "Meaning"]] + [list(a) for a in AUTOCOMPLETE_TOKENS]) + [PageBreak()]
    story += heading("Common MIME types", 0, "mime") + rl_table([["MIME type", "Extensions", "Use"]] + [list(m) for m in MIME_TYPES]) + [PageBreak()]
    story += heading("URL schemes used in href", 0, "schemes") + rl_table([["Scheme", "Meaning"]] + [list(u) for u in URL_SCHEMES]) + [PageBreak()]
    story += heading("Named colours", 0, "colors") + [P("The 148 colour names recognised by CSS and by the legacy HTML color attributes, with their hexadecimal values.")]
    crow = []
    crows = [["Name", "Hex", "Name", "Hex"]]
    for i in range(0, len(COLOR_NAMES), 2):
        chunk = COLOR_NAMES[i:i + 2]
        r = []
        for c in chunk:
            r += [c[0], c[1]]
        while len(r) < 4:
            r += ["", ""]
        crows.append(r)
    story += rl_table(crows, col_widths=[AVAIL * 0.3, AVAIL * 0.2] * 2) + [PageBreak()]
    story += heading("Character entity reference", 0, "entities") + [P("Named and numeric character references. Numeric references also work in hexadecimal: &#x20AC; equals &#8364;. With UTF-8 you can type most of these directly; only &lt;, &gt; and &amp; are essential.")]
    story += rl_table([["Named", "Numeric", "Character"]] + [list(e) for e in ENTITIES], col_widths=[AVAIL * 0.3, AVAIL * 0.25, AVAIL * 0.45]) + [PageBreak()]

    # ----- CSS
    story += part(11, "CSS Reference", "Fundamentals, selectors, properties and a cookbook for styling HTML elements.")
    story += heading("CSS fundamentals", 0, "css") + blocks(CSS_INTRO) + [PageBreak()]
    story += heading("CSS selectors", 0, "cssel")
    story.extend(rl_table([["Selector", "Meaning"]] + [[a, b] for (a, b, c) in CSS_SELECTORS]))
    story.append(PageBreak())
    for (sel, meaning, ex) in CSS_SELECTORS:
        story += [Bookmark("sel-" + re.sub(r"\W", "", sel), sel, 1), P("Selector: " + sel, "h1"), P("What it selects", "h3"), P(meaning),
                  P("Example", "h3"), code_block(ex), P("Tips", "h3")]
        for it in ["Selectors are case-sensitive for class names and IDs, but HTML element names are matched case-insensitively.",
                   "Combine selectors with a comma to apply one rule to several targets: h1, h2, h3 { ... }.",
                   "Test any selector in the browser console with document.querySelectorAll('%s').length." % sel.replace("'", "\\'")]:
            story.append(Paragraph(esc(it), S["li"], bulletText="\u2022"))
        story.append(PageBreak())
    story += heading("CSS property reference", 0, "cssprops")
    story.append(P("Properties are grouped by purpose. Each entry gives the accepted values, an explanation and an example."))
    lastgroup = None
    for (group, prop, values, desc, ex) in CSS_PROPERTIES:
        if group != lastgroup:
            story.append(P(group, "h2"))
            story.append(Bookmark("cssg-" + re.sub(r"\W", "", group), group, 1))
            lastgroup = group
        story += [P(prop, "h1"), P("Group: %s" % group, "meta"), P("Values", "h3"), P(values), P("Description", "h3"), P(desc),
                  P("Example", "h3"), code_block(ex), P("Where to apply it", "h3"),
                  P("In an external style sheet (recommended), in a <style> element in the <head>, or inline in a style attribute. "
                    "Check the property in your browser's developer tools (Elements panel, Styles tab): declarations shown struck through are being "
                    "overridden or are invalid."), PageBreak()]
    story += heading("Styling HTML elements: cookbook", 0, "csscook") + blocks(CSS_HTML_STYLING_GUIDE) + [PageBreak()]
    story += heading("Lists and tables with CSS", 0, "csslt") + blocks(CSS_LISTS_TABLES) + [PageBreak()]

    # ----- Course
    story += part(12, "HTML and CSS Course", "Thirty-six lessons from first page to finished project, following the W3Schools HTML and CSS tutorial.")
    story += heading("About this course", 0, "course")
    story.append(P("This part is a guided course rather than a reference: read the lessons in order, type the examples, and change them. "
                   "Its structure follows the W3Schools HTML and CSS tutorial (foundations, styling core, layout, enhancements, quality, project). "
                   "Whenever a lesson mentions an element or property, the full details are in Parts 6 and 11."))
    story.extend(rl_table([["Lesson", "Topic"]] + [[str(i + 1), t.split(":", 1)[1].strip() if ":" in t else t] for i, (t, _) in enumerate(COURSE)]))
    story.append(PageBreak())
    for i, (ct, cb) in enumerate(COURSE):
        story += heading(ct, 1, "lesson%d" % i) + blocks(cb) + [PageBreak()]

    # ----- Guides
    story += part(13, "Practical Guides", "Step-by-step guidance for pages, lists, tables, forms, media, accessibility, SEO and migration.")
    for i, (gt, gb) in enumerate(GUIDES):
        story += heading(gt, 0, "guide%d" % i) + blocks(gb) + [PageBreak()]

    # ----- Glossary and index
    story += part(14, "Glossary and Index", "Definitions of terms and an alphabetical index of everything in the book.")
    story += heading("Glossary", 0, "glossary")
    story.extend(rl_table([["Term", "Definition"]] + [list(g) for g in GLOSSARY]))
    story.append(PageBreak())
    story += heading("Glossary in depth", 0, "glossary2")
    story.append(P("Each term again, with the places in this book where it matters most, so you can jump from a word you do not know to the chapter that explains it."))
    story.append(PageBreak())
    elnames = {e["name"] for e in ELEMENTS}
    propnames = [p[1] for p in CSS_PROPERTIES]
    for (term, definition) in GLOSSARY:
        words = set(re.findall(r"[a-z][a-z0-9-]+", (term + " " + definition).lower()))
        rel_el = sorted(w for w in words if w in elnames)[:12]
        rel_css = sorted(p for p in propnames if any(w == p or w in p.split(" / ") for w in words))[:8]
        story += [Bookmark("gl-" + re.sub(r"\W", "", term), term, 1), P(term, "h1"), P("Definition", "h3"), P(definition),
                  P("Where to read more", "h3")]
        story.append(Paragraph(esc("Related elements (Part 6): " + (", ".join("<%s>" % x for x in rel_el) if rel_el else "see the index")), S["li"], bulletText="\u2022"))
        if rel_css:
            story.append(Paragraph(esc("Related CSS properties (Part 11): " + ", ".join(rel_css)), S["li"], bulletText="\u2022"))
        story.append(Paragraph(esc("Search tip: in the HTML edition type '%s' in the search box to list every entry that mentions it." % term), S["li"], bulletText="\u2022"))
        story.append(PageBreak())
    story += heading("Alphabetical index", 0, "index")
    story.append(P("Elements are shown in angle brackets, attributes in plain type, CSS properties with a leading dot-free name marked (CSS). "
                   "Use your PDF reader's search (Ctrl+F) for anything not listed here."))
    entries = []
    for e in ELEMENTS:
        entries.append(("<%s>" % e["name"], "Part 6: %s" % e["title"]))
        for al in e.get("aliases", []):
            entries.append(("<%s>" % al, "Part 6: see <%s>" % e["name"]))
    for a in GLOBAL_ATTRS:
        entries.append((a[0], "Part 4: global attribute"))
    for name, uses in idx.items():
        entries.append((name, "Part 9: attribute on " + ", ".join(sorted({"<%s>" % u[0] for u in uses}))))
    for t in INPUT_TYPES:
        entries.append(("type=%s" % t[0], "Part 7: input type"))
    for p in CSS_PROPERTIES:
        entries.append((p[1] + " (CSS)", "Part 11: " + p[0]))
    for g in GLOSSARY:
        entries.append((g[0], "Part 14: glossary"))
    entries.sort(key=lambda x: re.sub(r"[<>]", "", x[0]).lower())
    rows = [["Term", "Where to find it"]] + [list(x) for x in entries]
    story.extend(rl_table(rows, col_widths=[AVAIL * 0.32, AVAIL * 0.68]))

    # ----- Page templates
    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("Sans", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(LM, 9 * mm, TITLE)
        canvas.drawRightString(PAGE[0] - RM, 9 * mm, "Page %d" % doc.page)
        canvas.setStrokeColor(LINE)
        canvas.line(LM, 12.5 * mm, PAGE[0] - RM, 12.5 * mm)
        canvas.restoreState()

    doc = Doc(path, pagesize=PAGE, leftMargin=LM, rightMargin=RM, topMargin=14 * mm, bottomMargin=16 * mm,
              title=TITLE, author="Arena.ai Agent Mode", subject=SUBTITLE)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="cover", frames=[frame]), PageTemplate(id="body", frames=[frame], onPage=on_page)])
    doc.multiBuild(story)


# ============================================================================
# HTML (searchable single page)
# ============================================================================
def build_html(path):
    E = htmlmod.escape

    def blocks(seq):
        out = []
        for kind, val in seq:
            if kind in ("h2", "h3"):
                out.append("<%s>%s</%s>" % (kind, E(val), kind))
            elif kind == "p":
                out.append("<p>%s</p>" % E(val))
            elif kind == "code":
                out.append("<pre><code>%s</code></pre>" % E(val))
            elif kind == "ul":
                out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % E(i) for i in val))
            elif kind == "table":
                out.append(table(val))
            elif kind == "note":
                out.append("<div class=\"note\">%s</div>" % E(val))
        return "\n".join(out)

    def table(rows):
        h = "<table><thead><tr>%s</tr></thead><tbody>" % "".join("<th>%s</th>" % E(c) for c in rows[0])
        for r in rows[1:]:
            h += "<tr>%s</tr>" % "".join("<td>%s</td>" % E(c) for c in r)
        return h + "</tbody></table>"

    def section(sid, title, body, kind="section", keywords=""):
        return ("<section id=\"%s\" class=\"entry\" data-kind=\"%s\" data-title=\"%s\" data-keywords=\"%s\">"
                "<h2 class=\"entry-title\">%s</h2>%s</section>\n") % (sid, kind, E(title), E(keywords), E(title), body)

    parts = []
    nav = []

    def add_part(pid, title, inner_sections):
        nav.append((pid, title))
        parts.append("<article id=\"%s\" class=\"part\"><h1>%s</h1>%s</article>" % (pid, E(title), "".join(inner_sections)))

    add_part("part-howto", "How to use this book", [section("howto", "How to use this book", blocks(HOW_TO_USE))])
    add_part("part-history", "Part 1: The History of HTML", [section("history", "A short history of HTML", blocks(HISTORY), keywords="html 1 2 3.2 4.01 xhtml html5 living standard timeline berners-lee")])
    add_part("part-fund", "Part 2: HTML Fundamentals", [section("fundamentals", "HTML fundamentals", blocks(FUNDAMENTALS), keywords="syntax element tag attribute void nesting doctype comment entity whitespace block inline")])

    secs = []
    for (vk, vtitle, keys, vintro) in VERSIONS:
        els = elements_for_version(keys)
        b = "<p>%s</p>%s" % (E(vintro), table([["Element", "Meaning", "Status today"]] + [["<%s>" % e["name"], e["title"], e["status"]] for e in els]))
        b += "".join("<h3><a href=\"#el-%s\">&lt;%s&gt;</a> %s</h3><p>%s</p>" % (e["name"], e["name"], E(e["title"]), E(e["desc"][0])) for e in els)
        secs.append(section("ver-" + vk.replace(" ", ""), vtitle, b, kind="Version", keywords="version history " + vk))
    add_part("part-versions", "Part 3: HTML Version by Version", secs)

    secs = []
    for (name, values, desc, ver, ex) in GLOBAL_ATTRS:
        body = "<p class=\"meta\">Values: <code>%s</code> &middot; Since: %s</p><p>%s</p><pre><code>%s</code></pre>" % (E(values), E(ver), E(desc), E(ex))
        secs.append(section("attr-" + re.sub(r"\W", "", name), name, body, kind="Global attribute", keywords="global attribute " + values))
    add_part("part-globals", "Part 4: Global Attributes", secs)

    rows = [["Attribute", "Event", "Fires when", "Applies to"]] + [[a[0], a[1], a[2] + ((" " + a[4]) if a[4] else ""), a[3]] for a in EVENT_ATTRS]
    ev_secs = [section("events", "Event handler attributes",
                       "<p>Every element accepts on* attributes whose value is JavaScript run when the event fires. Prefer addEventListener in scripts.</p>" + table(rows),
                       kind="Events", keywords=" ".join(a[0] for a in EVENT_ATTRS))]
    add_part("part-events", "Part 5: Event Handler Attributes", ev_secs)

    secs = []
    idx_rows = [["Element", "Meaning", "Status", "Since"]] + [["<%s>" % e["name"], e["title"], e["status"], e["versions"]] for e in ELEMENTS]
    secs.append(section("element-index", "Element index", table(idx_rows), kind="Index"))
    for e in ELEMENTS:
        b = ["<p class=\"meta\"><span class=\"badge %s\">%s</span> Category: %s &middot; Versions: %s</p>" % (e["status"], e["status"], E(e["cat"]), E(e["versions"]))]
        if e.get("aliases"):
            b.append("<p class=\"meta\">Also covers: %s</p>" % ", ".join("&lt;%s&gt;" % a for a in e["aliases"]))
        b.append("<h3>Description</h3>" + "".join("<p>%s</p>" % E(d) for d in e["desc"]))
        b.append("<h3>Syntax</h3><pre><code>%s</code></pre>" % E(e["syntax"]))
        b.append("<h3>Technical summary</h3>" + table([["Property", "Value"], ["Void element", "Yes (no closing tag)" if e["void"] else "No"], ["Default display", e["display"]],
                                                       ["Content categories", e["categories"]], ["Permitted content", e["content"]], ["Permitted parents", e["parents"]],
                                                       ["Tag omission", e["omission"]], ["DOM interface", e["dom"]]]))
        b.append("<h3>Attributes</h3>")
        if e["attrs"]:
            b.append("<p class=\"small\">In addition to the global and event attributes:</p>" + table([["Attribute", "Values", "Description", "Since"]] + [list(a) for a in e["attrs"]]))
        else:
            b.append("<p>Only the global attributes and event handler attributes.</p>")
        b.append("<h3>Examples</h3>")
        for (t, c, note) in e["examples"]:
            b.append("<h4>%s</h4><pre><code>%s</code></pre>%s" % (E(t), E(c), ("<p class=\"small\">%s</p>" % E(note)) if note else ""))
        if e["css"]:
            b.append("<h3>Default browser CSS</h3><pre><code>%s</code></pre>" % E(e["css"]))
        if e["a11y"]:
            b.append("<h3>Accessibility</h3><ul>%s</ul>" % "".join("<li>%s</li>" % E(a) for a in e["a11y"]))
        if e["mistakes"]:
            b.append("<h3>Common mistakes</h3><ul>%s</ul>" % "".join("<li>%s</li>" % E(m) for m in e["mistakes"]))
        if e["related"]:
            b.append("<h3>See also</h3><p>%s</p>" % ", ".join("<a href=\"#el-%s\">&lt;%s&gt;</a>" % (r if r not in ("h2", "h3", "h4", "h5", "h6") else "h1", r) for r in e["related"]))
        kw = " ".join([e["name"], e["title"], e["cat"], e["status"]] + [a[0] for a in e["attrs"]] + e.get("aliases", []))
        secs.append(section("el-" + e["name"], "<%s> %s" % (e["name"], e["title"]), "".join(b), kind="Element", keywords=kw))
    add_part("part-elements", "Part 6: Element Reference", secs)

    secs = [section("input-types", "Input types overview", table([["type", "Control", "Since"]] + [[t[0], t[1], t[2]] for t in INPUT_TYPES]), kind="Index")]
    for (typ, ttl, since, desc, sattrs, ex, notes) in INPUT_TYPES:
        b = "<p class=\"meta\">Since: %s</p><p>%s</p><h3>Type-specific attributes</h3>%s<h3>Example</h3><pre><code>%s</code></pre>%s" % (
            E(since), E(desc), table([["Attribute", "Note"]] + [list(a) for a in sattrs]), E(ex), ("<p class=\"small\">%s</p>" % E(notes)) if notes else "")
        secs.append(section("input-" + typ, "<input type=\"%s\"> %s" % (typ, ttl), b, kind="Input type", keywords="input type " + typ + " " + ttl))
    add_part("part-inputs", "Part 7: The input Element in Depth", secs)

    obs = [e for e in ELEMENTS if e["status"] in ("obsolete", "deprecated", "experimental")]
    secs = [section("obsolete", "Obsolete and deprecated elements", table([["Element", "Status", "Was used for", "Use instead"]] + [
        ["<%s>" % e["name"], e["status"], e["title"], ", ".join("<%s>" % r for r in e["related"]) or "CSS"] for e in obs]), kind="Index", keywords="obsolete deprecated old html 3.2 4")]
    add_part("part-obsolete", "Part 8: Obsolete and Deprecated Features", secs)

    idx = attribute_index()
    secs = []
    for name, uses in idx.items():
        secs.append(section("a-" + re.sub(r"\W", "", name), name, table([["Element", "Values", "Description", "Since"]] + [["<%s>" % u[0], u[1], u[2], u[3]] for u in uses]),
                            kind="Attribute", keywords="attribute " + " ".join(u[0] for u in uses)))
    add_part("part-attrs", "Part 9: Attribute Reference", secs)

    secs = [
        section("rels", "Link relationship types (rel)", table([["Value", "Allowed on", "Meaning"]] + [list(l) for l in LINK_TYPES]), kind="Reference", keywords="rel link types " + " ".join(l[0] for l in LINK_TYPES)),
        section("metanames", "Standard meta names", table([["Name", "Meaning"]] + [list(m) for m in META_NAMES]), kind="Reference", keywords="meta name viewport description robots og twitter"),
        section("autocomplete", "Autocomplete tokens", table([["Token", "Meaning"]] + [list(a) for a in AUTOCOMPLETE_TOKENS]), kind="Reference", keywords="autocomplete autofill"),
        section("mime", "Common MIME types", table([["MIME type", "Extensions", "Use"]] + [list(m) for m in MIME_TYPES]), kind="Reference", keywords="mime type content-type"),
        section("schemes", "URL schemes", table([["Scheme", "Meaning"]] + [list(u) for u in URL_SCHEMES]), kind="Reference", keywords="url scheme mailto tel https"),
        section("colors", "Named colours", table([["Name", "Hex"]] + [list(c) for c in COLOR_NAMES]), kind="Reference", keywords="color colour names hex " + " ".join(c[0] for c in COLOR_NAMES)),
        section("entities", "Character entity reference", table([["Named", "Numeric", "Character"]] + [list(e) for e in ENTITIES]), kind="Reference", keywords="entity entities character reference nbsp copy amp"),
    ]
    add_part("part-values", "Part 10: Value References", secs)

    secs = [section("css", "CSS fundamentals", blocks(CSS_INTRO), kind="CSS", keywords="css cascade specificity box model flexbox grid units colours responsive")]
    secs.append(section("css-selectors", "CSS selectors", "".join("<h3><code>%s</code></h3><p>%s</p><pre><code>%s</code></pre>" % (E(s), E(m), E(x)) for (s, m, x) in CSS_SELECTORS),
                        kind="CSS", keywords="css selector pseudo-class pseudo-element " + " ".join(s[0] for s in CSS_SELECTORS)))
    for (group, prop, values, desc, ex) in CSS_PROPERTIES:
        b = "<p class=\"meta\">Group: %s &middot; Values: <code>%s</code></p><p>%s</p><pre><code>%s</code></pre>" % (E(group), E(values), E(desc), E(ex))
        secs.append(section("css-" + re.sub(r"\W", "", prop), prop, b, kind="CSS property", keywords="css property " + group))
    secs.append(section("css-cookbook", "Styling HTML elements: cookbook", blocks(CSS_HTML_STYLING_GUIDE), kind="CSS", keywords="css cookbook style footer table list form nav header"))
    secs.append(section("css-lists-tables", "Lists and tables with CSS", blocks(CSS_LISTS_TABLES), kind="CSS", keywords="css list ul ol dl table td th border collapse zebra list-style marker bullets responsive table"))
    add_part("part-css", "Part 11: CSS Reference", secs)

    secs = [section("lesson-%d" % i, ct, blocks(cb), kind="Lesson", keywords="course lesson tutorial w3schools") for i, (ct, cb) in enumerate(COURSE)]
    add_part("part-course", "Part 12: HTML and CSS Course", secs)

    secs = [section("guide-%d" % i, gt, blocks(gb), kind="Guide") for i, (gt, gb) in enumerate(GUIDES)]
    add_part("part-guides", "Part 13: Practical Guides", secs)

    secs = [section("glossary", "Glossary", table([["Term", "Definition"]] + [list(g) for g in GLOSSARY]), kind="Glossary", keywords=" ".join(g[0] for g in GLOSSARY))]
    add_part("part-glossary", "Part 14: Glossary", secs)

    el_links = "".join("<a href=\"#el-%s\">&lt;%s&gt;</a>" % (e["name"], e["name"]) for e in ELEMENTS)
    nav_html = "".join("<li><a href=\"#%s\">%s</a></li>" % (pid, E(t)) for pid, t in nav)

    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(sub)s">
<style>
:root { --brand:#b90000; --ink:#1b2431; --muted:#5b6472; --line:#d9d2c3; --bg:#faf8f3; --panel:#fff; --code:#f4f1ea; }
* { box-sizing: border-box; }
body { margin:0; font-family: Georgia, "Times New Roman", serif; color:var(--ink); background:var(--bg); line-height:1.6; }
header.top { position:sticky; top:0; z-index:5; background:var(--panel); border-bottom:1px solid var(--line); padding:10px 16px; display:flex; gap:12px; align-items:center; flex-wrap:wrap; }
header.top h1 { font-size:1.05rem; margin:0; color:var(--brand); font-family: system-ui, Arial, sans-serif; }
#q { flex:1; min-width:220px; font: 1rem system-ui, Arial, sans-serif; padding:10px 14px; border:2px solid var(--line); border-radius:999px; }
#q:focus { outline:none; border-color:var(--brand); }
#count { font: 0.85rem system-ui, sans-serif; color:var(--muted); }
.layout { display:grid; grid-template-columns: 260px 1fr; gap:0; }
aside.side { position:sticky; top:62px; height:calc(100vh - 62px); overflow:auto; background:var(--panel); border-right:1px solid var(--line); padding:12px; font-family: system-ui, Arial, sans-serif; font-size:0.85rem; }
aside.side ul { list-style:none; padding:0; margin:0 0 12px; }
aside.side li a { display:block; padding:4px 6px; color:var(--ink); text-decoration:none; border-radius:6px; }
aside.side li a:hover { background:var(--code); }
.elgrid { display:flex; flex-wrap:wrap; gap:4px; }
.elgrid a { font: 0.78rem ui-monospace, Consolas, monospace; background:var(--code); padding:2px 6px; border-radius:4px; text-decoration:none; color:var(--ink); }
main { padding:20px 28px 80px; max-width:1000px; }
article.part > h1 { font-size:1.8rem; color:var(--brand); border-bottom:3px solid var(--brand); padding-bottom:6px; margin-top:48px; }
section.entry { background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:18px 22px; margin:18px 0; }
section.entry h2.entry-title { margin-top:0; font-size:1.4rem; color:var(--brand); }
section.entry h3 { font-family: system-ui, Arial, sans-serif; font-size:0.95rem; margin:18px 0 6px; color:var(--brand); text-transform:uppercase; letter-spacing:.04em; }
section.entry h4 { font-family: system-ui, Arial, sans-serif; font-size:0.95rem; margin:14px 0 4px; }
.meta, .small { font: 0.85rem system-ui, Arial, sans-serif; color:var(--muted); }
.badge { display:inline-block; font-size:.75rem; padding:1px 8px; border-radius:999px; background:#e7f5ea; color:#0f6a37; text-transform:uppercase; font-weight:600; }
.badge.obsolete { background:#fde8e8; color:#9b1c1c; } .badge.deprecated { background:#fff4d6; color:#8a5a00; } .badge.experimental { background:#e8f0fe; color:#1a4fa0; }
pre { background:var(--code); border:1px solid var(--line); border-radius:8px; padding:12px 14px; overflow-x:auto; font: 0.82rem/1.45 ui-monospace, Consolas, "Courier New", monospace; }
code { font-family: ui-monospace, Consolas, monospace; font-size:.92em; }
table { border-collapse:collapse; width:100%%; font: 0.86rem system-ui, Arial, sans-serif; margin:8px 0 14px; }
th, td { border:1px solid var(--line); padding:6px 8px; text-align:left; vertical-align:top; }
th { background:#f0e9dc; }
tbody tr:nth-child(even) { background:#fcfbf8; }
.note { background:#fff8e1; border:1px solid #e6c65c; border-radius:8px; padding:10px 14px; margin:10px 0; }
mark { background:#ffe58a; }
.hidden { display:none !important; }
.searching article.part > h1 { display:none; }
#noresults { display:none; padding:40px; text-align:center; color:var(--muted); font-family: system-ui, sans-serif; }
@media (max-width: 900px) { .layout { grid-template-columns: 1fr; } aside.side { position:static; height:auto; border-right:0; border-bottom:1px solid var(--line); } main { padding:16px; } }
@media print { header.top, aside.side { display:none; } section.entry { break-inside: avoid; border:0; } }
</style>
</head>
<body>
<header class="top">
  <h1>%(title)s</h1>
  <label for="q" class="visually-hidden" style="position:absolute;left:-9999px">Search the book</label>
  <input id="q" type="search" placeholder="Search anything: footer, td, font-family, href, italic, table border..." autocomplete="off">
  <span id="count"></span>
</header>
<div class="layout">
<aside class="side">
  <strong>Contents</strong>
  <ul>%(nav)s</ul>
  <strong>All elements</strong>
  <div class="elgrid">%(els)s</div>
</aside>
<main id="main">
<p class="small">%(sub)s. %(count)d element entries, %(nattr)d attribute index entries, %(ncss)d CSS properties. Type in the search box to filter every entry instantly; clear it to return to the full book.</p>
%(parts)s
<div id="noresults">No entries match. Try another word, a tag name without brackets, or an attribute name.</div>
</main>
</div>
<script>
(function () {
  var q = document.getElementById('q'), entries = Array.prototype.slice.call(document.querySelectorAll('section.entry'));
  var count = document.getElementById('count'), none = document.getElementById('noresults'), body = document.body;
  var cache = entries.map(function (s) { return (s.dataset.title + ' ' + s.dataset.keywords + ' ' + s.textContent).toLowerCase(); });
  function score(i, terms) {
    var t = (entries[i].dataset.title || '').toLowerCase(), k = (entries[i].dataset.keywords || '').toLowerCase(), s = 0;
    for (var j = 0; j < terms.length; j++) {
      var w = terms[j];
      if (cache[i].indexOf(w) === -1) return -1;
      if (t.replace(/[<>]/g, '').split(/\\s+/)[0] === w) s += 100;
      else if (t.indexOf(w) !== -1) s += 30;
      else if (k.indexOf(w) !== -1) s += 10;
      else s += 1;
    }
    return s;
  }
  function run() {
    var v = q.value.trim().toLowerCase().replace(/[<>]/g, '');
    if (!v) { entries.forEach(function (s) { s.classList.remove('hidden'); }); body.classList.remove('searching'); count.textContent = ''; none.style.display = 'none'; return; }
    var terms = v.split(/\\s+/), shown = 0, best = -1, bestI = -1;
    body.classList.add('searching');
    entries.forEach(function (s, i) {
      var sc = score(i, terms);
      if (sc < 0) s.classList.add('hidden'); else { s.classList.remove('hidden'); shown++; if (sc > best) { best = sc; bestI = i; } }
    });
    count.textContent = shown + ' result' + (shown === 1 ? '' : 's');
    none.style.display = shown ? 'none' : 'block';
    if (bestI >= 0) { var m = document.getElementById('main'); m.insertBefore(entries[bestI].parentNode, m.children[1]); entries[bestI].scrollIntoView({ block: 'start' }); window.scrollBy(0, -70); }
  }
  var t; q.addEventListener('input', function () { clearTimeout(t); t = setTimeout(run, 120); });
  q.addEventListener('keydown', function (e) { if (e.key === 'Escape') { q.value = ''; run(); } });
  document.addEventListener('keydown', function (e) { if (e.key === '/' && document.activeElement !== q) { e.preventDefault(); q.focus(); } });
  if (location.hash) { var el = document.querySelector(location.hash); if (el) el.scrollIntoView(); }
})();
</script>
</body>
</html>
""" % dict(title=E(TITLE), sub=E(SUBTITLE), nav=nav_html, els=el_links, parts="\n".join(parts), count=len(ELEMENTS), nattr=len(idx), ncss=len(CSS_PROPERTIES))
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)


if __name__ == "__main__":
    validate()
    pdf = os.path.join(OUT_DIR, "HTML-Reference-Book.pdf")
    htmlp = os.path.join(OUT_DIR, "HTML-Reference-Book.html")
    build_html(htmlp)
    print("HTML written:", htmlp)
    build_pdf(pdf)
    print("PDF written:", pdf)
