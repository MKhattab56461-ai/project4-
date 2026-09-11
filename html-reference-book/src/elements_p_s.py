# -*- coding: utf-8 -*-
"""Element reference entries, letters P to S."""

ELEMENTS = [

dict(
    name="p", title="Paragraph", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <p> element represents a paragraph: a block of related text, usually a group of sentences on "
        "one topic. Browsers display paragraphs as blocks separated by vertical space (a margin of 1em above "
        "and below). Paragraphs are one of the most used elements in HTML and one of the original elements "
        "from 1991, where <p> was a separator between paragraphs rather than a container.",
        "A paragraph may contain only phrasing content (text, links, emphasis, images, and so on). It "
        "cannot contain block-level elements such as <div>, <ul>, <table>, headings or another <p>. If the "
        "browser encounters one of these inside a <p> it automatically closes the paragraph first, which "
        "often produces layouts that look wrong for no obvious reason.",
        "The end tag may be omitted because the browser knows a paragraph ends when the next block starts, "
        "but writing </p> makes the code much clearer. Do not use empty <p></p> elements to add space; use "
        "CSS margins.",
    ],
    syntax="<p>Text of the paragraph.</p>", void=False, display="block",
    categories="Flow content, palpable content", content="Phrasing content",
    parents="Any element that accepts flow content",
    omission="End tag may be omitted if the <p> is immediately followed by address, article, aside, blockquote, details, dialog, div, dl, fieldset, figcaption, figure, footer, form, h1-h6, header, hgroup, hr, main, menu, nav, ol, p, pre, search, section, table or ul, or if there is no more content in the parent (except when the parent is <a>, <audio>, <del>, <ins>, <map>, <noscript> or <video>)",
    dom="HTMLParagraphElement",
    attrs=[("align", "left | center | right | justify", "Obsolete. Use CSS text-align.", "HTML 3.2")],
    examples=[
        ("Two paragraphs", "<p>HTML describes the structure of a page.</p>\n<p>CSS describes how the page looks.</p>", ""),
        ("Inline elements inside a paragraph", "<p>I <em>really</em> love <a href=\"https://developer.mozilla.org\">MDN</a>, and I read it <strong>every day</strong>.</p>", ""),
        ("Wrong: a list inside a paragraph",
         "<!-- Wrong: the browser closes the <p> before the <ul> -->\n<p>Shopping:\n  <ul><li>Milk</li></ul>\n</p>\n\n<!-- Right -->\n<p>Shopping:</p>\n<ul><li>Milk</li></ul>", ""),
        ("Typography with CSS", "<style>\n  p { line-height: 1.6; max-width: 65ch; margin: 0 0 1em; }\n  p + p { text-indent: 1.5em; margin-top: -0.5em; }\n</style>", "65ch keeps lines at a comfortable reading length; text-indent gives book-style paragraphs."),
    ],
    a11y=["Screen readers pause between paragraphs; use real paragraphs rather than <br><br>.", "Keep paragraphs reasonably short; long walls of text are hard for everyone."],
    mistakes=["Block elements inside <p>.", "Empty paragraphs for spacing.", "Using <br><br> instead of a new paragraph.", "Using <p> for every line in an address (use <br> inside one <p>)."],
    related=["br", "div", "span", "blockquote", "pre"], css="p { display: block; margin-block: 1em; }",
),

dict(
    name="param", title="Object parameter (deprecated)", cat="Embedded content",
    versions="HTML 3.2, HTML 4.01, HTML5; deprecated in the Living Standard", status="deprecated",
    desc=[
        "The <param> element defined a parameter for an <object> element, passing a name/value pair to the "
        "plug-in that displayed the object (for example the autoplay setting of a Flash movie). Since "
        "plug-ins no longer exist, the element serves no purpose; the Living Standard marks it deprecated "
        "and it is retained only for compatibility. It is a void element.",
    ],
    syntax="<object data=\"movie.swf\">\n  <param name=\"quality\" value=\"high\">\n</object>", void=True, display="none",
    categories="None", content="None (void element)", parents="<object>, before any flow content", omission="No end tag", dom="HTMLParamElement",
    attrs=[("name", "text", "The parameter name.", "HTML 3.2"), ("value", "text", "The parameter value.", "HTML 3.2"),
           ("type", "MIME type", "Obsolete. Type of the value when valuetype=ref.", "HTML 4.01"),
           ("valuetype", "data | ref | object", "Obsolete. How to interpret value.", "HTML 4.01")],
    examples=[("Historical Flash embed", "<object data=\"movie.swf\" type=\"application/x-shockwave-flash\" width=\"400\" height=\"300\">\n  <param name=\"quality\" value=\"high\">\n  <param name=\"wmode\" value=\"transparent\">\n  <p>Flash is no longer supported.</p>\n</object>", "")],
    a11y=[], mistakes=["Any use in new pages."], related=["object", "embed"], css="param { display: none; }",
),

dict(
    name="picture", title="Picture (responsive image container)", cat="Image and multimedia",
    versions="HTML 5.1 (2016)", status="current",
    desc=[
        "The <picture> element contains zero or more <source> elements and exactly one <img> element, and "
        "lets the browser choose the most suitable image from several candidates. The browser examines "
        "each <source> in order and uses the first whose media query matches and whose type it supports; if "
        "none match it falls back to the <img>. The <img> element is required: it is what is actually "
        "displayed, and it carries the alt text, width, height, loading and other attributes.",
        "Use <picture> for three purposes: art direction (a cropped image on phones, a wide one on "
        "desktops), format selection (AVIF or WebP for modern browsers, JPEG for old ones), and "
        "dark-mode variants. For simply serving different sizes of the same image, srcset and sizes on a "
        "plain <img> are enough.",
    ],
    syntax="<picture>\n  <source srcset=\"...\" media=\"...\" type=\"...\">\n  <img src=\"...\" alt=\"...\">\n</picture>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content, palpable content",
    content="Zero or more <source> elements, followed by one <img>, optionally intermixed with <script> and <template>",
    parents="Any element that accepts embedded content", omission="Neither tag may be omitted", dom="HTMLPictureElement",
    attrs=[],
    examples=[
        ("Modern formats with fallback", "<picture>\n  <source srcset=\"photo.avif\" type=\"image/avif\">\n  <source srcset=\"photo.webp\" type=\"image/webp\">\n  <img src=\"photo.jpg\" alt=\"Sunset over the Nile\" width=\"800\" height=\"500\">\n</picture>", "Browsers that support AVIF use it; others try WebP; the rest use JPEG."),
        ("Art direction", "<picture>\n  <source media=\"(max-width: 600px)\" srcset=\"hero-portrait.jpg\">\n  <source media=\"(min-width: 601px)\" srcset=\"hero-wide.jpg\">\n  <img src=\"hero-wide.jpg\" alt=\"Our team in the office\" width=\"1200\" height=\"600\">\n</picture>", "A tight portrait crop on phones, the full wide picture on larger screens."),
        ("Dark mode image", "<picture>\n  <source media=\"(prefers-color-scheme: dark)\" srcset=\"logo-dark.svg\">\n  <img src=\"logo-light.svg\" alt=\"Book Store\" width=\"120\" height=\"40\">\n</picture>", ""),
        ("Combining with srcset sizes", "<picture>\n  <source type=\"image/webp\" srcset=\"p-400.webp 400w, p-800.webp 800w\" sizes=\"(max-width: 600px) 100vw, 600px\">\n  <img src=\"p-800.jpg\" srcset=\"p-400.jpg 400w, p-800.jpg 800w\" sizes=\"(max-width: 600px) 100vw, 600px\" alt=\"...\" width=\"800\" height=\"533\">\n</picture>", ""),
    ],
    a11y=["All accessibility comes from the <img>: alt text goes there, never on <source>."],
    mistakes=["Omitting the <img>.", "Putting <img> before the <source> elements (sources after img are ignored).", "Using src instead of srcset on <source>.", "Styling the <picture> instead of the <img> (picture has no box of its own in most cases)."],
    related=["img", "source", "figure"], css="picture { display: inline; }",
),

