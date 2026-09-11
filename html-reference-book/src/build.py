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
from data_projects import all_projects, THEMES, TYPES
from data_js import JS_INTRO, JS_REFERENCE, JS_COURSE
import elements_a_d, elements_e_h, elements_i_o, elements_p_s, elements_t_z

ELEMENTS = (elements_a_d.ELEMENTS + elements_e_h.ELEMENTS + elements_i_o.ELEMENTS
            + elements_p_s.ELEMENTS + elements_t_z.ELEMENTS)
ELEMENTS.sort(key=lambda e: e["name"])

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TITLE = "The Complete HTML Reference Book"
SUBTITLE = "Every element and attribute from HTML 1 (1991) to the HTML Living Standard, with CSS and JavaScript"

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


# Line-by-line explanations for project code -------------------------------------------------
HTML_EXPLAIN = [
    (r"<!DOCTYPE html>", "Declares modern HTML so the browser renders in standards mode."),
    (r"<html lang=", "Root element; lang tells screen readers and search engines the page language."),
    (r'<meta charset="utf-8">', "Character encoding: makes Arabic, accents and symbols display correctly."),
    (r'<meta name="viewport"', "Makes the page use the real device width on phones."),
    (r"<title>", "Text shown in the browser tab and search results."),
    (r'<link rel="stylesheet"', "Loads the external CSS file styles.css."),
    (r"<header", "Introductory content: logo, title, navigation."),
    (r"<nav", "A block of navigation links; aria-label names it for screen readers."),
    (r"<main", "The unique content of this page; exactly one per page."),
    (r"<section", "A thematic group of content, normally with its own heading."),
    (r"<article", "A self-contained piece: card, post, product."),
    (r"<aside", "Content related to, but separate from, the main content."),
    (r"<footer", "Footer of the page or of a section."),
    (r"<h1", "The main heading; only one per page."),
    (r"<h2", "Second-level heading for a section."),
    (r"<h3", "Third-level heading, inside an h2 section."),
    (r"<p", "A paragraph of text."),
    (r'<a class="btn"', "A link styled as a button; it navigates, so it is a link and not a <button>."),
    (r"<a href=", "A hyperlink; href gives the destination."),
    (r"<ul", "Unordered (bulleted) list."),
    (r"<ol", "Ordered (numbered) list; the order matters."),
    (r"<li", "One list item."),
    (r"<dl", "Description list of term / description pairs."),
    (r"<dt", "A term (name) in a description list."),
    (r"<dd", "The description of the preceding term."),
    (r"<img", "An image; alt describes it, width and height reserve space before it loads."),
    (r"<figure", "Self-contained media with an optional caption."),
    (r"<figcaption", "Caption for the figure."),
    (r"<picture", "Container offering several image sources; the browser picks the first it supports."),
    (r"<video", "Video player; controls shows the built-in buttons."),
    (r"<audio", "Audio player."),
    (r"<source", "One media source with its MIME type."),
    (r"<track", "Captions or subtitles file for media."),
    (r"<iframe", "Embeds another page; title describes it for assistive technology."),
    (r"<table", "Tabular data in rows and columns."),
    (r"<caption", "Title of the table."),
    (r"<thead", "Group of header rows."),
    (r"<tbody", "Group of data rows."),
    (r"<tfoot", "Group of footer rows (totals)."),
    (r"<tr", "A table row."),
    (r'<th scope="col"', "Header cell for a column."),
    (r'<th scope="row"', "Header cell for a row."),
    (r"<th", "A header cell."),
    (r"<td", "A data cell."),
    (r"<form", "A form; action is where the data goes, method how it is sent."),
    (r"<fieldset", "Groups related form controls."),
    (r"<legend", "Caption for the fieldset."),
    (r"<label", "Text label for a control; for matches the control's id, or the label wraps the control."),
    (r'type="email"', "Email field: validated automatically and shows the @ keyboard on phones."),
    (r'type="password"', "Password field: characters are hidden."),
    (r'type="radio"', "Radio button: one choice from a group sharing the same name."),
    (r'type="checkbox"', "Checkbox: on or off."),
    (r'type="date"', "Date picker."),
    (r'type="time"', "Time picker."),
    (r'type="number"', "Numeric input with min, max and step."),
    (r'type="tel"', "Telephone number; shows the phone keypad on mobiles."),
    (r'type="search"', "Search field."),
    (r"<input", "A form control; its type decides what it looks like."),
    (r"<select", "Drop-down list."),
    (r"<option", "One choice in a select or datalist."),
    (r"<datalist", "Suggestions for an input linked with the list attribute."),
    (r"<textarea", "Multi-line text field."),
    (r"<button", "A clickable button; inside a form it submits by default."),
    (r"required", "The field must be filled before the form can be submitted."),
    (r"autocomplete=", "Tells the browser which saved value to offer (name, email, tel...)."),
    (r"<details", "Disclosure widget that can be opened and closed."),
    (r"<summary", "The always-visible heading of a details element."),
    (r"<dialog", "A dialog box; showModal() opens it as a modal."),
    (r"<time", "A date or time; datetime holds the machine-readable value."),
    (r"<address", "Contact information for the page or article."),
    (r"<blockquote", "A long quotation from another source."),
    (r"<cite", "Title of a work or source."),
    (r"<strong", "Strong importance (bold by default)."),
    (r"<b>", "Keyword or name drawn to attention without extra importance."),
    (r"<small", "Side comment or fine print."),
    (r"<span", "Generic inline container for styling."),
    (r"<div", "Generic block container for grouping and layout."),
    (r"<progress", "Progress of a task."),
    (r"<meter", "A measurement within a known range."),
    (r"<search", "Container for search functionality."),
    (r"aria-current=", "Tells assistive technology which item is the current page or step."),
    (r"aria-label=", "Accessible name for an element that has no visible text."),
    (r'aria-hidden="true"', "Hides decorative content from screen readers."),
    (r'role="', "Gives the element an ARIA role for assistive technology."),
    (r'loading="lazy"', "Defers loading until the image is near the viewport."),
    (r"<script", "JavaScript; here only a few lines to open a dialog or switch a theme."),
    (r"&copy;", "Character entity for the copyright sign."),
    (r"&middot;", "Character entity for a middle dot separator."),
]
CSS_EXPLAIN = [
    (r"box-sizing: border-box", "Width and height include padding and border, which makes sizing predictable."),
    (r":root {", "Custom properties (variables) defined on the root so every element can use them."),
    (r"--brand", "The brand colour variable; change it once and every use follows."),
    (r"font-family", "The typeface stack: preferred font first, fallbacks after."),
    (r"line-height", "Space between lines; 1.5 to 1.7 is comfortable for body text."),
    (r"max-width", "Limits how wide the element can grow, keeping lines readable."),
    (r"margin: 0 auto", "Centres a block horizontally: zero top/bottom, automatic left/right."),
    (r"margin-inline: auto", "Same as margin: 0 auto using logical properties."),
    (r"padding", "Space inside the element between its border and content."),
    (r"display: grid", "Turns the element into a grid container."),
    (r"grid-template-columns", "Defines the columns of the grid."),
    (r"grid-template-areas", "Names regions of the grid so children can be placed by name."),
    (r"grid-area", "Places a child into a named area."),
    (r"repeat(auto-fit", "Creates as many columns as fit; auto-fit collapses empty tracks."),
    (r"repeat(auto-fill", "Creates as many columns as fit; auto-fill keeps empty tracks."),
    (r"minmax(", "A track that is at least the first value and at most the second."),
    (r"place-items: center", "Centres items horizontally and vertically in a grid."),
    (r"place-content: center", "Centres the whole grid content in the container."),
    (r"display: flex", "Turns the element into a flex container (one-dimensional layout)."),
    (r"flex-direction: column", "Stacks flex items vertically."),
    (r"flex-direction: column-reverse", "Stacks flex items vertically in reverse visual order."),
    (r"flex-wrap: wrap", "Allows flex items to move to a new line when they do not fit."),
    (r"justify-content: space-between", "Spreads items so the first touches the start and the last the end."),
    (r"justify-content: center", "Centres items along the main axis."),
    (r"align-items: center", "Centres items on the cross axis."),
    (r"align-items: start", "Aligns items to the start of the cross axis (no stretching)."),
    (r"align-content: center", "Centres the lines of a multi-line flex or grid container."),
    (r"flex: 1 1", "The item can grow and shrink from the given basis."),
    (r"flex: 1;", "All items share free space equally."),
    (r"flex: 0 0", "Fixed size: never grows or shrinks."),
    (r"flex-basis: 100%", "The item takes a whole line, pushing the next items down."),
    (r"gap:", "Space between grid or flex items without extra margins."),
    (r"order:", "Changes the visual order of a flex item without changing the source."),
    (r"list-style: none", "Removes bullets or numbers from a list."),
    (r"list-style-type", "Chooses the bullet or numbering style."),
    (r"text-decoration: none", "Removes the underline from links."),
    (r"text-align: center", "Centres inline content such as text."),
    (r"text-align: right", "Right-aligns inline content, typical for numbers."),
    (r"text-transform: uppercase", "Displays text in capitals without changing the HTML."),
    (r"letter-spacing", "Adds space between letters; useful for small capitals."),
    (r"font-variant-numeric: tabular-nums", "Makes all digits the same width so columns of numbers line up."),
    (r"clamp(", "A fluid value between a minimum and a maximum, based on the middle expression."),
    (r"min(", "Uses the smaller of the listed values."),
    (r"border-radius: 50%", "Turns a square into a circle."),
    (r"border-radius: 999px", "Fully rounded pill shape."),
    (r"border-radius", "Rounds the corners."),
    (r"border-collapse: collapse", "Merges adjacent table cell borders into single lines."),
    (r"border-collapse: separate", "Keeps each cell's border separate so cells look like tiles."),
    (r"border-spacing", "Gap between cells in the separate border model."),
    (r"table-layout: fixed", "Columns get equal widths regardless of content; faster rendering."),
    (r"border-left", "A thick left border used as an accent stripe."),
    (r"border-top", "A top border used as an accent or separator."),
    (r"border-bottom", "A bottom border used as a separator line."),
    (r"border: 0", "Removes the default border (for example on an iframe or button)."),
    (r"box-shadow", "Soft shadow that lifts the element from the page."),
    (r"text-shadow", "Shadow behind text to improve contrast over images."),
    (r"background: linear-gradient", "A gradient (here often used as a translucent overlay over an image)."),
    (r"background-size: cover", "Scales the background image to cover the box without distortion."),
    (r"background:", "Background colour or image."),
    (r"object-fit: cover", "Crops an image to fill its box while keeping its proportions."),
    (r"aspect-ratio", "Keeps a fixed width-to-height ratio, reserving space before media loads."),
    (r"overflow: hidden", "Clips content that sticks out, so images follow rounded corners."),
    (r"overflow-x: auto", "Adds a horizontal scrollbar only when needed (responsive tables)."),
    (r"position: relative", "Keeps normal flow but becomes the reference for absolutely positioned children."),
    (r"position: absolute", "Removes the element from flow and positions it relative to the nearest positioned ancestor."),
    (r"position: sticky", "Scrolls normally until it reaches the given offset, then sticks."),
    (r"position: fixed", "Stays fixed relative to the viewport while scrolling."),
    (r"inset: 0", "Shorthand for top, right, bottom and left all zero: stretches over the parent."),
    (r"z-index", "Stacking order for positioned elements; higher is on top."),
    (r"translate:", "Moves the element without affecting the layout of others."),
    (r"transform: scale", "Enlarges or shrinks the element visually."),
    (r"transition", "Animates property changes smoothly, for example on hover."),
    (r"animation", "Runs a @keyframes animation."),
    (r"opacity", "Transparency from 0 (invisible) to 1 (solid)."),
    (r"filter: brightness", "Darkens or brightens the element; a cheap hover effect."),
    (r"backdrop-filter", "Blurs or filters whatever is behind the element."),
    (r"::before", "Generated content inserted before the element's content (decorations, numbers, lines)."),
    (r"::after", "Generated content inserted after the element's content."),
    (r"::backdrop", "The dimmed layer behind a modal dialog."),
    (r"content:", "The text or empty string for a pseudo-element."),
    (r"counter-reset", "Starts a CSS counter."),
    (r"counter-increment", "Adds one to the counter for each matching element."),
    (r"counter(", "Prints the current counter value in generated content."),
    (r":hover", "Applies while the pointer is over the element."),
    (r":focus-visible", "Applies when the element is focused by keyboard; keeps focus rings visible."),
    (r":checked", "Applies to a checked radio or checkbox; combined with ~ it drives CSS-only widgets."),
    (r":target", "Applies to the element whose id matches the URL fragment."),
    (r":not(", "Excludes elements from a selector."),
    (r":empty", "Matches elements with no children or text."),
    (r":nth-child(even)", "Every second element: zebra striping."),
    (r":first-child", "The first child of its parent."),
    (r":last-child", "The last child of its parent."),
    (r"li + li", "Adjacent sibling combinator: every li that follows another li."),
    (r"~ ", "General sibling combinator: later siblings of the matched element."),
    (r"[aria-current", "Attribute selector: styles the current page or step."),
    (r"[open]", "Attribute selector: a details or dialog that is open."),
    (r"[data-theme", "Attribute selector on a data attribute set by JavaScript."),
    (r":user-invalid", "A field the user has edited that fails validation."),
    (r"accent-color", "Colours native checkboxes, radios, progress and range controls."),
    (r"color-scheme", "Tells the browser which colour schemes the page supports so native controls match."),
    (r"@media (prefers-color-scheme: dark)", "Applies when the user's system is in dark mode."),
    (r"@media (min-width", "Applies from the given width upwards (mobile-first breakpoint)."),
    (r"@media (max-width", "Applies up to the given width."),
    (r"@media print", "Applies only when printing."),
    (r"@page", "Sets the printed page margins."),
    (r"scroll-margin-top", "Leaves room above an anchor target so a sticky header does not cover it."),
    (r"cursor: pointer", "Shows the hand cursor to indicate something clickable."),
    (r"font: inherit", "Makes form controls use the page font instead of the browser default."),
    (r"width: 100%", "Fills the container width."),
    (r"min-height: 100vh", "At least as tall as the viewport."),
    (r"height: auto", "Keeps the natural height, preserving image proportions."),
    (r"pointer-events: none", "The element ignores mouse clicks."),
    (r".sr-only", "Visually hidden but still read by screen readers."),
    (r"clip: rect(0 0 0 0)", "Part of the screen-reader-only pattern: clips the box to nothing."),
    (r"white-space: nowrap", "Prevents text from wrapping to a new line."),
    (r"font-weight", "Thickness of the text."),
    (r"font-size", "Size of the text."),
    (r"color:", "Text colour."),
    (r"margin", "Space outside the element."),
    (r"border", "The line around the element: width, style and colour."),
    (r"display: block", "Element starts on a new line and fills the width (used on links and images)."),
    (r"display: inline-block", "Flows in text but accepts width, height and vertical padding."),
    (r"display: none", "Removes the element from rendering completely."),
    (r"visibility", "Hides while keeping the space."),
    (r"vertical-align: top", "Aligns cell content to the top."),
    (r"text-overflow", "Shows an ellipsis for overflowing text."),
]


