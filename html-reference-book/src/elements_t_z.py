# -*- coding: utf-8 -*-
"""Element reference entries, letters T to Z."""

ELEMENTS = [

dict(
    name="table", title="Table", cat="Table content",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <table> element represents tabular data: information arranged in a two-dimensional grid of "
        "rows and columns, where the position of each cell gives it meaning (this value belongs to this row "
        "and this column). Examples: price lists, timetables, statistics, comparison charts, spreadsheets.",
        "A table is built row by row. <tr> creates a row; inside it <th> creates a header cell and <td> a "
        "data cell. Optional <thead>, <tbody> and <tfoot> group the rows; <caption> gives the table a title; "
        "<colgroup> and <col> describe columns. The cells of each row must add up to the same number of "
        "columns, taking colspan and rowspan into account.",
        "Tables were introduced in HTML 3.2 and were immediately misused for page layout because there was "
        "no CSS. Layout tables are wrong today: they are inaccessible (screen readers announce rows and "
        "columns that mean nothing), not responsive, and hard to maintain. Use CSS flexbox and grid for "
        "layout; use <table> only for data.",
        "Browsers render tables without borders by default. Add them with CSS. border-collapse: collapse "
        "merges adjacent cell borders into single lines, which is almost always what you want.",
    ],
    syntax="<table>\n  <caption>Title</caption>\n  <thead><tr><th>Head</th></tr></thead>\n  <tbody><tr><td>Data</td></tr></tbody>\n</table>", void=False, display="table",
    categories="Flow content, palpable content",
    content="In this order: an optional <caption>, zero or more <colgroup>, an optional <thead>, either zero or more <tbody> or one or more <tr>, an optional <tfoot>; <script> and <template> may be intermixed",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLTableElement",
    attrs=[
        ("align", "left | center | right", "Obsolete. Alignment of the table on the page. Use CSS margin.", "HTML 3.2"),
        ("bgcolor", "colour", "Obsolete. Background colour. Use CSS background-color.", "HTML 3.2"),
        ("border", "pixels", "Obsolete. Border width around the table and cells. Use CSS border.", "HTML 3.2"),
        ("cellpadding", "pixels", "Obsolete. Space between cell content and cell border. Use CSS padding on td/th.", "HTML 3.2"),
        ("cellspacing", "pixels", "Obsolete. Space between cells. Use CSS border-spacing or border-collapse.", "HTML 3.2"),
        ("frame", "void | above | below | hsides | lhs | rhs | vsides | box | border", "Obsolete. Which outer borders to draw. Use CSS border.", "HTML 4.01"),
        ("rules", "none | groups | rows | cols | all", "Obsolete. Which inner borders to draw. Use CSS border on cells.", "HTML 4.01"),
        ("summary", "text", "Obsolete. Description of the table for screen readers. Use <caption> or aria-describedby.", "HTML 4.01"),
        ("width", "pixels or percentage", "Obsolete. Table width. Use CSS width.", "HTML 3.2"),
        ("height", "pixels", "Obsolete, non-standard. Use CSS.", "Netscape"),
    ],
    examples=[
        ("A complete data table",
         "<table>\n  <caption>Book prices, September 2026</caption>\n  <thead>\n    <tr>\n      <th scope=\"col\">Title</th>\n      <th scope=\"col\">Format</th>\n      <th scope=\"col\">Price (EGP)</th>\n    </tr>\n  </thead>\n"
         "  <tbody>\n    <tr>\n      <td>Learn HTML</td>\n      <td>PDF</td>\n      <td>120</td>\n    </tr>\n    <tr>\n      <td>Learn CSS</td>\n      <td>PDF</td>\n      <td>140</td>\n    </tr>\n  </tbody>\n"
         "  <tfoot>\n    <tr>\n      <th scope=\"row\" colspan=\"2\">Total</th>\n      <td>260</td>\n    </tr>\n  </tfoot>\n</table>", ""),
        ("Essential CSS for tables",
         "<style>\n  table { border-collapse: collapse; width: 100%; }\n  th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }\n  th { background: #f4f4f4; }\n  tbody tr:nth-child(even) { background: #fafafa; }\n  tbody tr:hover { background: #fff4e0; }\n  td.num { text-align: right; }\n</style>",
         "border-collapse removes double lines; nth-child gives zebra stripes; right-align numbers."),
        ("Row and column headers together",
         "<table>\n  <tr>\n    <td></td>\n    <th scope=\"col\">Mon</th>\n    <th scope=\"col\">Tue</th>\n  </tr>\n  <tr>\n    <th scope=\"row\">Morning</th>\n    <td>HTML</td>\n    <td>CSS</td>\n  </tr>\n  <tr>\n    <th scope=\"row\">Afternoon</th>\n    <td>Practice</td>\n    <td>Project</td>\n  </tr>\n</table>", ""),
        ("Spanning cells", "<table>\n  <tr>\n    <th colspan=\"2\">Name</th>\n    <th rowspan=\"2\">Age</th>\n  </tr>\n  <tr>\n    <th>First</th>\n    <th>Last</th>\n  </tr>\n  <tr>\n    <td>Ahmed</td>\n    <td>Ali</td>\n    <td>20</td>\n  </tr>\n</table>", "Each row still totals three columns."),
        ("Responsive: horizontal scroll on small screens", "<div style=\"overflow-x: auto\">\n  <table>...</table>\n</div>", ""),
        ("HTML 3.2 style attributes and their CSS replacement",
         "<!-- Old -->\n<table border=\"1\" cellpadding=\"5\" cellspacing=\"0\" width=\"100%\" bgcolor=\"#eeeeee\">\n\n<!-- New -->\n<style>\n  table { border-collapse: collapse; width: 100%; background: #eee; }\n  td, th { border: 1px solid #000; padding: 5px; }\n</style>\n<table>", ""),
    ],
    a11y=["Use <th> with scope for every header so screen readers can announce 'Price, 120' instead of just '120'.",
          "Give every data table a <caption>.", "Avoid layout tables; if unavoidable, add role=\"presentation\".",
          "Do not nest tables.", "For complex tables with multi-level headers, use the headers attribute on cells."],
    mistakes=["Using tables for layout.", "Rows with different numbers of cells.", "Forgetting border-collapse and getting double borders.", "Using <td> for headers.", "Placing text directly inside <table> or <tr>."],
    related=["tr", "td", "th", "thead", "tbody", "tfoot", "caption", "colgroup", "col"], css="table { display: table; border-collapse: separate; border-spacing: 2px; box-sizing: border-box; text-indent: initial; }",
),