dict(
    name="plaintext", title="Plain text (obsolete)", cat="Obsolete text content",
    versions="HTML 1, HTML 2.0 (deprecated); obsolete", status="obsolete",
    desc=[
        "The <plaintext> element told the browser to treat everything after it as plain text, without "
        "interpreting any further tags, until the end of the file. It could not be closed. It was one of "
        "the 1991 elements, was deprecated in HTML 2.0 and is obsolete. Use <pre> for pre-formatted text, "
        "escaping < and & as entities, or serve the file as text/plain.",
    ],
    syntax="<plaintext>", void=True, display="block",
    categories="Historical", content="Everything after it", parents="Any", omission="No end tag possible", dom="HTMLElement",
    attrs=[],
    examples=[("Replacement", "<pre>&lt;p&gt;This shows the tag literally.&lt;/p&gt;</pre>", "")],
    a11y=[], mistakes=["Any use."], related=["pre", "xmp", "listing"], css="plaintext { display: block; font-family: monospace; white-space: pre; }",
),

dict(
    name="portal", title="Portal (experimental, abandoned)", cat="Embedded content",
    versions="Chrome experiment (2019-2022); not standardised", status="experimental",
    desc=[
        "The <portal> element was an experiment that embedded a preview of another page, like an iframe, "
        "with the ability to 'activate' it and navigate seamlessly into it with an animation. It was "
        "available only behind a flag in Chrome and the work has been superseded by the View Transitions "
        "API and prerendering with the Speculation Rules API. Do not use it.",
    ],
    syntax="<portal src=\"https://example.com\"></portal>", void=False, display="inline",
    categories="Experimental", content="None", parents="Embedded content", omission="Neither", dom="HTMLPortalElement (Chrome only)",
    attrs=[("src", "URL", "Page to preview.", "Experimental"), ("referrerpolicy", "policy", "Referrer policy.", "Experimental")],
    examples=[("Modern alternative", "<script type=\"speculationrules\">\n{ \"prerender\": [{ \"urls\": [\"/next-page.html\"] }] }\n</script>", "")],
    a11y=[], mistakes=["Any use."], related=["iframe", "fencedframe"], css="",
),

dict(
    name="pre", title="Pre-formatted text", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <pre> element represents pre-formatted text that is displayed exactly as written in the HTML "
        "file: every space, tab and line break is preserved, and a monospace (fixed-width) font is used. "
        "It is the standard way to show source code, ASCII art, poetry with meaningful spacing, email "
        "messages and terminal output.",
        "Markup inside <pre> is still interpreted, so to show HTML source you must escape < as &lt; and & "
        "as &amp;. For code, wrap the content in <code> inside the <pre>. A line break immediately after "
        "the opening <pre> tag is ignored by the parser, which is convenient for formatting.",
        "Long lines in <pre> do not wrap by default and can overflow the page horizontally; add CSS "
        "overflow-x: auto or white-space: pre-wrap.",
    ],
    syntax="<pre>\n  text with\n    preserved   spacing\n</pre>", void=False, display="block",
    categories="Flow content, palpable content", content="Phrasing content",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLPreElement",
    attrs=[("width", "integer", "Obsolete. Number of characters per line.", "HTML 2.0"),
           ("wrap", "boolean", "Non-standard. Wrap long lines. Use CSS white-space: pre-wrap.", "Netscape")],
    examples=[
        ("Code block", "<pre><code>&lt;footer&gt;\n  &lt;p&gt;&amp;copy; 2026&lt;/p&gt;\n&lt;/footer&gt;</code></pre>", "The entities display as the real characters."),
        ("ASCII art", "<pre>\n  /\\_/\\\n ( o.o )\n  &gt; ^ &lt;\n</pre>", ""),
        ("Scrollable, styled code", "<style>\n  pre { background: #1e1e1e; color: #eee; padding: 16px; border-radius: 8px; overflow-x: auto; tab-size: 2; }\n</style>", ""),
        ("Wrapping long lines", "<pre style=\"white-space: pre-wrap; word-break: break-word\">A very long line ...</pre>", ""),
    ],
    a11y=["For ASCII art or diagrams, add an explanation in text or a figcaption, because screen readers read the characters one by one.", "Use <pre> with <code> so assistive technology knows it is code."],
    mistakes=["Forgetting to escape < and &.", "Indenting the content in the source, which adds unwanted spaces to the output.", "Using <pre> for layout."],
    related=["code", "samp", "kbd", "xmp", "listing", "textarea"], css="pre { display: block; font-family: monospace; white-space: pre; margin: 1em 0; }",
),

dict(
    name="progress", title="Progress indicator", cat="Forms",
    versions="HTML5", status="current",
    desc=[
        "The <progress> element displays the completion progress of a task, such as a file upload, a "
        "download, a multi-step form or a loading operation. It is rendered as a progress bar. With a value "
        "attribute it shows a determinate bar (a known percentage); without value it shows an indeterminate, "
        "animated bar meaning 'working, but I do not know how long it will take'.",
        "Use <meter> instead for a measurement that is not progress (disk space, a score).",
    ],
    syntax="<progress value=\"30\" max=\"100\">30%</progress>", void=False, display="inline-block",
    categories="Flow content, phrasing content, labelable, palpable content", content="Phrasing content, but no <progress> descendants",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLProgressElement",
    attrs=[("value", "number", "How much has been completed, from 0 to max. Omit for an indeterminate bar.", "HTML5"),
           ("max", "number", "The total amount of work. Default 1.", "HTML5")],
    examples=[
        ("Determinate", "<label for=\"up\">Uploading photo</label>\n<progress id=\"up\" value=\"65\" max=\"100\">65%</progress>", ""),
        ("Indeterminate", "<progress>Loading...</progress>", ""),
        ("Updating from JavaScript", "<progress id=\"bar\" max=\"100\" value=\"0\"></progress>\n<script>\n  let v = 0;\n  const t = setInterval(() => {\n    document.getElementById('bar').value = ++v;\n    if (v === 100) clearInterval(t);\n  }, 50);\n</script>", ""),
        ("Styling", "<style>\n  progress { width: 100%; height: 12px; accent-color: #0f8a4c; }\n</style>", "accent-color is the simplest cross-browser way to colour the bar."),
    ],
    a11y=["Label the progress bar.", "Announce completion with a live region or by moving focus; the bar's value changes are not automatically spoken by all screen readers."],
    mistakes=["Using it for static measurements (use <meter>).", "Value greater than max."],
    related=["meter", "output"], css="progress { display: inline-block; appearance: auto; }",
),

