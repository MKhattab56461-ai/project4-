# -*- coding: utf-8 -*-
"""Element reference entries, letters A to D."""

ELEMENTS = [

dict(
    name="a", title="Anchor (hyperlink)", cat="Text-level semantics",
    versions="HTML 1 (1991), HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <a> element (anchor) creates a hyperlink to another web page, a file, a location within the "
        "same page, an email address, a telephone number, or any other resource that can be identified by a "
        "URL. Hyperlinks are the defining feature of the World Wide Web and <a> was one of the very first "
        "elements created by Tim Berners-Lee in 1991.",
        "The content of the <a> element is what the visitor sees and clicks. It is usually text, but in "
        "HTML5 it may also be an image, a whole card of content, or any other flow content, as long as the "
        "link does not contain another link or an interactive element such as a button.",
        "If the href attribute is missing the element is a placeholder: it is rendered as plain text, is not "
        "focusable and is not announced as a link by screen readers. This is useful, for example, for the "
        "current page in a navigation menu.",
        "In HTML 4 the <a> element was also used to define named anchors (<a name=\"top\">) that other links "
        "could jump to. In HTML5 the name attribute is obsolete; use the id attribute on any element instead.",
    ],
    syntax="<a href=\"URL\">link text</a>", void=False, display="inline",
    categories="Flow content, phrasing content, interactive content (when href is present), palpable content",
    content="Transparent (whatever the parent allows), but it must not contain interactive content or another <a>",
    parents="Any element that accepts phrasing content or flow content",
    omission="Neither the start tag nor the end tag may be omitted",
    dom="HTMLAnchorElement",
    attrs=[
        ("href", "URL", "The address the link points to. It may be absolute (https://example.com/page), relative "
         "(about.html, ../images/photo.jpg), a fragment (#section-2), or a special scheme (mailto:, tel:, sms:, "
         "javascript:). Without href the element is not a link.", "HTML 1"),
        ("target", "_self | _blank | _parent | _top | frame-name",
         "Where to open the linked document. _self (default) opens it in the same browsing context; _blank opens "
         "a new tab or window; _parent opens it in the parent frame; _top opens it in the full window, "
         "replacing all frames. A custom name targets an <iframe> with that name.", "HTML 4.01"),
        ("rel", "space-separated link types",
         "The relationship between the current document and the linked document. Common values: nofollow, "
         "noopener, noreferrer, external, alternate, author, bookmark, help, license, next, prev, search, tag. "
         "See the link types table in Part 9.", "HTML 4.01"),
        ("download", "empty or filename",
         "Instructs the browser to download the resource instead of navigating to it. If a value is given it is "
         "used as the suggested file name. Only works for same-origin URLs and blob:/data: URLs.", "HTML5"),
        ("hreflang", "BCP 47 language tag", "The language of the linked document, for example en, ar, fr-CA. "
         "Purely advisory.", "HTML 4.01"),
        ("type", "MIME type", "The media type of the linked resource, for example application/pdf. Advisory only.", "HTML 4.01"),
        ("referrerpolicy", "no-referrer | no-referrer-when-downgrade | origin | origin-when-cross-origin | "
         "same-origin | strict-origin | strict-origin-when-cross-origin | unsafe-url",
         "How much referrer information is sent when following the link.", "HTML5"),
        ("ping", "space-separated URLs", "A list of URLs that receive a POST request with the body PING when the "
         "link is followed. Used for tracking.", "HTML5"),
        ("attributionsrc", "empty or URL", "Experimental: registers an attribution source for the Attribution "
         "Reporting API.", "Living Standard"),
        ("charset", "character encoding", "Obsolete. The character encoding of the linked resource. "
         "Use the HTTP Content-Type header instead.", "HTML 4.01 (obsolete in HTML5)"),
        ("coords", "comma-separated numbers", "Obsolete. Coordinates for use with shape in old image maps. "
         "Use <area> instead.", "HTML 4.01 (obsolete in HTML5)"),
        ("name", "text", "Obsolete. Defined a named anchor that could be linked to with #name. Use id instead.", "HTML 1 (obsolete in HTML5)"),
        ("rev", "link types", "Obsolete. Reverse relationship. Use rel instead.", "HTML 4.01 (obsolete in HTML5)"),
        ("shape", "rect | circle | poly | default", "Obsolete. Shape of a clickable region. Use <area> instead.", "HTML 4.01 (obsolete in HTML5)"),
    ],
    examples=[
        ("Basic links",
         "<p>Read the <a href=\"https://developer.mozilla.org/\">MDN documentation</a>.</p>\n"
         "<p>See our <a href=\"about.html\">About page</a>.</p>\n"
         "<p>Jump to the <a href=\"#footer\">bottom of this page</a>.</p>",
         "The first link is absolute, the second is relative to the current page, and the third is a fragment "
         "link that scrolls to the element whose id is footer."),
        ("Opening in a new tab safely",
         "<a href=\"https://example.com\" target=\"_blank\" rel=\"noopener noreferrer\">\n  Example (opens in a new tab)\n</a>",
         "When you use target=\"_blank\" add rel=\"noopener\" so the new page cannot access your page through "
         "window.opener. Modern browsers do this automatically, but adding it is still good practice. Tell the "
         "user that the link opens in a new tab."),
        ("Email, telephone and download links",
         "<a href=\"mailto:info@example.com?subject=Hello\">Email us</a>\n"
         "<a href=\"tel:+201001234567\">Call us: 010 0123 4567</a>\n"
         "<a href=\"report.pdf\" download=\"annual-report-2026.pdf\">Download the report (PDF)</a>",
         "mailto: opens the visitor's email program; tel: dials on a phone; download forces a save dialog "
         "with the suggested file name."),
        ("A link wrapping a whole card (HTML5)",
         "<a href=\"product.html\" class=\"card\">\n"
         "  <img src=\"shoe.jpg\" alt=\"Red running shoe\">\n"
         "  <h3>Running shoe</h3>\n"
         "  <p>450 EGP</p>\n</a>",
         "Since HTML5 an anchor may contain block-level content. The entire card becomes clickable."),
        ("A placeholder link for the current page",
         "<nav>\n  <a>Home</a>\n  <a href=\"shop.html\">Shop</a>\n  <a href=\"contact.html\">Contact</a>\n</nav>",
         "Home has no href, so it is shown as text and is not focusable, which is correct for the page the "
         "visitor is already on. You could also add aria-current=\"page\" to a real link instead."),
    ],
    a11y=[
        "Link text must make sense on its own. Screen reader users often read a list of all links on a page; "
        "'click here' or 'read more' tells them nothing. Prefer 'Download the 2026 price list'.",
        "Do not use the same link text for links that go to different places.",
        "When a link contains only an image, the image's alt text becomes the link text, so it must describe the destination.",
        "Links should look different from ordinary text (usually underlined) and have a visible focus outline.",
        "Do not use javascript: URLs; use a <button> for actions that are not navigation.",
    ],
    mistakes=[
        "Nesting an <a> inside another <a>, or putting a <button> inside an <a>.",
        "Using an <a> without href as a button. Use <button> instead.",
        "Forgetting rel=\"noopener\" with target=\"_blank\" on old browsers.",
        "Using onclick=\"location.href=...\" on a <div> instead of a real link, which breaks keyboard access, right-click and search engines.",
        "Writing the URL with spaces or with backslashes instead of forward slashes.",
    ],
    related=["area", "link", "button", "nav"],
    css="a:-webkit-any-link { color: -webkit-link; cursor: pointer; text-decoration: underline; }",
),

dict(
    name="abbr", title="Abbreviation", cat="Text-level semantics",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <abbr> element marks an abbreviation or acronym. The optional title attribute holds the full "
        "expansion, which most browsers show as a tooltip when the mouse hovers over the text.",
        "Use <abbr> the first time an abbreviation appears in a document, ideally writing the expansion in "
        "the text as well, because tooltips are not available on touch screens and are not read by every "
        "screen reader.",
        "HTML 4.01 also had an <acronym> element for pronounceable abbreviations such as NASA. It was "
        "removed in HTML5; use <abbr> for both.",
    ],
    syntax="<abbr title=\"expansion\">ABBR</abbr>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content",
    content="Phrasing content", parents="Any element that accepts phrasing content",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[
        ("title", "text", "The full expansion of the abbreviation. On <abbr> this attribute has a specific "
         "meaning and should contain nothing else.", "HTML 4.01"),
    ],
    examples=[
        ("Abbreviation with tooltip",
         "<p>The <abbr title=\"World Health Organization\">WHO</abbr> was founded in 1948.</p>",
         "Hovering WHO shows 'World Health Organization'."),
        ("Defining an abbreviation with <dfn>",
         "<p><dfn><abbr title=\"HyperText Markup Language\">HTML</abbr></dfn> is the language of the web.</p>",
         "Wrapping in <dfn> marks this as the place where the term is defined."),
        ("Styling the dotted underline",
         "<style>\n  abbr[title] { text-decoration: underline dotted; cursor: help; }\n</style>\n"
         "<p>Pages are served over <abbr title=\"HyperText Transfer Protocol Secure\">HTTPS</abbr>.</p>",
         "Most browsers already show a dotted underline; this rule makes it consistent."),
    ],
    a11y=["Provide the expansion in plain text at least once; do not rely on the tooltip alone.",
          "Some screen readers can be set to read the title attribute, but it is off by default."],
    mistakes=["Using <acronym>, which is obsolete.", "Putting long explanations in title; it is for the expansion only."],
    related=["dfn", "acronym"],
    css="abbr[title] { text-decoration: underline dotted; }",
),

