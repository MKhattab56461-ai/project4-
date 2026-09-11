# -*- coding: utf-8 -*-
"""Element reference entries, letters I to O."""

ELEMENTS = [

dict(
    name="i", title="Idiomatic text (italic)", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <i> element marks a span of text that is set off from the normal prose for some reason "
        "other than emphasis or importance: an alternative voice or mood, a technical term, a taxonomic "
        "name (Homo sapiens), a phrase in another language, a thought, a ship's name, or a transliteration. "
        "Browsers render it in italics.",
        "In HTML 4 <i> simply meant 'italic'. HTML5 gave it the meaning above so that it stays valid. "
        "Choose the most specific element first: <em> for emphasis, <cite> for titles of works, <dfn> for "
        "defined terms, <strong> for importance. Use <i> only when none of those apply, and consider adding "
        "a class or lang attribute to say why the text is different.",
    ],
    syntax="<i>text</i>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Foreign phrase and scientific name",
         "<p>The Egyptians say <i lang=\"ar\">inshallah</i> often.</p>\n<p>The domestic cat is <i>Felis catus</i>.</p>", ""),
        ("A thought", "<p><i>I should have used a footer</i>, she thought.</p>", ""),
    ],
    a11y=["No announcement in screen readers; use <em> when the italic carries stress."],
    mistakes=["Using <i> for icons with no text (<i class=\"fa fa-home\"></i>) is common in icon libraries but semantically wrong; add aria-hidden and a text label.", "Using <i> instead of <em> or <cite>."],
    related=["em", "b", "cite", "dfn"], css="i { font-style: italic; }",
),

dict(
    name="iframe", title="Inline frame", cat="Embedded content",
    versions="Internet Explorer 3 (1996), HTML 4.01, HTML5", status="current",
    desc=[
        "The <iframe> element embeds another HTML page inside the current page, in a rectangular area "
        "called a nested browsing context. Each iframe has its own document, its own window object and its "
        "own history. Common uses are embedding videos from YouTube, maps, advertisements, payment forms, "
        "social media widgets and third-party tools.",
        "Because the embedded page may come from another site, iframes have security controls. The sandbox "
        "attribute restricts what the embedded page may do (run scripts, submit forms, open popups, navigate "
        "the top page). The allow attribute grants specific features such as camera or fullscreen. Sites can "
        "refuse to be framed with the X-Frame-Options or Content-Security-Policy headers.",
        "Every iframe costs memory and processing time. Use loading=\"lazy\" for iframes far down the page, "
        "and always give the iframe a title describing its content.",
    ],
    syntax="<iframe src=\"URL\" title=\"description\" width=\"600\" height=\"400\"></iframe>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content, interactive content, palpable content",
    content="None (the element must be empty; older browsers displayed content inside it as fallback)",
    parents="Any element that accepts embedded content", omission="Neither tag may be omitted", dom="HTMLIFrameElement",
    attrs=[
        ("src", "URL", "The page to embed. about:blank shows an empty page.", "HTML 4.01"),
        ("srcdoc", "HTML text", "Inline HTML to display instead of loading src. Overrides src if present.", "HTML5"),
        ("title", "text", "A description of the embedded content for assistive technology. Strongly recommended.", "HTML 4.01"),
        ("name", "text", "A name that can be used as the target of links and forms.", "HTML 4.01"),
        ("width", "pixels", "Width of the frame (default 300).", "HTML 4.01"),
        ("height", "pixels", "Height of the frame (default 150).", "HTML 4.01"),
        ("sandbox", "empty or space-separated tokens",
         "Applies extra restrictions. Empty value = all restrictions. Tokens that lift restrictions: allow-downloads, "
         "allow-forms, allow-modals, allow-orientation-lock, allow-pointer-lock, allow-popups, allow-popups-to-escape-sandbox, "
         "allow-presentation, allow-same-origin, allow-scripts, allow-top-navigation, allow-top-navigation-by-user-activation, allow-top-navigation-to-custom-protocols.", "HTML5"),
        ("allow", "permissions policy", "Features the frame may use, for example allow=\"camera; microphone; fullscreen; geolocation; autoplay; picture-in-picture\".", "HTML5"),
        ("allowfullscreen", "boolean", "Legacy form of allow=\"fullscreen\".", "HTML5"),
        ("loading", "eager | lazy", "lazy defers loading until the frame is near the viewport.", "Living Standard"),
        ("referrerpolicy", "referrer policy keyword", "Which referrer to send when loading the frame.", "HTML5"),
        ("credentialless", "boolean", "Experimental: load the frame in a new, empty cookie/storage context.", "Experimental"),
        ("csp", "policy string", "Experimental: Content Security Policy to enforce on the embedded document.", "Experimental"),
        ("align", "left | right | top | middle | bottom", "Obsolete. Use CSS.", "HTML 4.01"),
        ("frameborder", "0 | 1", "Obsolete. Use CSS border.", "HTML 4.01"),
        ("longdesc", "URL", "Obsolete. Link to a long description.", "HTML 4.01"),
        ("marginheight / marginwidth", "pixels", "Obsolete. Use CSS in the framed document.", "HTML 4.01"),
        ("scrolling", "yes | no | auto", "Obsolete. Use CSS overflow in the framed document.", "HTML 4.01"),
        ("allowpaymentrequest", "boolean", "Obsolete. Use allow=\"payment\".", "HTML5 (removed)"),
    ],
    examples=[
        ("Embedding a YouTube video",
         "<iframe width=\"560\" height=\"315\"\n  src=\"https://www.youtube.com/embed/qfPUMV9J5yw\"\n  title=\"HTML tutorial video\"\n  allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"\n  allowfullscreen loading=\"lazy\"></iframe>", ""),
        ("Sandboxed untrusted content", "<iframe src=\"https://untrusted.example.com/widget\" title=\"Widget\" sandbox=\"allow-scripts\"></iframe>",
         "The widget can run scripts but cannot submit forms, open popups, or access cookies of its origin."),
        ("Inline document with srcdoc", "<iframe title=\"Preview\" srcdoc=\"<h1>Hello</h1><p>Rendered from srcdoc.</p>\"></iframe>", ""),
        ("Responsive 16:9 video frame", "<style>\n  .video { aspect-ratio: 16 / 9; width: 100%; border: 0; }\n</style>\n<iframe class=\"video\" src=\"...\" title=\"Video\"></iframe>", ""),
        ("Targeting an iframe from a link", "<iframe name=\"preview\" title=\"Preview\" src=\"about:blank\"></iframe>\n<a href=\"page1.html\" target=\"preview\">Load page 1 in the frame</a>", ""),
    ],
    a11y=["Always provide a meaningful title; screen readers announce it when entering the frame.",
          "Content inside the iframe must itself be accessible; you cannot fix it from outside.",
          "Avoid iframes that steal keyboard focus or auto-play media."],
    mistakes=["No title.", "Never combining allow-scripts and allow-same-origin in sandbox for untrusted content (it lets the frame remove its own sandbox).",
              "Sizing with width=\"100%\" attribute (percent is not valid; use CSS).", "Embedding sites that forbid framing and getting a blank box."],
    related=["embed", "object", "frame", "fencedframe", "portal"], css="iframe { border: 2px inset; }",
),

dict(
    name="image", title="Image (non-standard alias, obsolete)", cat="Obsolete embedded content",
    versions="Never standard", status="obsolete",
    desc=[
        "<image> is an ancient, non-standard synonym for <img>. For compatibility, the HTML parser "
        "silently converts a start tag named image into img. Never write it; always use <img>.",
    ],
    syntax="<image src=\"x.png\">  <!-- becomes <img src=\"x.png\"> -->", void=True, display="inline",
    categories="Historical", content="None", parents="Phrasing content", omission="No end tag", dom="HTMLImageElement (after parsing)",
    attrs=[("src, alt, etc.", "as <img>", "Whatever the parser transfers to the <img> it creates.", "-")],
    examples=[("Use <img>", "<img src=\"x.png\" alt=\"Description\">", "")],
    a11y=[], mistakes=["Any use."], related=["img"], css="",
),