dict(
    name="q", title="Inline quotation", cat="Text-level semantics",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <q> element indicates a short inline quotation that sits within a sentence. Browsers "
        "automatically add quotation marks around it, choosing the correct style for the language declared "
        "with lang (curly double quotes in English, guillemets in French, and so on), so you should not "
        "type quotation marks yourself. For long quotations that need their own paragraph use <blockquote>.",
    ],
    syntax="<q cite=\"URL\">quoted words</q>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLQuoteElement",
    attrs=[("cite", "URL", "The source of the quotation. Not displayed.", "HTML 4.01")],
    examples=[
        ("Basic quote", "<p>Tim Berners-Lee said <q>the Web is for everyone</q>.</p>", "Renders as: Tim Berners-Lee said \u201cthe Web is for everyone\u201d."),
        ("Language-aware quotation marks", "<p lang=\"fr\">Il a dit <q>bonjour</q>.</p>", "Renders with \u00ab bonjour \u00bb."),
        ("Custom quote characters", "<style>\n  q { quotes: '\u201e' '\u201c'; }\n</style>", ""),
    ],
    a11y=["Screen readers may or may not announce the quotation; the generated quote marks are usually read."],
    mistakes=["Adding manual quotation marks inside <q>, giving double marks.", "Using <q> for irony or scare quotes."],
    related=["blockquote", "cite"], css="q { display: inline; }\nq::before { content: open-quote; }\nq::after { content: close-quote; }",
),

dict(
    name="rb", title="Ruby base (deprecated)", cat="Text-level semantics (ruby)",
    versions="XHTML 1.1 Ruby, HTML 5.1; removed from the Living Standard", status="deprecated",
    desc=[
        "The <rb> element explicitly marked the base text component of a ruby annotation, the text that "
        "the <rt> annotation is placed above. The Living Standard removed it because the base text can "
        "simply be written directly inside <ruby>. Browsers still support it.",
    ],
    syntax="<ruby><rb>\u6f22</rb><rt>kan</rt></ruby>", void=False, display="ruby-base",
    categories="None", content="Phrasing content", parents="<ruby>", omission="End tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("Old and new", "<!-- With rb -->\n<ruby><rb>\u6771</rb><rt>t\u014d</rt><rb>\u4eac</rb><rt>ky\u014d</rt></ruby>\n\n<!-- Without rb -->\n<ruby>\u6771<rt>t\u014d</rt>\u4eac<rt>ky\u014d</rt></ruby>", "")],
    a11y=[], mistakes=["Relying on it in new markup."], related=["ruby", "rt", "rp", "rtc"], css="rb { display: ruby-base; }",
),

dict(
    name="rp", title="Ruby fallback parenthesis", cat="Text-level semantics (ruby)",
    versions="HTML5", status="current",
    desc=[
        "The <rp> element provides fallback parentheses for browsers that do not support ruby annotations. "
        "Browsers that support ruby hide the <rp> content; older browsers display it, so the annotation "
        "appears in brackets after the base text instead of above it. Place one <rp> before and one after "
        "each <rt>.",
    ],
    syntax="<ruby>\u6f22<rp>(</rp><rt>kan</rt><rp>)</rp></ruby>", void=False, display="none",
    categories="None", content="Text", parents="<ruby>, immediately before or after an <rt>", omission="End tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("With fallback", "<ruby>\u660e\u65e5<rp>(</rp><rt>\u3042\u3057\u305f</rt><rp>)</rp></ruby>", "Modern browsers: annotation above. Old browsers: \u660e\u65e5(\u3042\u3057\u305f).")],
    a11y=[], mistakes=["Omitting rp when supporting very old browsers."], related=["ruby", "rt"], css="rp { display: none; }",
),

dict(
    name="rt", title="Ruby text (annotation)", cat="Text-level semantics (ruby)",
    versions="HTML5", status="current",
    desc=[
        "The <rt> element specifies the ruby text component of a ruby annotation: the small text placed "
        "above (or beside) the base characters to show pronunciation, translation or transliteration. It is "
        "used for East Asian typography (furigana in Japanese, pinyin/zhuyin in Chinese) and increasingly "
        "for other languages. It must be inside a <ruby> element.",
    ],
    syntax="<ruby>base<rt>annotation</rt></ruby>", void=False, display="ruby-text",
    categories="None", content="Phrasing content", parents="<ruby>", omission="End tag may be omitted if followed by <rt> or <rp> or if there is no more content in the parent", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Japanese furigana", "<ruby>\u6f22\u5b57<rt>\u304b\u3093\u3058</rt></ruby>", ""),
        ("Arabic word with transliteration", "<ruby lang=\"ar\">\u0643\u062a\u0627\u0628<rt lang=\"en\">kit\u0101b</rt></ruby>", ""),
        ("Styling", "<style>\n  rt { font-size: 0.6em; color: #666; }\n</style>", ""),
    ],
    a11y=["Screen readers generally read only the base text; use <rt> for supplementary information, not essential content."],
    mistakes=["Using <rt> outside <ruby>."], related=["ruby", "rp", "rb", "rtc"], css="rt { display: ruby-text; font-size: 50%; }",
),

dict(
    name="rtc", title="Ruby text container (deprecated)", cat="Text-level semantics (ruby)",
    versions="HTML 5.1; removed from the Living Standard", status="deprecated",
    desc=[
        "The <rtc> element grouped several <rt> annotations so that a base text could have two layers of "
        "annotation (for example pronunciation above and meaning below). Only Firefox implemented it, and "
        "the Living Standard removed it. Nest two <ruby> elements for double-sided annotations.",
    ],
    syntax="<ruby>base<rtc><rt>a</rt></rtc><rtc><rt>b</rt></rtc></ruby>", void=False, display="ruby-text-container",
    categories="None", content="Phrasing content or <rt>", parents="<ruby>", omission="End tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("Historical", "<ruby>\u65e7\u91d1\u5c71<rtc><rt>ji\u00f9 j\u012bn sh\u0101n</rt></rtc><rtc><rt>San Francisco</rt></rtc></ruby>", "")],
    a11y=[], mistakes=["Relying on it."], related=["ruby", "rt", "rb"], css="rtc { display: ruby-text-container; }",
),

dict(
    name="ruby", title="Ruby annotation", cat="Text-level semantics (ruby)",
    versions="XHTML 1.1 (2001), HTML5", status="current",
    desc=[
        "The <ruby> element represents small annotations rendered above, below or beside base text, most "
        "often used to show the pronunciation of East Asian characters. The name comes from a small "
        "typographic size called 'ruby' used by British printers. The base text is written directly inside "
        "<ruby>, each annotation in an <rt>, and optional fallback parentheses in <rp>.",
    ],
    syntax="<ruby>base<rp>(</rp><rt>annotation</rt><rp>)</rp></ruby>", void=False, display="ruby",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content, <rt>, <rp>",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Furigana over each character", "<ruby>\u6771<rp>(</rp><rt>\u3068\u3046</rt><rp>)</rp>\u4eac<rp>(</rp><rt>\u304d\u3087\u3046</rt><rp>)</rp></ruby>", ""),
        ("Whole word annotation", "<ruby>\u5317\u4eac<rt>B\u011bij\u012bng</rt></ruby>", ""),
        ("Annotation below with CSS", "<style>\n  ruby { ruby-position: under; }\n</style>", ""),
    ],
    a11y=["Do not put essential meaning only in the annotation."], mistakes=["Placing <rt> outside <ruby>.", "Forgetting <rp> if old browser support is needed."],
    related=["rt", "rp", "rb", "rtc"], css="ruby { display: ruby; }",
),