dict(
    name="tbody", title="Table body", cat="Table content",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <tbody> element groups the main data rows of a table, as distinct from the header rows in "
        "<thead> and the summary rows in <tfoot>. A table may have several <tbody> elements to group rows "
        "into sections (for example one per category), which can then be styled separately. When you write "
        "<tr> directly inside <table> without a <tbody>, the browser creates one automatically, so a tbody "
        "is always present in the DOM.",
        "Using explicit thead/tbody/tfoot lets browsers repeat the header on every printed page of a long "
        "table and lets CSS make the body scroll independently.",
    ],
    syntax="<tbody>\n  <tr>...</tr>\n</tbody>", void=False, display="table-row-group",
    categories="None", content="Zero or more <tr>, <script>, <template>", parents="<table>, after <caption>, <colgroup> and <thead>",
    omission="Start tag may be omitted if the first thing inside is a <tr> and it is not preceded by a tbody, thead or tfoot whose end tag was omitted; end tag may be omitted if followed by <tbody> or <tfoot> or if there is no more content in the parent",
    dom="HTMLTableSectionElement",
    attrs=[("align, bgcolor, char, charoff, valign", "various", "Obsolete presentational attributes. Use CSS.", "HTML 4.01")],
    examples=[
        ("Multiple bodies for grouped rows",
         "<table>\n  <thead><tr><th>Item</th><th>Price</th></tr></thead>\n  <tbody>\n    <tr><th colspan=\"2\">Books</th></tr>\n    <tr><td>Learn HTML</td><td>120</td></tr>\n  </tbody>\n  <tbody>\n    <tr><th colspan=\"2\">Courses</th></tr>\n    <tr><td>CSS Basics</td><td>300</td></tr>\n  </tbody>\n</table>", ""),
        ("Scrolling body with fixed header", "<style>\n  .wrap { max-height: 300px; overflow-y: auto; }\n  thead th { position: sticky; top: 0; background: #fff; }\n</style>\n<div class=\"wrap\"><table>...</table></div>", ""),
    ],
    a11y=["No special role; it exists for structure and styling."], mistakes=["Putting tbody before thead.", "Placing cells directly inside tbody without tr."],
    related=["table", "thead", "tfoot", "tr"], css="tbody { display: table-row-group; vertical-align: middle; }",
),

dict(
    name="td", title="Table data cell", cat="Table content",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <td> element defines a cell of a table that contains data. It must be inside a <tr>. Each "
        "<td> occupies one column by default; colspan makes it span several columns and rowspan several "
        "rows. The headers attribute can list the ids of the <th> cells that describe it, which is needed "
        "only for complex tables where scope is not enough.",
        "Data cells are left-aligned and normal weight by default, in contrast to header cells (<th>) which "
        "are bold and centred. Use <th> for headers even if you restyle them, because the distinction is "
        "what screen readers rely on.",
    ],
    syntax="<tr>\n  <td>Data</td>\n</tr>", void=False, display="table-cell",
    categories="Sectioning root", content="Flow content", parents="<tr>",
    omission="Start tag required; end tag may be omitted if followed by <td> or <th> or if there is no more content in the parent", dom="HTMLTableCellElement",
    attrs=[
        ("colspan", "positive integer", "Number of columns the cell spans. Default 1, maximum 1000.", "HTML 3.2"),
        ("rowspan", "non-negative integer", "Number of rows the cell spans. Default 1; 0 means to the end of the row group. Maximum 65534.", "HTML 3.2"),
        ("headers", "space-separated ids", "The ids of <th> cells that provide headers for this cell.", "HTML 4.01"),
        ("abbr", "text", "Obsolete on td (valid on th). Abbreviated description.", "HTML 4.01"),
        ("align", "left | center | right | justify | char", "Obsolete. Use CSS text-align.", "HTML 3.2"),
        ("axis", "text", "Obsolete. Category names.", "HTML 4.01"),
        ("bgcolor", "colour", "Obsolete. Use CSS background-color.", "HTML 3.2"),
        ("char / charoff", "character / number", "Obsolete. Character alignment.", "HTML 4.01"),
        ("height", "pixels", "Obsolete. Use CSS height.", "HTML 3.2"),
        ("nowrap", "boolean", "Obsolete. Use CSS white-space: nowrap.", "HTML 3.2"),
        ("scope", "-", "Obsolete on td (use on th).", "HTML 4.01"),
        ("valign", "top | middle | bottom | baseline", "Obsolete. Use CSS vertical-align.", "HTML 3.2"),
        ("width", "pixels or percentage", "Obsolete. Use CSS width.", "HTML 3.2"),
    ],
    examples=[
        ("Basic cells", "<table>\n  <tr>\n    <th>Name</th>\n    <th>Age</th>\n  </tr>\n  <tr>\n    <td>Ahmed</td>\n    <td>20</td>\n  </tr>\n  <tr>\n    <td>Sara</td>\n    <td>22</td>\n  </tr>\n</table>", "Row 1 has header cells, rows 2 and 3 have data cells."),
        ("colspan and rowspan", "<table>\n  <tr>\n    <td rowspan=\"2\">Spans two rows</td>\n    <td>Row 1</td>\n  </tr>\n  <tr>\n    <td>Row 2</td>\n  </tr>\n  <tr>\n    <td colspan=\"2\">Spans two columns</td>\n  </tr>\n</table>", ""),
        ("Complex header association", "<table>\n  <tr>\n    <th id=\"n\">Name</th>\n    <th id=\"q1\">Q1</th>\n    <th id=\"q2\">Q2</th>\n  </tr>\n  <tr>\n    <th id=\"r1\" headers=\"n\">Ahmed</th>\n    <td headers=\"r1 q1\">10</td>\n    <td headers=\"r1 q2\">12</td>\n  </tr>\n</table>", ""),
        ("Cell styling", "<style>\n  td { padding: 8px 12px; border-bottom: 1px solid #e0e0e0; vertical-align: top; }\n  td.num { text-align: right; font-variant-numeric: tabular-nums; }\n</style>", ""),
    ],
    a11y=["Do not leave header cells as <td>.", "Empty cells are fine; do not fill them with &nbsp; unless needed for old-browser borders."],
    mistakes=["Placing <td> outside <tr>.", "Inconsistent column counts.", "Using td for headers."],
    related=["th", "tr", "table"], css="td { display: table-cell; vertical-align: inherit; padding: 1px; }",
),

