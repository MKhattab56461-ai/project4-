# -*- coding: utf-8 -*-
"""Element reference entries, letters E to H."""

ELEMENTS = [

dict(
    name="em", title="Emphasis", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <em> element marks text that has stress emphasis: the word or phrase you would say more "
        "forcefully if you were reading the sentence aloud. Changing which word is emphasised changes the "
        "meaning of the sentence. Browsers render it in italics.",
        "<em> is not the same as <i>. <i> marks text in an alternative voice or mood (a technical term, a "
        "foreign phrase, a ship name) without emphasis. And it is not the same as <strong>, which marks "
        "importance, seriousness or urgency rather than spoken stress. Nested <em> elements indicate a "
        "greater degree of emphasis.",
        "If you only want italic text for visual reasons, with no emphasis intended, use CSS font-style: "
        "italic on a <span> instead.",
    ],
    syntax="<em>text</em>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Emphasis changes meaning",
         "<p><em>I</em> did not say he stole the money.</p>\n<p>I did not say he <em>stole</em> the money.</p>\n<p>I did not say he stole <em>the money</em>.</p>",
         "Each sentence has the same words but a different meaning because of where the stress falls."),
        ("em, i and strong compared",
         "<p>You <em>must</em> read the <i>Odyssey</i>. <strong>Warning:</strong> it is long.</p>", ""),
    ],
    a11y=["Some screen readers change voice pitch for <em>; most do not by default, so do not rely on it to carry critical meaning."],
    mistakes=["Using <em> for every italic, such as book titles (<cite>) or foreign words (<i>).", "Using <em> for whole paragraphs."],
    related=["strong", "i", "b", "mark", "cite"],
    css="em { font-style: italic; }",
),

dict(
    name="embed", title="External content", cat="Embedded content",
    versions="Netscape extension (1995), standardised in HTML5", status="current",
    desc=[
        "The <embed> element embeds external content at a specified point in the document. The content is "
        "provided by an external application or plug-in, or is a natively supported type such as an image, "
        "video, PDF or HTML page. It is a void element with no fallback content.",
        "It was a Netscape invention widely used for Flash movies and was finally standardised in HTML5. "
        "Today, for video use <video>, for audio use <audio>, for other pages use <iframe>, and for "
        "PDFs <iframe> or <object> are more flexible because they allow fallback content.",
    ],
    syntax="<embed src=\"file.pdf\" type=\"application/pdf\" width=\"600\" height=\"400\">", void=True, display="inline",
    categories="Flow content, phrasing content, embedded content, interactive content, palpable content",
    content="None (void element)", parents="Any element that accepts embedded content", omission="No end tag", dom="HTMLEmbedElement",
    attrs=[
        ("src", "URL", "The URL of the resource.", "Netscape / HTML5"),
        ("type", "MIME type", "The type of the resource, used to choose the plug-in or handler.", "Netscape / HTML5"),
        ("width", "pixels", "Width of the display area.", "Netscape / HTML5"),
        ("height", "pixels", "Height of the display area.", "Netscape / HTML5"),
        ("Any other attribute", "text", "Additional attributes are passed to the plug-in as parameters (for example, old Flash used quality, wmode, allowfullscreen).", "Netscape"),
    ],
    examples=[
        ("Embedding a PDF", "<embed src=\"guide.pdf\" type=\"application/pdf\" width=\"100%\" height=\"600\">", ""),
        ("Embedding a video (prefer <video>)", "<embed src=\"clip.mp4\" type=\"video/mp4\" width=\"640\" height=\"360\">", ""),
    ],
    a11y=["There is no fallback content and no accessible name; add a title attribute and provide a link to the resource next to it."],
    mistakes=["Using <embed> for video or audio.", "Writing a closing tag."],
    related=["object", "iframe", "video", "audio", "picture"], css="embed { display: inline; }",
),

dict(
    name="fencedframe", title="Fenced frame (experimental)", cat="Embedded content",
    versions="Experimental (Chromium, 2024)", status="experimental",
    desc=[
        "The <fencedframe> element embeds another HTML page in a way that is even more isolated than an "
        "<iframe>: the embedded page cannot communicate with the embedding page, and the URL is chosen "
        "through privacy-preserving APIs rather than given directly. It is part of the Privacy Sandbox "
        "proposals for showing personalised advertisements without cross-site tracking. It is not yet a "
        "standard and is only available in Chromium browsers.",
    ],
    syntax="<fencedframe width=\"300\" height=\"250\"></fencedframe>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content, interactive content, palpable content",
    content="None", parents="Any element that accepts embedded content", omission="Neither", dom="HTMLFencedFrameElement",
    attrs=[("allow", "permissions policy", "Features allowed inside the frame.", "Experimental"),
           ("width / height", "pixels", "Size of the frame.", "Experimental")],
    examples=[("Configured from JavaScript", "<fencedframe id=\"ad\"></fencedframe>\n<script>\n  // config comes from an API such as Protected Audience\n  // document.getElementById('ad').config = config;\n</script>", "")],
    a11y=["Same considerations as <iframe>."], mistakes=["Using it in production sites today."], related=["iframe"], css="",
),