dict(
    name="s", title="Strikethrough (no longer accurate)", cat="Text-level semantics",
    versions="HTML 3.2, HTML 4.01 (deprecated), HTML5 (redefined)", status="current",
    desc=[
        "The <s> element renders text with a line through it and represents content that is no longer "
        "accurate or no longer relevant, such as an old price next to the new one, or a sold-out item. In "
        "HTML 4 it was a purely presentational strike-through synonym for <strike> and was deprecated; HTML5 "
        "gave it this meaning and made it valid again while removing <strike>.",
        "Do not use <s> to indicate document edits; that is what <del> is for.",
    ],
    syntax="<s>outdated text</s>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Old price", "<p>Price: <s>150 EGP</s> <strong>99 EGP</strong></p>", ""),
        ("Sold-out event", "<p><s>Workshop: Saturday 10 am</s> (sold out)</p>", ""),
        ("Accessible old price", "<p>Price: <s><span class=\"sr-only\">Was </span>150 EGP</s> <span class=\"sr-only\">now </span>99 EGP</p>", "Visually hidden words make the meaning clear to screen readers."),
    ],
    a11y=["The strike-through is not announced; add hidden text where the meaning matters."],
    mistakes=["Using <s> for deletions in a revision (use <del>).", "Using <strike>."],
    related=["del", "strike", "u"], css="s { text-decoration: line-through; }",
),

dict(
    name="samp", title="Sample output", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <samp> element marks sample or quoted output from a computer program or system: error "
        "messages, terminal output, log lines. Browsers render it in a monospace font. Nest <kbd> inside "
        "<samp> to show input echoed by the system, and <samp> inside <kbd> for input that names an on-screen item.",
    ],
    syntax="<samp>program output</samp>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Error message", "<p>If the file is missing you will see <samp>404 Not Found</samp>.</p>", ""),
        ("Terminal session", "<pre><samp>$ <kbd>ls</kbd>\nindex.html  style.css\n$ </samp></pre>", ""),
    ],
    a11y=[], mistakes=["Using <code> for output.", "Using <samp> for user input."], related=["code", "kbd", "pre", "var"], css="samp { font-family: monospace; }",
),

dict(
    name="script", title="Script", cat="Scripting",
    versions="HTML 3.2 (reserved), HTML 4.01, HTML5", status="current",
    desc=[
        "The <script> element embeds executable code, almost always JavaScript, or links to an external "
        "script file with the src attribute. It can also hold data blocks (JSON, templates, import maps, "
        "speculation rules) that the browser does not execute when type is set to a non-script MIME type.",
        "By default a script blocks HTML parsing: the browser stops, downloads and runs the script, then "
        "continues. To avoid slowing down the page, put scripts at the end of <body> or, better, in <head> "
        "with the defer attribute (run after parsing, in order) or async (run as soon as downloaded, in any "
        "order). Module scripts (type=\"module\") are deferred automatically and support import/export.",
        "An element with src must be empty; inline code and src cannot be combined. Inside an inline "
        "script the sequence </script> ends the element even inside a string, so write it as '<\\/script>' "
        "in JavaScript strings.",
    ],
    syntax="<script src=\"app.js\" defer></script>\n<script>\n  // inline code\n</script>", void=False, display="none",
    categories="Metadata content, flow content, phrasing content, script-supporting element",
    content="Script code or data, depending on type; nothing if src is present", parents="Any element that accepts metadata or phrasing content",
    omission="Neither tag may be omitted", dom="HTMLScriptElement",
    attrs=[
        ("src", "URL", "External script file.", "HTML 4.01"),
        ("type", "omitted | module | importmap | speculationrules | MIME type", "Omitted or text/javascript: classic script. module: ES module. importmap: JSON import map. Any other type: data block that is not executed.", "HTML 4.01 / HTML5"),
        ("defer", "boolean", "Download in parallel, execute after the document has been parsed, in document order. Only for external classic scripts.", "HTML 4.01"),
        ("async", "boolean", "Download in parallel, execute as soon as ready, possibly out of order. For independent scripts such as analytics.", "HTML5"),
        ("nomodule", "boolean", "Do not run in browsers that support modules; used to provide fallbacks for old browsers.", "HTML5"),
        ("crossorigin", "anonymous | use-credentials", "CORS setting; needed to get full error details from cross-origin scripts.", "HTML5"),
        ("integrity", "hash", "Subresource Integrity hash.", "SRI"),
        ("referrerpolicy", "referrer policy", "Referrer to send.", "HTML5"),
        ("fetchpriority", "high | low | auto", "Download priority hint.", "Living Standard"),
        ("blocking", "render", "Block rendering until the script runs.", "Living Standard"),
        ("nonce", "text", "Cryptographic nonce for Content Security Policy (global attribute).", "CSP"),
        ("attributionsrc", "empty or URL", "Experimental attribution reporting.", "Experimental"),
        ("charset", "encoding", "Obsolete. Encoding of the script; use UTF-8 for everything.", "HTML 4.01"),
        ("language", "text", "Obsolete. Scripting language name. Use type or omit.", "HTML 3.2"),
        ("event, for", "text", "Obsolete. Internet Explorer event binding.", "HTML 4.01"),
    ],
    examples=[
        ("Recommended: deferred external script in head", "<head>\n  <script src=\"app.js\" defer></script>\n</head>", "The script downloads while the HTML parses and runs when the DOM is ready."),
        ("Inline script", "<script>\n  document.querySelector('footer').textContent = '\u00a9 ' + new Date().getFullYear();\n</script>", ""),
        ("ES module", "<script type=\"module\">\n  import { greet } from './greet.js';\n  greet('world');\n</script>", ""),
        ("Async analytics", "<script src=\"https://analytics.example.com/tag.js\" async></script>", ""),
        ("JSON data block", "<script id=\"config\" type=\"application/json\">\n  { \"currency\": \"EGP\", \"vat\": 14 }\n</script>\n<script>\n  const cfg = JSON.parse(document.getElementById('config').textContent);\n</script>", ""),
        ("Structured data for search engines", "<script type=\"application/ld+json\">\n{ \"@context\": \"https://schema.org\", \"@type\": \"Book\", \"name\": \"Learn HTML\" }\n</script>", ""),
        ("Import map", "<script type=\"importmap\">\n{ \"imports\": { \"lodash\": \"https://cdn.example.com/lodash.js\" } }\n</script>", ""),
        ("HTML 4 style with comment hiding (no longer needed)", "<script type=\"text/javascript\">\n<!--\n  alert('old style');\n//-->\n</script>", "The comment trick hid code from 1995 browsers that did not know <script>."),
    ],
    a11y=["Content generated by scripts must be as accessible as static content: manage focus, announce changes with live regions, keep keyboard support."],
    mistakes=["Placing a blocking script in head without defer, so the page appears slowly.", "Running DOM code before the elements exist (fix with defer or DOMContentLoaded).",
              "Writing <script src=\"x.js\" /> (self-closing is not allowed; everything after it becomes script).", "Putting </script> inside a string."],
    related=["noscript", "template", "link", "style"], css="script { display: none; }",
),