dict(
    name="template", title="Content template", cat="Scripting / web components",
    versions="HTML5 (2013)", status="current",
    desc=[
        "The <template> element holds HTML that is not rendered when the page loads but can be cloned and "
        "inserted into the document later by JavaScript. The content is parsed into a separate document "
        "fragment (template.content): scripts inside do not run, images do not load and the markup is "
        "invisible. It is the standard way to define reusable markup for lists, cards and web components.",
        "Declarative Shadow DOM uses <template shadowrootmode=\"open\"> inside a custom element to create a "
        "shadow root without JavaScript.",
    ],
    syntax="<template id=\"t\">\n  <li class=\"item\"></li>\n</template>", void=False, display="none",
    categories="Metadata content, flow content, phrasing content, script-supporting element",
    content="Anything (stored in a DocumentFragment, not rendered)", parents="Almost anywhere: head, body, and inside table, colgroup, dl, ol, ul, select...",
    omission="Neither tag may be omitted", dom="HTMLTemplateElement",
    attrs=[
        ("shadowrootmode", "open | closed", "Creates a declarative shadow root on the parent element.", "Living Standard"),
        ("shadowrootdelegatesfocus", "boolean", "Sets delegatesFocus on the declarative shadow root.", "Living Standard"),
        ("shadowrootclonable", "boolean", "Sets clonable on the declarative shadow root.", "Living Standard"),
        ("shadowrootserializable", "boolean", "Sets serializable on the declarative shadow root.", "Living Standard"),
    ],
    examples=[
        ("Cloning a row template",
         "<table id=\"cart\"><tbody></tbody></table>\n<template id=\"row\">\n  <tr><td class=\"name\"></td><td class=\"price\"></td></tr>\n</template>\n<script>\n  const items = [['Learn HTML', 120], ['Learn CSS', 140]];\n  const tpl = document.getElementById('row');\n  const body = document.querySelector('#cart tbody');\n"
         "  for (const [name, price] of items) {\n    const clone = tpl.content.cloneNode(true);\n    clone.querySelector('.name').textContent = name;\n    clone.querySelector('.price').textContent = price;\n    body.append(clone);\n  }\n</script>", ""),
        ("Declarative shadow DOM", "<my-card>\n  <template shadowrootmode=\"open\">\n    <style>p { color: #b90000; }</style>\n    <p><slot></slot></p>\n  </template>\n  Hello from the light DOM\n</my-card>", ""),
    ],
    a11y=["Template content is not in the accessibility tree until inserted."],
    mistakes=["Using innerHTML on template instead of template.content.", "Expecting scripts inside the template to run before insertion."],
    related=["slot", "script", "noscript"], css="template { display: none; }",
),

dict(
    name="textarea", title="Multi-line text input", cat="Forms",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <textarea> element creates a multi-line plain-text editing control, for comments, messages, "
        "addresses and any free-form text. Unlike <input>, it is not a void element: its initial value is "
        "the text between its tags, not a value attribute. Whitespace and line breaks inside the tags are "
        "preserved, so keep the closing tag right after the text to avoid unwanted spaces.",
        "The rows and cols attributes set its visible size in lines and characters; CSS width/height are "
        "more flexible. Most browsers let the user drag-resize it; control this with the CSS resize "
        "property. The field-sizing: content CSS property (new) makes it grow with its content.",
    ],
    syntax="<textarea name=\"n\" rows=\"4\" cols=\"40\">initial text</textarea>", void=False, display="inline-block",
    categories="Flow content, phrasing content, interactive content, listed, labelable, resettable, submittable, form-associated, palpable",
    content="Text", parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLTextAreaElement",
    attrs=[
        ("name", "text", "Name submitted with the form.", "HTML 2.0"),
        ("rows", "positive integer", "Visible number of lines. Default 2.", "HTML 2.0"),
        ("cols", "positive integer", "Visible width in average characters. Default 20.", "HTML 2.0"),
        ("placeholder", "text", "Hint shown when empty. Not a label.", "HTML5"),
        ("required", "boolean", "Must not be empty.", "HTML5"),
        ("disabled", "boolean", "Cannot be used or submitted.", "HTML 4.01"),
        ("readonly", "boolean", "Cannot be edited; is submitted.", "HTML 4.01"),
        ("maxlength", "integer", "Maximum characters.", "HTML5"),
        ("minlength", "integer", "Minimum characters.", "HTML5"),
        ("wrap", "soft | hard | off", "soft (default): lines wrap visually but newlines are not submitted. hard: newlines are inserted at wrap points when submitting (requires cols). off: no wrapping (non-standard).", "HTML5"),
        ("autocomplete", "on | off | token", "Autofill hint (street-address, etc.).", "HTML5"),
        ("autofocus", "boolean", "Focus on load.", "HTML5"),
        ("spellcheck", "true | false", "Enable or disable spell checking (global).", "HTML5"),
        ("dirname", "text", "Submit text direction.", "HTML5"),
        ("form", "form id", "Associated form.", "HTML5"),
    ],
    examples=[
        ("Message field", "<label for=\"msg\">Message</label>\n<textarea id=\"msg\" name=\"message\" rows=\"5\" placeholder=\"Write your message...\" required maxlength=\"500\"></textarea>", ""),
        ("With initial text", "<textarea name=\"bio\">Write a short bio here.</textarea>", ""),
        ("Styling and resize control", "<style>\n  textarea { width: 100%; min-height: 120px; padding: 8px; font: inherit; resize: vertical; box-sizing: border-box; }\n</style>", ""),
        ("Character counter", "<textarea id=\"t\" maxlength=\"200\"></textarea>\n<output id=\"c\" for=\"t\">0 / 200</output>\n<script>\n  t.addEventListener('input', () => c.value = t.value.length + ' / 200');\n</script>", ""),
    ],
    a11y=["Label it.", "Do not remove the resize handle without good reason.", "Announce character limits in the label or description."],
    mistakes=["Writing <textarea value=\"...\"> (value is not an attribute here).", "Indenting the content and getting leading spaces.", "Forgetting the closing tag; everything after becomes part of the textarea."],
    related=["input", "form", "label", "output"], css="textarea { display: inline-block; white-space: pre-wrap; resize: both; }",
),