dict(
    name="img", title="Image", cat="Image and multimedia",
    versions="Mosaic (1993), HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <img> element embeds an image in the document. It is a void element; the image file is "
        "identified by the src attribute and is loaded separately. Supported formats include JPEG, PNG, GIF, "
        "WebP, AVIF, SVG, APNG, BMP and ICO. The alt attribute holds a text alternative that is displayed if "
        "the image cannot load and is read aloud by screen readers; it is required for accessibility.",
        "HTML5 added responsive-image attributes: srcset lists several versions of the image at different "
        "sizes or pixel densities and sizes tells the browser how wide the image will be displayed, so the "
        "browser can download the smallest adequate file. The loading=\"lazy\" attribute defers loading until "
        "the image is near the viewport, and decoding=\"async\" lets the browser decode it off the main thread.",
        "Always give width and height attributes (the intrinsic size in pixels). The browser uses them to "
        "reserve space before the image loads, which prevents the page from jumping (layout shift). With CSS "
        "max-width: 100%; height: auto the image still scales down on small screens.",
        "The <img> element was invented by Marc Andreessen for the Mosaic browser in 1993 and was the first "
        "element to bring graphics to the web. In HTML 3.2 and 4.01 it carried presentational attributes "
        "(align, border, hspace, vspace) that are obsolete today.",
    ],
    syntax="<img src=\"URL\" alt=\"description\" width=\"W\" height=\"H\">", void=True, display="inline",
    categories="Flow content, phrasing content, embedded content, palpable content; form-associated and interactive if it has usemap",
    content="None (void element)", parents="Any element that accepts embedded content", omission="No end tag", dom="HTMLImageElement",
    attrs=[
        ("src", "URL", "The image URL. Required (unless srcset is used with a browser that supports it).", "HTML 2.0"),
        ("alt", "text", "Text alternative. Describe the content or function of the image. Use alt=\"\" (empty) for purely decorative images so that screen readers skip them. Omitting alt entirely is an error.", "HTML 2.0"),
        ("width", "pixels", "Intrinsic width. Helps the browser reserve space.", "HTML 3.2"),
        ("height", "pixels", "Intrinsic height.", "HTML 3.2"),
        ("srcset", "comma-separated candidates", "Alternative image files: 'small.jpg 480w, large.jpg 1200w' (width descriptors) or 'img.jpg 1x, img@2x.jpg 2x' (density descriptors).", "HTML5"),
        ("sizes", "media conditions and lengths", "How wide the image will be rendered, for example '(max-width: 600px) 100vw, 50vw'. Required when srcset uses width descriptors.", "HTML5"),
        ("loading", "eager | lazy", "lazy delays loading until the image is near the viewport. Do not lazy-load images visible at page load.", "Living Standard"),
        ("decoding", "sync | async | auto", "Hint about how to decode the image.", "Living Standard"),
        ("fetchpriority", "high | low | auto", "Hint about the download priority; set high on the hero image.", "Living Standard"),
        ("crossorigin", "anonymous | use-credentials", "Load with CORS so the image can be used in canvas without tainting it.", "HTML5"),
        ("referrerpolicy", "referrer policy keyword", "Which referrer to send.", "HTML5"),
        ("usemap", "#map-name", "Links the image to a <map> element to make it an image map.", "HTML 3.2"),
        ("ismap", "boolean", "Makes the image a server-side image map; the click coordinates are appended to the link URL. Only valid inside <a href>.", "HTML 2.0"),
        ("elementtiming", "text", "Marks the image for the Element Timing performance API.", "Living Standard"),
        ("attributionsrc", "empty or URL", "Experimental attribution reporting.", "Experimental"),
        ("align", "top | middle | bottom | left | right", "Obsolete. Use CSS float or vertical-align.", "HTML 2.0"),
        ("border", "pixels", "Obsolete. Border width. Use CSS border.", "HTML 3.2"),
        ("hspace / vspace", "pixels", "Obsolete. Horizontal and vertical margins. Use CSS margin.", "HTML 3.2"),
        ("longdesc", "URL", "Obsolete. Link to a long description. Use a normal link or aria-describedby.", "HTML 4.01"),
        ("name", "text", "Obsolete. Use id.", "HTML 4.01"),
        ("lowsrc", "URL", "Obsolete, non-standard. Low-quality placeholder loaded first.", "Netscape"),
    ],
    examples=[
        ("Basic image with good alt text", "<img src=\"cat.jpg\" alt=\"A grey cat sleeping on a red cushion\" width=\"400\" height=\"300\">", ""),
        ("Decorative image", "<img src=\"divider.png\" alt=\"\" width=\"600\" height=\"8\">", "Empty alt tells screen readers to ignore it."),
        ("Responsive images with srcset and sizes",
         "<img src=\"photo-800.jpg\"\n  srcset=\"photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w\"\n  sizes=\"(max-width: 600px) 100vw, 600px\"\n  alt=\"Cairo skyline at night\" width=\"800\" height=\"533\">",
         "On a phone the image fills the screen, so the browser picks the 400w or 800w file; on a desktop it is shown at 600px wide."),
        ("High-DPI (retina) logo", "<img src=\"logo.png\" srcset=\"logo.png 1x, logo@2x.png 2x\" alt=\"Book Store\" width=\"120\" height=\"40\">", ""),
        ("Lazy loading images below the fold", "<img src=\"gallery-12.jpg\" alt=\"...\" loading=\"lazy\" decoding=\"async\" width=\"300\" height=\"200\">", ""),
        ("Image as a link", "<a href=\"index.html\"><img src=\"logo.svg\" alt=\"Book Store home\" width=\"120\" height=\"40\"></a>", "The alt describes where the link goes."),
        ("Fluid image CSS", "<style>\n  img { max-width: 100%; height: auto; }\n</style>", "Keeps images inside their container on small screens while width/height attributes still prevent layout shift."),
        ("HTML 3.2 style and its replacement",
         "<!-- Old -->\n<img src=\"a.jpg\" align=\"left\" hspace=\"10\" border=\"0\">\n\n<!-- New -->\n<img src=\"a.jpg\" alt=\"...\" style=\"float: left; margin: 0 10px; border: 0\">", ""),
    ],
    a11y=["alt is required. Write what the image conveys, not 'image of'. Keep it under about 150 characters; for complex images give a longer description in the text.",
          "Text inside images cannot be read by screen readers or resized; use real text.",
          "Animated GIFs that flash can trigger seizures; avoid or provide a pause control."],
    mistakes=["Omitting alt or writing alt=\"image\".", "Omitting width and height, causing layout shift.", "Using a huge original file where a resized one would do.",
              "Lazy-loading the hero image (it delays the largest contentful paint).", "Using the align attribute."],
    related=["picture", "source", "figure", "map", "area", "canvas", "svg"], css="img { display: inline; }",
),

dict(
    name="input", title="Input control", cat="Forms",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <input> element creates an interactive control for accepting data from the user. It is the "
        "most versatile element in HTML: the type attribute selects one of more than twenty different "
        "controls, from a plain text box to a colour picker, a file chooser, a range slider or a hidden "
        "field. It is a void element.",
        "HTML 2.0 defined text, password, checkbox, radio, submit, reset, hidden and image; HTML 3.2 and "
        "4.01 added file and button; HTML5 added email, url, tel, search, number, range, color, date, "
        "month, week, time and datetime-local. Browsers fall back to type=\"text\" for any type they do not "
        "recognise, so new types are safe to use.",
        "Each type accepts a different subset of attributes; the complete table below lists every "
        "attribute and Part 6 of this book describes every type in its own entry with examples.",
    ],
    syntax="<input type=\"text\" name=\"field\" id=\"field\">", void=True, display="inline-block",
    categories="Flow content, phrasing content, listed, submittable, resettable, form-associated, palpable; interactive and labelable unless type=hidden",
    content="None (void element)", parents="Any element that accepts phrasing content", omission="No end tag", dom="HTMLInputElement",
    attrs=[
        ("type", "see Part 6", "The kind of control. Default text. Values: button, checkbox, color, date, datetime-local, email, file, hidden, image, month, number, password, radio, range, reset, search, submit, tel, text, time, url, week.", "HTML 2.0 / HTML5"),
        ("name", "text", "The name under which the value is submitted. Without it the control is not submitted. Radio buttons with the same name form a group.", "HTML 2.0"),
        ("value", "text", "The initial value (text types), the value submitted when checked (checkbox, radio), or the button label (submit, reset, button).", "HTML 2.0"),
        ("id", "identifier", "Links the control to a <label for=\"id\">.", "HTML 4.01"),
        ("disabled", "boolean", "Cannot be used or focused and is not submitted.", "HTML 4.01"),
        ("readonly", "boolean", "Cannot be edited but is focusable and submitted. Text-like types only.", "HTML 4.01"),
        ("required", "boolean", "Must have a value before the form can be submitted.", "HTML5"),
        ("placeholder", "text", "Hint shown inside an empty text-like control. Not a substitute for a label.", "HTML5"),
        ("autocomplete", "on | off | token list", "Autofill hint: name, email, tel, street-address, postal-code, cc-number, new-password, current-password, one-time-code and more (see Part 9).", "HTML5"),
        ("autofocus", "boolean", "Focus this control on page load. Only one per page.", "HTML5"),
        ("checked", "boolean", "Initially selected (checkbox, radio).", "HTML 2.0"),
        ("maxlength", "integer", "Maximum number of characters (text-like types).", "HTML 2.0"),
        ("minlength", "integer", "Minimum number of characters.", "HTML5"),
        ("size", "integer", "Visible width in characters (text-like types). Prefer CSS width.", "HTML 2.0"),
        ("min", "number or date", "Minimum value (number, range, date/time types).", "HTML5"),
        ("max", "number or date", "Maximum value.", "HTML5"),
        ("step", "number or any", "Granularity of allowed values; 'any' allows any value.", "HTML5"),
        ("pattern", "regular expression", "A JavaScript regular expression the value must match (text, search, url, tel, email, password). Describe the format in title.", "HTML5"),
        ("list", "datalist id", "Links to a <datalist> of suggestions.", "HTML5"),
        ("multiple", "boolean", "Allow several values (email: comma-separated; file: several files).", "HTML5"),
        ("accept", "MIME types / extensions", "Allowed file types for type=file, for example image/*, .pdf, audio/*.", "HTML 4.01"),
        ("capture", "user | environment", "For type=file on phones: use the front (user) or back (environment) camera/microphone directly.", "Media Capture spec"),
        ("src", "URL", "The image for type=image.", "HTML 2.0"),
        ("alt", "text", "Alternative text for type=image.", "HTML 2.0"),
        ("width / height", "pixels", "Size of the image for type=image.", "HTML5"),
        ("form", "form id", "Associate with a form anywhere in the document.", "HTML5"),
        ("formaction", "URL", "Override the form action (submit, image).", "HTML5"),
        ("formenctype", "encoding type", "Override the form enctype (submit, image).", "HTML5"),
        ("formmethod", "get | post | dialog", "Override the form method (submit, image).", "HTML5"),
        ("formnovalidate", "boolean", "Skip validation when submitting with this button.", "HTML5"),
        ("formtarget", "browsing context", "Override the form target (submit, image).", "HTML5"),
        ("dirname", "text", "Submit the text direction of the value under this name.", "HTML5"),
        ("inputmode", "none | text | decimal | numeric | tel | search | email | url", "Which virtual keyboard to show on touch devices (global attribute).", "HTML5"),
        ("popovertarget / popovertargetaction", "id / show | hide | toggle", "Control a popover from a button-type input.", "Living Standard"),
        ("alpha", "boolean", "Experimental: allow transparency in type=color.", "Experimental"),
        ("colorspace", "limited-srgb | display-p3", "Experimental: colour space for type=color.", "Experimental"),
        ("align", "left | right | top | middle | bottom", "Obsolete. Use CSS.", "HTML 3.2"),
        ("usemap", "#map", "Obsolete on input. Use <img usemap>.", "HTML 4.01"),
        ("incremental, results, webkitdirectory, orient, mozactionhint", "various", "Non-standard browser-specific attributes.", "Non-standard"),
    ],
    examples=[
        ("Text with label, placeholder and required", "<label for=\"user\">Username</label>\n<input id=\"user\" name=\"user\" type=\"text\" placeholder=\"e.g. ahmed99\" required minlength=\"3\" maxlength=\"20\" autocomplete=\"username\">", ""),
        ("Email and password", "<label for=\"e\">Email</label>\n<input id=\"e\" name=\"email\" type=\"email\" required autocomplete=\"email\">\n<label for=\"p\">Password</label>\n<input id=\"p\" name=\"password\" type=\"password\" required minlength=\"8\" autocomplete=\"current-password\">", ""),
        ("Checkboxes and radio buttons",
         "<label><input type=\"checkbox\" name=\"terms\" value=\"yes\" required> I agree to the terms</label>\n\n"
         "<fieldset>\n  <legend>Size</legend>\n  <label><input type=\"radio\" name=\"size\" value=\"s\"> Small</label>\n  <label><input type=\"radio\" name=\"size\" value=\"m\" checked> Medium</label>\n  <label><input type=\"radio\" name=\"size\" value=\"l\"> Large</label>\n</fieldset>", ""),
        ("Number, range and date",
         "<label>Quantity <input type=\"number\" name=\"qty\" min=\"1\" max=\"10\" step=\"1\" value=\"1\"></label>\n"
         "<label>Volume <input type=\"range\" name=\"vol\" min=\"0\" max=\"100\" value=\"50\"></label>\n"
         "<label>Delivery date <input type=\"date\" name=\"date\" min=\"2026-09-12\"></label>", ""),
        ("Pattern validation with an explanation", "<label>Postal code <input name=\"zip\" pattern=\"[0-9]{5}\" title=\"Five digits, for example 12511\" inputmode=\"numeric\"></label>", ""),
        ("Hidden field", "<input type=\"hidden\" name=\"product_id\" value=\"42\">", "Sent with the form but not shown."),
        ("File upload restricted to images", "<input type=\"file\" name=\"photo\" accept=\"image/png, image/jpeg\" multiple>", ""),
        ("Styling validity", "<style>\n  input:invalid { border-color: #b90000; }\n  input:valid { border-color: #0f8a4c; }\n  input:focus { outline: 2px solid #1b6fd8; }\n</style>", ""),
    ],
    a11y=["Every input needs a label (visible <label> or aria-label).", "Placeholder disappears when typing; never use it as the only label.",
          "Use the correct type so mobile keyboards and screen readers behave correctly.", "Group radio buttons and checkboxes in a fieldset with a legend.",
          "Do not disable the submit button until the form is valid; let users submit and see the errors."],
    mistakes=["Missing name (nothing submitted).", "Missing label.", "Using type=\"number\" for values that are not quantities (phone numbers, postal codes); use type=\"tel\" or text with inputmode.",
              "Writing a closing </input> tag.", "Relying only on client-side validation; always validate on the server too."],
    related=["form", "label", "button", "select", "textarea", "datalist", "output", "fieldset"], css="input { display: inline-block; }",
),