dict(
    name="fieldset", title="Form field group", cat="Forms",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <fieldset> element groups related controls and labels inside a form, for example all the "
        "fields of a postal address, or a set of radio buttons that answer one question. The optional "
        "<legend> element, which must be the first child, gives the group a caption. Browsers draw a border "
        "around the group with the legend placed on the border.",
        "Setting disabled on a fieldset disables every control inside it at once, which is convenient for "
        "showing or hiding optional sections of a form.",
    ],
    syntax="<fieldset>\n  <legend>Caption</legend>\n  ...controls...\n</fieldset>", void=False, display="block",
    categories="Flow content, sectioning root, listed, form-associated, palpable content",
    content="An optional <legend> followed by flow content", parents="Any element that accepts flow content",
    omission="Neither tag may be omitted", dom="HTMLFieldSetElement",
    attrs=[
        ("disabled", "boolean", "Disables all descendant form controls (except those inside the <legend>).", "HTML 4.01"),
        ("form", "form id", "Associates the fieldset with a form elsewhere in the document.", "HTML5"),
        ("name", "text", "The name of the group, accessible from the form's elements collection.", "HTML5"),
    ],
    examples=[
        ("Radio button group",
         "<fieldset>\n  <legend>Payment method</legend>\n  <label><input type=\"radio\" name=\"pay\" value=\"cash\" checked> Cash on delivery</label><br>\n"
         "  <label><input type=\"radio\" name=\"pay\" value=\"wallet\"> Mobile wallet</label><br>\n  <label><input type=\"radio\" name=\"pay\" value=\"card\"> Card</label>\n</fieldset>", ""),
        ("Disabling a whole section",
         "<fieldset disabled>\n  <legend>Shipping address (same as billing)</legend>\n  <input name=\"street\" placeholder=\"Street\">\n  <input name=\"city\" placeholder=\"City\">\n</fieldset>", ""),
        ("Removing the default border", "<style>\n  fieldset { border: none; padding: 0; margin: 0 0 1em; }\n  legend { font-weight: bold; padding: 0; }\n</style>", ""),
    ],
    a11y=["A fieldset with a legend is the standard, well-supported way to give a group of radio buttons or checkboxes a shared accessible name.",
          "Screen readers announce the legend when the user enters the group."],
    mistakes=["Using a heading instead of <legend> (the heading is not linked to the group).", "Nesting fieldsets too deeply.",
              "Forgetting that fieldset is display: block and has odd default styling that is hard to override (for example, it ignores display: flex in some browsers)."],
    related=["legend", "form", "input", "label"], css="fieldset { display: block; margin-inline: 2px; padding: 0.35em 0.75em 0.625em; border: 2px groove; min-inline-size: min-content; }",
),

dict(
    name="figcaption", title="Figure caption", cat="Text content",
    versions="HTML5", status="current",
    desc=[
        "The <figcaption> element provides a caption or legend for the content of its parent <figure> "
        "element. It must be either the first or the last child of the <figure>. The caption is "
        "programmatically associated with the figure, which gives the figure an accessible name.",
    ],
    syntax="<figure>\n  <img ...>\n  <figcaption>Caption</figcaption>\n</figure>", void=False, display="block",
    categories="None", content="Flow content", parents="<figure>, as its first or last child",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Image with caption", "<figure>\n  <img src=\"pyramids.jpg\" alt=\"The three pyramids of Giza at sunset\">\n  <figcaption>Figure 1: The Giza pyramids, photographed in 2026.</figcaption>\n</figure>", ""),
        ("Caption first", "<figure>\n  <figcaption>Listing 2: A minimal page</figcaption>\n  <pre><code>&lt;!DOCTYPE html&gt;...</code></pre>\n</figure>", ""),
    ],
    a11y=["The caption becomes the figure's accessible name. The image's alt should describe the image; the caption should not merely repeat it."],
    mistakes=["Placing figcaption in the middle of the figure.", "Using figcaption outside a figure."],
    related=["figure", "caption", "img"], css="figcaption { display: block; }",
),