dict(
    name="tfoot", title="Table footer", cat="Table content",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <tfoot> element groups the rows that summarise the columns of a table: totals, averages, "
        "counts. In HTML5 it is placed after the <tbody> elements (HTML 4.01 required it before them so "
        "that the browser could render the footer before receiving all data). When printing a long table, "
        "browsers can repeat the tfoot at the bottom of every page.",
    ],
    syntax="<tfoot>\n  <tr><th>Total</th><td>260</td></tr>\n</tfoot>", void=False, display="table-footer-group",
    categories="None", content="Zero or more <tr>, <script>, <template>", parents="<table>, after caption, colgroup, thead and tbody",
    omission="End tag may be omitted if there is no more content in the parent", dom="HTMLTableSectionElement",
    attrs=[("align, bgcolor, char, charoff, valign", "various", "Obsolete presentational attributes. Use CSS.", "HTML 4.01")],
    examples=[("Totals row", "<table>\n  <thead><tr><th>Item</th><th>Price</th></tr></thead>\n  <tbody>\n    <tr><td>Book</td><td>120</td></tr>\n    <tr><td>Pen</td><td>10</td></tr>\n  </tbody>\n  <tfoot>\n    <tr><th scope=\"row\">Total</th><td>130</td></tr>\n  </tfoot>\n</table>", ""),
              ("Styling", "<style>\n  tfoot { font-weight: bold; background: #f4f4f4; border-top: 2px solid #333; }\n</style>", "")],
    a11y=["No special role, but grouping totals in tfoot helps users understand the table structure."],
    mistakes=["Placing tfoot in the middle of the table.", "Multiple tfoot elements."],
    related=["table", "thead", "tbody"], css="tfoot { display: table-footer-group; vertical-align: middle; }",
),

dict(
    name="th", title="Table header cell", cat="Table content",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <th> element defines a header cell in a table: a cell that labels a column or a row rather "
        "than holding data. Browsers render it bold and centred. The scope attribute states whether the "
        "header applies to its column (col), its row (row), a group of columns (colgroup) or a group of rows "
        "(rowgroup). Browsers can usually guess for simple tables, but stating it explicitly is best "
        "practice because screen readers use the header text when reading each data cell.",
    ],
    syntax="<th scope=\"col\">Header</th>", void=False, display="table-cell",
    categories="None", content="Flow content, but no header, footer, sectioning content or heading content", parents="<tr>",
    omission="End tag may be omitted if followed by <td> or <th> or if there is no more content in the parent", dom="HTMLTableCellElement",
    attrs=[
        ("scope", "row | col | rowgroup | colgroup", "Which cells this header describes.", "HTML 4.01"),
        ("colspan", "positive integer", "Columns spanned.", "HTML 3.2"),
        ("rowspan", "non-negative integer", "Rows spanned.", "HTML 3.2"),
        ("headers", "space-separated ids", "Other header cells that apply to this one (for multi-level headers).", "HTML 4.01"),
        ("abbr", "text", "A short alternative label that screen readers may use when reading the header repeatedly.", "HTML 4.01"),
        ("align, axis, bgcolor, char, charoff, height, nowrap, valign, width", "various", "Obsolete presentational attributes. Use CSS.", "HTML 3.2 / 4.01"),
    ],
    examples=[
        ("Column and row headers", "<table>\n  <tr>\n    <th scope=\"col\">Product</th>\n    <th scope=\"col\">Price</th>\n  </tr>\n  <tr>\n    <th scope=\"row\">Notebook</th>\n    <td>25</td>\n  </tr>\n</table>", "A screen reader on the '25' cell announces: 'Notebook, Price, 25'."),
        ("Group headers", "<table>\n  <tr>\n    <th scope=\"colgroup\" colspan=\"2\">2025</th>\n    <th scope=\"colgroup\" colspan=\"2\">2026</th>\n  </tr>\n  <tr>\n    <th scope=\"col\">Q1</th><th scope=\"col\">Q2</th>\n    <th scope=\"col\">Q1</th><th scope=\"col\">Q2</th>\n  </tr>\n</table>", ""),
        ("Left-aligned headers", "<style>\n  th { text-align: left; background: #f4f4f4; }\n  th[scope=\"row\"] { font-weight: 600; }\n</style>", ""),
    ],
    a11y=["Always use <th> for headers and set scope.", "Use abbr for long headers that will be repeated often."],
    mistakes=["Using <td> with bold styling instead of <th>.", "Omitting scope in tables with both row and column headers."],
    related=["td", "tr", "table", "thead"], css="th { display: table-cell; vertical-align: inherit; font-weight: bold; text-align: center; padding: 1px; }",
),

dict(
    name="thead", title="Table header", cat="Table content",
    versions="HTML 4.01, HTML5", status="current",
    desc=[
        "The <thead> element groups the rows that hold the column headers of a table. It comes after any "
        "<caption> and <colgroup> and before <tbody> and <tfoot>. Browsers repeat the thead at the top of "
        "each printed page of a long table, and CSS position: sticky on its cells keeps the headers "
        "visible while scrolling. A table may have at most one thead.",
    ],
    syntax="<thead>\n  <tr><th>Column</th></tr>\n</thead>", void=False, display="table-header-group",
    categories="None", content="Zero or more <tr>, <script>, <template>", parents="<table>, after caption and colgroup, before tbody, tfoot and tr",
    omission="End tag may be omitted if followed by <tbody> or <tfoot>", dom="HTMLTableSectionElement",
    attrs=[("align, bgcolor, char, charoff, valign", "various", "Obsolete presentational attributes. Use CSS.", "HTML 4.01")],
    examples=[("Header group", "<table>\n  <thead>\n    <tr>\n      <th scope=\"col\">Name</th>\n      <th scope=\"col\">Email</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr><td>Ahmed</td><td>ahmed@example.com</td></tr>\n  </tbody>\n</table>", ""),
              ("Sticky header", "<style>\n  thead th { position: sticky; top: 0; background: #fff; box-shadow: 0 1px 0 #ccc; }\n</style>", "")],
    a11y=["Helps assistive technology identify header rows; combine with th scope=\"col\"."],
    mistakes=["Two thead elements.", "Putting data rows in thead."],
    related=["table", "tbody", "tfoot", "th"], css="thead { display: table-header-group; vertical-align: middle; }",
),