dict(
    name="acronym", title="Acronym (obsolete)", cat="Obsolete text-level",
    versions="HTML 4.01; obsolete in HTML5", status="obsolete",
    desc=[
        "The <acronym> element marked an acronym: an abbreviation pronounced as a word, such as NASA or "
        "laser. HTML5 removed it because the distinction from <abbr> was confusing and browsers treated the "
        "two identically.",
        "Replace every <acronym> with <abbr>.",
    ],
    syntax="<acronym title=\"expansion\">NASA</acronym>", void=False, display="inline",
    categories="Phrasing content (historical)", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[("title", "text", "The expansion of the acronym.", "HTML 4.01")],
    examples=[("Old code and its replacement",
               "<!-- HTML 4.01 -->\n<acronym title=\"National Aeronautics and Space Administration\">NASA</acronym>\n\n"
               "<!-- HTML5 -->\n<abbr title=\"National Aeronautics and Space Administration\">NASA</abbr>", "")],
    a11y=["Same as <abbr>."], mistakes=["Using it at all in new pages."], related=["abbr"],
    css="acronym { text-decoration: underline dotted; }",
),

dict(
    name="address", title="Contact address", cat="Content sectioning",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <address> element indicates that its content provides contact information for a person, "
        "people or an organisation. When placed inside an <article> it gives the contact details of the "
        "article's author; when placed in the page <footer> or <body> it gives the contact details for the "
        "whole document.",
        "The contact information may be any kind: physical address, email, telephone, URL, social media "
        "handle, geographic coordinates. Despite its name, <address> is not meant for arbitrary postal "
        "addresses (such as the shipping address in an order); it is only for contact details of the author "
        "or owner of the content.",
        "Browsers display <address> in italics by default, exactly as they did in 1991.",
    ],
    syntax="<address>contact information</address>", void=False, display="block",
    categories="Flow content, palpable content",
    content="Flow content, but no heading content, no sectioning content, and no <header>, <footer> or nested <address>",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Contact details in the page footer",
         "<footer>\n  <address>\n    Written by <a href=\"mailto:jane@example.com\">Jane Doe</a>.<br>\n"
         "    Visit us at:<br>\n    Example Ltd.<br>\n    12 Nile Street<br>\n    Giza, Egypt\n  </address>\n</footer>", ""),
        ("Author contact inside an article",
         "<article>\n  <h2>Learning HTML</h2>\n  <p>...</p>\n  <address>Contact the author: <a href=\"tel:+201000000000\">+20 100 000 0000</a></address>\n</article>",
         "Here the address applies to the article only."),
    ],
    a11y=["Screen readers may announce the element as 'contact information', which helps users find it."],
    mistakes=["Using <address> for every postal address on a page (for example in an order form).",
              "Placing headings or sections inside it."],
    related=["footer", "article", "a"],
    css="address { display: block; font-style: italic; }",
),

dict(
    name="applet", title="Java applet (obsolete)", cat="Obsolete embedded content",
    versions="HTML 3.2, HTML 4.01 (deprecated); obsolete in HTML5", status="obsolete",
    desc=[
        "The <applet> element embedded a Java applet in the page. Applets were small Java programs that ran "
        "inside the browser with the help of a plug-in. Java applets were popular in the late 1990s but were "
        "slow, insecure and not supported on mobile devices. HTML 4.01 deprecated <applet> in favour of "
        "<object>, and HTML5 removed it entirely. No modern browser runs applets.",
    ],
    syntax="<applet code=\"MyApplet.class\" width=\"300\" height=\"200\"></applet>", void=False, display="inline-block",
    categories="Embedded content (historical)", content="Zero or more <param> elements followed by fallback content",
    parents="Any element that accepts embedded content", omission="Neither tag may be omitted", dom="HTMLUnknownElement",
    attrs=[
        ("code", "class file name", "The name of the compiled applet class file.", "HTML 3.2"),
        ("codebase", "URL", "The base URL for the applet's class files.", "HTML 3.2"),
        ("archive", "comma-separated URLs", "JAR archives to preload.", "HTML 4.01"),
        ("object", "file name", "A serialised applet file.", "HTML 4.01"),
        ("alt", "text", "Alternative text for browsers without Java.", "HTML 3.2"),
        ("name", "text", "A name so that applets on the same page can find each other.", "HTML 3.2"),
        ("width / height", "pixels", "Size of the applet display area.", "HTML 3.2"),
        ("align", "left | right | top | middle | bottom", "Alignment relative to surrounding text.", "HTML 3.2"),
        ("hspace / vspace", "pixels", "Horizontal and vertical margins.", "HTML 3.2"),
    ],
    examples=[("Historical example",
               "<applet code=\"Clock.class\" width=\"200\" height=\"200\">\n  <param name=\"timezone\" value=\"Africa/Cairo\">\n"
               "  Your browser does not support Java applets.\n</applet>",
               "For comparison, modern pages implement such features with JavaScript and <canvas>.")],
    a11y=["Applets were inaccessible to assistive technology."],
    mistakes=["Any use in a modern page."], related=["object", "embed", "canvas"],
    css="applet { display: inline-block; }",
),

dict(
    name="area", title="Image map area", cat="Image and multimedia",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <area> element defines a clickable region inside an image map. An image map is an image "
        "(<img usemap=\"#name\">) linked to a <map name=\"name\"> element that contains one or more <area> "
        "elements. Each area has a shape and coordinates, and behaves like a hyperlink.",
        "<area> is a void element: it has no content and no closing tag. It may only be used inside <map>.",
    ],
    syntax="<area shape=\"rect\" coords=\"x1,y1,x2,y2\" href=\"URL\" alt=\"text\">", void=True, display="inline",
    categories="Flow content, phrasing content", content="None (void element)",
    parents="<map> (the <area> may be a descendant of <map> at any depth, as long as there is no intervening <a>)",
    omission="No end tag", dom="HTMLAreaElement",
    attrs=[
        ("alt", "text", "Alternative text for the area. Required when href is present so that the link has an "
         "accessible name.", "HTML 3.2"),
        ("coords", "comma-separated numbers", "The coordinates of the shape in CSS pixels measured from the "
         "top-left corner of the image. rect: x1,y1,x2,y2 (top-left and bottom-right). circle: x,y,radius. "
         "poly: x1,y1,x2,y2,... (any number of points).", "HTML 3.2"),
        ("shape", "rect | circle | poly | default", "The shape of the region. default covers the whole image.", "HTML 3.2"),
        ("href", "URL", "The destination of the link.", "HTML 3.2"),
        ("target", "_self | _blank | _parent | _top | name", "Where to open the destination.", "HTML 4.01"),
        ("download", "empty or filename", "Download the resource instead of navigating.", "HTML5"),
        ("rel", "link types", "Relationship of the linked resource.", "HTML5"),
        ("ping", "URLs", "URLs to ping when the link is followed.", "HTML5"),
        ("referrerpolicy", "referrer policy keyword", "Referrer policy for the navigation.", "HTML5"),
        ("nohref", "boolean", "Obsolete. Indicated the area had no link. Simply omit href instead.", "HTML 3.2 (obsolete)"),
        ("type", "MIME type", "Obsolete in HTML5. Type of the linked resource.", "HTML 4.01"),
    ],
    examples=[
        ("A world map with three clickable regions",
         "<img src=\"map.png\" alt=\"Map of the office\" usemap=\"#office\" width=\"400\" height=\"300\">\n"
         "<map name=\"office\">\n"
         "  <area shape=\"rect\" coords=\"0,0,200,150\" href=\"kitchen.html\" alt=\"Kitchen\">\n"
         "  <area shape=\"circle\" coords=\"300,75,50\" href=\"meeting.html\" alt=\"Meeting room\">\n"
         "  <area shape=\"poly\" coords=\"0,150,200,150,100,300\" href=\"desks.html\" alt=\"Desks\">\n"
         "  <area shape=\"default\" href=\"office.html\" alt=\"Whole office\">\n"
         "</map>",
         "The rectangle covers the top-left quarter, the circle has centre (300,75) and radius 50, and the "
         "polygon is a triangle. The default area catches clicks anywhere else."),
    ],
    a11y=["Every <area> with href needs a meaningful alt.",
          "Image maps do not scale well on small screens; consider SVG with real links instead."],
    mistakes=["Forgetting the # in usemap=\"#name\".", "Coordinates that do not match the displayed image size.",
              "Writing a closing </area> tag."],
    related=["map", "img", "a"],
    css="area { display: inline; }",
),

dict(
    name="article", title="Self-contained article", cat="Content sectioning",
    versions="HTML5", status="current",
    desc=[
        "The <article> element represents a complete, self-contained piece of content that would make "
        "sense on its own if it were distributed independently, for example in an RSS feed. Typical uses are "
        "a blog post, a news story, a forum post, a product card, a user comment or an interactive widget.",
        "An <article> usually has its own heading, and may have its own <header>, <footer> and <address>. "
        "Articles can be nested: comments on a blog post are articles inside the post's article.",
        "The test for choosing <article> rather than <section> or <div> is: 'Could this piece be copied to "
        "another site and still make sense?' If yes, it is an article.",
    ],
    syntax="<article>...</article>", void=False, display="block",
    categories="Flow content, sectioning content, palpable content",
    content="Flow content", parents="Any element that accepts flow content, but not inside <address>",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("A blog post",
         "<article>\n  <header>\n    <h2>How I learned HTML</h2>\n    <p>Posted <time datetime=\"2026-09-11\">11 September 2026</time> by Ahmed</p>\n  </header>\n"
         "  <p>It started with a single footer tag...</p>\n"
         "  <footer>\n    <p>Tags: html, learning</p>\n  </footer>\n</article>", ""),
        ("Nested articles for comments",
         "<article>\n  <h2>Post title</h2>\n  <p>Post text.</p>\n  <section>\n    <h3>Comments</h3>\n"
         "    <article>\n      <p>Great post!</p>\n      <footer>- Sara</footer>\n    </article>\n  </section>\n</article>", ""),
        ("Product cards in a shop",
         "<article class=\"product\">\n  <img src=\"book.jpg\" alt=\"Cover of Learn HTML\">\n  <h3>Learn HTML</h3>\n  <p>120 EGP</p>\n  <button>Add to cart</button>\n</article>", ""),
    ],
    a11y=["Screen readers expose <article> with the role 'article' and may let users jump between articles.",
          "Give each article a heading so it can be identified."],
    mistakes=["Using <article> for every box on the page; use <section> or <div> for content that is not self-contained.",
              "Omitting a heading inside the article."],
    related=["section", "aside", "header", "footer", "main", "nav"],
    css="article { display: block; }",
),

