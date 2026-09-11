# -*- coding: utf-8 -*-
"""Front matter, history and fundamentals chapters of the HTML Reference Book.

Every chapter is a list of blocks. A block is a tuple:
    ("h2", text)      second-level heading
    ("h3", text)      third-level heading
    ("p", text)       paragraph (simple inline <code> allowed)
    ("code", text)    pre-formatted code sample
    ("ul", [items])   bullet list
    ("table", [header_row, row, row, ...])
    ("note", text)    call-out box
"""

HOW_TO_USE = [
    ("p", "This book is a complete desk reference for the HTML language, from the very first "
          "version published by Tim Berners-Lee in 1991 up to the HTML Living Standard that browsers "
          "implement today. It is written for people who are learning HTML for the first time and "
          "for experienced developers who need to look something up quickly."),
    ("h3", "How the book is organised"),
    ("ul", [
        "Part 1 - History: what changed in HTML 1, 2, 3.2, 4.01, XHTML and HTML5.",
        "Part 2 - Fundamentals: syntax, document structure, nesting rules, content categories, "
        "comments, entities and the rules that apply to every tag.",
        "Part 3 - HTML version by version: what HTML 1, 2.0, 3.2, 4.01, XHTML and HTML5 each introduced.",
        "Part 4 - Global attributes: attributes such as id, class, style, title, hidden, lang and "
        "data-* that can be placed on any element.",
        "Part 5 - Event handler attributes: onclick, onload, onchange and every other on* attribute.",
        "Part 6 - Element reference: one full entry for every HTML element, alphabetically ordered. "
        "Each entry contains a description, syntax, content model, a table of every attribute, "
        "one or more complete examples, accessibility notes, version history and common mistakes.",
        "Part 7 - The input element in depth: every value of the type attribute with its own entry.",
        "Part 8 - Obsolete and deprecated features: elements and attributes from HTML 2, 3.2 and 4 "
        "that you may meet in old pages, with the modern replacement for each.",
        "Part 9 - Attribute reference: every attribute in the language listed alphabetically with the "
        "elements that accept it.",
        "Part 10 - Value references: link relationship types, MIME types, meta names, autocomplete tokens, "
        "colour names, URL schemes and the character entity table.",
        "Part 11 - CSS reference: selectors, every common property, and a cookbook for styling HTML.",
        "Part 12 - JavaScript reference: the language from zero, the DOM, events, forms, storage and fetch.",
        "Part 13 - Course: 47 lessons (HTML, CSS, then JavaScript), each followed by two practice projects.",
        "Part 14 - Practical guides: forms, tables, lists, media, semantic layout, accessibility, SEO.",
        "Part 15 - Glossary and alphabetical index.",
        "Part 16 - Practice projects: every project type for every business theme, with full code.",
        "Every chapter (part) ends with two practice projects that use what it taught. Page numbers "
        "start at 1 on the first chapter page; the cover and contents use roman numerals.",
    ]),
    ("h3", "How to find something quickly"),
    ("ul", [
        "In the HTML edition, type any word into the search box at the top: a tag name, an attribute "
        "name, a value, or a plain English word such as 'italic' or 'bottom of page'.",
        "In the PDF edition, use the table of contents at the front, the alphabetical index at the back, "
        "or your PDF reader's search function (Ctrl+F).",
        "Every element entry has the same layout, so once you know where the attribute table is in "
        "one entry you know where it is in all of them.",
    ]),
    ("h3", "Conventions used in this book"),
    ("table", [
        ["Notation", "Meaning"],
        ["<tag>", "An HTML element written with its tag name, for example <footer>."],
        ["attribute", "An attribute name, written in lower case, for example href."],
        ["attribute=\"value\"", "An attribute together with an example value."],
        ["Void element", "An element that has no closing tag and no content, for example <br>."],
        ["Deprecated", "Still works in browsers but should not be used in new pages."],
        ["Obsolete", "Removed from the standard; browsers may still render it for old pages."],
        ["HTML 2 / 3.2 / 4.01 / 5", "The version of the specification in which a feature first appeared."],
    ]),
    ("note", "All examples in this book are complete and valid. You can copy any of them into a file "
             "named index.html and open it in a browser."),
]