dict(
    name="search", title="Search section", cat="Content sectioning",
    versions="Living Standard (2023)", status="current",
    desc=[
        "The <search> element represents a part of the document whose contents are search or filtering "
        "controls: a site search form, a filter panel in a product list, or the controls of a find-in-page "
        "feature. It has no visual effect; it exposes the 'search' landmark to assistive technology. It "
        "replaces the old pattern <form role=\"search\">. The form itself still goes inside it.",
    ],
    syntax="<search>\n  <form>...</form>\n</search>", void=False, display="block",
    categories="Flow content, palpable content", content="Flow content", parents="Any element that accepts flow content",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Site search", "<search>\n  <form action=\"/search\">\n    <label for=\"q\">Search books</label>\n    <input id=\"q\" name=\"q\" type=\"search\">\n    <button>Search</button>\n  </form>\n</search>", ""),
        ("Filter panel", "<search aria-label=\"Filter products\">\n  <label><input type=\"checkbox\" name=\"instock\"> In stock only</label>\n  <label>Max price <input type=\"range\" name=\"max\" min=\"0\" max=\"500\"></label>\n</search>", ""),
    ],
    a11y=["Exposed as the 'search' landmark; screen reader users can jump straight to it.", "In older browsers add role=\"search\" to the <search> element for the same effect."],
    mistakes=["Using <search> for the search results (it is for the controls).", "Nesting several search landmarks without labels."],
    related=["form", "input", "nav"], css="search { display: block; }",
),

dict(
    name="section", title="Generic section", cat="Content sectioning",
    versions="HTML5", status="current",
    desc=[
        "The <section> element represents a generic, thematic grouping of content, typically with a "
        "heading. Examples: the chapters of an article, the tabs of a tabbed interface, the 'Introduction', "
        "'Features' and 'Pricing' areas of a landing page. Each section should be identifiable, usually by "
        "an <h2>-<h6> heading as its first child.",
        "Choosing between the sectioning elements: use <article> if the content is self-contained and "
        "could be syndicated; <nav> for navigation; <aside> for tangential content; <section> when the "
        "content is a distinct part of the page with its own heading; and <div> when the grouping is only "
        "for styling or scripting and has no meaning. A <section> without a heading is usually a sign that "
        "<div> is more appropriate.",
    ],
    syntax="<section>\n  <h2>Heading</h2>\n  ...\n</section>", void=False, display="block",
    categories="Flow content, sectioning content, palpable content", content="Flow content",
    parents="Any element that accepts flow content, but not <address>", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Landing page sections", "<main>\n  <section id=\"features\">\n    <h2>Features</h2>\n    <p>...</p>\n  </section>\n  <section id=\"pricing\">\n    <h2>Pricing</h2>\n    <p>...</p>\n  </section>\n</main>", ""),
        ("Sections inside an article", "<article>\n  <h1>Learn HTML</h1>\n  <section>\n    <h2>Part 1: Tags</h2>\n    <p>...</p>\n  </section>\n  <section>\n    <h2>Part 2: Attributes</h2>\n    <p>...</p>\n  </section>\n</article>", ""),
        ("Labelled section as a region landmark", "<section aria-labelledby=\"faq-h\">\n  <h2 id=\"faq-h\">FAQ</h2>\n  ...\n</section>", "A section with an accessible name is exposed as a 'region' landmark."),
    ],
    a11y=["Sections become 'region' landmarks only when they have an accessible name (aria-labelledby or aria-label).", "Always include a heading."],
    mistakes=["Using <section> as a styling wrapper instead of <div>.", "Sections without headings.", "Assuming <section> resets heading levels (it does not in practice; use the correct h-level)."],
    related=["article", "aside", "nav", "div", "h1", "main"], css="section { display: block; }",
),

dict(
    name="select", title="Drop-down / list box", cat="Forms",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <select> element creates a control for choosing one option (or, with multiple, several) from "
        "a list. It contains <option> elements, optionally grouped in <optgroup>. By default it appears as "
        "a drop-down menu; with the multiple attribute or a size greater than 1 it appears as a scrolling "
        "list box. The name attribute and the value of the chosen option(s) are submitted with the form.",
        "A select is best for lists of roughly 5 to 30 fixed choices. For 2 to 4 choices radio buttons are "
        "easier to see at a glance; for very long lists or free text with suggestions use <input> with a "
        "<datalist>. Newer browsers allow a customisable select (CSS appearance: base-select) with rich "
        "option content.",
    ],
    syntax="<select name=\"n\">\n  <option value=\"1\">One</option>\n</select>", void=False, display="inline-block",
    categories="Flow content, phrasing content, interactive content, listed, labelable, resettable, submittable, form-associated, palpable",
    content="Zero or more <option>, <optgroup>, <hr>, <script>, <template>; optionally a <button> first for customisable selects", parents="Any element that accepts phrasing content",
    omission="Neither tag may be omitted", dom="HTMLSelectElement",
    attrs=[
        ("name", "text", "Name submitted with the form.", "HTML 2.0"),
        ("multiple", "boolean", "Allow several options to be selected (Ctrl/Cmd-click).", "HTML 2.0"),
        ("size", "integer", "Number of visible rows. 1 (default) gives a drop-down; more gives a list box.", "HTML 2.0"),
        ("required", "boolean", "The user must choose an option with a non-empty value.", "HTML5"),
        ("disabled", "boolean", "The control cannot be used.", "HTML 4.01"),
        ("autofocus", "boolean", "Focus on load.", "HTML5"),
        ("autocomplete", "token", "Autofill hint, for example country, cc-exp-month.", "HTML5"),
        ("form", "form id", "Associated form.", "HTML5"),
    ],
    examples=[
        ("Drop-down with placeholder", "<label for=\"pay\">Payment</label>\n<select id=\"pay\" name=\"pay\" required>\n  <option value=\"\">-- Select --</option>\n  <option value=\"cod\">Cash on delivery</option>\n  <option value=\"wallet\">Mobile wallet</option>\n</select>", ""),
        ("Multiple selection list box", "<label for=\"langs\">Languages you read</label>\n<select id=\"langs\" name=\"langs\" multiple size=\"4\">\n  <option>Arabic</option>\n  <option>English</option>\n  <option>French</option>\n  <option>German</option>\n</select>", "Submitted as langs=Arabic&langs=English."),
        ("Reading the value in JavaScript", "<select id=\"s\"><option value=\"a\">A</option><option value=\"b\">B</option></select>\n<script>\n  document.getElementById('s').addEventListener('change', e => console.log(e.target.value));\n</script>", ""),
        ("Basic styling", "<style>\n  select { padding: 8px 12px; border: 1px solid #ccc; border-radius: 6px; font: inherit; }\n</style>", ""),
    ],
    a11y=["Always label the select.", "Do not trigger navigation on change alone; keyboard users change the value with arrow keys and would be redirected before reaching their choice. Provide a Go button.",
          "Multiple selects are hard to use; consider a group of checkboxes."],
    mistakes=["No empty placeholder option with required, so the first real option is submitted silently.", "Using select for 2 choices (use radio buttons).", "Putting HTML inside <option>."],
    related=["option", "optgroup", "datalist", "input", "label"], css="select { display: inline-block; }",
),