dict(
    name="time", title="Date / time", cat="Text-level semantics",
    versions="HTML5", status="current",
    desc=[
        "The <time> element represents a specific period in time: a date, a time of day, a date and time, "
        "a duration, a week or a month. The optional datetime attribute holds the value in a machine-readable "
        "format so that browsers, search engines, calendars and scripts can understand it, while the "
        "visible content can be written in any human-friendly way ('11 September 2026', 'yesterday', "
        "'\u0661\u0661 \u0633\u0628\u062a\u0645\u0628\u0631'). If datetime is omitted, the text content itself must be in a valid format.",
    ],
    syntax="<time datetime=\"2026-09-11\">11 September 2026</time>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLTimeElement",
    attrs=[
        ("datetime", "date/time string", "Machine-readable value. Formats: 2026-09-11 (date); 14:30 or 14:30:00 (time); 2026-09-11T14:30 (local date-time); 2026-09-11T14:30Z or 2026-09-11T14:30+02:00 (with time zone); 2026-09 (month); 2026-W37 (week); 2026 (year); 09-11 (yearless date); PT2H30M or 2h 30m (duration).", "HTML5"),
    ],
    examples=[
        ("Publication date", "<p>Published <time datetime=\"2026-09-11\">11 September 2026</time></p>", ""),
        ("Event with time zone", "<p>The webinar starts at <time datetime=\"2026-10-01T19:00+02:00\">7 pm Cairo time on 1 October</time>.</p>", ""),
        ("Duration", "<p>Reading time: <time datetime=\"PT8M\">8 minutes</time></p>", ""),
        ("Relative text with exact value", "<p>Posted <time datetime=\"2026-09-10T09:15Z\" title=\"10 Sep 2026, 09:15 UTC\">yesterday</time></p>", ""),
    ],
    a11y=["Screen readers read the visible text, not datetime; keep the visible text understandable."],
    mistakes=["Invalid datetime formats such as 11/09/2026.", "Using <time> for vague periods ('the Middle Ages')."],
    related=["data", "article"], css="time { display: inline; }",
),

dict(
    name="title", title="Document title", cat="Document metadata",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <title> element defines the title of the document, shown in the browser's title bar or tab, "
        "used as the default name for bookmarks, displayed as the clickable headline in search engine "
        "results, and announced first by screen readers when the page loads. It contains text only; any "
        "tags inside are treated as literal text. Every document must have exactly one <title>, inside <head>.",
        "A good title is unique for each page, describes the page's content, puts the most specific "
        "information first ('Learn HTML - Book Store' rather than 'Book Store - Learn HTML'), and is under "
        "about 60 characters so search engines do not truncate it.",
    ],
    syntax="<title>Page title</title>", void=False, display="none",
    categories="Metadata content", content="Text (not inter-element whitespace only)", parents="<head> (exactly one)",
    omission="Neither tag may be omitted", dom="HTMLTitleElement",
    attrs=[],
    examples=[
        ("Good titles", "<title>Learn HTML (PDF) - Book Store</title>\n<title>Contact us - Book Store</title>\n<title>Order #1042 confirmed - Book Store</title>", ""),
        ("Changing the title from JavaScript", "<script>\n  document.title = '(3) New messages - Chat';\n</script>", ""),
    ],
    a11y=["The title is the first thing announced; unique, descriptive titles are a WCAG requirement (2.4.2)."],
    mistakes=["Same title on every page.", "Empty or missing title.", "Putting HTML tags inside.", "Keyword stuffing."],
    related=["head", "meta", "h1"], css="title { display: none; }",
),

dict(
    name="tr", title="Table row", cat="Table content",
    versions="HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <tr> element defines a row of cells in a table. It contains <th> (header) and/or <td> (data) "
        "cells and is placed inside <table>, <thead>, <tbody> or <tfoot>. Rows are the fundamental unit of "
        "table construction: you build a table one row at a time, and the columns emerge from the cells in "
        "each row.",
    ],
    syntax="<tr>\n  <td>Cell 1</td>\n  <td>Cell 2</td>\n</tr>", void=False, display="table-row",
    categories="None", content="Zero or more <td>, <th>, <script>, <template>", parents="<table> (directly), <thead>, <tbody>, <tfoot>",
    omission="End tag may be omitted if followed by another <tr> or if there is no more content in the parent", dom="HTMLTableRowElement",
    attrs=[
        ("align", "left | center | right | justify | char", "Obsolete. Use CSS text-align on cells.", "HTML 3.2"),
        ("bgcolor", "colour", "Obsolete. Use CSS background-color.", "HTML 3.2"),
        ("char / charoff", "character / number", "Obsolete.", "HTML 4.01"),
        ("valign", "top | middle | bottom | baseline", "Obsolete. Use CSS vertical-align.", "HTML 3.2"),
    ],
    examples=[
        ("Three rows", "<table>\n  <tr>\n    <th>Name</th>\n    <th>Age</th>\n  </tr>\n  <tr>\n    <td>Ahmed</td>\n    <td>20</td>\n  </tr>\n  <tr>\n    <td>Sara</td>\n    <td>22</td>\n  </tr>\n</table>", ""),
        ("Row styling", "<style>\n  tr:nth-child(even) { background: #f9f9f9; }\n  tr:hover { background: #eef; }\n  tr.selected { outline: 2px solid #1b6fd8; }\n</style>", ""),
        ("Adding a row with JavaScript", "<script>\n  const row = document.querySelector('table').insertRow();\n  row.insertCell().textContent = 'Omar';\n  row.insertCell().textContent = '25';\n</script>", ""),
    ],
    a11y=["Screen readers announce row numbers; keep one logical record per row."],
    mistakes=["Text or elements directly inside <tr> that are not td/th.", "Different numbers of cells per row.", "Nesting tr inside td without a new table."],
    related=["table", "td", "th", "thead", "tbody", "tfoot"], css="tr { display: table-row; vertical-align: inherit; }",
),