dict(
    name="ins", title="Inserted text", cat="Demarcating edits",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <ins> element marks text that has been added to a document, to show changes between versions. "
        "Browsers underline it by default. It is the counterpart of <del>. Like <del> it accepts optional "
        "cite and datetime attributes that record why and when the change was made.",
    ],
    syntax="<ins datetime=\"YYYY-MM-DD\">inserted text</ins>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Transparent",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLModElement",
    attrs=[("cite", "URL", "A URL explaining the change.", "HTML 4.01"),
           ("datetime", "date or date-time", "When the change was made.", "HTML 4.01")],
    examples=[
        ("Tracking a change", "<p>Our office is open <del>9 to 5</del> <ins datetime=\"2026-09-01\">8 to 4</ins>.</p>", ""),
        ("Styling insertions", "<style>\n  ins { background: #dfffe0; text-decoration: none; }\n  del { background: #ffe0e0; }\n</style>", ""),
    ],
    a11y=["Not announced by most screen readers by default; add hidden text if the change must be conveyed."],
    mistakes=["Using <u> to show insertions.", "Wrapping several block elements in one inline <ins>."],
    related=["del", "u"], css="ins { text-decoration: underline; }",
),

dict(
    name="isindex", title="Search index prompt (obsolete)", cat="Obsolete forms",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01 (deprecated); obsolete in HTML5", status="obsolete",
    desc=[
        "The <isindex> element, one of the original 1991 elements, told the browser that the document was "
        "a searchable index and made it display a single-line text field with a prompt. Submitting the "
        "field reloaded the page with ?keywords in the URL. It was made redundant by forms in HTML 2.0, "
        "deprecated in HTML 4.01 and removed in HTML5. Use a <form> with an <input type=\"search\">.",
    ],
    syntax="<isindex prompt=\"Search: \">", void=True, display="block",
    categories="Historical", content="None", parents="<head> or <body>", omission="No end tag", dom="HTMLUnknownElement",
    attrs=[("prompt", "text", "The label shown before the field.", "HTML 2.0"), ("action", "URL", "Where to send the query (non-standard).", "Netscape")],
    examples=[("Replacement", "<form action=\"/search\" method=\"get\">\n  <label>Search: <input type=\"search\" name=\"q\"></label>\n</form>", "")],
    a11y=[], mistakes=["Any use."], related=["form", "input"], css="",
),

dict(
    name="kbd", title="Keyboard input", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <kbd> element marks text that represents user input from a keyboard, voice command, or other "
        "input device. Browsers render it in a monospace font. Nesting <kbd> elements inside a <kbd> "
        "represents individual keys in a key combination; wrapping <kbd> in <samp> represents input echoed "
        "by the system.",
    ],
    syntax="<kbd>Ctrl</kbd> + <kbd>S</kbd>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Keyboard shortcut", "<p>Press <kbd><kbd>Ctrl</kbd> + <kbd>S</kbd></kbd> to save.</p>", ""),
        ("Key-cap styling", "<style>\n  kbd { border: 1px solid #aaa; border-radius: 4px; padding: 0 4px; background: #f5f5f5; font-size: 0.9em; box-shadow: 0 1px 0 #999; }\n</style>", ""),
        ("Menu selection", "<p>Choose <kbd>File</kbd> then <kbd>Save As...</kbd>.</p>", ""),
    ],
    a11y=[], mistakes=["Using <code> for keys.", "Using <kbd> for program output (use <samp>)."],
    related=["code", "samp", "var"], css="kbd { font-family: monospace; }",
),

dict(
    name="keygen", title="Key-pair generator (obsolete)", cat="Obsolete forms",
    versions="Netscape, briefly in HTML5; removed", status="obsolete",
    desc=[
        "The <keygen> element generated a public/private key pair when a form was submitted, for client "
        "certificate enrolment. It came from Netscape, was added to HTML5 and then removed from the standard "
        "in 2017 and from all browsers. There is no direct replacement; use the Web Crypto API.",
    ],
    syntax="<keygen name=\"key\" challenge=\"...\">", void=True, display="inline-block",
    categories="Historical", content="None", parents="Phrasing content", omission="No end tag", dom="HTMLUnknownElement",
    attrs=[("challenge", "text", "Challenge string.", "HTML5"), ("keytype", "rsa | dsa | ec", "Key algorithm.", "HTML5"),
           ("name", "text", "Form field name.", "HTML5"), ("autofocus, disabled, form", "-", "As on other controls.", "HTML5")],
    examples=[("Do not use", "<!-- No modern replacement in HTML; see crypto.subtle.generateKey() -->", "")],
    a11y=[], mistakes=["Any use."], related=["input", "form"], css="",
),

dict(
    name="label", title="Form control label", cat="Forms",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <label> element gives a caption to a form control. Associating a label with a control has two "
        "big benefits: clicking the label focuses or toggles the control (a much larger click target for "
        "checkboxes and radio buttons), and screen readers announce the label when the control gets focus.",
        "There are two ways to associate them. Explicit: give the control an id and set the label's for "
        "attribute to that id. Implicit: nest the control inside the label. You may combine both. A label "
        "may be associated with only one control, but a control may have several labels.",
        "Labelable elements are <button>, <input> (except hidden), <meter>, <output>, <progress>, <select> "
        "and <textarea>.",
    ],
    syntax="<label for=\"id\">Text</label> <input id=\"id\">\n<!-- or -->\n<label>Text <input></label>", void=False, display="inline",
    categories="Flow content, phrasing content, interactive content, form-associated, palpable content",
    content="Phrasing content, but no other <label> and at most one labelable descendant",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLLabelElement",
    attrs=[
        ("for", "id of a labelable element", "The control this label describes.", "HTML 4.01"),
        ("form", "form id", "Obsolete in the Living Standard; was meant to associate the label with a form.", "HTML5 (removed)"),
    ],
    examples=[
        ("Explicit association", "<label for=\"city\">City</label>\n<input id=\"city\" name=\"city\">", ""),
        ("Implicit association (wrapping)", "<label>\n  <input type=\"checkbox\" name=\"news\"> Send me the newsletter\n</label>", "Clicking anywhere on the text toggles the box."),
        ("Labels stacked above fields", "<style>\n  label { display: block; margin-bottom: 4px; font-weight: 600; }\n  input, select, textarea { display: block; width: 100%; margin-bottom: 16px; }\n</style>", ""),
        ("Required-field indicator", "<label for=\"n\">Name <span aria-hidden=\"true\">*</span></label>\n<input id=\"n\" name=\"n\" required aria-required=\"true\">", ""),
    ],
    a11y=["A label is the correct way to name a control; aria-label is a fallback when no visible text is possible.",
          "Do not put headings or interactive elements inside a label.", "Keep the label visible; placeholder text is not a label."],
    mistakes=["for pointing to a name instead of an id.", "Two controls inside one label.", "Using <label> for text that is not a caption for a control."],
    related=["input", "select", "textarea", "button", "fieldset", "legend"], css="label { cursor: default; }",
),