dict(
    name="shadow", title="Shadow root insertion point (obsolete)", cat="Obsolete web components",
    versions="Shadow DOM v0; obsolete", status="obsolete",
    desc=[
        "The <shadow> element was part of Shadow DOM v0 and marked where an older shadow root should be "
        "rendered inside a newer one. It was removed with Shadow DOM v1, which does not support multiple "
        "shadow roots per element. Use <slot>.",
    ],
    syntax="<shadow></shadow>", void=False, display="inline", categories="Historical", content="Any", parents="Shadow root", omission="Neither", dom="HTMLUnknownElement",
    attrs=[], examples=[("Replacement", "<slot></slot>", "")], a11y=[], mistakes=["Any use."], related=["slot", "template", "content"], css="",
),

dict(
    name="slot", title="Shadow DOM slot", cat="Web components",
    versions="HTML5 / DOM Standard (2016)", status="current",
    desc=[
        "The <slot> element is a placeholder inside a web component's shadow tree that is filled with "
        "content from the light DOM (the markup written by the user of the component). A named slot "
        "receives children that have a matching slot attribute; the unnamed default slot receives all "
        "other children. Content inside the <slot> element itself is fallback content shown when nothing is "
        "slotted.",
    ],
    syntax="<slot name=\"title\">Default title</slot>", void=False, display="contents",
    categories="Flow content, phrasing content", content="Transparent (fallback content)",
    parents="Any element that accepts phrasing content (inside a shadow tree)", omission="Neither tag may be omitted", dom="HTMLSlotElement",
    attrs=[("name", "text", "The slot's name. Children with slot=\"name\" are placed here. Omit for the default slot.", "DOM")],
    examples=[
        ("A user-card component",
         "<template id=\"card\">\n  <style>.card { border: 1px solid #ccc; padding: 12px; }</style>\n  <div class=\"card\">\n    <h3><slot name=\"name\">Anonymous</slot></h3>\n    <p><slot>No description</slot></p>\n  </div>\n</template>\n\n"
         "<user-card>\n  <span slot=\"name\">Ahmed</span>\n  Front-end developer from Giza.\n</user-card>\n\n"
         "<script>\n  customElements.define('user-card', class extends HTMLElement {\n    constructor() {\n      super();\n      this.attachShadow({ mode: 'open' }).append(document.getElementById('card').content.cloneNode(true));\n    }\n  });\n</script>", ""),
        ("Styling slotted content", "<style>\n  ::slotted(span) { color: #b90000; }\n</style>", ""),
    ],
    a11y=["Slotted content keeps its own semantics; the shadow boundary is transparent to the accessibility tree."],
    mistakes=["Using <slot> outside a shadow root (it does nothing).", "Slot attribute on a nested descendant rather than a direct child of the host."],
    related=["template", "content", "shadow"], css="slot { display: contents; }",
),

dict(
    name="small", title="Side comment (fine print)", cat="Text-level semantics",
    versions="HTML 3.2, HTML 4.01, HTML5 (redefined)", status="current",
    desc=[
        "The <small> element represents side comments and small print: disclaimers, caveats, legal "
        "restrictions, copyright notices, attribution. It renders the text one size smaller. In HTML 3.2 and "
        "4 it was purely presentational ('smaller text'); HTML5 kept it and gave it this meaning, while its "
        "counterpart <big> was removed.",
        "<small> does not reduce the importance of text. It is intended for short runs of inline text, not "
        "for whole sections; for that, use CSS font-size.",
    ],
    syntax="<small>fine print</small>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Copyright in the footer", "<footer>\n  <p><small>&copy; 2026 Book Store. All rights reserved.</small></p>\n</footer>", ""),
        ("Price disclaimer", "<p>From 99 EGP <small>(excluding delivery)</small></p>", ""),
    ],
    a11y=["No special announcement; the meaning is visual and semantic only."],
    mistakes=["Wrapping entire paragraphs or sections in <small> for font size.", "Using <small> for sub-headings."],
    related=["big", "sub", "sup", "footer"], css="small { font-size: smaller; }",
),

dict(
    name="source", title="Media or image source", cat="Image and multimedia",
    versions="HTML5", status="current",
    desc=[
        "The <source> element specifies one of several alternative resources for a <picture>, <audio> or "
        "<video> element. It is a void element. The browser examines the sources in order and uses the first "
        "one it can display: for <picture> it checks the media query and image type, for <audio>/<video> it "
        "checks the type (MIME type and codecs). Because it is used inside three different parents, the set "
        "of relevant attributes differs: <picture> uses srcset, sizes, media, type, width and height; media "
        "elements use src, type and (for video) media.",
    ],
    syntax="<source src=\"file\" type=\"MIME\">  <!-- in audio/video -->\n<source srcset=\"file\" type=\"MIME\" media=\"query\">  <!-- in picture -->", void=True, display="none",
    categories="None", content="None (void element)", parents="<picture> (before the <img>), <audio>, <video> (before any <track> or flow content)",
    omission="No end tag", dom="HTMLSourceElement",
    attrs=[
        ("src", "URL", "The media file. Required in <audio>/<video>; ignored in <picture>.", "HTML5"),
        ("srcset", "candidate list", "Image candidates. Required in <picture>; ignored in media elements.", "HTML5"),
        ("sizes", "size list", "Display widths for width-descriptor srcset (picture only).", "HTML5"),
        ("type", "MIME type, optionally with codecs", "The resource type, for example image/webp, video/mp4, video/webm; codecs=\"vp9, opus\". Lets the browser skip unsupported files without downloading them.", "HTML5"),
        ("media", "media query", "Use this source only when the query matches. Valid in picture and video (audio ignores it in most browsers).", "HTML5"),
        ("width / height", "pixels", "Intrinsic size of the image candidate (picture only).", "Living Standard"),
    ],
    examples=[
        ("Video with two formats", "<video controls width=\"640\" height=\"360\">\n  <source src=\"clip.webm\" type=\"video/webm\">\n  <source src=\"clip.mp4\" type=\"video/mp4\">\n  <p>Download the <a href=\"clip.mp4\">video</a>.</p>\n</video>", ""),
        ("Picture with format and size choice", "<picture>\n  <source srcset=\"img.avif\" type=\"image/avif\">\n  <source srcset=\"img.webp\" type=\"image/webp\">\n  <img src=\"img.jpg\" alt=\"...\" width=\"800\" height=\"600\">\n</picture>", ""),
        ("Different video for small screens", "<video controls>\n  <source src=\"small.mp4\" type=\"video/mp4\" media=\"(max-width: 600px)\">\n  <source src=\"large.mp4\" type=\"video/mp4\">\n</video>", ""),
    ],
    a11y=["Accessibility attributes (alt, captions) go on the <img>, <video> or <track>, not on <source>."],
    mistakes=["Using src inside <picture> (must be srcset).", "Placing <source> after the <img> or after <track>.", "Omitting type, forcing the browser to download files to test them."],
    related=["picture", "audio", "video", "img", "track"], css="source { display: none; }",
),