JS_EXPLAIN = [
    (r"document.querySelector(", "Finds the first element matching a CSS selector."),
    (r"document.querySelectorAll(", "Finds every matching element (a NodeList; spread into an array with [...])."),
    (r"document.getElementById(", "Finds one element by its id."),
    (r"addEventListener('click'", "Runs the function when the element is clicked."),
    (r"addEventListener('input'", "Runs on every keystroke or change in a field."),
    (r"addEventListener('submit'", "Runs when the form is submitted (Enter or button)."),
    (r"addEventListener('keydown'", "Runs when a key is pressed; e.key tells which."),
    (r"addEventListener('change'", "Runs when a checkbox, radio or select value changes."),
    (r"addEventListener('blur'", "Runs when the field loses focus."),
    (r"e.preventDefault()", "Stops the browser's default action (here: reloading on submit)."),
    (r"e.target.closest(", "Event delegation: finds the clicked button even if a child was clicked."),
    (r"const ", "Declares a variable that will not be reassigned."),
    (r"let ", "Declares a variable that can change."),
    (r"function ", "Defines a reusable block of code."),
    (r"=> ", "Arrow function: a short way to write a function."),
    (r"textContent", "Reads or sets the text inside an element (safe: never interprets HTML)."),
    (r".innerHTML = ''", "Empties an element before re-rendering."),
    (r"createElement(", "Creates a new element in memory."),
    (r".append(", "Adds nodes at the end of an element."),
    (r"replaceChildren(", "Replaces all children with the given nodes in one step."),
    (r"createDocumentFragment", "A lightweight container for building many nodes before inserting them once."),
    (r"cloneNode(true)", "Copies a template's content, including its children."),
    (r".dataset.", "Reads a data-* attribute (data-title becomes dataset.title)."),
    (r"setAttribute(", "Sets an attribute value as a string."),
    (r"getAttribute(", "Reads an attribute value."),
    (r".hidden = ", "Shows or hides the element through the hidden attribute."),
    (r".disabled = ", "Enables or disables a control."),
    (r".focus()", "Moves keyboard focus to the element."),
    (r".contains(", "True if the node is inside the element (used to detect clicks outside)."),
    (r"classList", "Adds, removes or toggles CSS classes."),
    (r"style.translate", "Sets an inline CSS property from JavaScript."),
    (r"localStorage.getItem(", "Reads a saved string from the browser's storage."),
    (r"localStorage.setItem(", "Saves a string that survives page reloads."),
    (r"JSON.parse(", "Turns a JSON string back into arrays and objects."),
    (r"JSON.stringify(", "Turns arrays and objects into a JSON string for storage or sending."),
    (r"?? []", "Nullish coalescing: use the right side when the left is null or undefined."),
    (r"async function", "A function that can await promises."),
    (r"await fetch(", "Requests a URL and waits for the response."),
    (r"res.ok", "True for HTTP status 200-299."),
    (r"await res.json()", "Parses the response body as JSON."),
    (r"try {", "Runs code that may fail; errors jump to catch."),
    (r"catch (err)", "Handles the error instead of crashing."),
    (r"throw new Error(", "Creates an error on purpose (for example a bad HTTP status)."),
    (r"setInterval(", "Runs a function repeatedly every n milliseconds."),
    (r"clearInterval(", "Stops a running interval."),
    (r"new Date(", "Creates a date/time value."),
    (r"Math.floor(", "Rounds down to a whole number."),
    (r"Math.max(", "The larger of two numbers (here: never below zero)."),
    (r"padStart(2, '0')", "Pads to two characters with a leading zero."),
    (r"toLocaleString(", "Formats a number with thousands separators for a locale."),
    (r"toLocaleTimeString(", "Formats a time for a locale."),
    (r"parseInt(", "Reads a whole number from the start of a string."),
    (r"Number(", "Converts a string to a number."),
    (r"String(", "Converts a value to a string."),
    (r".trim()", "Removes spaces at both ends of a string."),
    (r".toLowerCase()", "Lower-cases a string for case-insensitive comparison."),
    (r".includes(", "True if the string or array contains the value."),
    (r".forEach(", "Runs a function for each item of an array."),
    (r".map(", "Builds a new array by transforming each item."),
    (r".filter(", "Builds a new array with the items that pass a test."),
    (r".reduce(", "Folds an array into one value (here: a total)."),
    (r".every(", "True if every item passes the test."),
    (r".find(", "The first item that passes the test."),
    (r".push(", "Adds an item to the end of an array."),
    (r".splice(", "Removes (or inserts) items at an index."),
    (r"for (const ", "Loops over the items of an array or NodeList."),
    (r"if (", "Runs code only when the condition is true."),
    (r"validity.", "The Constraint Validation API flags (valueMissing, typeMismatch, tooShort...)."),
    (r"form.elements.", "Accesses a form control by its name."),
    (r"matchMedia(", "Checks a media query from JavaScript (here: reduced motion)."),
    (r"aria-", "Updates an ARIA attribute so assistive technology knows the new state."),
    (r"`${", "Template literal: builds a string with embedded values."),
    (r"% ", "Remainder operator: wraps an index around (last -> first)."),
    (r"//", "A comment: ignored by the browser."),
]