dict(
    name="track", title="Text track for media", cat="Image and multimedia",
    versions="HTML5", status="current",
    desc=[
        "The <track> element adds timed text tracks to <audio> or <video>: subtitles (translations), "
        "captions (dialogue plus sound descriptions for deaf and hard-of-hearing viewers), descriptions "
        "(spoken description of the video for blind users), chapters (navigation) and metadata (for "
        "scripts). Tracks are WebVTT files (.vtt). It is a void element placed after any <source> elements.",
        "Only one track per kind may have the default attribute. Track files loaded from another origin "
        "require CORS headers and the crossorigin attribute on the media element.",
    ],
    syntax="<track kind=\"captions\" src=\"captions.vtt\" srclang=\"en\" label=\"English\" default>", void=True, display="none",
    categories="None", content="None (void element)", parents="<audio>, <video>, after <source> and before flow content",
    omission="No end tag", dom="HTMLTrackElement",
    attrs=[
        ("src", "URL", "Required. The WebVTT file.", "HTML5"),
        ("kind", "subtitles | captions | descriptions | chapters | metadata", "The type of track. Default subtitles.", "HTML5"),
        ("srclang", "language tag", "Language of the track. Required for subtitles.", "HTML5"),
        ("label", "text", "Human-readable title shown in the track menu.", "HTML5"),
        ("default", "boolean", "Enable this track by default (one per kind).", "HTML5"),
    ],
    examples=[
        ("Video with captions and subtitles",
         "<video controls width=\"640\" height=\"360\">\n  <source src=\"lesson.mp4\" type=\"video/mp4\">\n  <track kind=\"captions\" src=\"lesson-en.vtt\" srclang=\"en\" label=\"English captions\" default>\n  <track kind=\"subtitles\" src=\"lesson-ar.vtt\" srclang=\"ar\" label=\"\u0627\u0644\u0639\u0631\u0628\u064a\u0629\">\n  <track kind=\"chapters\" src=\"chapters.vtt\" srclang=\"en\">\n</video>", ""),
        ("A WebVTT file", "WEBVTT\n\n00:00:00.000 --> 00:00:04.000\nWelcome to the HTML course.\n\n00:00:04.500 --> 00:00:08.000\nToday we learn about the footer element.", "Save as lesson-en.vtt; the first line must be WEBVTT."),
    ],
    a11y=["Captions are required for accessible video (WCAG 1.2.2). Subtitles alone are not captions: captions also describe sounds.", "Provide descriptions for visual-only information."],
    mistakes=["Placing track before source.", "Wrong MIME type on the server (should be text/vtt).", "Two default tracks of the same kind."],
    related=["video", "audio", "source"], css="track { display: none; }",
),

dict(
    name="tt", title="Teletype text (obsolete)", cat="Obsolete presentational",
    versions="HTML 2.0, HTML 3.2, HTML 4.01; obsolete in HTML5", status="obsolete",
    desc=[
        "The <tt> element (teletype) rendered text in a monospace font, imitating a teletype or typewriter. "
        "It was purely presentational and HTML5 removed it. Use the semantic elements <code>, <kbd>, <samp> "
        "or <var>, or CSS font-family: monospace on a <span>.",
    ],
    syntax="<tt>text</tt>", void=False, display="inline",
    categories="Historical", content="Phrasing content", parents="Phrasing content", omission="Neither", dom="HTMLElement",
    attrs=[],
    examples=[("Replacements", "<!-- Old -->\n<tt>ls -la</tt>\n\n<!-- New -->\n<kbd>ls -la</kbd>  <!-- user input -->\n<code>ls -la</code> <!-- code -->\n<span style=\"font-family: monospace\">ls -la</span> <!-- style only -->", "")],
    a11y=[], mistakes=["Any use."], related=["code", "kbd", "samp", "var", "pre"], css="tt { font-family: monospace; }",
),

dict(
    name="u", title="Unarticulated annotation (underline)", cat="Text-level semantics",
    versions="HTML 3.2, HTML 4.01 (deprecated), HTML5 (redefined)", status="current",
    desc=[
        "The <u> element represents a span of inline text that should be rendered in a way that indicates "
        "a non-textual annotation: most commonly, marking misspelled words (as a word processor does with a "
        "wavy red line) or labelling proper names in Chinese text. Browsers render it with a solid underline. "
        "In HTML 4 <u> simply meant 'underline' and was deprecated; HTML5 redefined it.",
        "Because underlined text looks like a link on the web, avoid <u> for anything that is not one of "
        "its intended uses. For emphasis use <em>; for titles <cite>; for pure decoration CSS text-decoration.",
    ],
    syntax="<u>text</u>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Spelling error", "<p>Please chek <u class=\"spelling\">recieve</u> before sending.</p>\n<style>.spelling { text-decoration: red wavy underline; }</style>", ""),
        ("Wrong use", "<!-- Do not do this: looks like a link and carries no meaning -->\n<p><u>Important</u></p>\n\n<!-- Do this -->\n<p><strong>Important</strong></p>", ""),
    ],
    a11y=["Underlined non-link text confuses users; they may try to click it."],
    mistakes=["Using <u> for emphasis or headings."], related=["em", "ins", "s", "span"], css="u { text-decoration: underline; }",
),

dict(
    name="ul", title="Unordered list", cat="Text content",
    versions="HTML 1, HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <ul> element represents an unordered list of items: a list where changing the order would "
        "not change the meaning, such as a shopping list, a set of features, or the links of a navigation "
        "menu. Browsers show each item with a bullet. Each item is an <li>. If the order matters, use <ol>.",
        "Lists are among the most useful elements in HTML because they carry structure: screen readers "
        "announce how many items there are and let users jump between them. Navigation menus are almost "
        "always built as a <ul> inside a <nav>, with CSS removing the bullets and arranging the items "
        "horizontally.",
    ],
    syntax="<ul>\n  <li>Item</li>\n  <li>Item</li>\n</ul>", void=False, display="block",
    categories="Flow content; palpable if it has at least one <li>", content="Zero or more <li>, <script>, <template>",
    parents="Any element that accepts flow content", omission="Neither tag may be omitted", dom="HTMLUListElement",
    attrs=[
        ("type", "disc | circle | square", "Obsolete. Bullet style. Use CSS list-style-type.", "HTML 3.2"),
        ("compact", "boolean", "Obsolete. Compact rendering.", "HTML 2.0"),
    ],
    examples=[
        ("Shopping list", "<ul>\n  <li>Milk</li>\n  <li>Bread</li>\n  <li>Eggs</li>\n</ul>", "Shows three bulleted lines."),
        ("Nested lists", "<ul>\n  <li>Fruit\n    <ul>\n      <li>Apples</li>\n      <li>Bananas</li>\n    </ul>\n  </li>\n  <li>Vegetables</li>\n</ul>", "Nested lists get a different bullet automatically (disc, then circle, then square)."),
        ("Bullet styles", "<ul style=\"list-style-type: square\">...</ul>\n<ul style=\"list-style-type: '\u2713 '\">...</ul>\n<ul style=\"list-style-image: url(star.png)\">...</ul>", ""),
        ("Navigation menu", "<style>\n  .menu { list-style: none; margin: 0; padding: 0; display: flex; gap: 20px; }\n</style>\n<nav>\n  <ul class=\"menu\">\n    <li><a href=\"/\">Home</a></li>\n    <li><a href=\"/shop\">Shop</a></li>\n    <li><a href=\"/contact\">Contact</a></li>\n  </ul>\n</nav>", ""),
        ("Custom bullets with ::marker", "<style>\n  li::marker { color: #e60000; font-size: 1.2em; }\n</style>", ""),
    ],
    a11y=["Announced as 'list, 3 items'. In Safari, list-style: none removes list semantics; add role=\"list\" to the ul to keep them."],
    mistakes=["Text directly inside <ul> outside <li>.", "Using <ul> for ordered steps.", "Using <br> or paragraphs with dashes instead of a real list."],
    related=["ol", "li", "menu", "dl", "nav"], css="ul { display: block; list-style-type: disc; margin: 1em 0; padding-inline-start: 40px; }",
),