dict(
    name="legend", title="Fieldset caption", cat="Forms",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <legend> element provides a caption for its parent <fieldset>. It must be the first child of "
        "the fieldset. Browsers draw it on top of the fieldset's border. Screen readers announce the legend "
        "together with the label of each control inside the group, which is why fieldset/legend is the "
        "recommended way to caption groups of radio buttons or checkboxes.",
    ],
    syntax="<fieldset>\n  <legend>Caption</legend>\n  ...\n</fieldset>", void=False, display="block",
    categories="None", content="Phrasing content and optionally heading content", parents="<fieldset>, as its first child",
    omission="Neither tag may be omitted", dom="HTMLLegendElement",
    attrs=[("align", "left | center | right | top | bottom", "Obsolete. Use CSS.", "HTML 4.01")],
    examples=[
        ("Captioned group", "<fieldset>\n  <legend>Contact preference</legend>\n  <label><input type=\"radio\" name=\"c\" value=\"email\"> Email</label>\n  <label><input type=\"radio\" name=\"c\" value=\"phone\"> Phone</label>\n</fieldset>", ""),
        ("Legend containing a heading", "<fieldset>\n  <legend><h2>Billing address</h2></legend>\n  ...\n</fieldset>", "Allowed since the Living Standard; keeps the document outline while still captioning the group."),
    ],
    a11y=["Keep legends short; they are repeated by some screen readers for every control in the group."],
    mistakes=["Legend not first in the fieldset.", "Using legend outside a fieldset."],
    related=["fieldset", "label"], css="legend { display: block; padding-inline: 2px; }",
),

dict(
    name="li", title="List item", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <li> element represents one item in a list. It must be contained in an ordered list (<ol>), "
        "an unordered list (<ul>) or a menu (<menu>). In ordered lists the value attribute sets the number "
        "of the item, and subsequent items continue counting from it.",
        "A list item may contain any flow content: paragraphs, images, nested lists, even tables. To nest a "
        "list, place the inner <ul> or <ol> inside the <li>, not between two <li> elements.",
    ],
    syntax="<ul>\n  <li>Item</li>\n</ul>", void=False, display="list-item",
    categories="None", content="Flow content", parents="<ul>, <ol>, <menu>",
    omission="End tag may be omitted if followed by another <li> or if there is no more content in the parent", dom="HTMLLIElement",
    attrs=[
        ("value", "integer", "In <ol>: the ordinal number of this item. Following items count from it.", "HTML 3.2"),
        ("type", "1 | a | A | i | I | disc | circle | square", "Obsolete. Bullet or numbering style for this item. Use CSS list-style-type.", "HTML 3.2"),
    ],
    examples=[
        ("Unordered list", "<ul>\n  <li>Milk</li>\n  <li>Bread</li>\n  <li>Eggs</li>\n</ul>", "Displays with bullets."),
        ("Ordered list with a custom start value", "<ol>\n  <li value=\"10\">Tenth</li>\n  <li>Eleventh</li>\n  <li>Twelfth</li>\n</ol>", ""),
        ("Nested list (correct)", "<ul>\n  <li>Fruit\n    <ul>\n      <li>Apples</li>\n      <li>Oranges</li>\n    </ul>\n  </li>\n  <li>Vegetables</li>\n</ul>", "The inner list is inside the first <li>."),
        ("Rich list items", "<ol>\n  <li>\n    <h3>Step one</h3>\n    <p>Open your editor.</p>\n    <img src=\"editor.png\" alt=\"Editor window\" width=\"300\" height=\"200\">\n  </li>\n</ol>", ""),
        ("Horizontal menu with CSS", "<style>\n  nav ul { list-style: none; padding: 0; margin: 0; display: flex; gap: 16px; }\n</style>\n<nav><ul><li><a href=\"/\">Home</a></li><li><a href=\"/shop\">Shop</a></li></ul></nav>", ""),
    ],
    a11y=["Screen readers announce the number of items in a list and the position of each; this is lost if list-style: none is combined with display: contents in some browsers, or if you fake a list with <br>."],
    mistakes=["Placing <li> directly in <div> or <body>.", "Nesting a list between <li> elements rather than inside one.", "Using <br> instead of separate items."],
    related=["ul", "ol", "menu", "dl"], css="li { display: list-item; text-align: match-parent; }",
),

dict(
    name="link", title="External resource link", cat="Document metadata",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <link> element specifies a relationship between the current document and an external "
        "resource. By far its most common use is loading a CSS style sheet (rel=\"stylesheet\"), but it is "
        "also used for site icons (rel=\"icon\"), web app manifests, preloading and prefetching resources, "
        "canonical URLs for search engines, alternate language versions, RSS feeds and more. It is a void "
        "element and normally lives in <head>, though body-ok link types such as stylesheet may appear in "
        "<body>.",
        "The rel attribute is required and determines everything else. The media attribute lets a style "
        "sheet apply only to certain devices or screen sizes; the browser still downloads it but with low "
        "priority. The full list of link types is in Part 9.",
    ],
    syntax="<link rel=\"stylesheet\" href=\"style.css\">", void=True, display="none",
    categories="Metadata content; flow and phrasing content if itemprop or a body-ok rel is present",
    content="None (void element)", parents="<head>; <body> for body-ok types", omission="No end tag", dom="HTMLLinkElement",
    attrs=[
        ("rel", "space-separated link types", "Required. Relationship: stylesheet, icon, apple-touch-icon, manifest, canonical, alternate, preload, prefetch, preconnect, dns-prefetch, modulepreload, prerender, author, license, help, next, prev, search, pingback, privacy-policy, terms-of-service, expect.", "HTML 2.0"),
        ("href", "URL", "The resource URL.", "HTML 2.0"),
        ("type", "MIME type", "The type of the resource, for example text/css, image/png, application/rss+xml.", "HTML 2.0"),
        ("media", "media query", "Apply the style sheet only when the query matches: screen, print, (max-width: 600px), (prefers-color-scheme: dark).", "HTML 4.01"),
        ("as", "audio | document | embed | fetch | font | image | object | script | style | track | video | worker", "With rel=preload or modulepreload: the type of content being loaded, so the browser can prioritise it correctly.", "Living Standard"),
        ("crossorigin", "anonymous | use-credentials", "CORS mode for the request. Required when preloading fonts.", "HTML5"),
        ("hreflang", "language tag", "Language of the linked resource (with rel=alternate).", "HTML 4.01"),
        ("sizes", "any or WxH list", "Icon sizes, for example 16x16 32x32 or any (for SVG).", "HTML5"),
        ("title", "text", "For style sheets: the name of an alternate style sheet set. For feeds: the feed title.", "HTML 2.0"),
        ("integrity", "hash", "Subresource Integrity hash; the browser refuses the file if it does not match.", "SRI spec"),
        ("referrerpolicy", "referrer policy", "Referrer to send when fetching.", "HTML5"),
        ("fetchpriority", "high | low | auto", "Download priority hint.", "Living Standard"),
        ("blocking", "render", "Block rendering until the resource is loaded (for stylesheets/preloads/expect).", "Living Standard"),
        ("disabled", "boolean", "For style sheets: do not apply.", "HTML5"),
        ("imagesrcset / imagesizes", "srcset / sizes syntax", "With rel=preload as=image: responsive image candidates.", "Living Standard"),
        ("color", "colour", "With rel=mask-icon (Safari pinned tab).", "Non-standard"),
        ("charset", "encoding", "Obsolete. Character set of the resource.", "HTML 4.01"),
        ("rev", "link types", "Obsolete. Reverse relationship.", "HTML 4.01"),
        ("target", "browsing context", "Obsolete on link.", "HTML 4.01"),
    ],
    examples=[
        ("Style sheets", "<link rel=\"stylesheet\" href=\"style.css\">\n<link rel=\"stylesheet\" href=\"print.css\" media=\"print\">\n<link rel=\"stylesheet\" href=\"dark.css\" media=\"(prefers-color-scheme: dark)\">", ""),
        ("Icons", "<link rel=\"icon\" href=\"favicon.ico\" sizes=\"32x32\">\n<link rel=\"icon\" href=\"icon.svg\" type=\"image/svg+xml\">\n<link rel=\"apple-touch-icon\" href=\"apple-touch-icon.png\">\n<link rel=\"manifest\" href=\"manifest.webmanifest\">", ""),
        ("Performance hints", "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n<link rel=\"preload\" href=\"hero.jpg\" as=\"image\" fetchpriority=\"high\">\n<link rel=\"preload\" href=\"font.woff2\" as=\"font\" type=\"font/woff2\" crossorigin>\n<link rel=\"prefetch\" href=\"next-page.html\">", ""),
        ("SEO and alternates", "<link rel=\"canonical\" href=\"https://example.com/books/html\">\n<link rel=\"alternate\" hreflang=\"ar\" href=\"https://example.com/ar/books/html\">\n<link rel=\"alternate\" type=\"application/rss+xml\" title=\"Blog feed\" href=\"/feed.xml\">", ""),
        ("Google Fonts", "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n<link href=\"https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap\" rel=\"stylesheet\">", ""),
    ],
    a11y=["Alternate style sheets (rel=\"alternate stylesheet\" title=\"High contrast\") can offer accessible themes in browsers that support switching."],
    mistakes=["Forgetting rel.", "Using <link> to make a hyperlink (that is <a>).", "Wrong path to the CSS file (check the browser's network tab).", "Writing </link>."],
    related=["style", "a", "script", "meta", "head"], css="link { display: none; }",
),

