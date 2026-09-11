# -*- coding: utf-8 -*-
"""Global attributes, event handler attributes and input types."""

# (name, values, description, version, example)
GLOBAL_ATTRS = [
    ("accesskey", "single character",
     "Defines a keyboard shortcut that activates or focuses the element. The key combination depends on the "
     "browser and operating system (usually Alt + key on Windows/Linux in Chrome and Edge, Alt + Shift + key "
     "in Firefox, Control + Option + key on macOS). Because these combinations often collide with browser and "
     "assistive-technology shortcuts, accesskey is rarely recommended; if used, document the shortcuts on the page.",
     "HTML 4.01", "<button accesskey=\"s\">Save (Alt+S)</button>"),
    ("autocapitalize", "off | none | on | sentences | words | characters",
     "Controls whether and how text input is automatically capitalised on virtual keyboards (phones and "
     "tablets). It has no effect on physical keyboards. Inherited by descendant editable elements.",
     "Living Standard", "<input name=\"username\" autocapitalize=\"none\">\n<textarea autocapitalize=\"sentences\"></textarea>"),
    ("autocorrect", "on | off",
     "Controls whether the browser may automatically correct spelling in editable text. Originally a Safari "
     "extension, added to the Living Standard in 2024.",
     "Living Standard", "<input name=\"code\" autocorrect=\"off\">"),
    ("autofocus", "boolean",
     "Indicates that the element should receive focus as soon as the page loads (or the <dialog> it is in is "
     "shown). Only one element per document should have it. Use with care: moving focus automatically can "
     "disorient screen reader users and scrolls the page to the element.",
     "HTML5 (global since 2019)", "<input name=\"q\" type=\"search\" autofocus>"),
    ("class", "space-separated class names",
     "A list of the classes the element belongs to. Classes are the primary hook for CSS (selector .name) and "
     "for JavaScript (document.querySelectorAll('.name')). An element may have many classes and many elements "
     "may share a class. Class names are case-sensitive, should not start with a digit, and by convention use "
     "lowercase words joined with hyphens (kebab-case). Choose names that describe what the element is, not "
     "how it looks (product-card rather than red-box), so that the style can change without renaming.",
     "HTML 4.01", "<div class=\"card featured\">...</div>\n<style>.card { border: 1px solid #ccc; } .featured { border-color: gold; }</style>"),
    ("contenteditable", "true | false | plaintext-only | (empty = true)",
     "Makes the element's content editable by the user directly in the page, turning it into a basic rich-text "
     "editor. plaintext-only allows editing text but not formatting. The property is inherited: children of an "
     "editable element are editable unless they set contenteditable=\"false\". Combine with the input event and "
     "the document.execCommand or Selection APIs to build editors.",
     "HTML5", "<p contenteditable=\"true\">Click here and edit this text.</p>"),
    ("data-*", "any text",
     "Custom data attributes. Any attribute whose name starts with data- is reserved for the page author's own "
     "data and is guaranteed never to be given a meaning by browsers. The value is available in JavaScript "
     "through element.dataset (data-user-id becomes dataset.userId) and in CSS through attr(). Use them to "
     "attach information to elements without misusing class or id.",
     "HTML5", "<li data-product-id=\"42\" data-price=\"120\">Learn HTML</li>\n<script>\n  const li = document.querySelector('li');\n  console.log(li.dataset.productId, li.dataset.price); // \"42\" \"120\"\n</script>"),
    ("dir", "ltr | rtl | auto",
     "The text direction of the element's content. ltr = left to right (English, French...); rtl = right to "
     "left (Arabic, Hebrew, Persian, Urdu); auto = let the browser decide from the first strongly directional "
     "character, useful for user-generated content. Set it on <html> for the whole page. It affects text "
     "alignment, the side on which bullets and scrollbars appear, and the order of table columns.",
     "HTML 4.01", "<html lang=\"ar\" dir=\"rtl\">\n<p dir=\"ltr\">This English paragraph inside an Arabic page reads left to right.</p>\n<input dir=\"auto\">"),
    ("draggable", "true | false",
     "Whether the element can be dragged with the Drag and Drop API. Images and links are draggable by default; "
     "other elements need draggable=\"true\". The value must be written explicitly (it is not a boolean "
     "attribute). Dragging fires dragstart, drag, dragend on the source and dragenter, dragover, drop on the target.",
     "HTML5", "<div draggable=\"true\" ondragstart=\"event.dataTransfer.setData('text', 'hello')\">Drag me</div>"),
    ("enterkeyhint", "enter | done | go | next | previous | search | send",
     "A hint about which label or icon to show on the Enter key of virtual keyboards, matching the action that "
     "pressing Enter will perform in this field.",
     "Living Standard", "<input type=\"search\" enterkeyhint=\"search\">\n<textarea enterkeyhint=\"send\"></textarea>"),
    ("exportparts", "comma-separated part names (optionally name:alias)",
     "In web components: re-exports parts from a nested shadow tree so that they can be styled from outside with "
     "the ::part() pseudo-element.",
     "CSS Shadow Parts", "<my-dialog exportparts=\"header, footer:dialog-footer\"></my-dialog>"),
    ("hidden", "boolean | until-found",
     "Indicates that the element is not (yet) relevant and should not be rendered. Browsers implement it as "
     "display: none, so any CSS that sets display on the element will override it (add [hidden] { display: none !important } "
     "to be safe). The value until-found keeps the content hidden but searchable with find-in-page and fragment "
     "links; the browser reveals it automatically when found. Do not use hidden to hide content only visually "
     "while keeping it for screen readers; use a visually-hidden CSS class instead.",
     "HTML5", "<p hidden>Not shown.</p>\n<section hidden=\"until-found\">Revealed when the user searches for text inside it.</section>\n<script>document.querySelector('p').hidden = false;</script>"),
    ("id", "unique identifier",
     "A unique identifier for the element within the document. No two elements may share an id. It is used as "
     "the target of fragment links (href=\"#id\"), by CSS (#id), by JavaScript (getElementById), by <label for>, "
     "by aria-labelledby and aria-describedby, by <input list>, by <output for>, by the form attribute and by "
     "<map name>. Ids are case-sensitive, must not contain spaces, and should start with a letter.",
     "HTML 4.01", "<h2 id=\"pricing\">Pricing</h2>\n<a href=\"#pricing\">Jump to pricing</a>\n<label for=\"email\">Email</label> <input id=\"email\">"),
    ("inert", "boolean",
     "Makes the element and all its descendants inert: they cannot be focused, clicked, selected or found by "
     "find-in-page, and they are hidden from assistive technology. It is the tool for disabling everything "
     "behind a custom modal dialog or an open off-canvas menu. Native <dialog> showModal() applies inertness to "
     "the rest of the page automatically.",
     "Living Standard (2022)", "<main inert>Page content that cannot be interacted with while the menu is open</main>\n<nav class=\"drawer\">Menu</nav>"),
    ("inputmode", "none | text | decimal | numeric | tel | search | email | url",
     "A hint about which virtual keyboard to display when the element (an input, textarea or contenteditable) "
     "is focused. Unlike changing type, it does not change validation or the value: inputmode=\"numeric\" on a "
     "text input shows a number pad but still accepts a postal code with a leading zero.",
     "HTML5", "<input name=\"zip\" inputmode=\"numeric\" pattern=\"[0-9]*\">\n<input name=\"amount\" inputmode=\"decimal\">"),
    ("is", "custom element name",
     "Declares that a built-in element should behave like a customised built-in element defined with "
     "customElements.define(name, class, { extends: 'button' }). Not supported in Safari.",
     "HTML5 / Custom Elements", "<button is=\"fancy-button\">Click</button>"),
    ("itemid, itemprop, itemref, itemscope, itemtype", "various",
     "Microdata attributes that embed machine-readable structured data (for example schema.org vocabularies) "
     "into the page for search engines. itemscope creates an item; itemtype gives its type URL; itemprop names "
     "a property; itemid gives a global identifier; itemref includes properties located elsewhere. JSON-LD in "
     "a <script type=\"application/ld+json\"> is the more common approach today.",
     "HTML5 Microdata", "<div itemscope itemtype=\"https://schema.org/Book\">\n  <span itemprop=\"name\">Learn HTML</span> by\n  <span itemprop=\"author\">Sara</span>\n</div>"),
    ("lang", "BCP 47 language tag",
     "The language of the element's content. Language tags consist of a two-letter language code (en, ar, fr, "
     "de, es, zh, ja) optionally followed by a script (zh-Hans) and/or a region (en-GB, ar-EG, pt-BR). Set it on "
     "<html> for the page and on any element whose language differs. Browsers use it for hyphenation, "
     "quotation marks, font choice and spell checking; screen readers use it to switch voices; translation "
     "tools use it to decide what to translate. An empty value means the language is unknown.",
     "HTML 4.01", "<html lang=\"en\">\n<p>The word <span lang=\"ar\">\u0643\u062a\u0627\u0628</span> means book.</p>"),
    ("nonce", "cryptographic number used once",
     "A random token generated by the server for each response and listed in the Content-Security-Policy "
     "header, so that only the inline <script> and <style> elements carrying that nonce are allowed to run. "
     "Browsers hide the value from scripts after parsing.",
     "CSP", "<script nonce=\"r4nd0m\">/* allowed by CSP 'nonce-r4nd0m' */</script>"),
    ("part", "space-separated part names",
     "In web components: names an element inside a shadow tree so that it can be styled from outside with the "
     "::part(name) pseudo-element.",
     "CSS Shadow Parts", "<!-- inside the shadow tree -->\n<button part=\"confirm\">OK</button>\n<!-- outside -->\n<style>my-dialog::part(confirm) { background: green; }</style>"),
    ("popover", "auto | manual | hint | (empty = auto)",
     "Turns the element into a popover: hidden by default and displayed in the top layer (above everything "
     "else) when shown with a button that has popovertarget, or with showPopover()/togglePopover() in "
     "JavaScript. auto popovers close when the user clicks outside or presses Escape and only one is open at a "
     "time; manual popovers must be closed explicitly. Style the backdrop with ::backdrop and the open state with :popover-open.",
     "Living Standard (2023)", "<button popovertarget=\"menu\">Menu</button>\n<div id=\"menu\" popover>\n  <a href=\"/profile\">Profile</a>\n  <a href=\"/logout\">Log out</a>\n</div>"),
    ("role", "ARIA role name",
     "From WAI-ARIA: overrides or specifies the semantic role of the element for assistive technology, for "
     "example role=\"button\", role=\"navigation\", role=\"alert\", role=\"tab\". The first rule of ARIA is not to "
     "use it when a native element already has the right role: prefer <button> over <div role=\"button\">. Use "
     "it for widgets HTML lacks (tabs, trees, comboboxes) and for landmarks in older browsers.",
     "WAI-ARIA 1.0", "<div role=\"alert\">Your order was placed.</div>\n<ul role=\"tablist\"><li role=\"tab\" aria-selected=\"true\">Details</li></ul>"),
    ("aria-*", "various",
     "From WAI-ARIA: a family of attributes that describe the state and properties of elements for assistive "
     "technology. The most used: aria-label (accessible name from a string), aria-labelledby (name from another "
     "element), aria-describedby (description), aria-hidden (hide from AT), aria-expanded (open/closed), "
     "aria-current (current item), aria-live (announce changes), aria-controls, aria-selected, aria-checked, "
     "aria-disabled, aria-required, aria-invalid, aria-haspopup, aria-pressed, aria-busy, aria-modal.",
     "WAI-ARIA 1.0", "<button aria-label=\"Close\" aria-expanded=\"false\" aria-controls=\"panel\">\u00d7</button>\n<div id=\"status\" aria-live=\"polite\"></div>"),
    ("slot", "slot name",
     "Assigns the element to a named <slot> inside the shadow tree of its parent custom element.",
     "DOM Standard", "<user-card>\n  <span slot=\"name\">Ahmed</span>\n</user-card>"),
    ("spellcheck", "true | false",
     "Whether the browser should check the spelling and grammar of the element's editable text. Browsers "
     "decide the default per element (usually on for textarea and contenteditable, off for input). Turn it "
     "off for codes, usernames and passwords. Note: some browsers send checked text to a remote service.",
     "HTML5", "<textarea spellcheck=\"true\"></textarea>\n<input name=\"coupon\" spellcheck=\"false\">"),
    ("style", "CSS declarations",
     "Inline CSS applied to this element only. Declarations are written as property: value pairs separated "
     "by semicolons, exactly as inside a style sheet rule but without the selector and braces. Inline styles "
     "have higher specificity than any selector and are hard to override, cannot use media queries or "
     "pseudo-classes, and are blocked by strict Content Security Policies, so prefer classes and a style "
     "sheet. Inline styles are convenient for quick tests and for values computed by JavaScript.",
     "HTML 4.01", "<p style=\"color: red; font-size: 1.2em; margin-bottom: 0\">Inline styled paragraph</p>"),
    ("tabindex", "integer",
     "Controls whether the element can be focused with the keyboard (Tab key) and in what order. tabindex=\"0\" "
     "makes a normally non-focusable element (such as a div) focusable, in the natural document order. "
     "tabindex=\"-1\" makes it focusable by script (element.focus()) but not by Tab; use it for the target of a "
     "skip link or a container that receives focus programmatically. Positive values (1, 2, 3...) force a "
     "custom order before all other elements and should be avoided because they make the page confusing. "
     "Interactive elements (links, buttons, form controls) are focusable without tabindex.",
     "HTML 4.01", "<div tabindex=\"0\" role=\"button\">Focusable custom control</div>\n<main id=\"content\" tabindex=\"-1\">...</main>"),
    ("title", "text",
     "Advisory information about the element, shown by most desktop browsers as a tooltip when the mouse rests "
     "on it. On <abbr> it holds the expansion; on <link rel=stylesheet> it names an alternate style sheet; on "
     "<iframe> it is the accessible name. Tooltips are not accessible to touch-screen or keyboard users and are "
     "read inconsistently by screen readers, so never put essential information only in title. Do not repeat the "
     "visible text in title; it produces double announcements.",
     "HTML 4.01", "<abbr title=\"World Health Organization\">WHO</abbr>\n<button title=\"Save (Ctrl+S)\">Save</button>"),
    ("translate", "yes | no | (empty = yes)",
     "Whether the element's text and translatable attribute values should be translated when the page is "
     "localised by machine translation tools. Set translate=\"no\" on brand names, code, and addresses.",
     "HTML5", "<p>Buy it at <span translate=\"no\">Book Store</span> today.</p>\n<code translate=\"no\">getElementById</code>"),
    ("virtualkeyboardpolicy", "auto | manual",
     "For editable elements: whether the virtual keyboard opens automatically on focus (auto) or only when "
     "the script calls navigator.virtualKeyboard.show() (manual).",
     "VirtualKeyboard API", "<div contenteditable virtualkeyboardpolicy=\"manual\"></div>"),
    ("writingsuggestions", "true | false",
     "Whether the browser may offer writing suggestions (predictive text, autocomplete of sentences) in "
     "editable elements.",
     "Living Standard (2024)", "<textarea writingsuggestions=\"false\"></textarea>"),
    ("xml:lang, xml:base, xml:space", "various",
     "XML attributes that only have meaning in XHTML documents served as XML. In HTML they are ignored "
     "(xml:lang must match lang if both are present).",
     "XHTML 1.0", "<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">"),
]

# (attribute, event, when it fires, applies to, notes)
EVENT_ATTRS = [
    ("onabort", "abort", "Loading of a resource was aborted.", "img, audio, video, and others", ""),
    ("onauxclick", "auxclick", "A non-primary mouse button (middle, right) was clicked.", "All elements", ""),
    ("onbeforeinput", "beforeinput", "Just before the value of an editable element changes; can be cancelled.", "input, textarea, contenteditable", ""),
    ("onbeforematch", "beforematch", "Content hidden with hidden=until-found is about to be revealed by find-in-page.", "All elements", ""),
    ("onbeforetoggle", "beforetoggle", "A popover or <details> is about to open or close; cancellable for popovers.", "popover elements, details, dialog", ""),
    ("onblur", "blur", "The element lost focus. Does not bubble; use focusout for delegation.", "Focusable elements", ""),
    ("oncancel", "cancel", "The user pressed Escape in a <dialog>, or cancelled a file picker.", "dialog, input type=file", ""),
    ("oncanplay", "canplay", "Enough media data is available to start playing.", "audio, video", ""),
    ("oncanplaythrough", "canplaythrough", "The media can probably play to the end without buffering.", "audio, video", ""),
    ("onchange", "change", "The value of a form control was committed: after a text field loses focus with a changed value, or immediately when a checkbox, radio, select or file input changes.", "input, select, textarea", "Use input for live updates."),
    ("onclick", "click", "The element was clicked with the primary button, tapped, or activated with Enter/Space on a button or link.", "All elements", "The most used event attribute."),
    ("onclose", "close", "A <dialog> was closed, or a popover was hidden.", "dialog, popover", ""),
    ("oncontextmenu", "contextmenu", "The user requested the context menu (right-click, long press, Shift+F10).", "All elements", "Preventing default hides the browser menu."),
    ("oncopy, oncut, onpaste", "copy, cut, paste", "Clipboard operations on the element.", "All elements", ""),
    ("oncuechange", "cuechange", "The active text track cues changed.", "track", ""),
    ("ondblclick", "dblclick", "Double click.", "All elements", "Not fired on touch in most browsers."),
    ("ondrag, ondragend, ondragenter, ondragleave, ondragover, ondragstart, ondrop", "drag events", "Stages of a drag-and-drop operation: dragstart/drag/dragend on the dragged element, dragenter/dragover/dragleave/drop on the drop target.", "All elements", "Call preventDefault in dragover to allow dropping."),
    ("ondurationchange", "durationchange", "The media duration attribute was updated.", "audio, video", ""),
    ("onemptied", "emptied", "The media element became empty (for example after a network error or load()).", "audio, video", ""),
    ("onended", "ended", "Playback reached the end.", "audio, video", ""),
    ("onerror", "error", "A resource failed to load, or a script error occurred (on body/window).", "img, script, link, audio, video, body", ""),
    ("onfocus", "focus", "The element received focus. Does not bubble; use focusin for delegation.", "Focusable elements", ""),
    ("onformdata", "formdata", "The form's data is being constructed for submission; lets scripts add entries.", "form", ""),
    ("oninput", "input", "The value of an editable element changed, on every keystroke or change.", "input, select, textarea, contenteditable", ""),
    ("oninvalid", "invalid", "A control failed validation on submission.", "Form controls", ""),
    ("onkeydown", "keydown", "A key was pressed down. Repeats while held.", "Focusable elements, document", "Use event.key."),
    ("onkeypress", "keypress", "Deprecated. A character key was pressed. Use keydown.", "-", "Deprecated"),
    ("onkeyup", "keyup", "A key was released.", "Focusable elements", ""),
    ("onload", "load", "The resource (image, script, style sheet, frame, or the whole page on body) finished loading.", "img, script, link, iframe, body, object", ""),
    ("onloadeddata", "loadeddata", "The first frame of media has loaded.", "audio, video", ""),
    ("onloadedmetadata", "loadedmetadata", "Duration and dimensions are known.", "audio, video", ""),
    ("onloadstart", "loadstart", "The browser started loading media.", "audio, video", ""),
    ("onmousedown, onmouseup", "mousedown, mouseup", "A mouse button was pressed or released.", "All elements", ""),
    ("onmouseenter, onmouseleave", "mouseenter, mouseleave", "The pointer entered or left the element (does not bubble, not fired for children).", "All elements", ""),
    ("onmousemove", "mousemove", "The pointer moved over the element.", "All elements", "Fires very often."),
    ("onmouseover, onmouseout", "mouseover, mouseout", "The pointer entered or left the element or one of its children (bubbles).", "All elements", ""),
    ("onpause, onplay, onplaying", "pause, play, playing", "Playback paused / play() called / actually started after buffering.", "audio, video", ""),
    ("onpointerdown, onpointerup, onpointermove, onpointerover, onpointerout, onpointerenter, onpointerleave, onpointercancel, ongotpointercapture, onlostpointercapture", "pointer events", "Unified events for mouse, touch and pen input. Prefer them over mouse and touch events.", "All elements", ""),
    ("onprogress", "progress", "Periodic progress while downloading media.", "audio, video", ""),
    ("onratechange", "ratechange", "Playback speed changed.", "audio, video", ""),
    ("onreset", "reset", "The form was reset.", "form", ""),
    ("onresize", "resize", "The window was resized (on body); or an element resized (video).", "body, video", "Use ResizeObserver for elements."),
    ("onscroll", "scroll", "The element or document scrolled.", "Scrollable elements, body", ""),
    ("onscrollend", "scrollend", "Scrolling finished.", "Scrollable elements, body", ""),
    ("onsecuritypolicyviolation", "securitypolicyviolation", "A Content Security Policy rule was violated.", "All elements", ""),
    ("onseeked, onseeking", "seeked, seeking", "A seek operation finished / started.", "audio, video", ""),
    ("onselect", "select", "Text was selected inside an input or textarea.", "input, textarea", ""),
    ("onselectionchange", "selectionchange", "The document selection changed.", "document, input, textarea", ""),
    ("onslotchange", "slotchange", "The nodes assigned to a slot changed.", "slot", ""),
    ("onstalled", "stalled", "The browser is trying to fetch media data but none is arriving.", "audio, video", ""),
    ("onsubmit", "submit", "The form is about to be submitted; call preventDefault() to handle it with JavaScript.", "form", ""),
    ("onsuspend", "suspend", "Media loading was intentionally suspended.", "audio, video", ""),
    ("ontimeupdate", "timeupdate", "The playback position changed (several times per second).", "audio, video", ""),
    ("ontoggle", "toggle", "A <details> element or popover opened or closed.", "details, popover elements", ""),
    ("ontouchstart, ontouchmove, ontouchend, ontouchcancel", "touch events", "Touch screen interactions. Prefer pointer events.", "All elements", ""),
    ("onvolumechange", "volumechange", "Volume or muted state changed.", "audio, video", ""),
    ("onwaiting", "waiting", "Playback stopped because the next frame is not available.", "audio, video", ""),
    ("onwheel", "wheel", "A mouse wheel or trackpad scroll gesture.", "All elements", ""),
    ("onanimationstart, onanimationend, onanimationiteration, onanimationcancel", "animation events", "CSS animation lifecycle.", "All elements", ""),
    ("ontransitionstart, ontransitionend, ontransitionrun, ontransitioncancel", "transition events", "CSS transition lifecycle.", "All elements", ""),
    ("oncontextlost, oncontextrestored", "contextlost, contextrestored", "A canvas drawing context was lost or restored.", "canvas", ""),
    ("Window events on <body>: onafterprint, onbeforeprint, onbeforeunload, onhashchange, onlanguagechange, onmessage, onmessageerror, onoffline, ononline, onpagehide, onpagereveal, onpageshow, onpageswap, onpopstate, onrejectionhandled, onstorage, onunhandledrejection, onunload", "window events", "Events that fire on the window object and are exposed as attributes on <body> (and <frameset>).", "body", "See the <body> entry."),
]

# (type, title, since, description, specific attrs [(name, note)], example, notes)
INPUT_TYPES = [
    ("text", "Single-line text", "HTML 2.0",
     "The default type. A single-line text field. Line breaks are removed from the value. Use it for names, "
     "titles, and anything that has no more specific type.",
     [("maxlength / minlength", "Length limits."), ("pattern", "Regular expression to validate."), ("placeholder", "Hint text."),
      ("size", "Visible width in characters."), ("list", "Datalist of suggestions."), ("autocomplete", "Autofill token such as name, given-name, organization."), ("dirname", "Submit text direction.")],
     "<label for=\"n\">Full name</label>\n<input id=\"n\" name=\"name\" type=\"text\" autocomplete=\"name\" required>", ""),
    ("password", "Password", "HTML 2.0",
     "A single-line field whose characters are obscured with dots or asterisks. The value is still sent as "
     "plain text in the form submission, so the page must be served over HTTPS. Browsers offer to save and "
     "generate passwords when autocomplete is set to current-password or new-password.",
     [("minlength / maxlength", "Length rules."), ("pattern", "Complexity rules (explain them in title)."), ("autocomplete", "current-password, new-password, one-time-code.")],
     "<label for=\"pw\">Password</label>\n<input id=\"pw\" name=\"password\" type=\"password\" minlength=\"8\" autocomplete=\"new-password\" required>", "Add a 'show password' toggle for usability."),
    ("checkbox", "Check box", "HTML 2.0",
     "An on/off box. Each checkbox is independent; several checkboxes may share a name to send multiple "
     "values. Only checked boxes are submitted (as name=value). The indeterminate visual state can be set from "
     "JavaScript for 'some children selected'.",
     [("checked", "Initially ticked."), ("value", "Sent when checked; default 'on'."), ("required", "Must be ticked (useful for 'I agree').")],
     "<label><input type=\"checkbox\" name=\"topics\" value=\"html\" checked> HTML</label>\n<label><input type=\"checkbox\" name=\"topics\" value=\"css\"> CSS</label>", "Wrap the input in the label so the text is clickable."),
    ("radio", "Radio button", "HTML 2.0",
     "One of a group of mutually exclusive options. All radio buttons with the same name form a group and "
     "only one can be selected. Arrow keys move the selection within the group. Always provide a default or "
     "make the group required, and caption the group with fieldset/legend.",
     [("checked", "Initially selected."), ("value", "Sent for the selected button."), ("required", "One button in the group must be selected.")],
     "<fieldset>\n  <legend>Delivery</legend>\n  <label><input type=\"radio\" name=\"d\" value=\"standard\" checked> Standard</label>\n  <label><input type=\"radio\" name=\"d\" value=\"express\"> Express</label>\n</fieldset>", ""),
    ("submit", "Submit button", "HTML 2.0",
     "A button that submits the form. Its value is the button's label and, if it has a name, is submitted "
     "too. Prefer the <button> element, which can contain HTML content.",
     [("value", "Label (default 'Submit')."), ("formaction, formmethod, formenctype, formtarget, formnovalidate", "Override form settings.")],
     "<input type=\"submit\" value=\"Send message\">", ""),
    ("reset", "Reset button", "HTML 2.0",
     "A button that restores all controls of the form to their initial values. Rarely useful and often clicked "
     "by mistake; most forms omit it.",
     [("value", "Label (default 'Reset').")], "<input type=\"reset\" value=\"Clear form\">", ""),
    ("button", "Generic button", "HTML 3.2",
     "A button with no default behaviour, for use with JavaScript. Prefer <button type=\"button\">.",
     [("value", "Label.")], "<input type=\"button\" value=\"Show help\" onclick=\"alert('Help')\">", ""),
    ("hidden", "Hidden field", "HTML 2.0",
     "A control that is not displayed but whose value is submitted with the form. Used for record ids, CSRF "
     "tokens and other data the user does not edit. The name _charset_ has a special meaning: the browser fills "
     "it with the form's encoding.",
     [("value", "The value to submit.")], "<input type=\"hidden\" name=\"csrf\" value=\"a1b2c3\">", "Never rely on hidden fields for security; users can change them."),
    ("image", "Image submit button", "HTML 2.0",
     "A graphical submit button showing the image in src. When clicked it submits the form together with the "
     "click coordinates as name.x and name.y. Requires alt.",
     [("src", "Image URL."), ("alt", "Required text alternative."), ("width / height", "Size."), ("formaction etc.", "Override form settings.")],
     "<input type=\"image\" src=\"go.png\" alt=\"Search\" width=\"32\" height=\"32\">", ""),
    ("file", "File chooser", "HTML 3.2",
     "Lets the user select one or more files from their device to upload. The form must use method=\"post\" "
     "and enctype=\"multipart/form-data\". The selected files are available in JavaScript as input.files. "
     "For security the value cannot be set by script and shows only a fake path.",
     [("accept", "Allowed types: image/*, video/*, audio/*, .pdf, application/pdf, .doc,.docx"), ("multiple", "Allow several files."), ("capture", "user | environment: open camera/mic directly on phones."), ("webkitdirectory", "Non-standard: choose a folder.")],
     "<label for=\"cv\">Upload your CV (PDF)</label>\n<input id=\"cv\" name=\"cv\" type=\"file\" accept=\".pdf,application/pdf\">", ""),
    ("email", "Email address", "HTML5",
     "A text field validated as an email address (or a comma-separated list with multiple). Mobile keyboards "
     "show @ and . keys. The value is trimmed and validated as user@host; a domain without a dot is accepted.",
     [("multiple", "Allow several addresses separated by commas."), ("pattern", "Additional restriction, for example a company domain."), ("list", "Suggestions."), ("maxlength / minlength / size / placeholder / readonly", "As text.")],
     "<label for=\"e\">Email</label>\n<input id=\"e\" name=\"email\" type=\"email\" autocomplete=\"email\" required>", "Still validate on the server."),
    ("url", "Web address", "HTML5",
     "A text field validated as an absolute URL (it must include a scheme such as https://). Mobile keyboards "
     "show / and .com keys.",
     [("pattern", "Extra restriction, for example https only."), ("list, maxlength, minlength, placeholder, readonly, size", "As text.")],
     "<label for=\"site\">Website</label>\n<input id=\"site\" name=\"site\" type=\"url\" placeholder=\"https://example.com\">", ""),
    ("tel", "Telephone number", "HTML5",
     "A text field for telephone numbers. It is not validated (formats vary too much worldwide), but phones show "
     "a telephone keypad. Add pattern for a specific format.",
     [("pattern", "For example [0-9]{11} or \\+20[0-9]{10}."), ("list, maxlength, minlength, placeholder, readonly, size", "As text.")],
     "<label for=\"t\">Mobile</label>\n<input id=\"t\" name=\"tel\" type=\"tel\" autocomplete=\"tel\" pattern=\"01[0-9]{9}\" title=\"11 digits starting with 01\">", ""),
    ("search", "Search field", "HTML5",
     "A text field for search terms. Functionally identical to text, but some browsers style it with rounded "
     "corners and a clear (x) button, and mobile keyboards show a Search key. Line breaks are removed.",
     [("list, maxlength, minlength, pattern, placeholder, readonly, size", "As text."), ("incremental", "Non-standard (WebKit): fire search events while typing.")],
     "<search>\n  <label for=\"q\">Search</label>\n  <input id=\"q\" name=\"q\" type=\"search\" placeholder=\"Search books\">\n</search>", ""),
    ("number", "Numeric field", "HTML5",
     "A field for entering a number, usually with spinner arrows. Only digits, sign, decimal point and "
     "exponent are accepted; the value is validated against min, max and step. Use it only for actual "
     "quantities. For identifiers such as credit card numbers or postal codes use type=\"text\" with "
     "inputmode=\"numeric\" because they can have leading zeros and are not meant to be incremented.",
     [("min / max", "Range."), ("step", "Increment; 'any' allows decimals of any precision. Default 1, which rejects 2.5 unless step is 0.5 or any."), ("placeholder, readonly, list", "As text.")],
     "<label for=\"qty\">Quantity</label>\n<input id=\"qty\" name=\"qty\" type=\"number\" min=\"1\" max=\"99\" step=\"1\" value=\"1\">", "Scrolling the mouse wheel over a focused number input changes the value in some browsers."),
    ("range", "Slider", "HTML5",
     "A slider for choosing an approximate number where the exact value is not important, such as volume or "
     "brightness. Default range 0-100, step 1. Show the current value with an <output> because the slider "
     "itself does not display it.",
     [("min / max", "Range."), ("step", "Increment."), ("list", "Datalist for tick marks."), ("orient", "Non-standard (Firefox): vertical.")],
     "<label for=\"vol\">Volume</label>\n<input id=\"vol\" name=\"vol\" type=\"range\" min=\"0\" max=\"100\" value=\"40\" oninput=\"out.value = this.value\">\n<output id=\"out\">40</output>", ""),
    ("color", "Colour picker", "HTML5",
     "A control for choosing a colour, usually opening the operating system colour picker. The value is always "
     "a lowercase hexadecimal colour such as #ff0000; alpha (transparency) is not supported unless the "
     "experimental alpha attribute is used.",
     [("value", "Initial colour in #rrggbb form (default #000000)."), ("list", "Datalist of suggested colours."), ("alpha, colorspace", "Experimental.")],
     "<label for=\"c\">Theme colour</label>\n<input id=\"c\" name=\"color\" type=\"color\" value=\"#e60000\">", ""),
    ("date", "Date", "HTML5",
     "A control for a year, month and day, usually with a calendar pop-up. The value is always in the format "
     "YYYY-MM-DD regardless of how the browser displays it to the user, so it is safe to process on the server. "
     "Safari on macOS supports it since version 14.1.",
     [("min / max", "Earliest and latest date, as YYYY-MM-DD."), ("step", "In days."), ("list", "Suggested dates."), ("readonly, required", "As usual.")],
     "<label for=\"d\">Delivery date</label>\n<input id=\"d\" name=\"date\" type=\"date\" min=\"2026-09-12\" max=\"2026-12-31\" required>", "Set min to today's date with JavaScript to prevent past dates."),
    ("time", "Time of day", "HTML5",
     "A control for hours and minutes (and optionally seconds), without a time zone. The value format is "
     "HH:MM or HH:MM:SS in 24-hour form.",
     [("min / max", "As HH:MM."), ("step", "In seconds; 60 = minutes only (default), 1 = show seconds."), ("list", "Suggested times.")],
     "<label for=\"t\">Appointment time</label>\n<input id=\"t\" name=\"time\" type=\"time\" min=\"09:00\" max=\"17:00\" step=\"900\">", "step 900 = 15-minute increments."),
    ("datetime-local", "Local date and time", "HTML5",
     "A control for a date and time with no time zone, format YYYY-MM-DDTHH:MM. Convert to UTC on the server "
     "if needed. The older type=\"datetime\" (with time zone) was removed from the standard.",
     [("min / max", "As YYYY-MM-DDTHH:MM."), ("step", "In seconds."), ("list", "Suggestions.")],
     "<label for=\"dt\">Event start</label>\n<input id=\"dt\" name=\"start\" type=\"datetime-local\" value=\"2026-10-01T19:00\">", ""),
    ("month", "Month and year", "HTML5",
     "A control for a month in a year, value format YYYY-MM. Useful for card expiry dates and reports. Not "
     "supported in Firefox or Safari desktop, which fall back to a text field.",
     [("min / max", "As YYYY-MM."), ("step", "In months."), ("list", "Suggestions.")],
     "<label for=\"exp\">Card expiry</label>\n<input id=\"exp\" name=\"exp\" type=\"month\" autocomplete=\"cc-exp\">", ""),
    ("week", "Week of the year", "HTML5",
     "A control for an ISO week, value format YYYY-Www (for example 2026-W37). Limited browser support "
     "(Chromium only); others show a text field.",
     [("min / max", "As YYYY-Www."), ("step", "In weeks."), ("list", "Suggestions.")],
     "<label for=\"w\">Week</label>\n<input id=\"w\" name=\"week\" type=\"week\" value=\"2026-W37\">", ""),
]