dict(
    name="aside", title="Aside (sidebar / tangential content)", cat="Content sectioning",
    versions="HTML5", status="current",
    desc=[
        "The <aside> element represents content that is only indirectly related to the main content around "
        "it. It is often displayed as a sidebar or a call-out box: pull quotes, related links, advertising, "
        "author biographies, glossary definitions, or a list of other articles.",
        "Inside an <article>, an <aside> holds content related to that article. Directly inside <body> or "
        "<main>, it holds content related to the page as a whole, such as a site-wide sidebar.",
    ],
    syntax="<aside>...</aside>", void=False, display="block",
    categories="Flow content, sectioning content, palpable content", content="Flow content",
    parents="Any element that accepts flow content, but not inside <address>", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("A sidebar with related links",
         "<main>\n  <article>\n    <h1>The Nile</h1>\n    <p>The Nile is the longest river in Africa...</p>\n  </article>\n"
         "  <aside>\n    <h2>Related</h2>\n    <ul>\n      <li><a href=\"aswan.html\">Aswan Dam</a></li>\n      <li><a href=\"delta.html\">Nile Delta</a></li>\n    </ul>\n  </aside>\n</main>", ""),
        ("A pull quote inside an article",
         "<article>\n  <p>Learning takes time, but every tag you learn is a tool you keep.</p>\n"
         "  <aside><q>Every tag you learn is a tool you keep.</q></aside>\n  <p>...</p>\n</article>", ""),
    ],
    a11y=["Exposed as a 'complementary' landmark so users can skip to or over it."],
    mistakes=["Using <aside> for parenthetical text inside a paragraph; use parentheses or <span> for that.",
              "Putting the main content in an <aside>."],
    related=["article", "section", "main", "nav"],
    css="aside { display: block; }",
),

dict(
    name="audio", title="Embedded audio", cat="Image and multimedia",
    versions="HTML5", status="current",
    desc=[
        "The <audio> element embeds sound content: music, podcasts, sound effects or recorded speech. The "
        "source may be given with the src attribute or with one or more <source> child elements so that the "
        "browser can choose a format it supports. Content placed inside the element after the <source> "
        "elements is shown only by browsers that do not support <audio> at all.",
        "By default nothing is displayed. Add the controls attribute to show the browser's built-in play, "
        "pause, volume and progress controls, or control playback from JavaScript with the HTMLMediaElement "
        "methods play() and pause().",
        "Browsers block automatic playback with sound until the user has interacted with the page, so "
        "autoplay usually works only together with muted.",
    ],
    syntax="<audio src=\"file.mp3\" controls></audio>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content; interactive and palpable if controls is present",
    content="If src is present: zero or more <track> elements then transparent content with no media elements. "
            "If src is absent: zero or more <source>, then zero or more <track>, then transparent content with no media elements",
    parents="Any element that accepts embedded content", omission="Neither tag may be omitted", dom="HTMLAudioElement",
    attrs=[
        ("src", "URL", "The URL of the audio file. Alternatively use <source> children.", "HTML5"),
        ("controls", "boolean", "Show the browser's playback controls.", "HTML5"),
        ("autoplay", "boolean", "Start playing as soon as enough data has loaded. Usually blocked unless muted.", "HTML5"),
        ("loop", "boolean", "Restart from the beginning when the end is reached.", "HTML5"),
        ("muted", "boolean", "Start with the sound muted.", "HTML5"),
        ("preload", "none | metadata | auto", "A hint about how much to download before playback: nothing, only "
         "metadata such as duration (default in most browsers), or the whole file.", "HTML5"),
        ("crossorigin", "anonymous | use-credentials", "How to handle cross-origin requests, needed when the audio "
         "will be processed with the Web Audio API or canvas.", "HTML5"),
        ("controlslist", "nodownload | nofullscreen | noremoteplayback", "Hides specific built-in controls (non-standard, Chromium).", "Living Standard"),
        ("disableremoteplayback", "boolean", "Disables casting to remote devices.", "Living Standard"),
    ],
    examples=[
        ("Simple player",
         "<audio src=\"song.mp3\" controls>\n  Your browser does not support the audio element.\n  <a href=\"song.mp3\">Download the song</a>.\n</audio>", ""),
        ("Multiple formats with <source>",
         "<audio controls preload=\"metadata\">\n  <source src=\"podcast.opus\" type=\"audio/ogg; codecs=opus\">\n"
         "  <source src=\"podcast.mp3\" type=\"audio/mpeg\">\n  <p>Download the <a href=\"podcast.mp3\">MP3</a>.</p>\n</audio>",
         "The browser uses the first source it can play. Opus is smaller; MP3 works everywhere."),
        ("Controlling playback with JavaScript",
         "<audio id=\"beep\" src=\"beep.wav\"></audio>\n<button onclick=\"document.getElementById('beep').play()\">Play beep</button>", ""),
        ("Background music that loops (muted by default)",
         "<audio src=\"ambient.mp3\" autoplay loop muted></audio>", "The user must unmute it themselves."),
    ],
    a11y=["Provide a transcript for spoken content; <track> captions are supported only on <video> in most browsers.",
          "Always include controls or provide your own accessible buttons.",
          "Never autoplay sound; it is disorienting and can hide a screen reader's speech."],
    mistakes=["Expecting autoplay with sound to work.", "Using a single format that not all browsers support.",
              "Forgetting the type attribute on <source>, which forces the browser to download each file to test it."],
    related=["video", "source", "track", "embed", "object"],
    css="audio:not([controls]) { display: none !important; }",
),

dict(
    name="b", title="Bring attention to (bold)", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <b> element draws the reader's attention to a span of text without giving it extra importance, "
        "emphasis or an alternative voice. Browsers render it in bold. Typical uses are keywords in a summary, "
        "product names in a review, or the lead sentence of an article.",
        "In HTML 4 <b> was a purely presentational element meaning 'bold'. HTML5 redefined it with the meaning "
        "above so that it remains valid, but the standard says to use <b> only as a last resort when no other "
        "element is more appropriate: <strong> for importance, <em> for emphasis, <mark> for relevance, "
        "<h1>-<h6> for headings, and CSS font-weight for pure styling.",
    ],
    syntax="<b>text</b>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Keywords in a product description",
         "<p>This laptop has a <b>15-inch display</b>, <b>16 GB of RAM</b> and a <b>1 TB SSD</b>.</p>",
         "The keywords stand out but are not more 'important' in the <strong> sense."),
        ("Difference between <b> and <strong>",
         "<p><strong>Warning:</strong> the <b>red</b> wire carries current.</p>",
         "'Warning' is important (strong); 'red' is merely highlighted as a keyword (b)."),
    ],
    a11y=["Screen readers do not announce <b> in any special way. Use <strong> when the boldness carries meaning."],
    mistakes=["Using <b> for headings instead of <h1>-<h6>.", "Using <b> for emphasis instead of <em> or <strong>."],
    related=["strong", "em", "i", "mark"],
    css="b { font-weight: bold; }",
),

dict(
    name="base", title="Document base URL", cat="Document metadata",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <base> element specifies the base URL used to resolve all relative URLs in the document, and/or "
        "the default target for all links and forms. There may be only one <base> element per document and "
        "it must be placed in <head>, before any element that uses a URL.",
        "It is a void element. At least one of href or target must be present.",
    ],
    syntax="<base href=\"URL\" target=\"_blank\">", void=True, display="none",
    categories="Metadata content", content="None (void element)", parents="<head> (only one allowed)",
    omission="No end tag", dom="HTMLBaseElement",
    attrs=[
        ("href", "URL", "The base URL. Relative URLs such as images/logo.png are resolved against it.", "HTML 2.0"),
        ("target", "_self | _blank | _parent | _top | name", "The default browsing context for links and forms that do not specify their own target.", "HTML 4.01"),
    ],
    examples=[
        ("Making all relative links point to another server",
         "<head>\n  <base href=\"https://cdn.example.com/assets/\">\n</head>\n<body>\n  <img src=\"logo.png\" alt=\"Logo\">\n  <!-- loads https://cdn.example.com/assets/logo.png -->\n</body>", ""),
        ("Opening every link in a new tab",
         "<head>\n  <base target=\"_blank\">\n</head>", "Individual links can still override this with their own target."),
    ],
    a11y=["Opening all links in new tabs without warning is confusing; use with care."],
    mistakes=["Placing <base> after a <link> or <script> that uses a relative URL; it does not apply retroactively.",
              "Having more than one <base>.", "Forgetting that fragment links (#top) are also affected and will navigate to the base URL."],
    related=["head", "link", "a"],
    css="base { display: none; }",
),

dict(
    name="basefont", title="Base font (obsolete)", cat="Obsolete presentational",
    versions="HTML 3.2, HTML 4.01 (deprecated); obsolete in HTML5", status="obsolete",
    desc=[
        "The <basefont> element set the default font size, colour and face for the whole document. It was "
        "a presentational element from HTML 3.2 and was deprecated in HTML 4.01 in favour of CSS. HTML5 "
        "removed it. Use CSS on the body element instead.",
    ],
    syntax="<basefont size=\"3\" color=\"black\" face=\"Arial\">", void=True, display="none",
    categories="Historical", content="None", parents="<head> or <body>", omission="No end tag", dom="HTMLUnknownElement",
    attrs=[("size", "1 to 7", "Default font size on the 1-7 HTML scale (3 = normal).", "HTML 3.2"),
           ("color", "colour", "Default text colour.", "HTML 4.01"),
           ("face", "comma-separated font names", "Default font family.", "HTML 4.01")],
    examples=[("Replacement in CSS", "<!-- Old -->\n<basefont size=\"4\" face=\"Arial\" color=\"#333\">\n\n<!-- New -->\n<style>\n  body { font: 18px Arial, sans-serif; color: #333; }\n</style>", "")],
    a11y=[], mistakes=["Any use."], related=["font", "body"], css="",
),