HISTORY = [
    ("p", "HTML (HyperText Markup Language) is the language used to describe the structure of pages on "
          "the World Wide Web. It has existed for more than three decades and has gone through several "
          "official versions. Knowing the history helps you understand why some tags exist, why others "
          "are marked obsolete, and why modern HTML looks the way it does."),

    ("h2", "HTML 1.0 (1991 - 1993): the beginning"),
    ("p", "In 1989 Tim Berners-Lee, a scientist at CERN in Switzerland, proposed a system for sharing "
          "documents between researchers. In 1991 he published a short document called 'HTML Tags' that "
          "described 18 elements. There was no official 'HTML 1.0' specification; the name is used "
          "informally for this first generation of the language. In 1993 Berners-Lee and Dan Connolly "
          "published an Internet Draft called 'Hypertext Markup Language (HTML)' which is often called "
          "HTML 1.0."),
    ("p", "The first version was extremely simple. It had no images at first, no tables, no forms and no "
          "styling of any kind. Its purpose was to mark headings, paragraphs, lists and, most importantly, "
          "hyperlinks."),
    ("table", [
        ["Element", "Purpose in HTML 1"],
        ["<title>", "The document title."],
        ["<a>", "The anchor: a hyperlink to another document. The most important invention of HTML."],
        ["<h1> to <h6>", "Six levels of heading."],
        ["<p>", "A paragraph break (in the earliest version it was a separator, not a container)."],
        ["<ul>, <ol>, <li>", "Unordered and ordered lists."],
        ["<dl>, <dt>, <dd>", "Glossary (definition) lists."],
        ["<menu>, <dir>", "Compact list variants (later removed)."],
        ["<address>", "Author contact information."],
        ["<pre>, <listing>, <xmp>, <plaintext>", "Pre-formatted and literal text blocks."],
        ["<isindex>", "A searchable index prompt (later removed)."],
        ["<nextid>", "Used by editors to generate identifiers (later removed)."],
        ["<img>", "Added in 1993 by Marc Andreessen for the Mosaic browser."],
    ]),

    ("h2", "HTML 2.0 (1995): the first official standard"),
    ("p", "HTML 2.0 was published in November 1995 as RFC 1866 by the Internet Engineering Task Force "
          "(IETF). It gathered together everything that browsers of the time already supported and made "
          "it an official standard. It was written by Tim Berners-Lee and Dan Connolly."),
    ("p", "New in HTML 2.0:"),
    ("ul", [
        "Forms: <form>, <input>, <select>, <option>, <textarea>. For the first time a page could send "
        "information back to a server.",
        "Images with the <img> element and its src, alt and align attributes.",
        "Character formatting: <b>, <i>, <tt>, <em>, <strong>, <code>, <samp>, <kbd>, <var>, <cite>.",
        "The <head> and <body> structure and <meta>, <base>, <link>, <isindex> in the head.",
        "The <blockquote>, <br>, <hr> elements.",
        "Character entities such as &amp;, &lt;, &gt; and the ISO Latin-1 set (&eacute; and so on).",
        "The DOCTYPE declaration: <!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">",
    ]),
    ("note", "HTML 2.0 had no tables and no way to control colours or fonts. Pages were plain grey "
             "backgrounds with black text and blue links."),

    ("h2", "HTML 3.0 (1995, never finished) and HTML 3.2 (1997)"),
    ("p", "HTML 3.0 was an ambitious draft by Dave Raggett that proposed tables, mathematical formulas, "
          "figures and text flow around images. It was too large for browsers to implement and was "
          "abandoned. Meanwhile Netscape and Microsoft added their own tags (such as <font>, <center>, "
          "<blink> and <marquee>), starting the 'browser wars'."),
    ("p", "The newly formed World Wide Web Consortium (W3C) responded with HTML 3.2, published in January "
          "1997. Code-named 'Wilbur', it standardised what browsers actually did rather than what was "
          "ideal. HTML 3.2 is remembered as the version that mixed presentation into the markup."),
    ("p", "New in HTML 3.2:"),
    ("ul", [
        "Tables: <table>, <tr>, <td>, <th>, <caption>.",
        "Java applets: <applet>, <param>.",
        "Presentational elements: <font>, <center>, <big>, <small>, <strike>, <u>, <sub>, <sup>.",
        "Client-side image maps: <map>, <area>.",
        "<div> as a generic block container, with the align attribute.",
        "<script> and <style> were reserved for future use.",
        "Presentational attributes everywhere: bgcolor, text, link, vlink, alink on <body>; "
        "width, border, cellpadding, cellspacing on <table>; align on almost everything.",
    ]),

    ("h2", "HTML 4.0 (1997) and HTML 4.01 (1999): separation of structure and style"),
    ("p", "HTML 4.0 was published in December 1997 and revised as HTML 4.01 in December 1999. It is the "
          "version that introduced the idea that HTML should describe structure and meaning while "
          "Cascading Style Sheets (CSS) should describe appearance. Most presentational elements of "
          "HTML 3.2 were officially deprecated."),
    ("p", "HTML 4.01 came in three variants, chosen with the DOCTYPE:"),
    ("table", [
        ["Variant", "DOCTYPE", "Meaning"],
        ["Strict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">",
         "No deprecated elements, no frames."],
        ["Transitional", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">",
         "Deprecated elements allowed, to ease migration."],
        ["Frameset", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Frameset//EN\" \"http://www.w3.org/TR/html4/frameset.dtd\">",
         "Same as Transitional but the body is replaced by a <frameset>."],
    ]),
    ("p", "New in HTML 4.01:"),
    ("ul", [
        "Style sheets: the <style> element, the style attribute, the class and id attributes on all elements.",
        "Scripting: the <script> and <noscript> elements and the on* event attributes.",
        "Frames: <frameset>, <frame>, <noframes> and the inline <iframe>.",
        "Richer tables: <thead>, <tbody>, <tfoot>, <colgroup>, <col>, plus scope, headers, abbr, axis.",
        "Richer forms: <button>, <label>, <fieldset>, <legend>, <optgroup>, accesskey, tabindex, disabled, readonly.",
        "Internationalisation: lang and dir attributes, <bdo>, right-to-left text, Unicode support.",
        "Accessibility: the title attribute everywhere, alt required on <img>, longdesc, <abbr>, <acronym>.",
        "Generic <object> element for embedded content.",
        "New phrase elements: <ins>, <del>, <q>, <span>.",
    ]),

    ("h2", "XHTML 1.0 (2000) and XHTML 1.1 (2001)"),
    ("p", "XHTML was HTML 4.01 rewritten as an XML application. The elements were identical, but the "
          "syntax rules of XML applied: every tag must be closed (<br /> instead of <br>), all tag and "
          "attribute names must be lower case, attribute values must always be quoted, and a single error "
          "makes the whole page fail to display. XHTML 2.0 was planned as a completely new language but "
          "was abandoned in 2009 because it was not compatible with existing web pages."),

    ("h2", "HTML5 (2008 - 2014) and the HTML Living Standard (2019 - today)"),
    ("p", "In 2004 a group of browser makers (Apple, Mozilla and Opera) formed the WHATWG (Web Hypertext "
          "Application Technology Working Group) to evolve HTML in a backward-compatible way. Their work "
          "became HTML5. The W3C adopted it in 2007 and published HTML5 as a Recommendation in October "
          "2014, followed by HTML 5.1 (2016) and HTML 5.2 (2017)."),
    ("p", "In 2019 the W3C and WHATWG agreed that there would be only one HTML specification, the WHATWG "
          "'HTML Living Standard', which is updated continuously and has no version number. When people "
          "say 'HTML5' today they mean this living standard."),
    ("p", "New in HTML5:"),
    ("ul", [
        "A simple DOCTYPE: <!DOCTYPE html>",
        "Semantic sectioning elements: <header>, <footer>, <nav>, <main>, <article>, <section>, <aside>, <figure>, <figcaption>.",
        "Native audio and video: <audio>, <video>, <source>, <track>.",
        "Graphics: <canvas>, and inline <svg> and <math>.",
        "New form controls: input types email, url, tel, number, range, date, time, color, search; "
        "the placeholder, required, pattern, autofocus and autocomplete attributes; <datalist>, <output>, <progress>, <meter>.",
        "Interactive elements: <details>, <summary>, <dialog>.",
        "Text-level elements: <mark>, <time>, <data>, <wbr>, <bdi>, <ruby>, <rt>, <rp>.",
        "The <template>, <slot> and <picture> elements; the srcset and sizes attributes; lazy loading.",
        "Custom data attributes (data-*), contenteditable, draggable, hidden, spellcheck, translate.",
        "Removal of presentational elements: <font>, <center>, <big>, <strike>, <tt>, frames, <applet>.",
        "Precise parsing rules so that every browser builds the same document tree from the same HTML, "
        "even when the HTML contains mistakes.",
    ]),

    ("h2", "Timeline summary"),
    ("table", [
        ["Year", "Version", "Published by", "Key additions"],
        ["1991", "HTML Tags (HTML 1)", "Tim Berners-Lee, CERN", "Headings, paragraphs, lists, links"],
        ["1993", "HTML 1.0 draft", "IETF draft", "<img> added by Mosaic"],
        ["1995", "HTML 2.0", "IETF RFC 1866", "Forms, images, character formatting"],
        ["1997", "HTML 3.2", "W3C", "Tables, applets, <font>, <center>, presentational attributes"],
        ["1997", "HTML 4.0", "W3C", "CSS, scripting, frames, richer tables and forms"],
        ["1999", "HTML 4.01", "W3C", "Corrections to 4.0; Strict, Transitional, Frameset"],
        ["2000", "XHTML 1.0", "W3C", "HTML 4.01 in XML syntax"],
        ["2008", "HTML5 first draft", "WHATWG / W3C", "Semantic elements, audio, video, canvas"],
        ["2014", "HTML5 Recommendation", "W3C", "Official HTML5"],
        ["2016 / 2017", "HTML 5.1 / 5.2", "W3C", "<picture>, <dialog>, minor additions"],
        ["2019 - today", "HTML Living Standard", "WHATWG", "Single continuously updated specification"],
    ]),
]