# Two related projects are shown right after every lesson (type keys) ...
LESSON_PROJECTS = {
    1: ["landing", "404"], 2: ["card", "numbers"], 3: ["about", "alerts"], 4: ["footer", "breadcrumb"], 5: ["blog", "howto"],
    6: ["pricing", "invoice"], 7: ["nav", "sidebar"], 8: ["gallery", "video"], 9: ["contact", "signup"], 10: ["features", "team"],
    11: ["hero", "split"], 12: ["menu", "glossary"], 13: ["dark", "testimonials"], 14: ["cv", "event"], 15: ["hero", "dark"],
    16: ["card", "cardgrid"], 17: ["split", "timeline"], 18: ["modal", "burger"], 19: ["nav", "schedule"], 20: ["dashboard", "calendar"],
    21: ["onepage", "map"], 22: ["cardgrid", "plans"], 23: ["sidebar", "tabs"], 24: ["dark", "plans"], 25: ["progress", "numbers"],
    26: ["faq", "menu"], 27: ["gallery", "hero"], 28: ["progress", "alerts"], 29: ["testimonials", "modal"], 30: ["login", "booking"],
    31: ["features", "plans"], 32: ["video", "print"], 33: ["search", "faq"], 34: ["print", "onepage"], 35: ["landing", "onepage"],
    36: ["404", "glossary"], 37: ["js-counter", "js-countdown"], 38: ["js-counter", "js-countdown"], 39: ["js-filter", "js-countdown"],
    40: ["js-tabs", "js-menu"], 41: ["js-cart", "js-todo"], 42: ["js-filter", "js-slider"], 43: ["js-menu", "js-tabs"],
    44: ["js-validate", "js-todo"], 45: ["js-fetch", "js-cart"], 46: ["js-tabs", "js-slider"], 47: ["js-fetch", "js-cart"],
}
# ... and two at the end of every chapter (part).
PART_PROJECTS = {
    1: ["landing", "about"], 2: ["card", "footer"], 3: ["404", "numbers"], 4: ["alerts", "breadcrumb"], 5: ["js-counter", "js-menu"],
    6: ["blog", "event"], 7: ["signup", "booking"], 8: ["print", "glossary"], 9: ["contact", "search"], 10: ["features", "map"],
    11: ["cardgrid", "dark"], 12: ["js-todo", "js-fetch"], 13: ["landing", "js-validate"], 14: ["login", "invoice"], 15: ["cv", "js-slider"],
}