dict(
    name="figure", title="Figure with optional caption", cat="Text content",
    versions="HTML5", status="current",
    desc=[
        "The <figure> element represents self-contained content that is referenced from the main flow but "
        "could be moved elsewhere (to an appendix, a sidebar or another page) without affecting the meaning "
        "of the text: an illustration, a diagram, a photo, a code listing, a chart, a poem, a table. An "
        "optional <figcaption> gives it a caption.",
        "A figure is not only for images. The key idea is that the content is a unit that the text refers "
        "to ('see Figure 3'). Purely decorative images are not figures.",
    ],
    syntax="<figure>\n  content\n  <figcaption>Caption</figcaption>\n</figure>", void=False, display="block",
    categories="Flow content, sectioning root, palpable content",
    content="A <figcaption> followed by flow content, or flow content followed by a <figcaption>, or flow content alone",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Photo", "<figure>\n  <img src=\"nile.jpg\" alt=\"Boats on the Nile at Luxor\" width=\"600\" height=\"400\">\n  <figcaption>Feluccas on the Nile.</figcaption>\n</figure>", ""),
        ("Code listing", "<figure>\n  <pre><code>footer { text-align: center; }</code></pre>\n  <figcaption>Centring the footer text.</figcaption>\n</figure>", ""),
        ("Multiple images in one figure", "<figure>\n  <img src=\"before.jpg\" alt=\"Room before painting\">\n  <img src=\"after.jpg\" alt=\"Room after painting, walls now light blue\">\n  <figcaption>Before and after.</figcaption>\n</figure>", ""),
        ("Removing default margins", "<style>\n  figure { margin: 0; }\n  figure img { max-width: 100%; height: auto; }\n</style>", ""),
    ],
    a11y=["Exposed with the 'figure' role; the figcaption labels it."],
    mistakes=["Wrapping every image in a figure regardless of meaning.", "Forgetting that browsers add a 40px left and right margin by default."],
    related=["figcaption", "img", "picture", "table"], css="figure { display: block; margin: 1em 40px; }",
),

dict(
    name="font", title="Font (obsolete)", cat="Obsolete presentational",
    versions="HTML 3.2, HTML 4.01 (deprecated); obsolete in HTML5", status="obsolete",
    desc=[
        "The <font> element set the size, colour and typeface of its text. It was the main way to style text "
        "before CSS, was deprecated in HTML 4.01 and removed in HTML5. Browsers still render it for old pages. "
        "Every use of <font> can be replaced by CSS: font-size, color and font-family.",
        "The size attribute used a scale from 1 to 7 where 3 was the default; relative values such as +1 or "
        "-2 were also allowed.",
    ],
    syntax="<font size=\"4\" color=\"red\" face=\"Arial\">text</font>", void=False, display="inline",
    categories="Phrasing content (historical)", content="Phrasing content", parents="Any element that accepts phrasing content",
    omission="Neither tag may be omitted", dom="HTMLFontElement",
    attrs=[
        ("size", "1-7 or +n / -n", "Font size on the HTML scale: 1 = x-small, 2 = small, 3 = medium (default), 4 = large, 5 = x-large, 6 = xx-large, 7 = xxx-large.", "HTML 3.2"),
        ("color", "colour name or #rrggbb", "Text colour.", "HTML 3.2"),
        ("face", "comma-separated font names", "Typeface, tried in order.", "HTML 3.2"),
    ],
    examples=[("Replacement", "<!-- Old -->\n<font face=\"Arial\" size=\"5\" color=\"#e60000\">Sale!</font>\n\n<!-- New -->\n<span style=\"font-family: Arial, sans-serif; font-size: x-large; color: #e60000\">Sale!</span>", "")],
    a11y=["Fixed font sizes set with <font> ignore user preferences."], mistakes=["Any use in new pages."],
    related=["basefont", "span"], css="",
),