dict(
    name="bdi", title="Bidirectional isolate", cat="Text-level semantics",
    versions="HTML5", status="current",
    desc=[
        "The <bdi> element isolates a span of text that might be written in a different direction from the "
        "text around it, so that its direction does not affect the surrounding text. It is essential when "
        "you insert user-generated text of unknown direction, such as user names, into a sentence.",
        "Without isolation, an Arabic or Hebrew name followed by a number in an English sentence can cause "
        "the number and punctuation to appear in the wrong place. <bdi> tells the bidirectional algorithm to "
        "treat the inner text as a separate unit.",
        "It is equivalent to CSS unicode-bidi: isolate, and by default its direction is auto (detected from "
        "the content).",
    ],
    syntax="<bdi>text of unknown direction</bdi>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[("dir", "ltr | rtl | auto", "On <bdi> the default is auto, unlike other elements where dir is inherited.", "HTML5")],
    examples=[
        ("User names in a leaderboard",
         "<ul>\n  <li><bdi>Ahmed</bdi>: 120 points</li>\n  <li><bdi>محمد</bdi>: 95 points</li>\n  <li><bdi>Sara</bdi>: 80 points</li>\n</ul>",
         "Without <bdi> the second line could render as ': 95 points محمد' with the colon misplaced."),
    ],
    a11y=["Improves reading order for screen readers as well as visual order."],
    mistakes=["Using <bdo> when you want isolation; <bdo> forces a direction, <bdi> isolates."],
    related=["bdo", "span"],
    css="bdi { unicode-bidi: isolate; }",
),

dict(
    name="bdo", title="Bidirectional text override", cat="Text-level semantics",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <bdo> element overrides the current text direction and forces its content to be displayed in "
        "the direction given by the dir attribute, character by character, ignoring the Unicode "
        "bidirectional algorithm. The dir attribute is required.",
        "It is rarely needed; use it when you must display text backwards, for example to show how a "
        "right-to-left string is stored, or to fix a badly encoded document.",
    ],
    syntax="<bdo dir=\"rtl\">text</bdo>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[("dir", "ltr | rtl", "Required. The direction to force.", "HTML 4.01")],
    examples=[("Displaying English backwards", "<p><bdo dir=\"rtl\">This text is reversed</bdo></p>",
               "Renders as 'desrever si txet sihT'.")],
    a11y=["Screen readers read the characters in the overridden order, which may be nonsense; use sparingly."],
    mistakes=["Omitting dir, which is required.", "Using <bdo> for isolation; use <bdi>."],
    related=["bdi"],
    css="bdo { unicode-bidi: isolate-override; }",
),

dict(
    name="bgsound", title="Background sound (non-standard, obsolete)", cat="Obsolete embedded content",
    versions="Internet Explorer extension, never standard; obsolete", status="obsolete",
    desc=[
        "The <bgsound> element was an Internet Explorer extension that played a sound file automatically "
        "when the page loaded. It was never part of any HTML standard and is not supported by any modern "
        "browser. Use <audio> instead.",
    ],
    syntax="<bgsound src=\"music.mid\" loop=\"infinite\">", void=True, display="none",
    categories="Historical", content="None", parents="<head> or <body>", omission="No end tag", dom="HTMLUnknownElement",
    attrs=[("src", "URL", "The sound file.", "IE"), ("loop", "number | infinite", "Repeat count.", "IE"),
           ("balance", "-10000 to 10000", "Stereo balance.", "IE"), ("volume", "-10000 to 0", "Volume.", "IE")],
    examples=[("Replacement", "<audio src=\"music.mp3\" autoplay loop muted></audio>", "")],
    a11y=[], mistakes=["Any use."], related=["audio"], css="",
),

dict(
    name="big", title="Bigger text (obsolete)", cat="Obsolete presentational",
    versions="HTML 3.2, HTML 4.01; obsolete in HTML5", status="obsolete",
    desc=[
        "The <big> element rendered its content one font size larger than the surrounding text. It was "
        "purely presentational and was removed in HTML5. Its counterpart <small> survived because it was "
        "given a new meaning (side comments and fine print). Use CSS font-size instead of <big>.",
    ],
    syntax="<big>text</big>", void=False, display="inline",
    categories="Phrasing content (historical)", content="Phrasing content", parents="Any element that accepts phrasing content",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("Replacement", "<!-- Old -->\n<p>Only <big>3 days</big> left!</p>\n\n<!-- New -->\n<p>Only <span style=\"font-size: larger\">3 days</span> left!</p>", "")],
    a11y=[], mistakes=["Any use in new pages."], related=["small", "span"], css="big { font-size: larger; }",
),

dict(
    name="blink", title="Blinking text (non-standard, obsolete)", cat="Obsolete presentational",
    versions="Netscape extension, never standard; obsolete", status="obsolete",
    desc=[
        "The <blink> element made its text flash on and off. It was a Netscape Navigator extension from "
        "1994, was never part of any standard, and was widely considered the most annoying element ever "
        "created. All browsers removed support by 2013. Blinking content is also an accessibility hazard "
        "for people with photosensitive epilepsy and attention disorders.",
    ],
    syntax="<blink>text</blink>", void=False, display="inline",
    categories="Historical", content="Phrasing content", parents="Any", omission="Neither tag may be omitted", dom="HTMLUnknownElement",
    attrs=[],
    examples=[("Do not do this", "<blink>Sale!</blink>", "If you must animate, use a CSS animation with a slow, subtle effect and respect prefers-reduced-motion.")],
    a11y=["Flashing content can trigger seizures. WCAG forbids flashing more than three times per second."],
    mistakes=["Any use."], related=["marquee"], css="",
),

dict(
    name="blockquote", title="Block quotation", cat="Text content",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <blockquote> element indicates that the enclosed text is an extended quotation from another "
        "source. Browsers indent it on both sides by default. The optional cite attribute holds the URL of "
        "the source; a visible citation should be given with the <cite> element, usually in a <footer> "
        "inside the blockquote or in a following paragraph.",
        "For short quotations that sit inside a sentence use <q> instead.",
    ],
    syntax="<blockquote cite=\"URL\">quoted text</blockquote>", void=False, display="block",
    categories="Flow content, sectioning root, palpable content", content="Flow content",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLQuoteElement",
    attrs=[("cite", "URL", "The URL of the source document or message. Not displayed by browsers; readable by scripts and tools.", "HTML 4.01")],
    examples=[
        ("Quotation with source",
         "<blockquote cite=\"https://www.w3.org/People/Berners-Lee/\">\n  <p>The Web does not just connect machines, it connects people.</p>\n"
         "  <footer>- <cite>Tim Berners-Lee</cite></footer>\n</blockquote>", ""),
        ("Custom styling",
         "<style>\n  blockquote {\n    margin: 1em 0; padding: 0.5em 1em;\n    border-left: 4px solid #c8a24a; background: #fdf8f0;\n  }\n</style>\n"
         "<blockquote><p>Practice is the only tutorial that always works.</p></blockquote>", ""),
    ],
    a11y=["Screen readers announce 'blockquote' so users know the text is quoted."],
    mistakes=["Using <blockquote> just to indent text; use CSS margin for that.",
              "Putting the author's name inside the quotation as if it were quoted."],
    related=["q", "cite", "footer"],
    css="blockquote { display: block; margin: 1em 40px; }",
),

dict(
    name="body", title="Document body", cat="Sectioning root",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <body> element contains all the content of the document that is displayed to the visitor: "
        "text, images, links, forms, media, and the scripts that operate on them. There is exactly one "
        "<body> in a document and it is the second child of <html>, after <head>.",
        "In HTML 3.2 and 4.01 <body> carried presentational attributes (bgcolor, text, link, vlink, alink, "
        "background) that set page colours and background images. They are obsolete in HTML5; use CSS. The "
        "<body> element also accepts window event handler attributes such as onload and onresize, because "
        "events on the window are reflected onto the body.",
        "The start and end tags of <body> may technically be omitted and the browser will create the "
        "element automatically, but always write them for clarity.",
    ],
    syntax="<body>...</body>", void=False, display="block",
    categories="Sectioning root", content="Flow content", parents="<html>, as its second child",
    omission="Start tag may be omitted if the body is empty or starts with non-whitespace content that is not a comment, <script> or <style>; end tag may be omitted if not followed by a comment",
    dom="HTMLBodyElement",
    attrs=[
        ("onafterprint, onbeforeprint", "script", "Fired after and before the document is printed.", "HTML5"),
        ("onbeforeunload", "script", "Fired when the user is about to leave; can prompt for confirmation.", "HTML5"),
        ("onhashchange", "script", "Fired when the URL fragment (#...) changes.", "HTML5"),
        ("onlanguagechange", "script", "Fired when the preferred language changes.", "HTML5"),
        ("onload", "script", "Fired when the whole page, including images, has loaded.", "HTML 4.01"),
        ("onmessage, onmessageerror", "script", "Fired when a message is received via postMessage.", "HTML5"),
        ("onoffline, ononline", "script", "Fired when network connectivity is lost or regained.", "HTML5"),
        ("onpagehide, onpageshow", "script", "Fired when navigating away from or back to the page (including from the back-forward cache).", "HTML5"),
        ("onpopstate", "script", "Fired when the active history entry changes.", "HTML5"),
        ("onresize", "script", "Fired when the window is resized.", "HTML 4.01"),
        ("onstorage", "script", "Fired when localStorage or sessionStorage changes in another tab.", "HTML5"),
        ("onunload", "script", "Fired when the document is unloaded. Unreliable; prefer pagehide.", "HTML 4.01"),
        ("alink", "colour", "Obsolete. Colour of active (being clicked) links. Use CSS a:active.", "HTML 3.2"),
        ("background", "URL", "Obsolete. Background image. Use CSS background-image.", "HTML 3.2"),
        ("bgcolor", "colour", "Obsolete. Background colour. Use CSS background-color.", "HTML 3.2"),
        ("link", "colour", "Obsolete. Colour of unvisited links. Use CSS a:link.", "HTML 3.2"),
        ("text", "colour", "Obsolete. Text colour. Use CSS color.", "HTML 3.2"),
        ("vlink", "colour", "Obsolete. Colour of visited links. Use CSS a:visited.", "HTML 3.2"),
        ("bottommargin, leftmargin, rightmargin, topmargin", "pixels", "Obsolete, non-standard. Page margins. Use CSS margin.", "IE/Netscape"),
    ],
    examples=[
        ("Minimal document",
         "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"utf-8\">\n  <title>Hello</title>\n</head>\n<body>\n  <h1>Hello, world!</h1>\n</body>\n</html>", ""),
        ("HTML 3.2 colours and their CSS replacement",
         "<!-- HTML 3.2 -->\n<body bgcolor=\"#ffffff\" text=\"#000000\" link=\"#0000ff\" vlink=\"#800080\">\n\n"
         "<!-- HTML5 + CSS -->\n<style>\n  body { background: #fff; color: #000; }\n  a:link { color: blue; }\n  a:visited { color: purple; }\n</style>\n<body>", ""),
        ("Running code when the page has loaded",
         "<body onload=\"console.log('Page loaded')\">", "Prefer addEventListener('DOMContentLoaded', ...) in a script."),
    ],
    a11y=["Set the page language on <html>, not <body>.", "Keep a logical reading order in the body; CSS can rearrange the visual layout but assistive technology follows the source order."],
    mistakes=["Having two <body> elements.", "Putting <title> or <meta> in the body.", "Using the obsolete colour attributes."],
    related=["html", "head", "main", "header", "footer"],
    css="body { display: block; margin: 8px; }",
),