dict(
    name="var", title="Variable", cat="Text-level semantics",
    versions="HTML 2.0, HTML 3.2, HTML 4.01, HTML5", status="current",
    desc=[
        "The <var> element represents the name of a variable in a mathematical expression or a programming "
        "context, or a placeholder for a value the reader must supply. Browsers render it in italics. It is "
        "one of the four 'computer' phrase elements together with <code>, <kbd> and <samp>.",
    ],
    syntax="<var>x</var>", void=False, display="inline",
    categories="Flow content, phrasing content, palpable content", content="Phrasing content",
    parents="Any element that accepts phrasing content", omission="Neither tag may be omitted", dom="HTMLElement",
    attrs=[],
    examples=[("Maths", "<p>The area is <var>w</var> \u00d7 <var>h</var>.</p>", ""),
              ("Placeholder in instructions", "<p>Type <kbd>cd <var>folder-name</var></kbd> to enter a folder.</p>", "")],
    a11y=[], mistakes=["Using <i> or <em> for variables."], related=["code", "kbd", "samp", "math"], css="var { font-style: italic; }",
),

dict(
    name="video", title="Embedded video", cat="Image and multimedia",
    versions="HTML5", status="current",
    desc=[
        "The <video> element embeds a video player in the document. The video file is given by src or by "
        "one or more <source> children (so that the browser can pick a supported format), followed by "
        "optional <track> elements for captions and subtitles, and finally fallback content for browsers "
        "without video support. Common formats are MP4 (H.264/AAC, universally supported), WebM (VP9/AV1, "
        "smaller) and, in Safari, HEVC.",
        "The controls attribute shows the built-in play/pause, seek, volume, captions, picture-in-picture "
        "and fullscreen controls. Without it you must provide your own controls through the "
        "HTMLMediaElement API. Autoplay with sound is blocked by browsers; autoplay muted (for background "
        "video) is allowed. Set width and height or CSS aspect-ratio to prevent layout shift, and use "
        "preload=\"none\" or \"metadata\" to avoid downloading large files that may never be played.",
    ],
    syntax="<video src=\"clip.mp4\" controls width=\"640\" height=\"360\"></video>", void=False, display="inline",
    categories="Flow content, phrasing content, embedded content; interactive and palpable if controls is present",
    content="If src: zero or more <track> then transparent content with no media elements. Otherwise: zero or more <source>, zero or more <track>, then transparent content with no media elements",
    parents="Any element that accepts embedded content", omission="Neither tag may be omitted", dom="HTMLVideoElement",
    attrs=[
        ("src", "URL", "The video file. Or use <source> children.", "HTML5"),
        ("controls", "boolean", "Show built-in controls.", "HTML5"),
        ("autoplay", "boolean", "Start automatically (only reliable with muted).", "HTML5"),
        ("loop", "boolean", "Repeat when finished.", "HTML5"),
        ("muted", "boolean", "Start muted.", "HTML5"),
        ("poster", "URL", "Image shown before the video plays or while loading.", "HTML5"),
        ("preload", "none | metadata | auto", "How much to download before play.", "HTML5"),
        ("width / height", "pixels", "Display size; also prevents layout shift.", "HTML5"),
        ("playsinline", "boolean", "On iPhone, play inline instead of forcing fullscreen.", "Living Standard"),
        ("crossorigin", "anonymous | use-credentials", "CORS mode for the media (needed for canvas processing and cross-origin tracks).", "HTML5"),
        ("controlslist", "nodownload | nofullscreen | noremoteplayback", "Hide specific native controls (Chromium).", "Non-standard"),
        ("disablepictureinpicture", "boolean", "Hide the picture-in-picture option.", "Living Standard"),
        ("disableremoteplayback", "boolean", "Disable casting.", "Living Standard"),
    ],
    examples=[
        ("Complete accessible video",
         "<video controls width=\"640\" height=\"360\" poster=\"poster.jpg\" preload=\"metadata\">\n  <source src=\"lesson.webm\" type=\"video/webm\">\n  <source src=\"lesson.mp4\" type=\"video/mp4\">\n  <track kind=\"captions\" src=\"lesson-en.vtt\" srclang=\"en\" label=\"English\" default>\n  <p>Your browser cannot play this video. <a href=\"lesson.mp4\">Download it</a>.</p>\n</video>", ""),
        ("Background hero video", "<video autoplay muted loop playsinline poster=\"hero.jpg\" aria-hidden=\"true\">\n  <source src=\"hero.mp4\" type=\"video/mp4\">\n</video>", "Muted autoplay is allowed; aria-hidden because it is decorative. Respect prefers-reduced-motion by pausing it with JavaScript."),
        ("Responsive sizing", "<style>\n  video { width: 100%; height: auto; aspect-ratio: 16 / 9; background: #000; }\n</style>", ""),
        ("Custom play button", "<video id=\"v\" src=\"clip.mp4\" width=\"400\"></video>\n<button onclick=\"const v = document.getElementById('v'); v.paused ? v.play() : v.pause()\">Play / Pause</button>", ""),
    ],
    a11y=["Provide captions with <track kind=\"captions\">.", "Provide a transcript for audio and visual content.", "Never autoplay with sound.",
          "Keep native controls unless your custom controls are fully keyboard accessible.", "Avoid flashing content."],
    mistakes=["Expecting sound autoplay to work.", "A single format only.", "Huge files with preload=\"auto\".", "No poster, showing a black box until play.", "Missing playsinline on iOS."],
    related=["audio", "source", "track", "iframe", "picture"], css="video { object-fit: contain; }\nvideo:not([controls]) { /* nothing shown until play */ }",
),