dict(
    name="footer", title="Footer", cat="Content sectioning",
    versions="HTML5", status="current",
    desc=[
        "The <footer> element represents the footer of its nearest ancestor sectioning content or "
        "sectioning root: the page (<body>), an <article>, a <section>, an <aside> or a <nav>. A footer "
        "typically contains information about the section it belongs to: who wrote it, copyright data, "
        "links to related documents, contact details, a site map, or navigation back to the top.",
        "The most common use is the page footer at the bottom of <body>, but you can have as many footers "
        "as you have sections. A footer inside an <article> gives the article's metadata (author, date, "
        "tags); a footer inside a <blockquote> gives the source of the quotation.",
        "Visually, a <footer> is nothing more than a block like a <div>. Its value is semantic: it tells "
        "browsers, assistive technology and search engines what the content is. When a footer is a direct "
        "child of <body> it is exposed as a 'contentinfo' landmark that screen reader users can jump to. "
        "Contact information inside a footer should be wrapped in <address>. A footer may not contain "
        "another <footer> or a <header>.",
    ],
    syntax="<footer>...</footer>", void=False, display="block",
    categories="Flow content, palpable content",
    content="Flow content, but no <footer> or <header> descendants", parents="Any element that accepts flow content, but not <address>",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Page footer",
         "<body>\n  <header><h1>My Blog</h1></header>\n  <main>\n    <p>Today I learned <em>a lot</em> about HTML.</p>\n  </main>\n"
         "  <footer>\n    <p>&copy; 2026 My Blog. All rights reserved.</p>\n    <nav>\n      <a href=\"about.html\">About</a> |\n      <a href=\"privacy.html\">Privacy</a> |\n      <a href=\"#top\">Back to top</a>\n    </nav>\n"
         "    <address>Contact: <a href=\"mailto:me@example.com\">me@example.com</a></address>\n  </footer>\n</body>", ""),
        ("Styling a footer with CSS",
         "<style>\n  footer {\n    background-color: #222;\n    color: #fff;\n    text-align: center;\n    padding: 20px;\n    font-family: Arial, sans-serif;\n  }\n  footer a { color: #ffd166; }\n</style>",
         "font-family sets the letter style for all text in the footer; text-align centres it."),
        ("Article footer with metadata",
         "<article>\n  <h2>Learning the footer element</h2>\n  <p>...</p>\n  <footer>\n    <p>Posted by Ahmed on <time datetime=\"2026-09-11\">11 September 2026</time></p>\n    <p>Tags: html, semantics</p>\n  </footer>\n</article>", ""),
        ("Multi-column site footer",
         "<style>\n  .cols { display: flex; flex-wrap: wrap; gap: 32px; justify-content: center; }\n</style>\n<footer>\n  <div class=\"cols\">\n"
         "    <section>\n      <h3>Shop</h3>\n      <ul><li><a href=\"/books\">Books</a></li><li><a href=\"/deals\">Deals</a></li></ul>\n    </section>\n"
         "    <section>\n      <h3>Help</h3>\n      <ul><li><a href=\"/faq\">FAQ</a></li><li><a href=\"/returns\">Returns</a></li></ul>\n    </section>\n"
         "  </div>\n  <p>&copy; 2026 Book Store</p>\n</footer>", ""),
        ("Sticky footer at the bottom of short pages",
         "<style>\n  html, body { height: 100%; margin: 0; }\n  body { display: flex; flex-direction: column; }\n  main { flex: 1; }\n</style>\n<body>\n  <main>Short content</main>\n  <footer>Always at the bottom</footer>\n</body>", ""),
    ],
    a11y=["A body-level footer is announced as 'content information' landmark.",
          "Only one body-level footer should exist; footers inside articles and sections are not landmarks.",
          "Keep 'back to top' links inside the footer so keyboard users can find them."],
    mistakes=["Nesting a <footer> inside another <footer> or a <header>.", "Using <footer> for a sidebar or unrelated content.",
              "Using <div class=\"footer\"> when <footer> is available.", "Putting the main navigation only in the footer."],
    related=["header", "address", "nav", "article", "section", "body"], css="footer { display: block; }",
),

dict(
    name="form", title="Form", cat="Forms",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <form> element represents a section of the document containing interactive controls (text "
        "boxes, check boxes, radio buttons, drop-down lists, buttons and so on) for collecting information "
        "from the user and sending it to a server. When the form is submitted, the browser gathers the name "
        "and value of every control that has a name, encodes them, and sends them to the URL in the action "
        "attribute using the HTTP method in the method attribute.",
        "With method=\"get\" the data is appended to the URL as a query string (?name=value&...); this is "
        "suitable for searches and filters that can be bookmarked. With method=\"post\" the data is sent in the "
        "request body; use it for anything that changes data on the server, sends passwords or uploads files.",
        "HTML5 added built-in validation: attributes such as required, pattern, min, max and type=\"email\" "
        "are checked before submission and the browser shows an error message. The novalidate attribute "
        "turns this off. Forms may not be nested inside other forms.",
    ],
    syntax="<form action=\"URL\" method=\"post\">\n  ...controls...\n  <button>Submit</button>\n</form>", void=False, display="block",
    categories="Flow content, palpable content", content="Flow content, but no <form> descendants",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLFormElement",
    attrs=[
        ("action", "URL", "Where to send the data. If omitted, the data is sent to the current page URL.", "HTML 2.0"),
        ("method", "get | post | dialog", "The HTTP method. get puts data in the URL; post sends it in the body; dialog closes the enclosing <dialog>.", "HTML 2.0"),
        ("enctype", "application/x-www-form-urlencoded | multipart/form-data | text/plain",
         "How the data is encoded for post. Use multipart/form-data when the form contains <input type=\"file\">.", "HTML 2.0"),
        ("name", "text", "A name for the form, used by scripts (document.forms.name). Must be unique among forms.", "HTML 2.0"),
        ("target", "_self | _blank | _parent | _top | name", "Where to display the response.", "HTML 4.01"),
        ("autocomplete", "on | off", "Whether the browser may autofill controls in this form. Default on.", "HTML5"),
        ("novalidate", "boolean", "Do not validate the form on submission.", "HTML5"),
        ("accept-charset", "space-separated encodings", "The character encodings the server accepts. Use utf-8.", "HTML 4.01"),
        ("rel", "link types", "Relationship of the target resource, for example noopener or noreferrer.", "Living Standard"),
        ("accept", "MIME types", "Obsolete. Use accept on <input type=\"file\"> instead.", "HTML 4.01"),
    ],
    examples=[
        ("Contact form",
         "<form action=\"/contact\" method=\"post\">\n  <p>\n    <label for=\"name\">Name</label>\n    <input id=\"name\" name=\"name\" required>\n  </p>\n"
         "  <p>\n    <label for=\"email\">Email</label>\n    <input id=\"email\" name=\"email\" type=\"email\" required>\n  </p>\n"
         "  <p>\n    <label for=\"msg\">Message</label>\n    <textarea id=\"msg\" name=\"message\" rows=\"5\" required></textarea>\n  </p>\n  <button type=\"submit\">Send</button>\n</form>", ""),
        ("Search form using GET",
         "<form action=\"/search\" method=\"get\" role=\"search\">\n  <label for=\"q\">Search</label>\n  <input id=\"q\" name=\"q\" type=\"search\">\n  <button>Go</button>\n</form>",
         "Submitting with 'html' typed produces the URL /search?q=html."),
        ("File upload", "<form action=\"/upload\" method=\"post\" enctype=\"multipart/form-data\">\n  <input type=\"file\" name=\"photo\" accept=\"image/*\">\n  <button>Upload</button>\n</form>", ""),
        ("Handling submission with JavaScript",
         "<form id=\"f\">\n  <input name=\"city\">\n  <button>Save</button>\n</form>\n<script>\n  document.getElementById('f').addEventListener('submit', e => {\n    e.preventDefault();\n"
         "    const data = new FormData(e.target);\n    console.log(data.get('city'));\n  });\n</script>", ""),
    ],
    a11y=["Every control needs a <label>.", "Group related controls with <fieldset> and <legend>.",
          "Make error messages visible and associate them with the field using aria-describedby.", "Do not rely on placeholder text as the only label."],
    mistakes=["Nesting forms.", "Forgetting name attributes, so nothing is submitted.", "Forgetting enctype for file uploads.",
              "Using GET for passwords or large data.", "Having no submit button and relying on Enter alone."],
    related=["input", "button", "label", "select", "textarea", "fieldset", "output"], css="form { display: block; margin-top: 0; }",
),