dict(
    name="spacer", title="Spacer (non-standard, obsolete)", cat="Obsolete presentational",
    versions="Netscape 3-4 only", status="obsolete",
    desc=[
        "The <spacer> element inserted empty horizontal or vertical space, imitating the invisible 'spacer "
        "GIF' images used for layout in the 1990s. It existed only in Netscape and was never standardised. "
        "Use CSS margin, padding or gap.",
    ],
    syntax="<spacer type=\"horizontal\" size=\"20\">", void=True, display="none",
    categories="Historical", content="None", parents="Any", omission="No end tag", dom="HTMLUnknownElement",
    attrs=[("type", "horizontal | vertical | block", "Kind of space.", "Netscape"), ("size", "pixels", "Amount of space.", "Netscape"), ("width / height / align", "-", "For type=block.", "Netscape")],
    examples=[("CSS replacement", "<div style=\"margin-top: 20px\">...</div>", "")],
    a11y=[], mistakes=["Any use."], related=["br", "hr"], css="",
),

dict(
    name="span", title="Generic inline container", cat="Text-level semantics",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <span> element is a generic inline container for phrasing content. Like <div>, it has no "
        "meaning of its own and no visual effect; it exists to be a hook for CSS (via class or id) or "
        "JavaScript, or to carry attributes such as lang or dir on a part of a sentence. It should be used "
        "only when no other element is more appropriate: <em>, <strong>, <mark>, <time>, <abbr>, <code> and "
        "the other text-level elements all carry meaning that <span> does not.",
        "<span> is inline: it does not start a new line and it takes only as much width as its content. "
        "<div> is its block-level counterpart.",
    ],
    syntax="<span class=\"name\">text</span>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLSpanElement",
    attrs=[],
    examples=[
        ("Styling part of a sentence", "<style>\n  .price { color: #e60000; font-weight: bold; }\n</style>\n<p>The price is <span class=\"price\">50 EGP</span> only.</p>", "Only '50 EGP' turns red; the sentence stays on one line."),
        ("Marking a language change", "<p>The Arabic word for book is <span lang=\"ar\">\u0643\u062a\u0627\u0628</span>.</p>", ""),
        ("A hook for JavaScript", "<p>Items in cart: <span id=\"count\">0</span></p>\n<script>document.getElementById('count').textContent = 3;</script>", ""),
        ("Visually hidden text for screen readers", "<style>\n  .sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }\n</style>\n<button>\u00d7<span class=\"sr-only\">Close</span></button>", ""),
    ],
    a11y=["A span has no role; never make it clickable without adding role=\"button\", tabindex=\"0\" and keyboard handlers, and even then a real <button> is better."],
    mistakes=["Using <span> where <em>, <strong> or another semantic element fits.", "Putting block elements inside a span.", "Using <span> as a button."],
    related=["div", "em", "strong", "mark", "b", "i"], css="span { display: inline; }",
),

dict(
    name="strike", title="Strikethrough (obsolete)", cat="Obsolete presentational",
    versions="HTML 3.2, HTML 4.01 (deprecated); obsolete in HTML5", status="obsolete",
    desc=[
        "The <strike> element drew a line through its text. It was purely presentational, was deprecated in "
        "HTML 4.01 and removed in HTML5. Use <del> for removed content, <s> for content that is no longer "
        "accurate, or CSS text-decoration: line-through for pure styling.",
    ],
    syntax="<strike>text</strike>", void=False, display="inline",
    categories="Historical", content="Phrasing content", parents="Phrasing content", omission="Neither", dom="HTMLElement",
    attrs=[],
    examples=[("Replacements", "<!-- Old -->\n<strike>150 EGP</strike>\n\n<!-- New: no longer accurate -->\n<s>150 EGP</s>\n\n<!-- New: edit tracking -->\n<del>150 EGP</del>", "")],
    a11y=[], mistakes=["Any use."], related=["s", "del"], css="strike { text-decoration: line-through; }",
),

dict(
    name="strong", title="Strong importance", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <strong> element indicates that its content has strong importance, seriousness or urgency: a "
        "warning, a key instruction, the most important part of a sentence. Browsers render it in bold. "
        "Nesting <strong> inside <strong> increases the importance further.",
        "In HTML 4 the guidance was 'use <strong> instead of <b>'; HTML5 refined it. <strong> = important; "
        "<b> = draw attention without importance (keywords); <em> = spoken stress that changes meaning; "
        "<mark> = relevance to the reader's current task. A whole paragraph of <strong> text signals nothing "
        "because nothing stands out.",
    ],
    syntax="<strong>important text</strong>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Warning", "<p><strong>Warning:</strong> unplug the device before opening it.</p>", ""),
        ("Key instruction in a list", "<ul>\n  <li>Save the file as <strong>index.html</strong>.</li>\n  <li>Open it in a browser.</li>\n</ul>", ""),
        ("strong versus em", "<p><strong>Do not</strong> touch the wire. I said <em>do not</em>.</p>", "The first is a serious instruction; the second stresses the words."),
    ],
    a11y=["Most screen readers do not announce <strong> by default, but it is the correct semantic element and some users enable emphasis announcements."],
    mistakes=["Using <strong> just for bold styling.", "Using <strong> for headings.", "Wrapping large blocks in <strong>."],
    related=["b", "em", "mark", "i"], css="strong { font-weight: bold; }",
),

dict(
    name="style", title="Embedded style sheet", cat="Document metadata",
    versions="HTML 3.2 (reserved), HTML 4.01, HTML5", status="current",
    desc=[
        "The <style> element contains CSS rules that apply to the document. It belongs in <head>, though "
        "browsers tolerate it in <body>. A document may have any number of <style> elements; they are "
        "applied in order together with any linked style sheets. For anything larger than a few rules, an "
        "external file loaded with <link rel=\"stylesheet\"> is better because it can be cached and shared "
        "between pages.",
        "The media attribute restricts the rules to certain devices or conditions. The content is raw text: "
        "the sequence </style> ends the element, and HTML entities are not decoded inside it.",
    ],
    syntax="<style>\n  selector { property: value; }\n</style>", void=False, display="none",
    categories="Metadata content", content="CSS text", parents="<head>; also <noscript> in head; tolerated in <body>",
    omission="Neither tag may be omitted", dom="HTMLStyleElement",
    attrs=[
        ("media", "media query", "Apply only when the query matches, for example print or (max-width: 600px). Default all.", "HTML 4.01"),
        ("blocking", "render", "Block rendering until the style sheet is applied (it does anyway for inline styles).", "Living Standard"),
        ("nonce", "text", "CSP nonce (global).", "CSP"),
        ("title", "text", "Name of an alternate style sheet set.", "HTML 4.01"),
        ("type", "text/css", "Obsolete. The only allowed value is text/css; omit it.", "HTML 4.01"),
        ("scoped", "boolean", "Removed. Was meant to scope styles to the parent element; use Shadow DOM or @scope.", "HTML5 draft (removed)"),
    ],
    examples=[
        ("Basic page styles", "<head>\n  <style>\n    body   { font-family: Arial, sans-serif; margin: 0; }\n    footer { text-align: center; color: gray; padding: 20px; }\n  </style>\n</head>", ""),
        ("Print-only rules", "<style media=\"print\">\n  nav, footer { display: none; }\n  a::after { content: ' (' attr(href) ')'; }\n</style>", ""),
        ("Dark mode", "<style>\n  @media (prefers-color-scheme: dark) {\n    body { background: #111; color: #eee; }\n  }\n</style>", ""),
    ],
    a11y=["Do not use CSS to hide content that screen readers need; display: none hides it from everyone."],
    mistakes=["Putting CSS in <style> without the tags, or putting HTML inside <style>.", "Typing </style> inside a CSS string.", "Writing type=\"text/css\" (harmless but unnecessary)."],
    related=["link", "head", "script"], css="style { display: none; }",
),