dict(
    name="wbr", title="Word break opportunity", cat="Text-level semantics",
    versions="Netscape / IE extension, standardised in HTML5", status="current",
    desc=[
        "The <wbr> element marks a position inside a word where the browser may break the line if "
        "necessary, without inserting a hyphen or a visible character. It is useful for very long words, "
        "URLs and code identifiers that would otherwise overflow their container. If no break is needed, "
        "nothing is displayed. It is a void element.",
        "Alternatives: the zero-width space character (&#8203;) has the same effect; the soft hyphen "
        "(&shy;) breaks with a hyphen; CSS overflow-wrap: anywhere allows breaks anywhere in overflowing "
        "words.",
    ],
    syntax="Super<wbr>cali<wbr>fragilistic", void=True, display="inline",
    categories="Flow content, phrasing content", content="None (void element)", parents="Any element that accepts phrasing content",
    omission="No end tag", dom="HTMLElement",
    attrs=[],
    examples=[
        ("Long URL", "<p>Visit https://example.com/<wbr>very/<wbr>long/<wbr>path/<wbr>to/<wbr>a/<wbr>resource</p>", "The URL can break after each slash instead of overflowing."),
        ("Long identifier", "<code>HTMLTable<wbr>Section<wbr>Element</code>", ""),
    ],
    a11y=["Invisible to screen readers; does not affect pronunciation."],
    mistakes=["Using <br> where a soft break is wanted.", "Writing </wbr>."],
    related=["br", "nobr"], css="wbr { content: '\\200B'; }",
),

dict(
    name="xmp", title="Example text (obsolete)", cat="Obsolete text content",
    versions="HTML 1, HTML 2.0 (deprecated); obsolete", status="obsolete",
    desc=[
        "The <xmp> element (example) displayed its content literally, without interpreting any markup, in a "
        "monospace font, so that authors could show HTML source without escaping < and &. It was one of the "
        "1991 elements, deprecated in HTML 2.0 and removed in HTML 3.2, although browsers still support it "
        "for old pages. Use <pre> with escaped entities.",
    ],
    syntax="<xmp><p>shown literally</p></xmp>", void=False, display="block",
    categories="Historical", content="Raw text", parents="Flow content", omission="Neither", dom="HTMLPreElement",
    attrs=[],
    examples=[("Replacement", "<pre>&lt;p&gt;shown literally&lt;/p&gt;</pre>", "")],
    a11y=[], mistakes=["Any use."], related=["pre", "listing", "plaintext", "code"], css="xmp { display: block; font-family: monospace; white-space: pre; margin: 1em 0; }",
),

dict(
    name="selectedcontent", title="Selected option display (customisable select)", cat="Forms",
    versions="Living Standard (2025, experimental)", status="experimental",
    desc=[
        "The <selectedcontent> element is part of the customisable <select> proposal. Placed inside the <button> "
        "that sits at the start of a <select>, it mirrors the content of the currently selected <option>, so that "
        "rich option content (icons, colour swatches, descriptions) is shown in the closed control as well as in the "
        "open list. The browser clones the selected option's children into <selectedcontent> whenever the selection "
        "changes.",
        "It only has an effect when the select opts in with the CSS declaration appearance: base-select on both the "
        "select and its ::picker(select) pseudo-element. Browser support is still limited, so always test the "
        "fallback: browsers that do not understand it render the plain native select.",
    ],
    syntax="<select>\n  <button><selectedcontent></selectedcontent></button>\n  <option>...</option>\n</select>",
    void=False, display="inline", categories="None", content="Nothing authored; the browser fills it with a clone of the selected option's content",
    parents="A <button> that is the first child of a <select>", omission="Neither tag may be omitted", dom="HTMLSelectedContentElement",
    attrs=[],
    examples=[
        ("Rich select with icons", "<style>\n  select, ::picker(select) { appearance: base-select; }\n</style>\n<select>\n  <button><selectedcontent></selectedcontent></button>\n  <option value=\"red\"><span class=\"swatch\" style=\"background:red\"></span> Red</option>\n  <option value=\"green\"><span class=\"swatch\" style=\"background:green\"></span> Green</option>\n</select>", "The closed control shows the swatch and text of the chosen option."),
    ],
    a11y=["The control remains a combobox for assistive technology; the option text is announced as usual."],
    mistakes=["Placing it anywhere other than inside the leading <button> of a <select>.", "Relying on it without the appearance: base-select opt-in.", "Assuming support in every browser."],
    related=["select", "option", "button"], css="selectedcontent { display: contents; }",
),

dict(
    name="nextid", title="Next identifier (HTML 1 editor hint)", cat="Obsolete",
    versions="HTML 1 / HTML 2.0 (RFC 1866); removed in HTML 3.2", status="obsolete",
    desc=[
        "The <nextid> element was used by the very first HTML editors (the NeXT-based editor written at CERN) to "
        "remember the next automatically generated anchor name, so that the editor could continue numbering "
        "anchors (z1, z2, z3...) when a document was reopened. It carried a single attribute, n, holding that name. "
        "It had no visible effect and was placed in the <head>.",
        "It was already marked as an editor-only feature in HTML 2.0 and was dropped from HTML 3.2. Modern browsers "
        "ignore it entirely. It is documented here only for completeness, because it appears in the earliest HTML "
        "specifications and in archived pages from 1991 to 1995.",
    ],
    syntax="<nextid n=\"z12\">", void=True, display="none", categories="None (obsolete)", content="None (void element)",
    parents="<head> (historically)", omission="No end tag", dom="HTMLUnknownElement",
    attrs=[("n", "Text (anchor name)", "The next anchor name the editor should generate.", "HTML 1")],
    examples=[
        ("Historical usage", "<head>\n  <title>Welcome</title>\n  <nextid n=\"z5\">\n</head>", "Ignored by all modern browsers."),
    ],
    a11y=[], mistakes=["Any use in a new document."], related=["head", "isindex", "listing"], css="nextid { display: none; }",
),

]