dict(
    name="frame", title="Frame (obsolete)", cat="Obsolete frames",
    versions="Netscape 2 (1996), HTML 4.01 Frameset; obsolete in HTML5", status="obsolete",
    desc=[
        "The <frame> element defined one rectangular sub-window inside a <frameset>, each displaying a "
        "separate HTML document. Frames were used in the late 1990s to keep a navigation menu fixed while "
        "the content scrolled. They caused many problems: bookmarks and the back button did not work as "
        "expected, search engines could not index the pages properly, printing was unreliable and screen "
        "readers struggled. HTML5 removed <frame> and <frameset>. Use CSS for layout and <iframe> when you "
        "truly need to embed another document.",
    ],
    syntax="<frameset cols=\"200,*\">\n  <frame src=\"menu.html\" name=\"menu\">\n  <frame src=\"main.html\" name=\"main\">\n</frameset>", void=True, display="block",
    categories="Historical", content="None", parents="<frameset>", omission="No end tag", dom="HTMLFrameElement",
    attrs=[
        ("src", "URL", "The document to display.", "HTML 4.01"),
        ("name", "text", "Name used as a link target.", "HTML 4.01"),
        ("frameborder", "0 | 1", "Whether to draw a border.", "HTML 4.01"),
        ("marginwidth / marginheight", "pixels", "Margins inside the frame.", "HTML 4.01"),
        ("noresize", "boolean", "User cannot resize the frame.", "HTML 4.01"),
        ("scrolling", "yes | no | auto", "Scrollbar behaviour.", "HTML 4.01"),
        ("longdesc", "URL", "Link to a long description.", "HTML 4.01"),
    ],
    examples=[("Modern replacement",
               "<style>\n  body { display: grid; grid-template-columns: 200px 1fr; height: 100vh; margin: 0; }\n  nav { position: sticky; top: 0; }\n</style>\n<body>\n  <nav>Menu</nav>\n  <main>Content</main>\n</body>", "")],
    a11y=["Frames were a major accessibility barrier."], mistakes=["Any use."], related=["frameset", "noframes", "iframe"], css="",
),