def pick_projects(projects, keys, seed):
    """Return the projects of the given type keys, rotating the theme with the seed so neighbouring lessons differ."""
    out = []
    for j, key in enumerate(keys):
        cands = [p for p in projects if p["key"] == key]
        out.append(cands[(seed * 7 + j * 11) % len(cands)])
    return out


def explain_lines(code, table, css=False):
    """Return [(fragment, explanation)] for lines (HTML) or declarations (CSS) matching a pattern; each pattern once."""
    out = []
    used = set()
    if css:
        parts = []
        for line in code.split("\n"):
            line = line.strip()
            if not line:
                continue
            m = re.match(r"^([^{]+)\{(.*)\}?$", line)
            if m and not line.startswith("@"):
                parts.append(m.group(1).strip() + " {")
                parts.extend(d.strip() + ";" for d in m.group(2).rstrip("}").split(";") if d.strip())
            else:
                parts.append(line)
        lines = parts
    else:
        lines = [l.strip() for l in code.split("\n") if l.strip()]
    for line in lines:
        for pat, why in table:
            if pat in line and pat not in used:
                used.add(pat)
                out.append((line if len(line) <= 70 else line[:67] + "...", why))
                break
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
    S["toc2"] = ParagraphStyle("toc2", fontName="Sans", fontSize=8, leading=11, leftIndent=28, textColor=MUTED)
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
        def build(self, *a, **kw):
            if hasattr(self, "body_start"):
                del self.body_start  # recomputed on every multiBuild pass (the contents may grow)
            return BaseDocTemplate.build(self, *a, **kw)

        def afterFlowable(self, fl):
            if isinstance(fl, Bookmark):
                self.notify("TOCEntry", (fl.level, htmlmod.escape(fl.title, quote=False), self.page - getattr(self, "body_start", 1) + 1, fl.key))

    def heading(text, level, key):
        return [Bookmark(key, text, level), P(text, "h1" if level == 0 else "h2")]

    class BodyStart(Flowable):
        """Marks the first body page: page numbering restarts at 1 here (front matter is numbered i, ii, iii)."""
        def __init__(self):
            Flowable.__init__(self)
            self.width = self.height = 0

        def draw(self):
            doc = self.canv._doctemplate
            doc.body_start = self.canv.getPageNumber()
            self.canv.addPageLabel(0, style="ROMAN_LOWER")
            self.canv.addPageLabel(doc.body_start - 1, style="ARABIC", start=1)

    def project_flowables(pr, key, level, files_note=True):
        th = pr["theme"]
        files = "index.html, styles.css" + (", app.js" if pr.get("js") else "")
        out = [Bookmark(key, "Project %d: %s" % (pr["number"], pr["title"]), level)]
        out.append(P("Project %d: %s" % (pr["number"], pr["title"]), "h1"))
        out.append(P("Theme: %s (%s)   |   Level %d   |   Files: %s" % (th["name"], th["city"], pr["level"], files), "meta"))
        out.append(P("Brief", "h3"))
        out.append(P(pr["brief"]))
        out.append(P("Learning goals", "h3"))
        for g in pr["goals"]:
            out.append(Paragraph(esc(g), S["li"], bulletText="\u2022"))
        out.append(P("Elements and CSS used", "h3"))
        out.extend(rl_table([["HTML elements", "CSS features"], [", ".join(pr["elements"]), ", ".join(pr["css"])]], col_widths=[AVAIL * 0.5, AVAIL * 0.5]))
        out.append(P("Build guide", "h3"))
        for i, st in enumerate(pr["steps"]):
            out.append(Paragraph(esc(st), S["li"], bulletText="%d." % (i + 1)))
        out.append(PageBreak())
        out.append(P("Project %d: index.html" % pr["number"], "h2"))
        out.append(code_block(pr["html"]))
        out.append(P("Project %d: styles.css" % pr["number"], "h2"))
        out.append(code_block(pr["css_code"]))
        if pr.get("js"):
            out.append(P("Project %d: app.js" % pr["number"], "h2"))
            out.append(code_block(pr["js"]))
        hx = explain_lines(pr["html"], HTML_EXPLAIN)
        cx = explain_lines(pr["css_code"], CSS_EXPLAIN, css=True)
        out.append(PageBreak())
        out.append(P("Project %d explained line by line" % pr["number"], "h2"))
        out.append(P("The important lines of index.html", "h3"))
        out.extend(rl_table([["Line", "What it does"]] + [[a, b] for a, b in hx], col_widths=[AVAIL * 0.42, AVAIL * 0.58]))
        out.append(P("The important declarations of styles.css", "h3"))
        out.extend(rl_table([["Declaration", "What it does"]] + [[a, b] for a, b in cx], col_widths=[AVAIL * 0.42, AVAIL * 0.58]))
        if pr.get("js"):
            jx = explain_lines(pr["js"], JS_EXPLAIN)
            out.append(P("The important lines of app.js", "h3"))
            out.extend(rl_table([["Line", "What it does"]] + [[a, b] for a, b in jx], col_widths=[AVAIL * 0.42, AVAIL * 0.58]))
        out.append(P("Check your work", "h3"))
        for c in pr["checklist"]:
            out.append(Paragraph(esc(c), S["li"], bulletText="\u2610"))
        out.append(P("Exercises", "h3"))
        for i, ex in enumerate(pr["exercises"]):
            out.append(Paragraph(esc(ex), S["li"], bulletText="%d." % (i + 1)))
        out.append(P("Theme data for this project", "h3"))
        out.extend(rl_table([["Field", "Value"], ["Business", th["name"]], ["Tagline", th["tagline"]], ["City", th["city"]], ["Owner", th["person"]],
                             ["Brand colour", th["primary"]], ["Accent colour", th["accent"]], ["Offers", "; ".join("%s (%s)" % (a, c) for a, b, c in th["items"])]],
                            col_widths=[AVAIL * 0.25, AVAIL * 0.75]))
        out.append(PageBreak())
        return out

    PROJECTS = all_projects()

    def chapter_projects(num):
        """Two practice projects that close a chapter (part)."""
        keys = PART_PROJECTS.get(num)
        if not keys:
            return []
        prs = pick_projects(PROJECTS, keys, num)
        out = heading("Chapter %d projects" % num, 1, "cproj%d" % num)
        out.append(P("Before moving on, build these two projects. They use what this chapter covered; every project is also listed, "
                     "with all the others, in the Practice Projects part at the end of the book."))
        out.append(PageBreak())
        for k, pr in enumerate(prs):
            out += project_flowables(pr, "cproj%d-%d" % (num, k), 2)
        return out

    def lesson_projects(n):
        prs = pick_projects(PROJECTS, LESSON_PROJECTS[n], n)
        out = [Bookmark("lproj%d" % n, "Lesson %d projects" % n, 2), P("Lesson %d projects" % n, "h2"),
               P("Two short projects to practise this lesson. Type them, run them, then do the exercises."), PageBreak()]
        for k, pr in enumerate(prs):
            out += project_flowables(pr, "lproj%d-%d" % (n, k), 2)
        return out

    story = []
    # ----- Cover
    story += [Spacer(1, 90), P(TITLE, "title"), P(SUBTITLE, "subtitle"), Spacer(1, 20),
              P("HTML 1 \u2022 HTML 2.0 \u2022 HTML 3.2 \u2022 HTML 4.01 \u2022 XHTML \u2022 HTML5 \u2022 Living Standard", "center"),
              Spacer(1, 10), P("Elements \u2022 Attributes \u2022 Global attributes \u2022 Events \u2022 Input types \u2022 CSS \u2022 JavaScript \u2022 Course \u2022 Projects", "center"),
              Spacer(1, 120), P("Compiled from the HTML Living Standard, MDN Web Docs, htmlreference.io, codeshack.io and the W3Schools HTML and CSS tutorial.", "center"),
              P("Edition of September 2026", "center"), PageBreak()]
    # ----- TOC
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"], S["toc2"]]
    story += [P("Contents", "h1"), toc, NextPageTemplate("body"), PageBreak(), BodyStart()]

    def part(num, title, sub):
        return chapter_projects(num - 1) + [Bookmark("part%d" % num, "Part %d: %s" % (num, title), 0), P("Part %d" % num, "partsub"), P(title, "part"), P(sub, "partsub"), PageBreak()]

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

    # ----- JavaScript
    story += part(12, "JavaScript Reference", "The third language of the web: syntax, the DOM, events, forms, storage and fetch, with a reference of %d entries." % len(JS_REFERENCE))
    story += heading("JavaScript from zero", 0, "jsintro") + blocks(JS_INTRO) + [PageBreak()]
    story += heading("JavaScript quick reference", 0, "jsref")
    story.append(P("Every entry again in table form, grouped by topic, then one page per entry with a worked example."))
    jgroups = []
    for r in JS_REFERENCE:
        if r[0] not in jgroups:
            jgroups.append(r[0])
    for g in jgroups:
        story.append(P(g, "h3"))
        story.extend(rl_table([["Name", "Syntax", "What it does"]] + [[r[1], r[2], r[3]] for r in JS_REFERENCE if r[0] == g],
                              col_widths=[AVAIL * 0.24, AVAIL * 0.3, AVAIL * 0.46]))
    story.append(PageBreak())
    for g in jgroups:
        story += heading("JavaScript: " + g, 1, "jsg-" + re.sub(r"\W", "", g))
        for r in JS_REFERENCE:
            if r[0] != g:
                continue
            story.append(KeepTogether([Bookmark("js-" + re.sub(r"\W", "", r[1]), r[1], 2), P(r[1], "h2"), P("Syntax", "h3"), code_block(r[2]),
                                       P("Description", "h3"), P(r[3]), P("Example", "h3"), code_block(r[4])]))
        story.append(PageBreak())

    # ----- Course
    ALL_LESSONS = list(COURSE) + list(JS_COURSE)
    story += part(13, "HTML, CSS and JavaScript Course", "Forty-seven lessons from first page to interactive project, each followed by two practice projects.")
    story += heading("About this course", 0, "course")
    story.append(P("This part is a guided course rather than a reference: read the lessons in order, type the examples, and change them. "
                   "Lessons 1 to 36 follow the W3Schools HTML and CSS tutorial (foundations, styling core, layout, enhancements, quality, project); "
                   "lessons 37 to 47 add JavaScript. After every lesson come two complete practice projects that use what the lesson taught. "
                   "Whenever a lesson mentions an element, property or function, the full details are in Parts 6, 11 and 12."))
    story.extend(rl_table([["Lesson", "Topic", "Projects"]] + [[str(i + 1), t.split(":", 1)[1].strip() if ":" in t else t, ", ".join(LESSON_PROJECTS[i + 1])] for i, (t, _) in enumerate(ALL_LESSONS)],
                          col_widths=[AVAIL * 0.12, AVAIL * 0.55, AVAIL * 0.33]))
    story.append(PageBreak())
    for i, (ct, cb) in enumerate(ALL_LESSONS):
        story += heading(ct, 1, "lesson%d" % i) + blocks(cb) + [PageBreak()] + lesson_projects(i + 1)

    # ----- Guides
    story += part(14, "Practical Guides", "Step-by-step guidance for pages, lists, tables, forms, media, accessibility, SEO and migration.")
    for i, (gt, gb) in enumerate(GUIDES):
        story += heading(gt, 0, "guide%d" % i) + blocks(gb) + [PageBreak()]

    # ----- Glossary and index
    story += part(15, "Glossary and Index", "Definitions of terms and an alphabetical index of everything in the book.")
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
    for r in JS_REFERENCE:
        entries.append((r[1] + " (JS)", "Part 12: " + r[0]))
    for g in GLOSSARY:
        entries.append((g[0], "Part 15: glossary"))
    entries.sort(key=lambda x: re.sub(r"[<>]", "", x[0]).lower())
    rows = [["Term", "Where to find it"]] + [list(x) for x in entries]
    story.extend(rl_table(rows, col_widths=[AVAIL * 0.32, AVAIL * 0.68]))

    # ----- Projects
    story += part(16, "Practice Projects", "%d complete, ready-to-type projects: %d page types for %d different businesses, each with full HTML, CSS (and JavaScript where needed), a build guide, checklist and exercises." % (len(PROJECTS), len(TYPES), len(THEMES)))
    story += heading("How to use the projects", 0, "projects")
    story.append(P("Every project is a small but complete website page. Each one gives you: a brief, learning goals, the elements and CSS "
                   "features it teaches, a step-by-step build guide, the complete index.html and styles.css (plus app.js for JavaScript projects) to type or copy, an explanation "
                   "table for the important lines, a checklist to verify your result, and three exercises that extend it."))
    story.append(P("Projects are organised by type (%d types) and each type is repeated for %d businesses, so you can pick the theme closest "
                   "to your own idea, or build the same page for several themes to see how the same HTML skeleton changes with different content. "
                   "Level 1 projects need only Parts 2 and 6 of this book; level 2 add Flexbox and Grid; level 3 add pseudo-classes such as :checked "
                   "and :target, dialog, counters and JavaScript (Part 12). Two of these projects also appear after every lesson and every chapter." % (len(TYPES), len(THEMES))))
    story.append(P("Project types", "h2"))
    story.extend(rl_table([["#", "Type", "Level", "Teaches"]] + [[str(i + 1), tp["title"].replace(" for {name}", "").replace(" for {person}", ""), str(tp["level"]), ", ".join(tp["css"][:4])] for i, tp in enumerate(TYPES)],
                          col_widths=[AVAIL * 0.06, AVAIL * 0.4, AVAIL * 0.1, AVAIL * 0.44]))
    story.append(P("Business themes", "h2"))
    story.extend(rl_table([["Theme", "City", "Offers"]] + [[th["name"], th["city"], th["tagline"]] for th in THEMES]))
    story.append(PageBreak())
    lastkey = None
    for pr in PROJECTS:
        if pr["key"] != lastkey:
            tp = next(x for x in TYPES if x["key"] == pr["key"])
            story += [Bookmark("ptype-" + pr["key"], "Type: " + tp["title"].replace(" for {name}", "").replace(" for {person}", ""), 1),
                      P("Project type: " + tp["title"].replace(" for {name}", "").replace(" for {person}", ""), "h1"),
                      P("Level %d   |   %d projects, one per theme" % (tp["level"], len(THEMES)), "meta"), P(tp["brief"]), PageBreak()]
            lastkey = pr["key"]
        story += project_flowables(pr, "proj-%d" % pr["number"], 2)

    # ----- Page templates
    def on_page(canvas, doc):
        if not hasattr(doc, "body_start"):
            doc.body_start = doc.page  # first page drawn with the body template
        canvas.saveState()
        canvas.setFont("Sans", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(LM, 9 * mm, TITLE)
        canvas.drawRightString(PAGE[0] - RM, 9 * mm, "Page %d" % (doc.page - getattr(doc, "body_start", 1) + 1))
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

    PROJECTS = all_projects()

    def project_body(pr):
        th = pr["theme"]
        jsblock = ""
        if pr.get("js"):
            jsblock = "<h3>app.js</h3><pre><code>%s</code></pre>" % E(pr["js"])
        jsx = ""
        if pr.get("js"):
            jsx = table([["JavaScript line", "What it does"]] + [[a, b] for a, b in explain_lines(pr["js"], JS_EXPLAIN)])
        return ("<p class=\"meta\">Theme: %s (%s) &middot; Level %d &middot; Files: %s</p><h3>Brief</h3><p>%s</p><h3>Learning goals</h3><ul>%s</ul>"
                "<h3>Elements and CSS</h3><p><b>HTML:</b> %s<br><b>CSS:</b> %s</p><h3>Build guide</h3><ol>%s</ol>"
                "<h3>index.html</h3><pre><code>%s</code></pre><h3>styles.css</h3><pre><code>%s</code></pre>%s"
                "<h3>Explained line by line</h3>%s%s%s"
                "<h3>Check your work</h3><ul>%s</ul><h3>Exercises</h3><ol>%s</ol>") % (
            E(th["name"]), E(th["city"]), pr["level"], "index.html, styles.css" + (", app.js" if pr.get("js") else ""),
            E(pr["brief"]), "".join("<li>%s</li>" % E(g) for g in pr["goals"]),
            E(", ".join(pr["elements"])), E(", ".join(pr["css"])), "".join("<li>%s</li>" % E(x) for x in pr["steps"]),
            E(pr["html"]), E(pr["css_code"]), jsblock,
            table([["HTML line", "What it does"]] + [[a, b] for a, b in explain_lines(pr["html"], HTML_EXPLAIN)]),
            table([["CSS declaration", "What it does"]] + [[a, b] for a, b in explain_lines(pr["css_code"], CSS_EXPLAIN, css=True)]), jsx,
            "".join("<li>%s</li>" % E(x) for x in pr["checklist"]), "".join("<li>%s</li>" % E(x) for x in pr["exercises"]))

    def project_links(prs, intro):
        return "<div class=\"note\">%s %s</div>" % (E(intro), " &middot; ".join(
            "<a href=\"#project-%d\">Project %d: %s</a>" % (pr["number"], pr["number"], E(pr["title"])) for pr in prs))

    # JavaScript part
    secs = [section("js-intro", "JavaScript from zero", blocks(JS_INTRO), kind="JavaScript", keywords="javascript js script dom event function variable array object fetch storage")]
    for r in JS_REFERENCE:
        b = "<p class=\"meta\">Group: %s</p><h3>Syntax</h3><pre><code>%s</code></pre><h3>Description</h3><p>%s</p><h3>Example</h3><pre><code>%s</code></pre>" % (E(r[0]), E(r[2]), E(r[3]), E(r[4]))
        secs.append(section("js-" + re.sub(r"\W", "", r[1]), r[1], b, kind="JavaScript", keywords="javascript js " + r[0].lower()))
    add_part("part-js", "Part 12: JavaScript Reference", secs)

    ALL_LESSONS = list(COURSE) + list(JS_COURSE)
    secs = []
    for i, (ct, cb) in enumerate(ALL_LESSONS):
        prs = pick_projects(PROJECTS, LESSON_PROJECTS[i + 1], i + 1)
        secs.append(section("lesson-%d" % i, ct, blocks(cb) + project_links(prs, "Practice projects for this lesson:"), kind="Lesson", keywords="course lesson tutorial w3schools javascript"))
    add_part("part-course", "Part 13: HTML, CSS and JavaScript Course", secs)

    secs = [section("guide-%d" % i, gt, blocks(gb), kind="Guide") for i, (gt, gb) in enumerate(GUIDES)]
    add_part("part-guides", "Part 14: Practical Guides", secs)

    secs = [section("glossary", "Glossary", table([["Term", "Definition"]] + [list(g) for g in GLOSSARY]), kind="Glossary", keywords=" ".join(g[0] for g in GLOSSARY))]
    add_part("part-glossary", "Part 15: Glossary", secs)

    secs = []
    for pr in PROJECTS:
        th = pr["theme"]
        secs.append(section("project-%d" % pr["number"], "Project %d: %s" % (pr["number"], pr["title"]), project_body(pr), kind="Project",
                            keywords="project %s %s %s level %d%s" % (pr["key"], th["slug"], " ".join(pr["css"]), pr["level"], " javascript js" if pr.get("js") else "")))
    add_part("part-projects", "Part 16: Practice Projects (%d)" % len(PROJECTS), secs)

    # chapter projects: appended to the end of each part's article
    for num, keys in PART_PROJECTS.items():
        pid_index = next((k for k, (pid, t) in enumerate(nav) if t.startswith("Part %d:" % num)), None)
        if pid_index is None:
            continue
        prs = pick_projects(PROJECTS, keys, num)
        parts[pid_index] = parts[pid_index][:-len("</article>")] + section("chapter-projects-%d" % num, "Chapter %d projects" % num,
            project_links(prs, "Before moving on, build these two projects:"), kind="Projects", keywords="chapter projects practice") + "</article>"

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