dict(
    name="sub", title="Subscript", cat="Text-level semantics",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <sub> element renders text as a subscript: smaller and below the baseline. Use it only where "
        "the subscript has a typographic meaning, such as chemical formulas (H\u2082O), mathematical variable "
        "indices (x\u2081) or footnote markers in some styles. For purely visual lowering, use CSS vertical-align.",
    ],
    syntax="H<sub>2</sub>O", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("Chemistry", "<p>Water is H<sub>2</sub>O and carbon dioxide is CO<sub>2</sub>.</p>", ""),
              ("Maths", "<p>The sequence a<sub>1</sub>, a<sub>2</sub>, ... a<sub>n</sub>.</p>", "")],
    a11y=["Not announced; for critical meaning consider MathML."], mistakes=["Using sub/sup for layout tweaks."],
    related=["sup", "math"], css="sub { vertical-align: sub; font-size: smaller; }",
),

dict(
    name="summary", title="Disclosure summary", cat="Interactive elements",
    versions="HTML5 (5.1)", status="current",
    desc=[
        "The <summary> element specifies the visible heading, label or caption of a <details> element. "
        "Clicking it (or pressing Enter/Space when it is focused) toggles the details open and closed. It "
        "must be the first child of <details>. Browsers show a small triangle marker before it, which can "
        "be styled or removed with the ::marker pseudo-element or list-style: none.",
    ],
    syntax="<details>\n  <summary>Label</summary>\n  ...\n</details>", void=False, display="list-item",
    categories="None", content="Phrasing content, or one heading element", parents="<details>, as its first child",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("FAQ", "<details>\n  <summary>What is a footer?</summary>\n  <p>The bottom section of a page or section.</p>\n</details>", ""),
        ("Heading inside summary", "<details>\n  <summary><h3>Shipping</h3></summary>\n  <p>2-4 days.</p>\n</details>", "Keeps the document outline; style the h3 with display: inline."),
        ("Custom marker", "<style>\n  summary { list-style: none; cursor: pointer; }\n  summary::before { content: '+ '; }\n  details[open] summary::before { content: '- '; }\n</style>", ""),
    ],
    a11y=["Announced as a button with expanded/collapsed state.", "Do not put links or buttons inside summary; nested interactive elements confuse users."],
    mistakes=["Placing summary anywhere but first.", "Using summary outside details."],
    related=["details"], css="summary { display: list-item; counter-increment: list-item 0; list-style: disclosure-closed inside; }\ndetails[open] > summary { list-style-type: disclosure-open; }",
),

dict(
    name="sup", title="Superscript", cat="Text-level semantics",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <sup> element renders text as a superscript: smaller and above the baseline. Use it where the "
        "superscript has meaning: exponents (x\u00b2), ordinal suffixes (1<sup>st</sup>), footnote references, "
        "and abbreviations like M<sup>lle</sup>. For visual raising only, use CSS.",
    ],
    syntax="x<sup>2</sup>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("Exponent", "<p>The area is 5<sup>2</sup> = 25 m<sup>2</sup>.</p>", ""),
              ("Footnote reference", "<p>HTML was created in 1991.<sup><a href=\"#fn1\" id=\"ref1\">[1]</a></sup></p>", ""),
              ("Preventing line-height changes", "<style>\n  sup, sub { line-height: 0; }\n</style>", "Superscripts can push lines apart; zero line-height fixes it.")],
    a11y=["Not announced; complex maths should use MathML."], mistakes=["Using sup for trademark symbols where the \u2122 character already is superscript."],
    related=["sub", "math"], css="sup { vertical-align: super; font-size: smaller; }",
),

dict(
    name="svg", title="Scalable Vector Graphics root", cat="Embedded content (SVG)",
    versions="HTML5 (inline SVG)", status="current",
    desc=[
        "The <svg> element is the root of an inline SVG (Scalable Vector Graphics) image written directly "
        "in the HTML. SVG describes shapes with elements such as <circle>, <rect>, <line>, <path>, <text> "
        "and <g>, which scale to any size without losing sharpness, can be styled with CSS and animated "
        "with CSS or JavaScript. Inline SVG is ideal for icons, logos, charts and diagrams. SVG files can "
        "also be used through <img src=\"x.svg\">, but then CSS from the page cannot style their insides.",
        "The viewBox attribute defines the internal coordinate system; width and height (or CSS) define the "
        "displayed size. This book documents SVG only at the level of the <svg> root; SVG has its own large "
        "specification.",
    ],
    syntax="<svg viewBox=\"0 0 100 100\" width=\"100\" height=\"100\">\n  <circle cx=\"50\" cy=\"50\" r=\"40\"/>\n</svg>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content, palpable content", content="SVG elements",
    parents="Any element that accepts phrasing content", omission="Neither", dom="SVGSVGElement",
    attrs=[
        ("viewBox", "min-x min-y width height", "The internal coordinate system; makes the graphic scalable.", "SVG"),
        ("width / height", "length", "Displayed size.", "SVG"),
        ("preserveAspectRatio", "keyword", "How to fit the viewBox into the viewport.", "SVG"),
        ("xmlns", "http://www.w3.org/2000/svg", "Namespace; optional in HTML, required in standalone .svg files.", "SVG"),
        ("fill, stroke, stroke-width", "colour / length", "Presentation attributes for shapes (can also be CSS).", "SVG"),
        ("role, aria-label, aria-labelledby", "-", "Accessibility name and role for the graphic.", "ARIA"),
    ],
    examples=[
        ("Icon", "<svg viewBox=\"0 0 24 24\" width=\"24\" height=\"24\" aria-hidden=\"true\" focusable=\"false\">\n  <path d=\"M12 2L2 7l10 5 10-5-10-5z\" fill=\"currentColor\"/>\n</svg>", "currentColor makes the icon follow the text colour."),
        ("Accessible logo", "<svg viewBox=\"0 0 200 60\" width=\"200\" height=\"60\" role=\"img\" aria-labelledby=\"t\">\n  <title id=\"t\">Book Store</title>\n  <rect width=\"200\" height=\"60\" rx=\"8\" fill=\"#e60000\"/>\n  <text x=\"100\" y=\"38\" text-anchor=\"middle\" fill=\"#fff\" font-size=\"24\">Book Store</text>\n</svg>", ""),
        ("Responsive SVG", "<style>\n  svg { width: 100%; height: auto; }\n</style>", ""),
    ],
    a11y=["Decorative SVG: aria-hidden=\"true\". Meaningful SVG: role=\"img\" with <title> and aria-labelledby.", "Text in SVG <text> is real text and is readable, unlike text in raster images."],
    mistakes=["Omitting viewBox so the graphic does not scale.", "Forgetting focusable=\"false\" for inline icons in old Internet Explorer.", "Huge inline SVGs repeated many times; use <use> or an external sprite."],
    related=["img", "canvas", "math", "picture"], css="svg:not(:root) { overflow: hidden; }",
),

]