dict(
    name="br", title="Line break", cat="Text-level semantics",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <br> element produces a line break in text: the text after it starts on a new line. It is a "
        "void element with no closing tag. Use it only where the division of lines is part of the content, "
        "as in a postal address or a poem.",
        "Do not use <br> to create space between paragraphs or blocks. Use separate <p> elements and CSS "
        "margins instead. A series of <br><br><br> to push content down is a classic beginner mistake that "
        "breaks on different screen sizes and confuses screen readers.",
    ],
    syntax="<br>", void=True, display="inline",
    categories="Flow content, phrasing content", content="None (void element)",
    parents="Any element that accepts phrasing content", omission="No end tag", dom="HTMLBRElement",
    attrs=[("clear", "left | right | all | none", "Obsolete. Moved the following text below any floated images. Use CSS clear.", "HTML 3.2")],
    examples=[
        ("An address", "<p>\n  Example Ltd.<br>\n  12 Nile Street<br>\n  Giza, Egypt\n</p>", ""),
        ("A poem", "<p>\n  Roses are red,<br>\n  Violets are blue,<br>\n  HTML is easy,<br>\n  And so are you.\n</p>", ""),
        ("Wrong and right", "<!-- Wrong: spacing with br -->\n<p>First</p><br><br>\n<p>Second</p>\n\n<!-- Right: spacing with CSS -->\n<style>p { margin-bottom: 2em; }</style>\n<p>First</p>\n<p>Second</p>", ""),
    ],
    a11y=["Screen readers may announce each <br>, so many consecutive breaks are noisy."],
    mistakes=["Using <br> for vertical spacing.", "Writing </br>, which is invalid (browsers treat it as <br>).", "Using <br> to separate list items instead of <ul>/<li>."],
    related=["p", "wbr", "hr", "pre"],
    css="br { display: inline; }",
),

dict(
    name="button", title="Button", cat="Forms",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <button> element represents a clickable button that the user can activate with a mouse, "
        "keyboard, finger or voice to perform an action. Unlike <input type=\"button\">, a <button> may "
        "contain rich content: text, images, icons and other phrasing content.",
        "Inside a <form>, a button submits the form by default (type=\"submit\"). Set type=\"button\" for "
        "buttons that only run JavaScript, and type=\"reset\" to clear the form. Because the default is "
        "submit, forgetting type=\"button\" is a frequent cause of forms submitting unexpectedly.",
        "The button's form-related attributes (formaction, formmethod and so on) let one form have several "
        "submit buttons that send the data to different places or in different ways.",
    ],
    syntax="<button type=\"button\">label</button>", void=False, display="inline-block",
    categories="Flow content, phrasing content, interactive content, listed, labelable, submittable, form-associated, palpable",
    content="Phrasing content, but no interactive content and no descendant with the tabindex attribute",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLButtonElement",
    attrs=[
        ("type", "submit | reset | button", "submit (default) sends the form; reset restores default values; button does nothing by itself.", "HTML 4.01"),
        ("name", "text", "The name sent with the form data when this button submits the form.", "HTML 4.01"),
        ("value", "text", "The value sent with the name.", "HTML 4.01"),
        ("disabled", "boolean", "The button cannot be clicked or focused and is not submitted.", "HTML 4.01"),
        ("autofocus", "boolean", "Focus this button when the page loads (global in HTML5).", "HTML5"),
        ("form", "form id", "Associates the button with a form elsewhere in the document.", "HTML5"),
        ("formaction", "URL", "Overrides the form's action for this button.", "HTML5"),
        ("formenctype", "application/x-www-form-urlencoded | multipart/form-data | text/plain", "Overrides the form's enctype.", "HTML5"),
        ("formmethod", "get | post | dialog", "Overrides the form's method.", "HTML5"),
        ("formnovalidate", "boolean", "Skips validation when this button submits.", "HTML5"),
        ("formtarget", "_self | _blank | _parent | _top | name", "Overrides the form's target.", "HTML5"),
        ("popovertarget", "element id", "The popover element this button shows, hides or toggles.", "Living Standard"),
        ("popovertargetaction", "show | hide | toggle", "What to do to the popover (default toggle).", "Living Standard"),
        ("command", "show-modal | close | request-close | show-popover | hide-popover | toggle-popover | custom", "Experimental: declarative action to perform on commandfor's target.", "Living Standard"),
        ("commandfor", "element id", "Experimental: the element the command applies to.", "Living Standard"),
    ],
    examples=[
        ("Three button types in a form",
         "<form action=\"/save\" method=\"post\">\n  <label>Name <input name=\"name\"></label>\n"
         "  <button type=\"submit\">Save</button>\n  <button type=\"reset\">Clear</button>\n"
         "  <button type=\"button\" onclick=\"alert('Just a script')\">Help</button>\n</form>", ""),
        ("Button with an icon",
         "<button type=\"button\">\n  <img src=\"cart.svg\" alt=\"\" width=\"16\" height=\"16\">\n  Add to cart\n</button>",
         "The image is decorative (empty alt) because the text already labels the button."),
        ("Two submit buttons going to different URLs",
         "<form action=\"/save\" method=\"post\">\n  <input name=\"title\">\n  <button>Save draft</button>\n  <button formaction=\"/publish\">Publish</button>\n</form>", ""),
        ("Toggling a popover without JavaScript",
         "<button popovertarget=\"tip\">Show tip</button>\n<div id=\"tip\" popover>Press Ctrl+S to save.</div>", ""),
        ("Icon-only button with an accessible name",
         "<button type=\"button\" aria-label=\"Close\">&times;</button>", ""),
    ],
    a11y=["Buttons are focusable and activated with Enter or Space automatically; a <div onclick> is not.",
          "Every button needs a text label or aria-label.", "Use <button> for actions and <a> for navigation.",
          "Do not remove the focus outline without providing an alternative."],
    mistakes=["Forgetting type=\"button\" and accidentally submitting the form.", "Nesting an <a> or another <button> inside.",
              "Using <div> or <span> styled as a button.", "Using <input type=\"button\"> when you need HTML content inside."],
    related=["input", "form", "a", "label"],
    css="button { display: inline-block; text-align: center; cursor: default; padding: 1px 6px; }",
),

dict(
    name="canvas", title="Graphics canvas", cat="Scripting",
    versions="HTML5", status="current",
    desc=[
        "The <canvas> element provides a blank, resolution-dependent bitmap surface on which JavaScript can "
        "draw graphics: shapes, text, images, animations, charts, games and image processing. The element "
        "itself does nothing; all drawing is done through the 2D context (getContext('2d')) or a WebGL / "
        "WebGPU context.",
        "The width and height attributes set the size of the drawing surface in pixels (default 300 x 150). "
        "Setting the size with CSS instead scales the bitmap and makes it blurry; always set the attributes.",
        "Content placed between the tags is fallback content shown by browsers that do not support canvas "
        "and read by screen readers, because the drawn pixels are invisible to assistive technology.",
    ],
    syntax="<canvas id=\"c\" width=\"400\" height=\"300\">fallback</canvas>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content, palpable content",
    content="Transparent, but no interactive content other than <a>, <button>, <input> of certain types and <select> with focusable descendants",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLCanvasElement",
    attrs=[
        ("width", "positive integer", "Width of the bitmap in CSS pixels. Default 300.", "HTML5"),
        ("height", "positive integer", "Height of the bitmap in CSS pixels. Default 150.", "HTML5"),
        ("moz-opaque", "boolean", "Firefox only: hints that there is no transparency, for faster rendering.", "Non-standard"),
    ],
    examples=[
        ("Drawing a rectangle and text",
         "<canvas id=\"demo\" width=\"300\" height=\"150\">\n  A blue rectangle with the text Hello.\n</canvas>\n<script>\n"
         "  const ctx = document.getElementById('demo').getContext('2d');\n  ctx.fillStyle = '#1b6fd8';\n  ctx.fillRect(10, 10, 120, 80);\n"
         "  ctx.fillStyle = 'white';\n  ctx.font = '20px sans-serif';\n  ctx.fillText('Hello', 30, 60);\n</script>", ""),
        ("Simple animation",
         "<canvas id=\"ball\" width=\"200\" height=\"100\"></canvas>\n<script>\n  const c = document.getElementById('ball'), ctx = c.getContext('2d');\n  let x = 0;\n"
         "  function frame() {\n    ctx.clearRect(0, 0, c.width, c.height);\n    ctx.beginPath(); ctx.arc(x, 50, 10, 0, Math.PI * 2); ctx.fill();\n"
         "    x = (x + 2) % c.width;\n    requestAnimationFrame(frame);\n  }\n  frame();\n</script>", ""),
    ],
    a11y=["Canvas content is invisible to screen readers. Provide fallback content, an aria-label, or a text alternative next to it.",
          "For charts, provide the data as a table too.", "For diagrams and icons, SVG is usually more accessible than canvas."],
    mistakes=["Sizing the canvas with CSS instead of width/height attributes.", "Forgetting to clear before redrawing.",
              "Using canvas for content that should be real HTML text."],
    related=["svg", "img", "script"],
    css="canvas { display: inline; }",
),