dict(
    name="listing", title="Listing (obsolete)", cat="Obsolete text content",
    versions="HTML 1, HTML 2.0 (deprecated); obsolete", status="obsolete",
    desc=[
        "The <listing> element, from the 1991 tag set, displayed its content in a monospace font exactly as "
        "written, like <pre> but originally at a smaller size and without interpreting markup. It was "
        "deprecated already in HTML 2.0 and removed in HTML 3.2. Use <pre>, optionally with <code>.",
    ],
    syntax="<listing>text</listing>", void=False, display="block",
    categories="Historical", content="Text", parents="Flow content", omission="Neither", dom="HTMLPreElement",
    attrs=[],
    examples=[("Replacement", "<pre><code>line 1\nline 2</code></pre>", "")],
    a11y=[], mistakes=["Any use."], related=["pre", "xmp", "plaintext"], css="listing { display: block; font-family: monospace; white-space: pre; margin: 1em 0; }",
),

dict(
    name="main", title="Main content", cat="Content sectioning",
    versions="HTML 5.1 (2016)", status="current",
    desc=[
        "The <main> element represents the dominant content of the <body>: the content that is directly "
        "related to, or expands upon, the central topic of the page or the central function of the "
        "application. It excludes content repeated across pages such as the site header, navigation, "
        "sidebars, search box, logo and footer.",
        "A document must not have more than one visible <main>; additional <main> elements are allowed only "
        "if all but one carry the hidden attribute. <main> must not be a descendant of <article>, <aside>, "
        "<footer>, <header> or <nav>. It is exposed as the 'main' landmark, which lets screen reader users "
        "skip straight to the content, and it is the natural target for a 'skip to content' link.",
    ],
    syntax="<main>...</main>", void=False, display="block",
    categories="Flow content, palpable content", content="Flow content",
    parents="<html>, <body>, <div>, <form> without an accessible name, and autonomous custom elements; not inside article, aside, footer, header or nav",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Page structure with skip link",
         "<body>\n  <a href=\"#content\" class=\"skip\">Skip to main content</a>\n  <header>...</header>\n  <nav>...</nav>\n  <main id=\"content\">\n    <h1>Page title</h1>\n    <p>The unique content of this page.</p>\n  </main>\n  <aside>...</aside>\n  <footer>...</footer>\n</body>", ""),
        ("Visually hidden skip link that appears on focus", "<style>\n  .skip { position: absolute; left: -999px; }\n  .skip:focus { left: 8px; top: 8px; background: #fff; padding: 8px; }\n</style>", ""),
        ("Single-page app views", "<main id=\"home\">Home view</main>\n<main id=\"cart\" hidden>Cart view</main>", "Only one is visible at a time."),
    ],
    a11y=["The 'main' landmark is one of the most used shortcuts in screen readers; every page should have exactly one."],
    mistakes=["Two visible mains.", "Placing main inside article or nav.", "Putting the header and footer inside main."],
    related=["header", "footer", "nav", "aside", "article", "section"], css="main { display: block; }",
),

dict(
    name="map", title="Image map", cat="Image and multimedia",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <map> element, together with <area> elements, defines a client-side image map: an image with "
        "several clickable regions each linking to a different destination. The map is connected to an "
        "<img> through the img's usemap attribute, which must be # followed by the map's name.",
    ],
    syntax="<map name=\"n\">\n  <area ...>\n</map>\n<img usemap=\"#n\" ...>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Transparent",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLMapElement",
    attrs=[("name", "text", "Required. The map's name, without #, unique among maps. If id is also given it must have the same value.", "HTML 3.2")],
    examples=[
        ("Navigation image with two regions",
         "<img src=\"banner.png\" alt=\"Shop banner\" usemap=\"#banner\" width=\"600\" height=\"100\">\n<map name=\"banner\">\n"
         "  <area shape=\"rect\" coords=\"0,0,300,100\" href=\"books.html\" alt=\"Books\">\n  <area shape=\"rect\" coords=\"300,0,600,100\" href=\"deals.html\" alt=\"Deals\">\n</map>", ""),
    ],
    a11y=["Each area needs alt text. Provide an equivalent text list of links if the map is complex."],
    mistakes=["usemap without #.", "Map name mismatching.", "Coordinates for a different image size than displayed."],
    related=["area", "img"], css="map { display: inline; }",
),

dict(
    name="mark", title="Highlighted (marked) text", cat="Text-level semantics",
    versions="HTML5", status="current",
    desc=[
        "The <mark> element represents text that is marked or highlighted for reference because of its "
        "relevance in the current context. Typical uses: highlighting the search terms in a page of results, "
        "or drawing attention to a passage in a quotation that the current text discusses. Browsers render "
        "it with a yellow background, like a highlighter pen.",
        "Do not confuse it with <strong> (importance) or <em> (emphasis). <mark> is about relevance to the "
        "reader's current activity, not about the author's intent.",
    ],
    syntax="<mark>text</mark>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Search results", "<p>Results for 'footer': ... the <mark>footer</mark> element represents the <mark>footer</mark> of its section ...</p>", ""),
        ("Highlighting part of a quotation", "<blockquote><p>Any tag you learn is <mark>a tool you keep</mark>.</p></blockquote>\n<p>The phrase 'a tool you keep' is the key idea.</p>", ""),
        ("Custom colour", "<style>\n  mark { background: #ffe58a; color: inherit; padding: 0 2px; }\n</style>", ""),
    ],
    a11y=["Not announced by default; if the highlight matters, add visually hidden text such as '[highlight start]'."],
    mistakes=["Using <mark> for decorative colour.", "Using <mark> instead of <strong>."],
    related=["strong", "em", "span"], css="mark { background-color: yellow; color: black; }",
),

dict(
    name="marquee", title="Scrolling text (obsolete)", cat="Obsolete presentational",
    versions="Internet Explorer 2 (1995), never standard; obsolete in HTML5 (but its behaviour is specified for compatibility)", status="obsolete",
    desc=[
        "The <marquee> element scrolled its content horizontally or vertically across the screen. It was a "
        "Microsoft extension that became infamous alongside Netscape's <blink>. HTML5 lists it as obsolete "
        "but, because so many old pages use it, browsers still implement it. Moving text is hard to read "
        "and distracting; if you need an animation, use CSS animations with a pause control and respect the "
        "prefers-reduced-motion media query.",
    ],
    syntax="<marquee>text</marquee>", void=False, display="inline-block",
    categories="Historical", content="Flow content", parents="Flow content", omission="Neither", dom="HTMLMarqueeElement",
    attrs=[
        ("behavior", "scroll | slide | alternate", "Scrolling style.", "IE"), ("direction", "left | right | up | down", "Scroll direction.", "IE"),
        ("loop", "integer | -1", "Repeat count.", "IE"), ("scrollamount", "pixels", "Distance per step.", "IE"), ("scrolldelay", "ms", "Delay between steps.", "IE"),
        ("truespeed", "boolean", "Allow delays under 60 ms.", "IE"), ("bgcolor", "colour", "Background.", "IE"), ("width / height", "size", "Size.", "IE"),
        ("hspace / vspace", "pixels", "Margins.", "IE"),
    ],
    examples=[("CSS replacement", "<style>\n  @keyframes slide { from { transform: translateX(100%); } to { transform: translateX(-100%); } }\n  .ticker { white-space: nowrap; overflow: hidden; }\n  .ticker span { display: inline-block; animation: slide 12s linear infinite; }\n  @media (prefers-reduced-motion: reduce) { .ticker span { animation: none; } }\n</style>\n<div class=\"ticker\"><span>Breaking news...</span></div>", "")],
    a11y=["Moving text violates WCAG unless it can be paused."], mistakes=["Any use."], related=["blink"], css="marquee { display: inline-block; text-align: initial; }",
),

dict(
    name="math", title="MathML root", cat="Embedded content (MathML)",
    versions="HTML5 (inline MathML)", status="current",
    desc=[
        "The <math> element is the top-level element of MathML (Mathematical Markup Language), which can "
        "be written directly inside HTML5 documents to display mathematical formulas. Inside <math> you use "
        "MathML elements such as <mi> (identifier), <mn> (number), <mo> (operator), <mrow> (group), <mfrac> "
        "(fraction), <msup> (superscript), <msqrt> (square root) and <mtable>. All modern browsers support "
        "MathML Core.",
    ],
    syntax="<math>\n  <mi>x</mi><mo>=</mo><mn>2</mn>\n</math>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content, palpable content", content="MathML elements",
    parents="Any element that accepts phrasing content", omission="Neither", dom="MathMLElement",
    attrs=[("display", "block | inline", "Whether the formula is a block on its own line or inline in text.", "MathML"),
           ("xmlns", "http://www.w3.org/1998/Math/MathML", "Namespace; optional in HTML.", "MathML")],
    examples=[
        ("Quadratic formula",
         "<math display=\"block\">\n  <mi>x</mi><mo>=</mo>\n  <mfrac>\n    <mrow><mo>-</mo><mi>b</mi><mo>&#xB1;</mo><msqrt><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi></msqrt></mrow>\n    <mrow><mn>2</mn><mi>a</mi></mrow>\n  </mfrac>\n</math>", ""),
        ("Inline formula", "<p>The area of a circle is <math><mi>&#x3C0;</mi><msup><mi>r</mi><mn>2</mn></msup></math>.</p>", ""),
    ],
    a11y=["MathML is read by modern screen readers as mathematics; images of formulas are not."],
    mistakes=["Writing formulas as plain text or images.", "Forgetting display=\"block\" for standalone equations."],
    related=["svg", "canvas"], css="math { display: inline; math-style: compact; }\nmath[display=block] { display: block math; math-style: normal; }",
),