dict(
    name="frameset", title="Frameset (obsolete)", cat="Obsolete frames",
    versions="Netscape 2, HTML 4.01 Frameset; obsolete in HTML5", status="obsolete",
    desc=[
        "The <frameset> element replaced <body> in a frames document and divided the window into rows and "
        "columns, each filled by a <frame> or a nested <frameset>. It required the HTML 4.01 Frameset "
        "DOCTYPE. It is obsolete in HTML5. See <frame> for the reasons and the modern replacement.",
    ],
    syntax="<frameset rows=\"80,*\">...</frameset>", void=False, display="block",
    categories="Historical", content="<frame>, <frameset>, <noframes>", parents="<html>, instead of <body>", omission="Neither", dom="HTMLFrameSetElement",
    attrs=[
        ("cols", "comma-separated sizes", "Column widths in pixels, percentages or * (remaining space).", "HTML 4.01"),
        ("rows", "comma-separated sizes", "Row heights.", "HTML 4.01"),
        ("border, frameborder, framespacing", "pixels / 0 | 1", "Border appearance.", "HTML 4.01 / non-standard"),
        ("onload, onunload, and other window events", "script", "Window event handlers, as on <body>.", "HTML 4.01"),
    ],
    examples=[("Historical example", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Frameset//EN\">\n<html>\n<head><title>Frames</title></head>\n<frameset cols=\"25%,75%\">\n  <frame src=\"nav.html\">\n  <frame src=\"content.html\">\n  <noframes><body>Your browser does not support frames.</body></noframes>\n</frameset>\n</html>", "")],
    a11y=[], mistakes=["Any use."], related=["frame", "noframes", "iframe"], css="",
),

dict(
    name="h1", title="Headings h1 to h6", cat="Content sectioning",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    aliases=["h2", "h3", "h4", "h5", "h6"],
    desc=[
        "The <h1> to <h6> elements represent six levels of section headings. <h1> is the highest (most "
        "important) level and <h6> the lowest. Headings describe the topic of the section that follows "
        "them, and together they form the outline of the document, like the table of contents of a book.",
        "Use heading levels to express structure, not to choose a font size. A page should normally have a "
        "single <h1> describing the whole page, <h2> for its major sections, <h3> for sub-sections inside "
        "those, and so on. Do not skip levels (for example jumping from <h2> to <h4>) because it confuses "
        "the outline. If a heading looks too big or too small, change it with CSS, not by choosing a "
        "different level.",
        "Headings are one of the most important elements for accessibility: screen reader users navigate "
        "pages by jumping from heading to heading, and search engines give heading text extra weight.",
    ],
    syntax="<h1>Main title</h1>\n<h2>Section</h2>\n<h3>Sub-section</h3>", void=False, display="block",
    categories="Flow content, heading content, palpable content", content="Phrasing content",
    parents="Any element that accepts flow content; also directly inside <hgroup>", omission="Neither tag may be omitted", dom="HTMLHeadingElement",
    attrs=[("align", "left | center | right | justify", "Obsolete. Use CSS text-align.", "HTML 3.2")],
    examples=[
        ("A correct outline",
         "<h1>Cooking basics</h1>\n  <h2>Equipment</h2>\n    <h3>Knives</h3>\n    <h3>Pans</h3>\n  <h2>Techniques</h2>\n    <h3>Boiling</h3>\n    <h3>Frying</h3>\n      <h4>Deep frying</h4>",
         "Indentation is only for illustration; headings are written at the same indentation as their content."),
        ("Default sizes", "<h1>Heading 1 (2em)</h1>\n<h2>Heading 2 (1.5em)</h2>\n<h3>Heading 3 (1.17em)</h3>\n<h4>Heading 4 (1em)</h4>\n<h5>Heading 5 (0.83em)</h5>\n<h6>Heading 6 (0.67em)</h6>", ""),
        ("Changing the look without changing the level",
         "<style>\n  h2 { font-size: 1.2rem; text-transform: uppercase; letter-spacing: 0.1em; color: #555; }\n</style>\n<h2>Small-looking but still a level-2 heading</h2>", ""),
        ("Heading with a subtitle", "<hgroup>\n  <h1>HTML Reference</h1>\n  <p>Every tag from 1991 to today</p>\n</hgroup>", ""),
    ],
    a11y=["Screen reader users can list all headings and jump between them; a good heading structure is the single biggest navigation aid.",
          "Do not use headings for text that is merely large or bold.", "Do not leave headings empty.", "Each page should have one <h1>."],
    mistakes=["Choosing the level by size.", "Skipping levels.", "Several <h1> elements on a page (valid but unhelpful).",
              "Using <b> or <font size> instead of a heading.", "Placing a heading inside <p> or <a> incorrectly (a link may go inside a heading, not the reverse)."],
    related=["hgroup", "section", "article", "header", "p"], css="h1 { display: block; font-size: 2em; margin-block: 0.67em; font-weight: bold; }",
),

dict(
    name="head", title="Document head", cat="Document metadata",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <head> element contains machine-readable information (metadata) about the document: its "
        "title, character encoding, links to style sheets and icons, scripts, and <meta> tags for search "
        "engines and social networks. Nothing inside <head> is displayed on the page itself, except the "
        "title, which appears in the browser tab.",
        "<head> is the first child of <html>. Every document must have exactly one <title> inside its head "
        "(unless the title is supplied by a higher-level protocol, such as an email subject). The tags may "
        "be omitted and the browser will create the element automatically, but always write them.",
    ],
    syntax="<head>\n  <meta charset=\"utf-8\">\n  <title>Title</title>\n</head>", void=False, display="none",
    categories="None", content="Metadata content: exactly one <title>, at most one <base>, any number of <link>, <meta>, <script>, <style>, <noscript>, <template>",
    parents="<html>, as its first child",
    omission="Start tag may be omitted if the first thing inside is an element; end tag may be omitted if not followed by whitespace or a comment",
    dom="HTMLHeadElement",
    attrs=[("profile", "URLs", "Obsolete. Meta data profiles.", "HTML 4.01")],
    examples=[
        ("A complete, well-formed head",
         "<head>\n  <meta charset=\"utf-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n  <title>Book Store - Home</title>\n"
         "  <meta name=\"description\" content=\"Buy PDF books and pay with mobile wallet.\">\n  <link rel=\"icon\" href=\"favicon.ico\">\n  <link rel=\"stylesheet\" href=\"style.css\">\n"
         "  <script src=\"app.js\" defer></script>\n</head>", "Order matters a little: charset first, then viewport, then title, then styles, then scripts."),
    ],
    a11y=["The <title> is the first thing a screen reader announces; make it descriptive and unique per page."],
    mistakes=["Putting visible content (<p>, <div>, <img>) in the head; the browser moves it to the body.", "Omitting <title>.", "Placing <meta charset> after 1024 bytes of content."],
    related=["html", "title", "meta", "link", "style", "script", "base"], css="head { display: none; }",
),

dict(
    name="header", title="Header", cat="Content sectioning",
    versions="HTML5", status="current",
    desc=[
        "The <header> element represents introductory content for its nearest sectioning ancestor or for "
        "the page: typically a group of headings, a logo, a search form, the author's name, and the main "
        "navigation. A page usually has one header at the top of <body>, but articles and sections may "
        "have their own headers too.",
        "When a <header> is a direct child of <body> (not inside <article>, <aside>, <main>, <nav> or "
        "<section>) it is exposed as the 'banner' landmark. A header may not contain another <header> or a <footer>.",
    ],
    syntax="<header>...</header>", void=False, display="block",
    categories="Flow content, palpable content", content="Flow content, but no <header> or <footer> descendants",
    parents="Any element that accepts flow content, but not <address>", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Site header", "<header>\n  <img src=\"logo.svg\" alt=\"Book Store\" width=\"120\" height=\"40\">\n  <nav>\n    <a href=\"/\">Home</a>\n    <a href=\"/books\">Books</a>\n    <a href=\"/contact\">Contact</a>\n  </nav>\n  <form role=\"search\" action=\"/search\"><input name=\"q\" type=\"search\" aria-label=\"Search\"></form>\n</header>", ""),
        ("Article header", "<article>\n  <header>\n    <h2>Ten HTML tips</h2>\n    <p>By Sara, <time datetime=\"2026-09-01\">1 September 2026</time></p>\n  </header>\n  <p>...</p>\n</article>", ""),
        ("Sticky header", "<style>\n  header { position: sticky; top: 0; background: white; box-shadow: 0 2px 4px rgba(0,0,0,.1); }\n</style>", ""),
    ],
    a11y=["A body-level header is the 'banner' landmark; there should be only one.", "Put the site's main <nav> inside the header so it is found quickly."],
    mistakes=["Nesting header inside header or footer.", "Using <header> for the heading text alone; a lone <h1> does not need a header wrapper."],
    related=["footer", "nav", "h1", "hgroup", "main"], css="header { display: block; }",
),