dict(
    name="caption", title="Table caption", cat="Table content",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <caption> element gives a table a title or explanation. It must be the first child of the "
        "<table> element, and a table may have only one. By default it is displayed centred above the table; "
        "the CSS caption-side property can move it below.",
        "A caption is important for accessibility: screen readers announce it when the user enters the "
        "table, so the user knows what the data is about before hearing the cells.",
    ],
    syntax="<table>\n  <caption>Title</caption>\n  ...\n</table>", void=False, display="table-caption",
    categories="None", content="Flow content, but no descendant <table>", parents="<table>, as its first child",
    omission="End tag may be omitted if the caption is not followed by whitespace or a comment", dom="HTMLTableCaptionElement",
    attrs=[("align", "top | bottom | left | right", "Obsolete. Position of the caption. Use CSS caption-side and text-align.", "HTML 3.2")],
    examples=[
        ("Table with caption",
         "<table>\n  <caption>Monthly sales, 2026</caption>\n  <tr><th>Month</th><th>Sales</th></tr>\n  <tr><td>January</td><td>120</td></tr>\n  <tr><td>February</td><td>150</td></tr>\n</table>", ""),
        ("Caption below the table", "<style>\n  table { caption-side: bottom; }\n</style>", ""),
    ],
    a11y=["Prefer <caption> over a heading above the table; it is programmatically linked to the table.",
          "If the table is inside a <figure>, use <figcaption> instead of <caption>, not both."],
    mistakes=["Placing <caption> after <tr>.", "Multiple captions."],
    related=["table", "figcaption"],
    css="caption { display: table-caption; text-align: center; }",
),

dict(
    name="center", title="Centred block (obsolete)", cat="Obsolete presentational",
    versions="HTML 3.2, HTML 4.01 (deprecated); obsolete in HTML5", status="obsolete",
    desc=[
        "The <center> element horizontally centred its content. It was introduced by Netscape, standardised "
        "in HTML 3.2, deprecated in HTML 4.01 and removed in HTML5. It is equivalent to <div align=\"center\">. "
        "Use CSS instead: text-align: center for inline content, or margin: 0 auto with a width for blocks.",
    ],
    syntax="<center>content</center>", void=False, display="block",
    categories="Flow content (historical)", content="Flow content", parents="Any element that accepts flow content",
    omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("Replacement",
               "<!-- Old -->\n<center><h1>Welcome</h1></center>\n\n<!-- New: centre text -->\n<h1 style=\"text-align: center\">Welcome</h1>\n\n"
               "<!-- New: centre a block -->\n<div style=\"width: 600px; margin: 0 auto\">...</div>", "")],
    a11y=[], mistakes=["Any use in new pages."], related=["div"], css="center { display: block; text-align: -webkit-center; }",
),

dict(
    name="cite", title="Citation (title of a work)", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <cite> element marks the title of a creative work that is being referenced: a book, article, "
        "film, song, painting, play, poem, website, legal case, computer program, and so on. Browsers render "
        "it in italics.",
        "In HTML 4 <cite> could also mark the name of a person being quoted. The HTML Living Standard "
        "restricts it to titles of works; a person's name is not a title. In practice many pages use it for "
        "author names inside <blockquote> footers, and validators accept it.",
    ],
    syntax="<cite>Title of Work</cite>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Book title", "<p>I am reading <cite>The Pragmatic Programmer</cite> this month.</p>", ""),
        ("Source of a quotation",
         "<blockquote>\n  <p>Any fool can write code that a computer can understand.</p>\n  <footer>- Martin Fowler, <cite>Refactoring</cite></footer>\n</blockquote>", ""),
    ],
    a11y=["No special announcement; the meaning is mainly for search engines and styling."],
    mistakes=["Using <cite> for the URL of a source; that belongs in the cite attribute of <blockquote> or <q>.", "Using <i> instead of <cite> for titles."],
    related=["blockquote", "q", "i"],
    css="cite { font-style: italic; }",
),

dict(
    name="code", title="Inline code", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <code> element marks a fragment of computer code: an element name, a file name, a variable, a "
        "function, a command, or any other string a computer would recognise. Browsers render it in a "
        "monospace font.",
        "For a multi-line block of code, wrap a <code> element in a <pre> element so that line breaks and "
        "indentation are preserved. The class attribute may be used to indicate the language, conventionally "
        "as language-xxx.",
    ],
    syntax="<code>snippet</code>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Inline", "<p>Use the <code>&lt;footer&gt;</code> element for the bottom of the page and save the file as <code>index.html</code>.</p>",
         "Note that < and > inside code must still be written as &lt; and &gt;."),
        ("Code block",
         "<pre><code class=\"language-css\">footer {\n  text-align: center;\n  color: gray;\n}</code></pre>", ""),
    ],
    a11y=["Some screen readers switch to reading punctuation when they encounter <code>."],
    mistakes=["Forgetting to escape < and & inside code.", "Using <code> alone for multi-line blocks (line breaks collapse without <pre>)."],
    related=["pre", "kbd", "samp", "var"],
    css="code { font-family: monospace; }",
),

dict(
    name="col", title="Table column", cat="Table content",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <col> element defines one or more columns in a table so that attributes and styles can be "
        "applied to whole columns at once. It is a void element and lives inside a <colgroup>. The span "
        "attribute makes one <col> stand for several consecutive columns.",
        "Only a few CSS properties apply to columns: background, border, width and visibility. Text colour "
        "and font cannot be set on a column; set them on the cells.",
    ],
    syntax="<colgroup>\n  <col span=\"2\" style=\"background: #eee\">\n</colgroup>", void=True, display="table-column",
    categories="None", content="None (void element)", parents="<colgroup> that does not have a span attribute",
    omission="No end tag", dom="HTMLTableColElement",
    attrs=[
        ("span", "positive integer", "How many consecutive columns this element represents. Default 1.", "HTML 4.01"),
        ("align", "left | center | right | justify | char", "Obsolete. Horizontal alignment of the cells. Use CSS text-align.", "HTML 4.01"),
        ("bgcolor", "colour", "Obsolete. Background colour. Use CSS.", "HTML 4.01"),
        ("char", "character", "Obsolete. Alignment character (for align=char).", "HTML 4.01"),
        ("charoff", "number", "Obsolete. Offset from the alignment character.", "HTML 4.01"),
        ("valign", "top | middle | bottom | baseline", "Obsolete. Vertical alignment. Use CSS vertical-align.", "HTML 4.01"),
        ("width", "pixels or percentage", "Obsolete. Column width. Use CSS width.", "HTML 4.01"),
    ],
    examples=[
        ("Shading the first column and widening the last",
         "<table>\n  <colgroup>\n    <col style=\"background: #f0f0f0\">\n    <col>\n    <col style=\"width: 200px\">\n  </colgroup>\n"
         "  <tr><th>Item</th><th>Qty</th><th>Notes</th></tr>\n  <tr><td>Pen</td><td>3</td><td>Blue ink</td></tr>\n</table>", ""),
    ],
    a11y=["Columns have no accessibility role; use <th scope=\"col\"> for column headers."],
    mistakes=["Placing <col> outside <colgroup> (browsers insert an implicit colgroup, but be explicit).", "Trying to set font or colour on <col>."],
    related=["colgroup", "table"],
    css="col { display: table-column; }",
),

dict(
    name="colgroup", title="Table column group", cat="Table content",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <colgroup> element groups one or more columns of a table for the purpose of styling and "
        "structure. It is placed inside <table> after the optional <caption> and before any <thead>, "
        "<tbody>, <tfoot> or <tr>. It either has a span attribute (and no children) or contains <col> "
        "elements.",
    ],
    syntax="<colgroup span=\"2\"></colgroup>\n<!-- or -->\n<colgroup><col><col></colgroup>", void=False, display="table-column-group",
    categories="None", content="If span is absent: zero or more <col> and <template>. If span is present: nothing",
    parents="<table>, after <caption> and before <thead>, <tbody>, <tfoot> and <tr>",
    omission="Start tag may be omitted if the first thing inside is a <col>; end tag may be omitted if not followed by whitespace or a comment",
    dom="HTMLTableColElement",
    attrs=[
        ("span", "positive integer", "Number of columns in the group when there are no <col> children.", "HTML 4.01"),
        ("align, bgcolor, char, charoff, valign, width", "various", "Obsolete presentational attributes; see <col>.", "HTML 4.01"),
    ],
    examples=[
        ("Two groups with different backgrounds",
         "<table>\n  <colgroup style=\"background: #e8f4ff\"><col><col></colgroup>\n  <colgroup style=\"background: #fff4e8\"><col></colgroup>\n"
         "  <tr><th>First</th><th>Last</th><th>Age</th></tr>\n  <tr><td>Ahmed</td><td>Ali</td><td>20</td></tr>\n</table>", ""),
    ],
    a11y=[], mistakes=["Mixing a span attribute with <col> children.", "Placing colgroup after tbody."],
    related=["col", "table"], css="colgroup { display: table-column-group; }",
),

dict(
    name="content", title="Shadow DOM insertion point (obsolete)", cat="Obsolete web components",
    versions="Shadow DOM v0 (Chrome, 2013); obsolete", status="obsolete",
    desc=[
        "The <content> element was part of the first, experimental version of Shadow DOM (v0). It marked "
        "the point where light DOM children were inserted into a shadow tree. It was replaced by the "
        "standardised <slot> element and removed from browsers in 2019.",
    ],
    syntax="<content select=\".title\"></content>", void=False, display="inline",
    categories="Historical", content="Any", parents="Shadow root", omission="Neither", dom="HTMLUnknownElement",
    attrs=[("select", "CSS selector", "Which light DOM children to insert.", "Shadow DOM v0")],
    examples=[("Replacement", "<!-- Old -->\n<content select=\".title\"></content>\n\n<!-- New -->\n<slot name=\"title\"></slot>", "")],
    a11y=[], mistakes=["Any use."], related=["slot", "template", "shadow"], css="",
),