dict(
    name="menu", title="Menu (toolbar list)", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01 (deprecated), HTML5 (redefined)", status="current",
    desc=[
        "The <menu> element is a semantic alternative to <ul> for a list of commands or actions, such as "
        "a toolbar of buttons. Each command is an <li> containing a <button> or similar control. Browsers "
        "render it identically to <ul>.",
        "Its history is long: in HTML 1 and 2 it was a compact list like <dir>; HTML 4.01 deprecated it; "
        "early HTML5 drafts turned it into a rich context-menu system with type=\"context\" and "
        "<menuitem> children, which no browser except Firefox implemented and which was removed; the "
        "current definition is simply 'an unordered list of interactive items'.",
    ],
    syntax="<menu>\n  <li><button>Action</button></li>\n</menu>", void=False, display="block",
    categories="Flow content; palpable if it has at least one <li>", content="Zero or more <li>, <script>, <template>",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLMenuElement",
    attrs=[("compact", "boolean", "Obsolete. Compact rendering.", "HTML 2.0"),
           ("type", "context | toolbar | list", "Obsolete. From the abandoned HTML5 context menu design.", "HTML5 draft (removed)"),
           ("label", "text", "Obsolete. Menu label (context menus).", "HTML5 draft (removed)")],
    examples=[
        ("Editor toolbar", "<menu>\n  <li><button onclick=\"copy()\">Copy</button></li>\n  <li><button onclick=\"cut()\">Cut</button></li>\n  <li><button onclick=\"paste()\">Paste</button></li>\n</menu>", ""),
        ("Horizontal toolbar styling", "<style>\n  menu { display: flex; gap: 8px; list-style: none; padding: 0; margin: 0; }\n</style>", ""),
    ],
    a11y=["Exposed as a list, the same as <ul>. Add role=\"toolbar\" if the list is a real toolbar with arrow-key navigation."],
    mistakes=["Expecting native context menus from type=\"context\".", "Using <menu> for navigation links (use <nav><ul>)."],
    related=["ul", "li", "button", "nav", "menuitem"], css="menu { display: block; list-style-type: disc; margin: 1em 0; padding-inline-start: 40px; }",
),

dict(
    name="menuitem", title="Menu item (obsolete)", cat="Obsolete interactive",
    versions="HTML5 draft (Firefox only); removed 2017", status="obsolete",
    desc=[
        "The <menuitem> element represented a command in a <menu type=\"context\">, letting a page add "
        "custom items to the browser's right-click menu. Only Firefox implemented it; it was removed from "
        "the standard in 2017 and from Firefox in 2020. Build custom menus with lists, buttons and JavaScript "
        "(or the popover attribute) instead.",
    ],
    syntax="<menuitem label=\"Refresh\" onclick=\"...\">", void=True, display="none",
    categories="Historical", content="None", parents="<menu>", omission="No end tag", dom="HTMLUnknownElement",
    attrs=[("label", "text", "Item text.", "HTML5 draft"), ("type", "command | checkbox | radio", "Kind of item.", "HTML5 draft"),
           ("icon", "URL", "Icon image.", "HTML5 draft"), ("checked, disabled, default, radiogroup, command", "various", "State and grouping.", "HTML5 draft")],
    examples=[("Replacement", "<button popovertarget=\"m\">Options</button>\n<menu id=\"m\" popover>\n  <li><button>Refresh</button></li>\n</menu>", "")],
    a11y=[], mistakes=["Any use."], related=["menu", "button"], css="",
),

dict(
    name="meta", title="Metadata", cat="Document metadata",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <meta> element represents metadata about the document that cannot be expressed by <title>, "
        "<base>, <link>, <style> or <script>. It is a void element placed in <head>. Depending on which "
        "attributes are present it does one of four things: declares the character encoding (charset); "
        "provides document-level metadata as a name/content pair (name); simulates an HTTP response header "
        "(http-equiv); or supplies microdata (itemprop).",
        "The most important meta tags on every page are charset and viewport. Other frequently used names "
        "are description (shown in search results), robots, author, theme-color and the Open Graph "
        "(property=\"og:...\") and Twitter card tags used when a page is shared on social networks. Part 9 "
        "contains the full list of standard meta names.",
    ],
    syntax="<meta charset=\"utf-8\">\n<meta name=\"description\" content=\"...\">", void=True, display="none",
    categories="Metadata content; flow and phrasing content if itemprop is present", content="None (void element)",
    parents="<head>; <noscript> in head; anywhere if itemprop is present", omission="No end tag", dom="HTMLMetaElement",
    attrs=[
        ("charset", "utf-8", "Declares the document's character encoding. The only valid value in HTML5 is utf-8 (case-insensitive). Must be in the first 1024 bytes.", "HTML5"),
        ("name", "metadata name", "The kind of metadata: application-name, author, description, generator, keywords, referrer, theme-color, color-scheme, viewport, robots, googlebot, creator, publisher, and more.", "HTML 2.0"),
        ("content", "text", "The value for name or http-equiv. Required with them.", "HTML 2.0"),
        ("http-equiv", "content-type | default-style | refresh | content-security-policy | x-ua-compatible", "Pragma directive that acts like an HTTP header.", "HTML 2.0"),
        ("media", "media query", "With name=theme-color: apply only when the query matches.", "Living Standard"),
        ("property", "text", "Not in the HTML standard but universally used for RDFa / Open Graph tags such as og:title.", "RDFa"),
        ("itemprop", "text", "Microdata property name.", "HTML5 microdata"),
        ("scheme", "text", "Obsolete. Interpretation scheme for content.", "HTML 4.01"),
    ],
    examples=[
        ("The essential pair", "<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">", "Without the viewport tag, phones render the page as if it were 980px wide and shrink it."),
        ("Search engine metadata", "<meta name=\"description\" content=\"Buy PDF books in Arabic and English; pay with mobile wallet and download instantly.\">\n<meta name=\"robots\" content=\"index, follow\">\n<meta name=\"author\" content=\"Book Store team\">", ""),
        ("Social sharing (Open Graph and Twitter)", "<meta property=\"og:title\" content=\"Learn HTML\">\n<meta property=\"og:description\" content=\"A complete reference.\">\n<meta property=\"og:image\" content=\"https://example.com/cover.jpg\">\n<meta property=\"og:url\" content=\"https://example.com/html\">\n<meta name=\"twitter:card\" content=\"summary_large_image\">", ""),
        ("Theme colour and colour scheme", "<meta name=\"theme-color\" content=\"#e60000\">\n<meta name=\"theme-color\" content=\"#111\" media=\"(prefers-color-scheme: dark)\">\n<meta name=\"color-scheme\" content=\"light dark\">", ""),
        ("Redirect after 5 seconds (use sparingly)", "<meta http-equiv=\"refresh\" content=\"5; url=https://example.com/new-page\">", ""),
        ("Content Security Policy", "<meta http-equiv=\"content-security-policy\" content=\"default-src 'self'; img-src https:\">", ""),
        ("Old HTML 4 encoding declaration", "<!-- HTML 4.01 -->\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n\n<!-- HTML5 -->\n<meta charset=\"utf-8\">", ""),
    ],
    a11y=["Never use <meta name=\"viewport\" content=\"user-scalable=no\"> or maximum-scale=1; it stops users zooming and fails WCAG.",
          "Automatic refresh/redirect disorients users; prefer server-side redirects."],
    mistakes=["Placing charset after other content or after 1024 bytes.", "Using keywords meta (ignored by search engines since 2009).", "Writing </meta>."],
    related=["head", "title", "link", "base"], css="meta { display: none; }",
),

dict(
    name="meter", title="Scalar measurement (gauge)", cat="Forms",
    versions="HTML5", status="current",
    desc=[
        "The <meter> element represents a scalar measurement within a known range, or a fractional value: "
        "disk usage, the relevance of a search result, password strength, a score out of ten, temperature "
        "within safe limits. Browsers render it as a gauge bar whose colour changes depending on whether "
        "the value is in the optimum, suboptimal or bad region defined by low, high and optimum.",
        "Do not use <meter> for progress of a task; that is what <progress> is for. And do not use it for "
        "values with no known maximum (such as a bank balance) because the gauge needs a range.",
    ],
    syntax="<meter value=\"0.6\">60%</meter>", void=False, display="inline-block",
    categories="Flow content, phrasing content, labelable, palpable content", content="Phrasing content, but no <meter> descendants",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLMeterElement",
    attrs=[
        ("value", "number", "Required. The current value, between min and max.", "HTML5"),
        ("min", "number", "Lower bound of the range. Default 0.", "HTML5"),
        ("max", "number", "Upper bound. Default 1.", "HTML5"),
        ("low", "number", "Upper bound of the 'low' region.", "HTML5"),
        ("high", "number", "Lower bound of the 'high' region.", "HTML5"),
        ("optimum", "number", "The ideal value. Determines which region is shown as good (green) versus bad (red/yellow).", "HTML5"),
        ("form", "form id", "Associated form (for labelling purposes).", "HTML5"),
    ],
    examples=[
        ("Disk usage", "<label for=\"disk\">Disk usage</label>\n<meter id=\"disk\" value=\"70\" min=\"0\" max=\"100\" low=\"60\" high=\"85\" optimum=\"20\">70%</meter>", "Because optimum is low, 70 (above low) shows in yellow and anything above 85 in red."),
        ("Score out of ten", "<p>Rating: <meter value=\"8\" min=\"0\" max=\"10\">8 out of 10</meter></p>", ""),
        ("Fraction", "<meter value=\"0.25\">25%</meter>", "Default range 0 to 1."),
    ],
    a11y=["Provide the value as text inside the element or in a label; the bar alone is not enough.", "Always label the meter."],
    mistakes=["Using it as a progress bar.", "Omitting value.", "Value outside min-max (it is clamped)."],
    related=["progress", "output", "input"], css="meter { display: inline-block; appearance: auto; }",
),