FUNDAMENTALS = [
    ("h2", "What HTML is"),
    ("p", "HTML is a markup language, not a programming language. It cannot calculate, make decisions or "
          "loop. Its only job is to wrap pieces of content in tags that say what each piece is: 'this is a "
          "heading', 'this is a paragraph', 'this is a link to another page', 'this is the footer'. The "
          "browser reads these tags, builds a tree of objects called the DOM (Document Object Model), and "
          "draws the page. CSS (Cascading Style Sheets) then controls how it looks and JavaScript controls "
          "how it behaves."),

    ("h2", "Anatomy of an element"),
    ("code", "<p class=\"intro\">Hello, world!</p>\n"
             " |  |            |       |      |\n"
             " |  |            |       |      +-- closing tag\n"
             " |  |            |       +--------- content\n"
             " |  |            +----------------- end of opening tag\n"
             " |  +------------------------------ attribute name=\"value\"\n"
             " +--------------------------------- opening tag with tag name"),
    ("ul", [
        "The opening tag starts with < followed by the tag name and ends with >.",
        "Attributes go inside the opening tag, after the tag name, separated by spaces. Each attribute "
        "has a name and usually a value in quotes: name=\"value\".",
        "The content is everything between the opening and closing tag. It can be text, other elements or both.",
        "The closing tag is the same as the opening tag but with a slash after the <: </p>.",
        "The whole thing, from < to >, is called an element.",
    ]),

    ("h2", "Void elements (tags with no closing tag)"),
    ("p", "A small group of elements never have content and therefore never have a closing tag. Writing a "
          "closing tag for them is an error. In HTML5 you may write them as <br> or, in XML style, as <br />; "
          "both are accepted."),
    ("table", [
        ["Void element", "Purpose"],
        ["<area>", "Clickable region inside an image map"],
        ["<base>", "Base URL for the document"],
        ["<br>", "Line break"],
        ["<col>", "Table column properties"],
        ["<embed>", "External application content"],
        ["<hr>", "Thematic break (horizontal rule)"],
        ["<img>", "Image"],
        ["<input>", "Form control"],
        ["<link>", "External resource link (usually CSS)"],
        ["<meta>", "Metadata"],
        ["<source>", "Media or image source"],
        ["<track>", "Text track for media"],
        ["<wbr>", "Word break opportunity"],
    ]),

    ("h2", "The structure of a document"),
    ("code", "<!DOCTYPE html>\n"
             "<html lang=\"en\">\n"
             "<head>\n"
             "  <meta charset=\"utf-8\">\n"
             "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
             "  <title>Page title shown in the browser tab</title>\n"
             "  <link rel=\"stylesheet\" href=\"style.css\">\n"
             "</head>\n"
             "<body>\n"
             "  <header>\n"
             "    <h1>Site name</h1>\n"
             "    <nav><a href=\"/\">Home</a> <a href=\"/about\">About</a></nav>\n"
             "  </header>\n"
             "  <main>\n"
             "    <h2>Page heading</h2>\n"
             "    <p>Page content.</p>\n"
             "  </main>\n"
             "  <footer>\n"
             "    <p>&copy; 2026 Site name</p>\n"
             "  </footer>\n"
             "  <script src=\"app.js\"></script>\n"
             "</body>\n"
             "</html>"),
    ("table", [
        ["Line", "What it does"],
        ["<!DOCTYPE html>", "Tells the browser to use the modern standards rendering mode. Always the first line. Not a tag; it has no closing tag."],
        ["<html lang=\"en\">", "The root element. Everything else goes inside. lang states the language of the page."],
        ["<head>", "Information about the page that is not displayed: character set, title, links to CSS, metadata."],
        ["<meta charset=\"utf-8\">", "Declares the character encoding. Must come within the first 1024 bytes. UTF-8 supports every language."],
        ["<meta name=\"viewport\" ...>", "Makes the page scale correctly on phones."],
        ["<title>", "Required. Shown in the browser tab, bookmarks and search results."],
        ["<body>", "Everything the visitor sees."],
        ["<script>", "JavaScript. Usually placed at the end of the body or given the defer attribute so it does not block rendering."],
    ]),

    ("h2", "Attributes"),
    ("p", "Attributes give extra information about an element. They are written in the opening tag only. "
          "Rules:"),
    ("ul", [
        "Names are case-insensitive but by convention are written in lower case.",
        "Values should be quoted with double quotes. Single quotes are also allowed. Quotes may be omitted "
        "only if the value contains no spaces or special characters, but it is safer to always quote.",
        "A boolean attribute is either present or absent; its value does not matter. <input disabled>, "
        "<input disabled=\"\"> and <input disabled=\"disabled\"> all mean the same thing. Writing "
        "disabled=\"false\" still means disabled! To turn it off, remove the attribute.",
        "An attribute may appear only once on an element.",
        "Enumerated attributes accept a fixed list of keywords, for example dir=\"ltr\" or dir=\"rtl\".",
    ]),
    ("code", "<a href=\"https://example.com\" target=\"_blank\" rel=\"noopener\">Visit</a>\n"
             "<input type=\"checkbox\" checked disabled>\n"
             "<div id=\"main\" class=\"container wide\" data-user-id=\"42\"></div>"),

    ("h2", "Nesting"),
    ("p", "Elements must be properly nested: the element opened last must be closed first. "
          "<p><em>right</em></p> is correct; <p><em>wrong</p></em> is an error."),
    ("p", "Not every element may go inside every other. The rules are described by content categories "
          "(see below) and are listed in the 'Permitted parents' and 'Permitted content' rows of each "
          "element entry. The most common mistakes:"),
    ("ul", [
        "A <p> cannot contain block-level elements such as <div>, <ul>, <table> or another <p>. The browser "
        "will silently close the paragraph.",
        "An <a> cannot contain another <a> or any interactive element such as <button>.",
        "A <button> cannot contain interactive content.",
        "<li> must be a direct child of <ul>, <ol> or <menu>. <tr> must be inside <table>, <thead>, <tbody> "
        "or <tfoot>. <td> and <th> must be inside <tr>. <option> must be inside <select>, <optgroup> or <datalist>.",
        "<header> and <footer> cannot contain another <header> or <footer>.",
        "Heading elements must not be placed inside another heading.",
    ]),

    ("h2", "Content categories"),
    ("p", "HTML5 groups elements into categories that define where they may appear. An element may belong "
          "to several categories."),
    ("table", [
        ["Category", "Meaning", "Examples"],
        ["Metadata content", "Sets up the presentation or behaviour of the rest of the page; lives in <head>.",
         "<base>, <link>, <meta>, <noscript>, <script>, <style>, <title>"],
        ["Flow content", "Almost everything that may appear in <body>.",
         "<p>, <div>, <h1>, <ul>, <table>, <a>, <img>, plain text ..."],
        ["Sectioning content", "Defines the scope of headings and footers.",
         "<article>, <aside>, <nav>, <section>"],
        ["Heading content", "Section headings.", "<h1> to <h6>, <hgroup>"],
        ["Phrasing content", "Text and the elements that mark up text within a paragraph.",
         "<a>, <em>, <strong>, <span>, <img>, <input>, <code>, plain text ..."],
        ["Embedded content", "Imports another resource into the page.",
         "<audio>, <canvas>, <embed>, <iframe>, <img>, <math>, <object>, <picture>, <svg>, <video>"],
        ["Interactive content", "Designed for user interaction.",
         "<a href>, <button>, <details>, <input>, <label>, <select>, <textarea>, <video controls>"],
        ["Palpable content", "Content that is neither empty nor hidden, so that an element has something visible.", "Most flow and phrasing content"],
        ["Form-associated content", "Elements that have a form owner.",
         "<button>, <fieldset>, <input>, <label>, <meter>, <object>, <output>, <select>, <textarea>"],
    ]),

    ("h2", "Block-level and inline elements"),
    ("p", "Before HTML5 elements were described as either block-level or inline. The terms are still very "
          "useful because they match the default CSS display of each element."),
    ("table", [
        ["", "Block-level (display: block)", "Inline (display: inline)"],
        ["Starts on a new line?", "Yes", "No; flows with the text"],
        ["Takes full width?", "Yes, of its container", "Only as wide as its content"],
        ["Can set width/height?", "Yes", "No (unless display is changed)"],
        ["Can contain?", "Other blocks and inline elements", "Only other inline elements and text"],
        ["Examples", "<div>, <p>, <h1>-<h6>, <ul>, <ol>, <li>, <table>, <form>, <header>, <footer>, <section>, <article>, <nav>, <main>, <aside>, <blockquote>, <pre>, <hr>, <figure>",
         "<span>, <a>, <em>, <strong>, <b>, <i>, <img>, <code>, <br>, <input>, <label>, <button>, <select>, <textarea>, <abbr>, <cite>, <q>, <small>, <sub>, <sup>, <time>, <mark>"],
    ]),

    ("h2", "Comments"),
    ("code", "<!-- This is a comment. The browser ignores it. -->\n"
             "<!--\n  Comments can span\n  several lines.\n-->"),
    ("p", "Comments may not contain the sequence -- inside them and may not be nested. Remember that "
          "visitors can read comments by viewing the page source, so never put passwords or private "
          "information in them."),

    ("h2", "Character references (entities)"),
    ("p", "Some characters have special meaning in HTML and must be written as character references when "
          "you want them to appear as text. Every reference starts with & and ends with ;."),
    ("table", [
        ["Character", "Named reference", "Numeric reference", "Why it is needed"],
        ["<", "&lt;", "&#60;", "Starts a tag"],
        [">", "&gt;", "&#62;", "Ends a tag"],
        ["&", "&amp;", "&#38;", "Starts a reference"],
        ["\"", "&quot;", "&#34;", "Delimits attribute values"],
        ["'", "&apos;", "&#39;", "Delimits attribute values"],
        ["non-breaking space", "&nbsp;", "&#160;", "A space that will not wrap or collapse"],
        ["(c)", "&copy;", "&#169;", "Convenience"],
        ["EUR", "&euro;", "&#8364;", "Convenience"],
    ]),
    ("p", "Numeric references may be decimal (&#8364;) or hexadecimal (&#x20AC;). With UTF-8 encoding you "
          "can type most characters directly and only <, > and & really need references. The complete "
          "entity table is in Part 9."),

    ("h2", "Whitespace"),
    ("p", "In normal text the browser collapses any run of spaces, tabs and line breaks into a single space, "
          "and removes spaces at the start and end of a block. To preserve whitespace exactly, use the <pre> "
          "element or the CSS property white-space: pre. To force a line break use <br>. To insert a space "
          "that cannot collapse use &nbsp;."),

    ("h2", "Case sensitivity and quoting"),
    ("ul", [
        "Tag and attribute names are not case-sensitive in HTML (<DIV> equals <div>), but lower case is the "
        "universal convention and is required in XHTML.",
        "Attribute values may be case-sensitive depending on the attribute: id and class values are "
        "case-sensitive; enumerated keywords such as type=\"TEXT\" are not.",
        "Always quote attribute values. It avoids a whole category of bugs.",
    ]),

    ("h2", "Character encoding"),
    ("p", "Always save your files as UTF-8 and declare it with <meta charset=\"utf-8\"> as the first thing "
          "inside <head>. UTF-8 can represent every character of every language, including Arabic, and is "
          "the only encoding recommended by the HTML standard. If the encoding is wrong you will see "
          "question marks or strange symbols instead of your text."),

    ("h2", "Right-to-left languages"),
    ("p", "For Arabic, Hebrew, Persian and Urdu pages set dir=\"rtl\" and the correct lang on the <html> "
          "element. The browser then aligns text to the right, mirrors lists and tables and handles mixed "
          "left-to-right words correctly."),
    ("code", "<html lang=\"ar\" dir=\"rtl\">"),

    ("h2", "Validation"),
    ("p", "A validator is a tool that checks your HTML for errors. Browsers are forgiving and will display "
          "broken HTML, but the result may differ between browsers and may be inaccessible. Use the free W3C "
          "validator at https://validator.w3.org/ or the Nu HTML Checker at https://validator.nu/."),

    ("h2", "The ten most common beginner mistakes"),
    ("ul", [
        "Forgetting <!DOCTYPE html>, which puts the browser in 'quirks mode' and changes layout behaviour.",
        "Forgetting <meta charset=\"utf-8\">, which breaks non-English characters.",
        "Forgetting to close tags, or closing them in the wrong order.",
        "Putting block elements inside <p>.",
        "Using <br> repeatedly to create space instead of CSS margins.",
        "Using <table> for page layout instead of CSS.",
        "Using <b> and <i> for emphasis where <strong> and <em> carry the meaning.",
        "Omitting the alt attribute on images.",
        "Using <div> for everything where <header>, <nav>, <main>, <footer> describe the content better.",
        "Skipping heading levels (jumping from <h1> to <h4>).",
    ]),
]