dict(
    name="data", title="Machine-readable value", cat="Text-level semantics",
    versions="HTML5", status="current",
    desc=[
        "The <data> element links a piece of human-readable content with a machine-readable version of the "
        "same value held in the required value attribute. It is useful for product codes, numeric values "
        "written in words, sorting keys and similar cases where a script or search engine needs the exact "
        "value while the visitor sees a friendly form.",
        "If the value is a date or time, use <time> instead, which has the same purpose but a defined format.",
    ],
    syntax="<data value=\"machine value\">human text</data>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLDataElement",
    attrs=[("value", "text", "Required. The machine-readable form of the content.", "HTML5")],
    examples=[
        ("Product codes",
         "<ul>\n  <li><data value=\"SKU-1001\">Blue notebook</data></li>\n  <li><data value=\"SKU-1002\">Red notebook</data></li>\n</ul>", ""),
        ("Numbers written in words", "<p>We sold <data value=\"1000000\">one million</data> copies.</p>", ""),
    ],
    a11y=["The value attribute is not read by screen readers; the visible text must be understandable alone."],
    mistakes=["Using <data> for dates; use <time>."], related=["time", "meter"], css="data { display: inline; }",
),

dict(
    name="datalist", title="Predefined options for an input", cat="Forms",
    versions="HTML5", status="current",
    desc=[
        "The <datalist> element contains a set of <option> elements that represent suggested values for an "
        "<input>. The input is linked to the list with its list attribute, which must equal the datalist's "
        "id. The user can pick a suggestion or type any other value, which makes it a combination of a text "
        "box and a drop-down list (a 'combobox').",
        "The datalist itself is never displayed. Browsers show the suggestions in their own way, usually as "
        "a drop-down that filters as the user types. It works with text, search, url, tel, email, number, "
        "range, color, date and time inputs, though support for non-text types varies.",
    ],
    syntax="<input list=\"id\">\n<datalist id=\"id\">\n  <option value=\"...\">\n</datalist>", void=False, display="none",
    categories="Flow content, phrasing content", content="Either phrasing content or zero or more <option> elements",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLDataListElement",
    attrs=[],
    examples=[
        ("Browser suggestions",
         "<label for=\"browser\">Favourite browser</label>\n<input id=\"browser\" name=\"browser\" list=\"browsers\">\n"
         "<datalist id=\"browsers\">\n  <option value=\"Chrome\">\n  <option value=\"Firefox\">\n  <option value=\"Safari\">\n  <option value=\"Edge\">\n</datalist>", ""),
        ("Labelled values",
         "<input list=\"codes\" name=\"country\">\n<datalist id=\"codes\">\n  <option value=\"EG\">Egypt</option>\n  <option value=\"SA\">Saudi Arabia</option>\n</datalist>",
         "Some browsers show the label next to the value."),
        ("Tick marks on a range slider",
         "<input type=\"range\" min=\"0\" max=\"100\" list=\"ticks\">\n<datalist id=\"ticks\">\n  <option value=\"0\">\n  <option value=\"50\">\n  <option value=\"100\">\n</datalist>", ""),
    ],
    a11y=["Support in screen readers is inconsistent; consider a visible hint about available values."],
    mistakes=["Mismatched id and list values.", "Expecting the user to be limited to the options (use <select> for that)."],
    related=["input", "option", "select"], css="datalist { display: none; }",
),

dict(
    name="dd", title="Description details", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <dd> element provides the description, definition or value for the preceding term (<dt>) in a "
        "description list (<dl>). One term may have several <dd> elements, and several terms may share one "
        "<dd>. Browsers indent <dd> from the left by default.",
    ],
    syntax="<dl>\n  <dt>Term</dt>\n  <dd>Description</dd>\n</dl>", void=False, display="block",
    categories="None", content="Flow content", parents="<dl> or <div> inside <dl>, after a <dt> or <dd>",
    omission="End tag may be omitted if followed by another <dd> or <dt>, or if there is no more content in the parent",
    dom="HTMLElement",
    attrs=[("nowrap", "yes | no", "Obsolete, non-standard. Prevented wrapping.", "IE")],
    examples=[
        ("Glossary", "<dl>\n  <dt>HTML</dt>\n  <dd>The language that structures web pages.</dd>\n  <dt>CSS</dt>\n  <dd>The language that styles web pages.</dd>\n</dl>", ""),
        ("Several descriptions for one term", "<dl>\n  <dt>Footer</dt>\n  <dd>The bottom section of a page.</dd>\n  <dd>An HTML element: &lt;footer&gt;.</dd>\n</dl>", ""),
    ],
    a11y=["Screen readers announce the list structure so users know which description belongs to which term."],
    mistakes=["Using <dd> outside <dl>.", "Using <dd> just for indentation."],
    related=["dl", "dt"], css="dd { display: block; margin-inline-start: 40px; }",
),

dict(
    name="del", title="Deleted text", cat="Demarcating edits",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <del> element marks text that has been deleted from a document, typically to show changes "
        "between versions ('track changes'). Browsers render it with a line through it. It is usually paired "
        "with <ins>, which marks inserted text.",
        "<del> may contain either phrasing or flow content depending on where it is placed, but it should "
        "not cross the boundaries of block elements: to delete two paragraphs, wrap each in its own <del>.",
        "For text that is no longer accurate but not part of an edit history (such as an old price), use <s> instead.",
    ],
    syntax="<del datetime=\"YYYY-MM-DD\" cite=\"URL\">deleted text</del>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Transparent",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLModElement",
    attrs=[
        ("cite", "URL", "A URL explaining the change, such as a link to a change log or meeting minutes.", "HTML 4.01"),
        ("datetime", "date or date-time string", "When the change was made, in the format YYYY-MM-DD or YYYY-MM-DDThh:mm:ssZ.", "HTML 4.01"),
    ],
    examples=[
        ("Showing a correction", "<p>The meeting is on <del datetime=\"2026-09-10\">Monday</del> <ins datetime=\"2026-09-10\">Tuesday</ins>.</p>", ""),
        ("A completed to-do item", "<ul>\n  <li><del>Buy milk</del></li>\n  <li>Write HTML</li>\n</ul>", ""),
    ],
    a11y=["Most screen readers do not announce <del> by default. If the deletion is important, add visually hidden text such as 'deleted:' or use CSS ::before content with speak.",],
    mistakes=["Using <del> for a discounted price; use <s>.", "Using <strike>, which is obsolete."],
    related=["ins", "s", "strike"], css="del { text-decoration: line-through; }",
),

dict(
    name="details", title="Disclosure widget", cat="Interactive elements",
    versions="HTML5 (5.1)", status="current",
    desc=[
        "The <details> element creates a disclosure widget: a box that can be opened and closed by the "
        "user to show or hide its content, with no JavaScript at all. The first child should be a <summary> "
        "element, which provides the always-visible label and the clickable arrow. If there is no <summary> "
        "the browser shows the word 'Details'.",
        "The open attribute controls whether the content is visible. Adding or removing it from script "
        "opens or closes the widget, and the element fires a toggle event when its state changes. Giving "
        "several <details> the same name attribute makes them exclusive, like an accordion: opening one "
        "closes the others.",
    ],
    syntax="<details>\n  <summary>Label</summary>\n  content\n</details>", void=False, display="block",
    categories="Flow content, sectioning root, interactive content, palpable content",
    content="One <summary> followed by flow content", parents="Any element that accepts flow content",
    omission="Neither tag may be omitted", dom="HTMLDetailsElement",
    attrs=[
        ("open", "boolean", "The details are visible. Absent means collapsed.", "HTML5"),
        ("name", "text", "Groups details elements so that only one in the group can be open at a time.", "Living Standard"),
    ],
    examples=[
        ("FAQ item", "<details>\n  <summary>How do I centre a div?</summary>\n  <p>Use <code>display: flex; justify-content: center; align-items: center;</code> on the parent.</p>\n</details>", ""),
        ("Open by default", "<details open>\n  <summary>Shipping information</summary>\n  <p>Delivery takes 2-4 days.</p>\n</details>", ""),
        ("Accordion with the name attribute",
         "<details name=\"faq\"><summary>Question 1</summary><p>Answer 1</p></details>\n<details name=\"faq\"><summary>Question 2</summary><p>Answer 2</p></details>", ""),
        ("Styling the arrow", "<style>\n  summary { cursor: pointer; font-weight: bold; }\n  details[open] summary { color: #b90000; }\n</style>", ""),
    ],
    a11y=["Fully keyboard accessible and announced as a button with expanded/collapsed state, out of the box.",
          "Do not put interactive elements inside <summary>."],
    mistakes=["Putting <summary> anywhere other than first.", "Using open=\"false\" (which still means open)."],
    related=["summary", "dialog"], css="details { display: block; }",
),

dict(
    name="dfn", title="Definition term", cat="Text-level semantics",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <dfn> element marks the term that is being defined in the surrounding sentence or paragraph. "
        "The nearest paragraph, description list group or section is the definition. Browsers render it in "
        "italics. If the element has a title attribute, that is the term being defined; if it contains an "
        "<abbr> with a title, the abbreviation's expansion is the term; otherwise the text content is the term.",
    ],
    syntax="<dfn>term</dfn>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content, but no <dfn> descendants",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[("title", "text", "The term being defined, if different from the content.", "HTML 4.01")],
    examples=[
        ("Defining a term", "<p>A <dfn>void element</dfn> is an element that cannot have any content and therefore has no closing tag.</p>", ""),
        ("Linking to the definition", "<p>A <dfn id=\"def-footer\">footer</dfn> is the bottom section of a page.</p>\n...\n<p>Put the copyright in the <a href=\"#def-footer\">footer</a>.</p>", ""),
    ],
    a11y=["No special announcement; purely semantic."],
    mistakes=["Using <dfn> on every occurrence of a term; use it only where it is defined."],
    related=["abbr", "dl", "dt"], css="dfn { font-style: italic; }",
),