dict(
    name="multicol", title="Multi-column text (non-standard, obsolete)", cat="Obsolete presentational",
    versions="Netscape 3 only; never standard", status="obsolete",
    desc=[
        "The <multicol> element split its content into newspaper-style columns. It existed only in "
        "Netscape Navigator 3 and 4 and was never standardised. Use the CSS multi-column properties "
        "(column-count, column-width, column-gap) instead.",
    ],
    syntax="<multicol cols=\"3\" gutter=\"20\">text</multicol>", void=False, display="block",
    categories="Historical", content="Flow content", parents="Flow content", omission="Neither", dom="HTMLUnknownElement",
    attrs=[("cols", "integer", "Number of columns.", "Netscape"), ("gutter", "pixels", "Space between columns.", "Netscape"), ("width", "pixels", "Column width.", "Netscape")],
    examples=[("CSS replacement", "<div style=\"column-count: 3; column-gap: 20px\">Long text...</div>", "")],
    a11y=[], mistakes=["Any use."], related=["div"], css="",
),

dict(
    name="nav", title="Navigation section", cat="Content sectioning",
    versions="HTML5", status="current",
    desc=[
        "The <nav> element represents a section of the page whose purpose is to provide navigation links, "
        "either within the current document or to other documents. Typical uses are the main site menu, a "
        "table of contents, breadcrumbs, pagination and 'previous/next' links.",
        "Not every group of links needs a <nav>; it is intended for major navigation blocks. The list of "
        "links in a page footer, for example, is usually fine as a plain list, although a <nav> there is "
        "also acceptable. A page can have several <nav> elements; give each an aria-label so screen reader "
        "users can tell them apart. Links inside a <nav> are conventionally wrapped in a <ul>.",
    ],
    syntax="<nav>\n  <ul>\n    <li><a href=\"...\">Link</a></li>\n  </ul>\n</nav>", void=False, display="block",
    categories="Flow content, sectioning content, palpable content", content="Flow content",
    parents="Any element that accepts flow content, but not <address>", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Main site navigation",
         "<nav aria-label=\"Main\">\n  <ul>\n    <li><a href=\"/\" aria-current=\"page\">Home</a></li>\n    <li><a href=\"/books\">Books</a></li>\n    <li><a href=\"/about\">About</a></li>\n    <li><a href=\"/contact\">Contact</a></li>\n  </ul>\n</nav>", ""),
        ("Breadcrumbs", "<nav aria-label=\"Breadcrumb\">\n  <ol>\n    <li><a href=\"/\">Home</a></li>\n    <li><a href=\"/books\">Books</a></li>\n    <li aria-current=\"page\">Learn HTML</li>\n  </ol>\n</nav>", ""),
        ("Horizontal menu CSS", "<style>\n  nav ul { display: flex; gap: 24px; list-style: none; margin: 0; padding: 0; }\n  nav a { text-decoration: none; color: #1b2431; font-weight: 600; }\n  nav a[aria-current=\"page\"] { border-bottom: 2px solid #e60000; }\n</style>", ""),
        ("Table of contents", "<nav aria-label=\"On this page\">\n  <h2>Contents</h2>\n  <ol>\n    <li><a href=\"#intro\">Introduction</a></li>\n    <li><a href=\"#tags\">Tags</a></li>\n  </ol>\n</nav>", ""),
    ],
    a11y=["Exposed as the 'navigation' landmark.", "Label multiple navs with aria-label.", "Mark the current page with aria-current=\"page\".",
          "Provide a skip link so keyboard users can bypass long menus."],
    mistakes=["Wrapping every link group in <nav>.", "Putting non-navigation content inside.", "Not using a list for the links."],
    related=["header", "footer", "a", "ul", "menu", "main"], css="nav { display: block; }",
),

dict(
    name="nobr", title="No line break (non-standard, obsolete)", cat="Obsolete presentational",
    versions="Netscape / IE extension, never standard; obsolete", status="obsolete",
    desc=[
        "The <nobr> element prevented the browser from wrapping its text onto a new line. It was never "
        "standardised. Use CSS white-space: nowrap instead.",
    ],
    syntax="<nobr>text that will not wrap</nobr>", void=False, display="inline",
    categories="Historical", content="Phrasing content", parents="Phrasing content", omission="Neither", dom="HTMLElement",
    attrs=[],
    examples=[("CSS replacement", "<span style=\"white-space: nowrap\">+20 100 000 0000</span>", "")],
    a11y=[], mistakes=["Any use."], related=["wbr", "br"], css="nobr { white-space: nowrap; }",
),

dict(
    name="noembed", title="Fallback for embed (obsolete)", cat="Obsolete embedded content",
    versions="Netscape extension; obsolete", status="obsolete",
    desc=[
        "The <noembed> element provided fallback content for browsers that did not support <embed>. It "
        "was never standard and is obsolete. Use <object> with fallback content, or <video>/<audio> with "
        "fallback content inside them.",
    ],
    syntax="<noembed>fallback</noembed>", void=False, display="none",
    categories="Historical", content="Flow content", parents="Flow content", omission="Neither", dom="HTMLElement",
    attrs=[],
    examples=[("Replacement", "<object data=\"movie.mp4\" type=\"video/mp4\">\n  <p>Your browser cannot play this video. <a href=\"movie.mp4\">Download it</a>.</p>\n</object>", "")],
    a11y=[], mistakes=["Any use."], related=["embed", "object"], css="noembed { display: none; }",
),

dict(
    name="noframes", title="Fallback for frames (obsolete)", cat="Obsolete frames",
    versions="HTML 4.01 Frameset; obsolete in HTML5", status="obsolete",
    desc=[
        "The <noframes> element contained content to display in browsers that did not support frames. It "
        "became obsolete together with <frameset> and <frame> in HTML5.",
    ],
    syntax="<noframes><body>fallback</body></noframes>", void=False, display="none",
    categories="Historical", content="Flow content (a <body>)", parents="<frameset>", omission="Neither", dom="HTMLElement",
    attrs=[],
    examples=[("Historical", "<frameset cols=\"200,*\">\n  <frame src=\"menu.html\">\n  <frame src=\"main.html\">\n  <noframes><body><p>This page uses frames.</p></body></noframes>\n</frameset>", "")],
    a11y=[], mistakes=["Any use."], related=["frameset", "frame"], css="noframes { display: none; }",
),

dict(
    name="noscript", title="Fallback when scripting is disabled", cat="Scripting",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <noscript> element defines content to be shown only if scripting is disabled in the browser "
        "or the browser does not support scripting. When scripting is enabled the content is ignored "
        "entirely (in fact the parser treats it as raw text). It may be used in <head> (containing only "
        "<link>, <style> and <meta>) and in <body>.",
        "Common uses: a warning that the site requires JavaScript, a non-JavaScript version of a widget, "
        "or a <link> to a style sheet that only applies when scripts are off. Tracking pixels from analytics "
        "services also use it as a fallback.",
    ],
    syntax="<noscript>fallback content</noscript>", void=False, display="inline",
    categories="Metadata content, flow content, phrasing content",
    content="In <head>: <link>, <style>, <meta>. In <body>: transparent content, but no <noscript> descendants",
    parents="<head> and any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Warning message", "<noscript>\n  <p><strong>This page works best with JavaScript enabled.</strong></p>\n</noscript>", ""),
        ("Non-JavaScript style sheet", "<head>\n  <noscript><link rel=\"stylesheet\" href=\"no-js.css\"></noscript>\n</head>", ""),
        ("Image fallback for lazy-loaded pictures", "<img data-src=\"big.jpg\" alt=\"Sunset\" class=\"lazy\">\n<noscript><img src=\"big.jpg\" alt=\"Sunset\"></noscript>", ""),
    ],
    a11y=["Do not assume screen reader users have scripts disabled; almost all use JavaScript-enabled browsers."],
    mistakes=["Nesting noscript.", "Expecting noscript content to appear when a script merely fails to load (it appears only when scripting is off)."],
    related=["script", "template"], css="noscript { display: inline; }",
),

dict(
    name="object", title="External object", cat="Embedded content",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <object> element represents an external resource, treated as an image, a nested browsing "
        "context (like an iframe) or a resource handled by a plug-in, depending on its type. It was "
        "introduced in HTML 4.01 as a universal replacement for <img>, <applet> and <embed>. Unlike <embed>, "
        "it accepts fallback content between its tags, shown if the resource cannot be displayed, and it "
        "may contain <param> elements (now obsolete) that pass parameters to plug-ins.",
        "Today <object> is mainly used to embed PDFs and SVG images with fallback. For video, audio and "
        "other pages, the dedicated elements are better.",
    ],
    syntax="<object data=\"URL\" type=\"MIME\" width=\"W\" height=\"H\">fallback</object>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content, listed, form-associated, palpable content; interactive if usemap",
    content="Transparent (fallback content); historically zero or more <param> first", parents="Any element that accepts embedded content",
    omission="Neither tag may be omitted", dom="HTMLObjectElement",
    attrs=[
        ("data", "URL", "The resource URL. Required (or classid historically).", "HTML 4.01"),
        ("type", "MIME type", "The content type of the resource, for example application/pdf, image/svg+xml.", "HTML 4.01"),
        ("name", "text", "Name of the browsing context (for use as a target).", "HTML 4.01"),
        ("width / height", "pixels", "Display size.", "HTML 4.01"),
        ("form", "form id", "Associated form.", "HTML5"),
        ("usemap", "#map", "Image map to use (obsolete in the Living Standard).", "HTML 4.01"),
        ("archive, classid, codebase, codetype, declare, standby, typemustmatch, border, align, hspace, vspace", "various", "Obsolete attributes from HTML 4.01 plug-in usage or presentational attributes. Use CSS or drop them.", "HTML 4.01 / HTML5 (removed)"),
    ],
    examples=[
        ("PDF with fallback link", "<object data=\"catalogue.pdf\" type=\"application/pdf\" width=\"100%\" height=\"600\">\n  <p>Your browser cannot display the PDF. <a href=\"catalogue.pdf\">Download it</a>.</p>\n</object>", ""),
        ("SVG with PNG fallback", "<object data=\"chart.svg\" type=\"image/svg+xml\" width=\"400\" height=\"300\">\n  <img src=\"chart.png\" alt=\"Sales chart for 2026\" width=\"400\" height=\"300\">\n</object>", ""),
    ],
    a11y=["Provide fallback content that is accessible; there is no alt attribute on object.", "Add a title for screen readers when the object is a nested page."],
    mistakes=["Using <object> for video.", "Nested objects several levels deep as a 'fallback chain' for old plug-ins."],
    related=["embed", "iframe", "img", "param", "video"], css="object { display: inline; }",
),

