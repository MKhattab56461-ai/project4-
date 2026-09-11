# The Complete HTML Reference Book (with CSS and JavaScript)

A reference book for HTML 1, 2.0, 3.2, 4.01, XHTML, HTML5 and the Living Standard, plus CSS and JavaScript parts.

| File | What it is |
|------|------------|
| **`HTML-Elements-Illustrated.pdf`** | **The short illustrated edition (238 pages, A4): every element - what it does, example code, and a real picture of what the browser shows. Start here.** |
| `HTML-Elements-Illustrated.html` | Same content as one searchable web page (type an element name). |
| `HTML-Reference-Book.pdf` | The printable book (13,000+ pages, A5, bookmarks + table of contents + index). Search with Ctrl+F. |
| `HTML-Reference-Book.html` | The same content as one web page with an instant search box. Open it in any browser, type a word (for example `footer`, `td`, `font-family`, `href`) and only matching entries stay visible. Press `/` to jump to the search box, `Esc` to clear. |
| `src/` | The Python sources. `python3 src/build.py` regenerates both files (needs `pip install reportlab`). |
| `shots/` | 382 screenshots of every element example and every input type, rendered in headless Chrome by `src/render_shots.py` (start Chrome with `src/start_chrome.sh` first). They appear in the book after each example as **Result in the browser**. |

## Contents

1. History of HTML  2. Fundamentals  3. HTML version by version  4. Global attributes (one page each)
5. Event handler attributes (one page each)  6. Element reference: 144 elements, every attribute explained, and every example shown as code + **browser screenshot** + explanation
7. `<input>` types  8. Obsolete elements and attributes  9. Attribute reference (alphabetical)
10. Value references (rel, meta names, autocomplete, MIME, URL schemes, 148 colour names, entities)
11. CSS: fundamentals, selectors, properties, styling cookbook, lists and tables with CSS (W3Schools)
12. **JavaScript reference**: the language from zero (syntax, types, functions, arrays, objects, DOM, events, forms, storage, fetch, modules, classes) plus 121 one-page reference entries
13. **Course**: 47 lessons - 36 HTML & CSS lessons following the W3Schools tutorial, then 11 JavaScript lessons - **each lesson followed by two practice projects**
14. Practical guides  15. Glossary and index
16. **Practice projects**: 1,375 complete projects (55 page types x 25 businesses, 10 types with JavaScript), each with brief, goals, build guide, full `index.html` + `styles.css` (+ `app.js`), line-by-line explanation, checklist and exercises

Every chapter (part) also ends with two practice projects. Page numbering starts at 1 on the first chapter page; cover and contents use roman numerals.

Sources: WHATWG HTML Living Standard, MDN, htmlreference.io, codeshack.io, W3Schools (HTML & CSS Lists and Tables).