dict(
    name="dialog", title="Dialog box", cat="Interactive elements",
    versions="HTML 5.2 / Living Standard", status="current",
    desc=[
        "The <dialog> element represents a dialog box or other interactive component such as a confirmation "
        "prompt, an alert, a subwindow or a modal overlay. It is hidden by default and is shown with the open "
        "attribute or, preferably, with the JavaScript methods show() (non-modal) and showModal() (modal). "
        "A modal dialog blocks interaction with the rest of the page, is displayed on top of everything else, "
        "and can be closed with the Escape key.",
        "A <form method=\"dialog\"> inside the dialog closes it when submitted and sets the dialog's "
        "returnValue to the value of the submit button. The ::backdrop pseudo-element styles the dimmed "
        "area behind a modal dialog.",
    ],
    syntax="<dialog id=\"d\">...</dialog>\n<script>document.getElementById('d').showModal()</script>", void=False, display="block",
    categories="Flow content, sectioning root", content="Flow content", parents="Any element that accepts flow content",
    omission="Neither tag may be omitted", dom="HTMLDialogElement",
    attrs=[
        ("open", "boolean", "The dialog is visible. Set it with showModal() rather than by hand so that focus and the backdrop work correctly.", "HTML 5.2"),
        ("closedby", "any | closerequest | none", "Which user actions close the dialog: any (Escape, backdrop click, close request), closerequest (Escape only, the default for modal), or none.", "Living Standard"),
    ],
    examples=[
        ("Modal confirmation",
         "<dialog id=\"confirm\">\n  <form method=\"dialog\">\n    <p>Delete this item?</p>\n    <button value=\"cancel\">Cancel</button>\n    <button value=\"ok\">Delete</button>\n  </form>\n</dialog>\n"
         "<button onclick=\"document.getElementById('confirm').showModal()\">Delete</button>\n<script>\n  const d = document.getElementById('confirm');\n"
         "  d.addEventListener('close', () => console.log('User chose', d.returnValue));\n</script>", ""),
        ("Styling the backdrop", "<style>\n  dialog::backdrop { background: rgba(0, 0, 0, 0.6); }\n  dialog { border: none; border-radius: 12px; padding: 24px; }\n</style>", ""),
    ],
    a11y=["showModal() traps focus inside the dialog and returns it when closed, which custom modals often get wrong.",
          "Give the dialog an accessible name with aria-labelledby pointing at its heading.", "Always provide a visible close button."],
    mistakes=["Setting the open attribute directly for modals (no backdrop, no focus trap).", "Nesting a dialog inside a button or link."],
    related=["details", "form", "button"], css="dialog { position: absolute; inset-inline: 0; width: fit-content; margin: auto; border: solid; padding: 1em; background: Canvas; color: CanvasText; }\ndialog:not([open]) { display: none; }",
),

dict(
    name="dir", title="Directory list (obsolete)", cat="Obsolete text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01 (deprecated); obsolete in HTML5", status="obsolete",
    desc=[
        "The <dir> element was a list of short items, intended to be shown in columns like a file directory "
        "listing. Browsers never implemented the columns and rendered it like <ul>. It was deprecated in "
        "HTML 4.01 and removed in HTML5. Use <ul> instead.",
    ],
    syntax="<dir><li>item</li></dir>", void=False, display="block",
    categories="Historical", content="<li> elements", parents="Flow content", omission="Neither", dom="HTMLDirectoryElement",
    attrs=[("compact", "boolean", "Obsolete. Render more compactly.", "HTML 2.0")],
    examples=[("Replacement", "<!-- Old -->\n<dir><li>index.html</li><li>style.css</li></dir>\n\n<!-- New -->\n<ul><li>index.html</li><li>style.css</li></ul>", "")],
    a11y=[], mistakes=["Any use."], related=["ul", "menu"], css="dir { display: block; list-style-type: disc; margin: 1em 0; padding-inline-start: 40px; }",
),

dict(
    name="div", title="Generic block container", cat="Text content",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <div> element (division) is a generic container for flow content. It has no meaning of its "
        "own and no effect on the content or layout until it is styled with CSS (using class or id) or "
        "manipulated with JavaScript. Use it to group elements for styling purposes, for layout (flexbox, "
        "grid), or when no other element is more appropriate.",
        "Because it carries no meaning, <div> should be a last resort. Before using it ask whether "
        "<header>, <nav>, <main>, <section>, <article>, <aside>, <footer>, <figure> or another element "
        "describes the content better. A page built only from divs (so-called 'div soup') works visually but "
        "tells assistive technology and search engines nothing about its structure.",
        "The inline counterpart of <div> is <span>. Since HTML5, <div> may also be used inside <dl> to "
        "wrap a <dt>/<dd> group.",
    ],
    syntax="<div class=\"name\">...</div>", void=False, display="block",
    categories="Flow content, palpable content", content="Flow content; inside <dl>: one or more <dt> followed by one or more <dd>",
    parents="Any element that accepts flow content, and <dl>", omission="Neither tag may be omitted", dom="HTMLDivElement",
    attrs=[("align", "left | center | right | justify", "Obsolete. Horizontal alignment of the content. Use CSS text-align or margin.", "HTML 3.2")],
    examples=[
        ("Grouping for styling",
         "<style>\n  .card { border: 1px solid #ccc; border-radius: 8px; padding: 16px; }\n</style>\n<div class=\"card\">\n  <h2>Pizza</h2>\n  <p>Delicious and cheesy.</p>\n</div>", ""),
        ("Layout with flexbox",
         "<style>\n  .row { display: flex; gap: 16px; }\n  .row > div { flex: 1; background: #eee; padding: 8px; }\n</style>\n<div class=\"row\">\n  <div>Column 1</div>\n  <div>Column 2</div>\n  <div>Column 3</div>\n</div>", ""),
        ("Grouping a term and description in a list", "<dl>\n  <div>\n    <dt>Name</dt>\n    <dd>Ahmed</dd>\n  </div>\n  <div>\n    <dt>Age</dt>\n    <dd>20</dd>\n  </div>\n</dl>", ""),
        ("Div versus semantic elements",
         "<!-- Div soup -->\n<div class=\"header\">...</div>\n<div class=\"nav\">...</div>\n<div class=\"footer\">...</div>\n\n"
         "<!-- Semantic -->\n<header>...</header>\n<nav>...</nav>\n<footer>...</footer>", "Both look identical; the second is understood by screen readers and search engines."),
    ],
    a11y=["A <div> has no role. If you make it interactive with JavaScript you must add role, tabindex and keyboard handling yourself; usually a <button> is the right choice instead."],
    mistakes=["Using <div> where a semantic element exists.", "Using <div> as a button or link.", "Putting <div> inside <p> (invalid; the browser closes the paragraph)."],
    related=["span", "section", "article", "main", "header", "footer"], css="div { display: block; }",
),

dict(
    name="dl", title="Description list", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <dl> element represents a description list: a list of groups of terms (<dt>) and their "
        "descriptions (<dd>). Common uses are glossaries, dictionaries, metadata displays (key: value pairs), "
        "FAQ lists and product specifications.",
        "In HTML 4 it was called a 'definition list' and meant only for definitions. HTML5 renamed it and "
        "broadened the meaning to any name-value groups. Since HTML5 each group may optionally be wrapped in "
        "a <div> for styling.",
    ],
    syntax="<dl>\n  <dt>Term</dt>\n  <dd>Description</dd>\n</dl>", void=False, display="block",
    categories="Flow content; palpable if it contains at least one group",
    content="Zero or more groups each consisting of one or more <dt> followed by one or more <dd>, optionally mixed with <script> and <template>; or zero or more <div> elements each containing such a group",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLDListElement",
    attrs=[("compact", "boolean", "Obsolete. Render more compactly.", "HTML 2.0")],
    examples=[
        ("Glossary", "<dl>\n  <dt>Tag</dt>\n  <dd>The markup inside angle brackets, such as &lt;p&gt;.</dd>\n  <dt>Element</dt>\n  <dd>The opening tag, content and closing tag together.</dd>\n</dl>", ""),
        ("Product specifications as key-value pairs",
         "<dl>\n  <dt>Weight</dt>\n  <dd>1.2 kg</dd>\n  <dt>Colour</dt>\n  <dd>Black</dd>\n  <dt>Warranty</dt>\n  <dd>2 years</dd>\n</dl>", ""),
        ("Multiple terms sharing one description", "<dl>\n  <dt>Colour</dt>\n  <dt>Color</dt>\n  <dd>British and American spellings of the same word.</dd>\n</dl>", ""),
        ("Horizontal layout with CSS grid", "<style>\n  dl { display: grid; grid-template-columns: max-content 1fr; gap: 4px 16px; }\n  dt { font-weight: bold; }\n  dd { margin: 0; }\n</style>", ""),
    ],
    a11y=["Screen readers announce it as a list with terms and descriptions (support varies).",
          "Do not use <dl> to mark up dialogue (speaker: line); it is not a name-value list."],
    mistakes=["Putting anything other than <dt>, <dd>, <div>, <script>, <template> directly inside <dl>.", "Using <dl> for indentation."],
    related=["dt", "dd", "ul", "ol"], css="dl { display: block; margin: 1em 0; }",
),

dict(
    name="dt", title="Description term", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <dt> element specifies a term, name or key in a description list (<dl>). It is followed by "
        "one or more <dd> elements that describe it. Several <dt> elements in a row share the following "
        "<dd>. A <dt> may not contain headings, sections, headers or footers.",
    ],
    syntax="<dt>Term</dt>", void=False, display="block",
    categories="None", content="Flow content, but no <header>, <footer>, sectioning content or heading content",
    parents="<dl> or <div> inside <dl>, before a <dd> or another <dt>",
    omission="End tag may be omitted if followed by another <dt> or a <dd>", dom="HTMLElement",
    attrs=[],
    examples=[("Term and description", "<dl>\n  <dt>Footer</dt>\n  <dd>The bottom section of a page.</dd>\n</dl>", "")],
    a11y=[], mistakes=["Using <dt> outside <dl>.", "Putting a heading inside <dt>."],
    related=["dl", "dd", "dfn"], css="dt { display: block; }",
),

]