dict(
    name="ol", title="Ordered list", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <ol> element represents an ordered list of items: a list where the order matters, such as "
        "the steps of a recipe, the ranking of a competition, or the chapters of a book. Browsers number "
        "the items automatically. Each item is an <li>. If the order is not meaningful, use <ul> instead.",
        "The type attribute selects the numbering system (numbers, letters, roman numerals), start sets "
        "the first number and reversed counts downward. These attributes are not presentational and remain "
        "valid in HTML5 because changing the numbering style can change the meaning of references such as "
        "'see item iv'. For purely visual changes use CSS list-style-type.",
    ],
    syntax="<ol>\n  <li>First</li>\n  <li>Second</li>\n</ol>", void=False, display="block",
    categories="Flow content; palpable if it has at least one <li>", content="Zero or more <li>, <script>, <template>",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLOListElement",
    attrs=[
        ("type", "1 | a | A | i | I", "Numbering type: decimal (default), lowercase letters, uppercase letters, lowercase roman, uppercase roman.", "HTML 3.2"),
        ("start", "integer", "The number of the first item (always a decimal integer even if type is a or i).", "HTML 3.2"),
        ("reversed", "boolean", "Number the items in descending order.", "HTML5"),
        ("compact", "boolean", "Obsolete. Compact rendering.", "HTML 2.0"),
    ],
    examples=[
        ("Steps", "<ol>\n  <li>Open the editor.</li>\n  <li>Write the HTML.</li>\n  <li>Save as index.html.</li>\n  <li>Open it in the browser.</li>\n</ol>", ""),
        ("Letters and roman numerals", "<ol type=\"A\">\n  <li>Option A</li>\n  <li>Option B</li>\n</ol>\n<ol type=\"i\" start=\"4\">\n  <li>iv</li>\n  <li>v</li>\n</ol>", ""),
        ("Countdown", "<ol reversed>\n  <li>Third place</li>\n  <li>Second place</li>\n  <li>Winner</li>\n</ol>", "Numbers 3, 2, 1."),
        ("Nested numbering with CSS counters", "<style>\n  ol { counter-reset: item; list-style: none; }\n  ol li::before { counter-increment: item; content: counters(item, '.') ' '; }\n</style>\n<ol>\n  <li>Intro\n    <ol>\n      <li>History</li>\n      <li>Syntax</li>\n    </ol>\n  </li>\n</ol>", "Produces 1, 1.1, 1.2."),
        ("Removing the numbers", "<ol style=\"list-style: none; padding: 0\">...</ol>", ""),
    ],
    a11y=["Screen readers announce 'list, 4 items' and the number of each item, which is very helpful for instructions."],
    mistakes=["Using <ol> when order does not matter.", "Writing the numbers by hand inside the items.", "Putting text directly inside <ol> outside of <li>."],
    related=["ul", "li", "menu", "dl"], css="ol { display: block; list-style-type: decimal; margin: 1em 0; padding-inline-start: 40px; }",
),

dict(
    name="optgroup", title="Option group", cat="Forms",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <optgroup> element groups related <option> elements inside a <select> under a non-selectable "
        "heading given by the label attribute. Groups cannot be nested. Disabling an optgroup disables all "
        "its options.",
    ],
    syntax="<select>\n  <optgroup label=\"Group\">\n    <option>...</option>\n  </optgroup>\n</select>", void=False, display="block",
    categories="None", content="Zero or more <option>, <script>, <template>; optionally a <legend> first in newer browsers with customisable select",
    parents="<select>", omission="End tag may be omitted if followed by another <optgroup> or if there is no more content in the parent", dom="HTMLOptGroupElement",
    attrs=[("label", "text", "Required. The group heading shown in the list.", "HTML 4.01"),
           ("disabled", "boolean", "Disables all options in the group.", "HTML 4.01")],
    examples=[
        ("Cities grouped by country",
         "<label for=\"city\">City</label>\n<select id=\"city\" name=\"city\">\n  <optgroup label=\"Egypt\">\n    <option value=\"cai\">Cairo</option>\n    <option value=\"giz\">Giza</option>\n    <option value=\"alx\">Alexandria</option>\n  </optgroup>\n"
         "  <optgroup label=\"Saudi Arabia\">\n    <option value=\"ruh\">Riyadh</option>\n    <option value=\"jed\">Jeddah</option>\n  </optgroup>\n</select>", ""),
    ],
    a11y=["Screen readers announce the group label when entering the group."],
    mistakes=["Omitting label.", "Nesting optgroups.", "Trying to make the group heading selectable."],
    related=["select", "option"], css="optgroup { display: block; font-weight: bold; font-style: normal; }",
),

dict(
    name="option", title="Option", cat="Forms",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <option> element defines one item in a <select> drop-down list, an <optgroup>, or a "
        "<datalist> of suggestions. Its text content is what the user sees; the value attribute is what is "
        "submitted with the form. If value is omitted the text content is submitted instead.",
        "The selected attribute pre-selects the option. In a single-select list only one option should be "
        "selected; in a <select multiple> several may be. The end tag may be omitted.",
    ],
    syntax="<option value=\"v\">Text</option>", void=False, display="block",
    categories="None", content="Text, optionally with escaped characters",
    parents="<select>, <optgroup>, <datalist>",
    omission="End tag may be omitted if followed by another <option> or <optgroup>, or if there is no more content in the parent", dom="HTMLOptionElement",
    attrs=[
        ("value", "text", "The value submitted when this option is selected. Defaults to the text content.", "HTML 2.0"),
        ("selected", "boolean", "Initially selected.", "HTML 2.0"),
        ("disabled", "boolean", "Cannot be selected.", "HTML 4.01"),
        ("label", "text", "Alternative label shown instead of the text content (used mainly in datalist).", "HTML 4.01"),
    ],
    examples=[
        ("Basic select", "<select name=\"size\">\n  <option value=\"\">-- Choose a size --</option>\n  <option value=\"s\">Small</option>\n  <option value=\"m\" selected>Medium</option>\n  <option value=\"l\">Large</option>\n</select>", "The first option with an empty value acts as a placeholder; combine with required to force a choice."),
        ("Disabled placeholder that cannot be re-selected", "<select required>\n  <option value=\"\" disabled selected>Select a country</option>\n  <option>Egypt</option>\n</select>", ""),
        ("Datalist options with labels", "<datalist id=\"codes\">\n  <option value=\"EG\" label=\"Egypt\">\n  <option value=\"SA\" label=\"Saudi Arabia\">\n</datalist>", ""),
    ],
    a11y=["Keep option text short and unique.", "Do not rely on colour alone to differentiate options."],
    mistakes=["Nesting HTML inside option (only text is allowed).", "Multiple selected options in a single select (the last wins).", "Forgetting the value so a long label is submitted."],
    related=["select", "optgroup", "datalist"], css="option { display: block; padding: 0 2px 1px; white-space: nowrap; min-height: 1.2em; }",
),

dict(
    name="output", title="Calculation or user-action result", cat="Forms",
    versions="HTML5", status="current",
    desc=[
        "The <output> element is a container into which a site or app can inject the result of a "
        "calculation or the outcome of a user action, for example the total price in a cart, the current "
        "value of a range slider, or a status message. It is form-associated and labelable, and it is an "
        "ARIA live region by default (role=\"status\"), which means screen readers announce changes to its "
        "content automatically.",
    ],
    syntax="<output name=\"result\" for=\"a b\">0</output>", void=False, display="inline",
    categories="Flow content, phrasing content, listed, labelable, resettable, form-associated, palpable content",
    content="Phrasing content", parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLOutputElement",
    attrs=[
        ("for", "space-separated ids", "The elements that contributed to the calculation.", "HTML5"),
        ("form", "form id", "Associated form.", "HTML5"),
        ("name", "text", "Name of the output (not submitted with the form).", "HTML5"),
    ],
    examples=[
        ("Live sum of two inputs",
         "<form oninput=\"total.value = Number(a.value) + Number(b.value)\">\n  <input type=\"number\" id=\"a\" name=\"a\" value=\"0\"> +\n  <input type=\"number\" id=\"b\" name=\"b\" value=\"0\"> =\n  <output name=\"total\" for=\"a b\">0</output>\n</form>", ""),
        ("Showing a slider's value", "<label for=\"vol\">Volume</label>\n<input type=\"range\" id=\"vol\" min=\"0\" max=\"100\" value=\"50\" oninput=\"v.value = this.value\">\n<output id=\"v\" for=\"vol\">50</output>", ""),
    ],
    a11y=["Because it is a live region, changes are announced; do not update it dozens of times per second with noise."],
    mistakes=["Using a <span> for results that should be announced.", "Expecting the value to be submitted."],
    related=["input", "form", "meter", "progress"], css="output { display: inline; unicode-bidi: isolate; }",
),

]