dict(
    name="hgroup", title="Heading group", cat="Content sectioning",
    versions="HTML5 (removed from W3C HTML 5.0, kept in the Living Standard with a new definition)", status="current",
    desc=[
        "The <hgroup> element groups a heading (<h1>-<h6>) with one or more <p> elements that contain a "
        "subtitle, alternative title, tagline or other secondary text. It tells the browser that the "
        "paragraphs belong to the heading rather than being ordinary content.",
        "Its history is unusual: in early HTML5 drafts it grouped several headings of different levels and "
        "only the highest counted in the outline. The W3C dropped it in 2013, but the WHATWG kept it and in "
        "2022 redefined it as described above. It must contain exactly one heading element.",
    ],
    syntax="<hgroup>\n  <h1>Title</h1>\n  <p>Subtitle</p>\n</hgroup>", void=False, display="block",
    categories="Flow content, heading content, palpable content",
    content="Zero or more <p>, then one <h1>-<h6>, then zero or more <p> (plus <script> and <template>)",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Title with tagline", "<hgroup>\n  <h1>The Complete HTML Reference</h1>\n  <p>From HTML 1 to the Living Standard</p>\n</hgroup>", ""),
        ("Kicker above the headline", "<hgroup>\n  <p>Breaking news</p>\n  <h2>New HTML element announced</h2>\n</hgroup>", ""),
    ],
    a11y=["Exposed with role 'group'; the subtitle paragraphs are not read as headings, which is the desired behaviour."],
    mistakes=["Placing two headings inside one hgroup (old HTML5 style).", "Using a lower-level heading such as <h2> as the subtitle."],
    related=["h1", "header", "p"], css="hgroup { display: block; }",
),

dict(
    name="hr", title="Thematic break (horizontal rule)", cat="Text content",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <hr> element represents a thematic break between paragraph-level content: a change of scene "
        "in a story, a shift of topic within a section, or a separator between groups of options in a menu. "
        "Browsers render it as a horizontal line, which is where its name (horizontal rule) comes from.",
        "In HTML 4 it was purely a visual line with attributes for size, width and colour. HTML5 kept the "
        "element but gave it the semantic meaning above and made the presentational attributes obsolete. "
        "If you only want a decorative line, use a CSS border instead of <hr>. It is a void element.",
    ],
    syntax="<hr>", void=True, display="block",
    categories="Flow content", content="None (void element)", parents="Any element that accepts flow content, and <select>",
    omission="No end tag", dom="HTMLHRElement",
    attrs=[
        ("align", "left | center | right", "Obsolete. Alignment of the rule. Use CSS margin.", "HTML 3.2"),
        ("color", "colour", "Obsolete, non-standard. Colour of the rule. Use CSS border-color.", "IE"),
        ("noshade", "boolean", "Obsolete. Draw a solid line instead of a 3D groove. Use CSS.", "HTML 3.2"),
        ("size", "pixels", "Obsolete. Height of the rule. Use CSS height or border-width.", "HTML 3.2"),
        ("width", "pixels or percentage", "Obsolete. Width of the rule. Use CSS width.", "HTML 3.2"),
    ],
    examples=[
        ("Topic change", "<p>The first chapter ends here.</p>\n<hr>\n<p>The story continues years later.</p>", ""),
        ("Styled rule", "<style>\n  hr { border: none; border-top: 2px dashed #c8a24a; margin: 2em auto; width: 60%; }\n</style>\n<hr>", ""),
        ("Separator inside a select list", "<select>\n  <option>Egypt</option>\n  <option>Saudi Arabia</option>\n  <hr>\n  <option>Other</option>\n</select>", "Newer browsers draw a separator line between groups of options."),
    ],
    a11y=["Announced as 'separator' by screen readers. If the line is only decorative, use a CSS border so it is not announced."],
    mistakes=["Using <hr> as a layout spacer.", "Writing </hr>."],
    related=["p", "br", "section"], css="hr { display: block; margin: 0.5em auto; border: 1px inset; color: gray; overflow: hidden; }",
),

dict(
    name="html", title="Document root", cat="Main root",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <html> element is the root element of an HTML document: every other element is a descendant "
        "of it. It has exactly two children: <head> followed by <body>. It comes immediately after the "
        "<!DOCTYPE html> declaration.",
        "The most important attribute on <html> is lang, which declares the language of the page. It "
        "affects hyphenation, spell-checking, font selection, quotation marks, the voice used by screen "
        "readers and the behaviour of translation tools. For right-to-left languages add dir=\"rtl\". Both "
        "tags may technically be omitted, but always write them.",
    ],
    syntax="<!DOCTYPE html>\n<html lang=\"en\">\n  <head>...</head>\n  <body>...</body>\n</html>", void=False, display="block",
    categories="None", content="One <head> followed by one <body>", parents="None (root element)",
    omission="Start tag may be omitted if the first thing inside is not a comment; end tag may be omitted if not followed by a comment",
    dom="HTMLHtmlElement",
    attrs=[
        ("lang", "BCP 47 language tag", "The primary language of the document: en, en-GB, ar, ar-EG, fr, de, zh-Hans...", "HTML 4.01"),
        ("dir", "ltr | rtl | auto", "Text direction of the document.", "HTML 4.01"),
        ("xmlns", "http://www.w3.org/1999/xhtml", "XML namespace; required in XHTML, ignored in HTML.", "XHTML 1.0"),
        ("manifest", "URL", "Obsolete. Application cache manifest for offline pages. Replaced by service workers.", "HTML5 (removed)"),
        ("version", "text", "Obsolete. The HTML DTD version.", "HTML 2.0"),
    ],
    examples=[
        ("English page", "<!DOCTYPE html>\n<html lang=\"en\">\n<head><meta charset=\"utf-8\"><title>Hello</title></head>\n<body><p>Hello</p></body>\n</html>", ""),
        ("Arabic page, right to left", "<!DOCTYPE html>\n<html lang=\"ar\" dir=\"rtl\">\n<head><meta charset=\"utf-8\"><title>مرحبا</title></head>\n<body><p>مرحبا بكم</p></body>\n</html>", ""),
        ("Old DOCTYPEs for comparison",
         "<!-- HTML 2.0 -->\n<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\n\n<!-- HTML 3.2 -->\n<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n\n"
         "<!-- HTML 4.01 Strict -->\n<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n\n"
         "<!-- XHTML 1.0 Strict -->\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n\n<!-- HTML5 -->\n<!DOCTYPE html>", ""),
    ],
    a11y=["Always set lang. Without it screen readers may read the page in the wrong language with a heavy accent."],
    mistakes=["Omitting lang.", "Placing content outside <html>.", "Forgetting the DOCTYPE before it."],
    related=["head", "body"], css="html { display: block; }",
),

]
