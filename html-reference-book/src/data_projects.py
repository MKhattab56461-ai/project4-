# -*- coding: utf-8 -*-
"""1,125 practice projects = 45 project types x 25 themes. Each project returns a dict with
title, number, theme, kind, level, brief, goals, elements, css_props, steps, html, css, checklist, exercises."""

THEMES = [
    dict(name="Cairo Book Shop", slug="bookshop", noun="book", nouns="books", tagline="PDF and printed books about web development",
         city="Giza", person="Mohamed Khattab", primary="#b90000", accent="#f4f1ea",
         items=[("Learn HTML", "From your first tag to a complete page", "120 EGP"), ("CSS in Practice", "Layouts, colours and typography", "150 EGP"),
                ("JavaScript Basics", "Make pages interactive", "180 EGP"), ("Web Accessibility", "Pages everyone can use", "95 EGP")]),
    dict(name="Nile Bakery", slug="bakery", noun="pastry", nouns="pastries", tagline="Fresh bread and pastries every morning",
         city="Cairo", person="Sara Adel", primary="#a0522d", accent="#fff6ec",
         items=[("Sourdough loaf", "Slow fermented, crisp crust", "60 EGP"), ("Croissant", "Butter, 27 layers", "35 EGP"),
                ("Date cookies", "Traditional maamoul style", "80 EGP"), ("Baklava box", "Pistachio and honey", "220 EGP")]),
    dict(name="Pyramid Fitness", slug="gym", noun="class", nouns="classes", tagline="Train smarter, feel stronger",
         city="6th of October", person="Omar Farouk", primary="#0f766e", accent="#ecfdf5",
         items=[("Morning yoga", "Flexibility and calm, 60 minutes", "100 EGP"), ("Strength circuit", "Full body, all levels", "120 EGP"),
                ("Spinning", "High energy cycling", "110 EGP"), ("Personal training", "One to one coaching", "350 EGP")]),
    dict(name="Delta Dental Clinic", slug="clinic", noun="service", nouns="services", tagline="Gentle care for the whole family",
         city="Mansoura", person="Dr. Hana Youssef", primary="#1d4ed8", accent="#eff6ff",
         items=[("Check-up", "Examination and cleaning", "300 EGP"), ("Whitening", "Brighter smile in one visit", "1500 EGP"),
                ("Filling", "Tooth-coloured composite", "600 EGP"), ("Braces consultation", "Plan your treatment", "Free")]),
    dict(name="Red Sea Travel", slug="travel", noun="tour", nouns="tours", tagline="Discover Egypt from desert to reef",
         city="Hurghada", person="Laila Mansour", primary="#0369a1", accent="#f0f9ff",
         items=[("Luxor day trip", "Karnak, Valley of the Kings", "1200 EGP"), ("Snorkelling", "Giftun island reefs", "700 EGP"),
                ("Desert safari", "Quad bikes and Bedouin dinner", "900 EGP"), ("Nile cruise", "Three nights Aswan to Luxor", "6500 EGP")]),
    dict(name="Lotus Language School", slug="school", noun="course", nouns="courses", tagline="Learn English, French and German in small groups",
         city="Alexandria", person="Nour El Din", primary="#7c3aed", accent="#f5f3ff",
         items=[("English A1", "Beginner, 8 weeks", "1800 EGP"), ("French B1", "Intermediate conversation", "2200 EGP"),
                ("German A2", "Grammar and speaking", "2000 EGP"), ("IELTS preparation", "Exam strategies", "3000 EGP")]),
    dict(name="Green Leaf Cafe", slug="cafe", noun="drink", nouns="drinks", tagline="Specialty coffee and quiet corners",
         city="Zamalek", person="Karim Said", primary="#166534", accent="#f0fdf4",
         items=[("Flat white", "Double shot, silky milk", "55 EGP"), ("Cold brew", "18 hours steeped", "60 EGP"),
                ("Hibiscus iced tea", "Karkade with mint", "40 EGP"), ("Cheesecake", "Baked, with berries", "75 EGP")]),
    dict(name="Sinai Trekking Club", slug="trekking", noun="hike", nouns="hikes", tagline="Guided mountain walks for every level",
         city="Saint Catherine", person="Yara Hamdy", primary="#92400e", accent="#fffbeb",
         items=[("Mount Sinai sunrise", "Night climb, 7 km", "400 EGP"), ("Blue Desert loop", "Easy day walk", "250 EGP"),
                ("Wadi Gnai", "Palms and pools", "300 EGP"), ("Three-day traverse", "Camping under stars", "1900 EGP")]),
    dict(name="Horizon Photography", slug="photo", noun="session", nouns="sessions", tagline="Portraits, weddings and product photography",
         city="Maadi", person="Adham Nabil", primary="#111827", accent="#f3f4f6",
         items=[("Portrait session", "One hour, 20 edited photos", "1200 EGP"), ("Wedding day", "Full coverage, two photographers", "15000 EGP"),
                ("Product shoot", "White background, 10 items", "900 EGP"), ("Family session", "Outdoor, golden hour", "1500 EGP")]),
    dict(name="Papyrus Stationery", slug="stationery", noun="product", nouns="products", tagline="Notebooks, pens and paper made in Egypt",
         city="Heliopolis", person="Dina Fathy", primary="#be185d", accent="#fdf2f8",
         items=[("Dotted notebook", "A5, 160 pages", "140 EGP"), ("Fountain pen", "Steel nib, refillable", "350 EGP"),
                ("Washi tape set", "Six patterns", "90 EGP"), ("Desk planner", "Weekly, undated", "110 EGP")]),
    dict(name="Oasis Plant Nursery", slug="plants", noun="plant", nouns="plants", tagline="Indoor plants and gardening advice",
         city="Sheikh Zayed", person="Hossam Ali", primary="#15803d", accent="#f7fee7",
         items=[("Monstera", "Large leaves, easy care", "250 EGP"), ("Snake plant", "Survives anything", "120 EGP"),
                ("Basil pot", "Kitchen herb", "45 EGP"), ("Olive tree", "Balcony sized", "600 EGP")]),
    dict(name="Cedar Furniture", slug="furniture", noun="piece", nouns="pieces", tagline="Solid wood furniture made to order",
         city="Damietta", person="Tarek Lotfy", primary="#78350f", accent="#fef3c7",
         items=[("Oak dining table", "Seats six", "9500 EGP"), ("Bookshelf", "Five shelves, walnut", "4200 EGP"),
                ("Bedside table", "One drawer", "1500 EGP"), ("Coffee table", "Round, ash wood", "2800 EGP")]),
    dict(name="Byte Repair", slug="repair", noun="repair", nouns="repairs", tagline="Phone and laptop repairs while you wait",
         city="Nasr City", person="Mostafa Gamal", primary="#0891b2", accent="#ecfeff",
         items=[("Screen replacement", "Most phones, 1 hour", "From 800 EGP"), ("Battery swap", "Original cells", "From 500 EGP"),
                ("Laptop cleaning", "Fans and thermal paste", "350 EGP"), ("Data recovery", "Drives and cards", "From 1200 EGP")]),
    dict(name="Sahara Pet Care", slug="pets", noun="service", nouns="services", tagline="Grooming, boarding and vet visits",
         city="New Cairo", person="Rana Ibrahim", primary="#c2410c", accent="#fff7ed",
         items=[("Full grooming", "Bath, cut and nails", "400 EGP"), ("Day boarding", "Play and rest", "250 EGP"),
                ("Vaccination", "Annual boosters", "300 EGP"), ("Dog walking", "30 minutes", "100 EGP")]),
    dict(name="Alexandria Sailing School", slug="sailing", noun="lesson", nouns="lessons", tagline="Learn to sail on the Mediterranean",
         city="Alexandria", person="Amr Selim", primary="#1e40af", accent="#eff6ff",
         items=[("Taster session", "Two hours on the water", "500 EGP"), ("Beginner course", "Five sessions", "2200 EGP"),
                ("Racing clinic", "Tactics and trim", "1800 EGP"), ("Private lesson", "One to one", "900 EGP")]),
    dict(name="Habiba Handmade Jewellery", slug="jewellery", noun="item", nouns="items", tagline="Silver and brass pieces inspired by Nubia",
         city="Aswan", person="Habiba Saleh", primary="#a16207", accent="#fefce8",
         items=[("Lotus pendant", "Sterling silver", "650 EGP"), ("Brass cuff", "Hand engraved", "420 EGP"),
                ("Bead earrings", "Recycled glass", "180 EGP"), ("Ankh ring", "Adjustable", "300 EGP")]),
    dict(name="Fayoum Pottery Studio", slug="pottery", noun="workshop", nouns="workshops", tagline="Wheel throwing and glazing classes",
         city="Tunis Village", person="Ahmed Mahmoud", primary="#9a3412", accent="#fff7ed",
         items=[("Intro to the wheel", "Three hours, take home a bowl", "450 EGP"), ("Glazing day", "Colour your pieces", "300 EGP"),
                ("Kids clay class", "Ages 6 to 12", "200 EGP"), ("Weekend retreat", "Two days with meals", "2500 EGP")]),
    dict(name="Cleopatra Beauty Salon", slug="salon", noun="treatment", nouns="treatments", tagline="Hair, nails and skin care",
         city="Dokki", person="Mariam Adel", primary="#db2777", accent="#fdf2f8",
         items=[("Haircut and blow-dry", "Consultation included", "350 EGP"), ("Manicure", "Classic or gel", "200 EGP"),
                ("Facial", "Deep cleanse, 60 minutes", "600 EGP"), ("Bridal package", "Hair, make-up and nails", "4500 EGP")]),
    dict(name="Suez Auto Service", slug="auto", noun="service", nouns="services", tagline="Honest car servicing and repairs",
         city="Suez", person="Khaled Nasser", primary="#374151", accent="#f9fafb",
         items=[("Oil change", "Filter included", "600 EGP"), ("Brake pads", "Front axle", "1400 EGP"),
                ("Air conditioning", "Recharge and check", "900 EGP"), ("Pre-purchase inspection", "120 point check", "750 EGP")]),
    dict(name="Luxor Music Academy", slug="music", noun="course", nouns="courses", tagline="Oud, piano, guitar and voice lessons",
         city="Luxor", person="Salma Ragab", primary="#4c1d95", accent="#f5f3ff",
         items=[("Oud for beginners", "Eight weekly lessons", "1600 EGP"), ("Piano grade 1", "Theory and practice", "1800 EGP"),
                ("Guitar chords", "Play songs in a month", "1400 EGP"), ("Voice coaching", "Breathing and range", "1500 EGP")]),
    dict(name="Port Said Seafood", slug="restaurant", noun="dish", nouns="dishes", tagline="Grilled fish straight from the boats",
         city="Port Said", person="Sherif Wahba", primary="#0e7490", accent="#ecfeff",
         items=[("Grilled sea bass", "With rice and salad", "320 EGP"), ("Shrimp tagine", "Tomato and garlic", "280 EGP"),
                ("Calamari", "Fried, with tahini", "190 EGP"), ("Fish soup", "Daily catch", "120 EGP")]),
    dict(name="Delta Kids Library", slug="library", noun="programme", nouns="programmes", tagline="Stories, reading clubs and homework help",
         city="Tanta", person="Ghada Kamel", primary="#ea580c", accent="#fff7ed",
         items=[("Story hour", "Ages 3 to 6, Saturdays", "Free"), ("Reading club", "Ages 7 to 11", "50 EGP per month"),
                ("Homework help", "Weekday afternoons", "Free"), ("Summer challenge", "Read ten books", "Free")]),
    dict(name="Nubian Guest House", slug="guesthouse", noun="room", nouns="rooms", tagline="Colourful rooms on the west bank of the Nile",
         city="Aswan", person="Fatma Hassan", primary="#b45309", accent="#fffbeb",
         items=[("Garden room", "Double bed, shared terrace", "900 EGP"), ("Nile view suite", "Balcony and breakfast", "1800 EGP"),
                ("Family room", "Sleeps four", "1500 EGP"), ("Rooftop dorm", "Budget beds", "300 EGP")]),
    dict(name="Ismailia Cycling Store", slug="cycling", noun="bike", nouns="bikes", tagline="Bikes, parts and Friday group rides",
         city="Ismailia", person="Bassem Adly", primary="#dc2626", accent="#fef2f2",
         items=[("City bike", "Seven gears, basket", "6500 EGP"), ("Mountain bike", "Front suspension", "11000 EGP"),
                ("Kids bike", "20 inch wheels", "3200 EGP"), ("Tune-up", "Brakes, gears and true wheels", "250 EGP")]),
    dict(name="Minya Coding Club", slug="coding", noun="workshop", nouns="workshops", tagline="Free weekend coding for teenagers",
         city="Minya", person="Youssef Hany", primary="#2563eb", accent="#eff6ff",
         items=[("HTML weekend", "Build your first page", "Free"), ("CSS art", "Draw with code", "Free"),
                ("Scratch games", "Ages 10 to 13", "Free"), ("Hackathon", "48 hours, teams of four", "Free")]),
]

HEAD = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '  <title>{title}</title>\n  <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n')
FOOT = '</body>\n</html>'
BASE_CSS = ('*, *::before, *::after {{ box-sizing: border-box; }}\n:root {{ --brand: {primary}; --accent: {accent}; --ink: #1b2431; --muted: #5b6472; --line: #d9d9d9; }}\n'
            'body {{ margin: 0; font-family: system-ui, Arial, sans-serif; line-height: 1.6; color: var(--ink); }}\n')


def items_li(t, n=4, fmt='<li>{0}</li>'):
    return "\n".join("    " + fmt.format(*it) for it in t["items"][:n])


# --------------------------------------------------------------------------- 40 project types
# Each: key, title pattern, level (1-3), brief, goals, elements, css, steps, builder(t) -> (html, css), checklist, exercises
TYPES = []


def ptype(**kw):
    TYPES.append(kw)


def b_landing(t):
    html = HEAD.format(title=t["name"]) + f'''  <header class="hero">
    <h1>{t["name"]}</h1>
    <p class="tagline">{t["tagline"]}</p>
    <a class="btn" href="#offers">See our {t["nouns"]}</a>
  </header>
  <main>
    <section id="offers">
      <h2>Popular {t["nouns"]}</h2>
      <ul class="cards">
{items_li(t, 3, '<li class="card"><h3>{0}</h3><p>{1}</p><strong>{2}</strong></li>')}
      </ul>
    </section>
  </main>
  <footer>
    <p>&copy; 2026 {t["name"]}, {t["city"]}</p>
  </footer>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.hero { background: var(--brand); color: #fff; text-align: center; padding: 4rem 1rem; }
.hero h1 { margin: 0 0 .5rem; font-size: clamp(2rem, 5vw, 3rem); }
.tagline { font-size: 1.2rem; opacity: .9; }
.btn { display: inline-block; margin-top: 1rem; padding: .7rem 1.5rem; background: #fff; color: var(--brand); border-radius: 999px; text-decoration: none; font-weight: bold; }
main { max-width: 60rem; margin: 0 auto; padding: 2rem 1rem; }
.cards { list-style: none; padding: 0; display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); }
.card { background: var(--accent); padding: 1.25rem; border-radius: 12px; }
.card h3 { margin-top: 0; }
footer { text-align: center; padding: 1.5rem; color: var(--muted); border-top: 1px solid var(--line); }
'''
    return html, css


ptype(key="landing", title="Landing page for {name}", level=1,
      brief="Build a one-screen landing page: a coloured hero with the business name, tagline and a call-to-action button, a grid of three cards and a footer.",
      goals=["Use header, main, section and footer landmarks", "Centre content with max-width and margin auto", "Create a responsive card grid with one line of CSS Grid"],
      elements=["header", "h1", "p", "a", "main", "section", "h2", "ul", "li", "h3", "strong", "footer"],
      css=["background", "color", "padding", "border-radius", "display: grid", "grid-template-columns", "repeat(auto-fit, minmax())", "gap", "max-width"],
      steps=["Create index.html with the standard skeleton and link styles.css.", "Add the <header class=\"hero\"> with h1, tagline and a link styled as a button.",
             "Add <main> with a <section> containing a <ul class=\"cards\"> of three <li class=\"card\"> items.", "Add the footer with the copyright line.",
             "In styles.css set the CSS variables in :root, style the hero, then the grid.", "Resize the browser: the cards should go from three columns to one."],
      build=b_landing,
      checklist=["Exactly one h1", "Button link has descriptive text", "Cards wrap on narrow screens", "Footer text is readable (contrast)"],
      exercises=["Add a fourth card and check the grid still works.", "Change the hero to a background image with a dark overlay.", "Add a <nav> with three links inside the header."])


def b_nav(t):
    html = HEAD.format(title=t["name"] + " - Navigation") + f'''  <header class="site-header">
    <a class="logo" href="index.html">{t["name"]}</a>
    <nav aria-label="Main">
      <ul class="nav">
        <li><a href="index.html" aria-current="page">Home</a></li>
        <li><a href="{t["nouns"]}.html">{t["nouns"].capitalize()}</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <h1>Welcome to {t["name"]}</h1>
    <p>{t["tagline"]}.</p>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.site-header { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem; padding: .75rem 1.5rem; background: var(--brand); }
.logo { color: #fff; font-weight: bold; font-size: 1.25rem; text-decoration: none; }
.nav { display: flex; gap: .25rem; list-style: none; margin: 0; padding: 0; }
.nav a { display: block; padding: .5rem .9rem; color: #fff; text-decoration: none; border-radius: 6px; }
.nav a:hover, .nav a:focus-visible { background: rgb(255 255 255 / 20%); }
.nav a[aria-current="page"] { background: rgb(0 0 0 / 25%); }
main { padding: 2rem 1.5rem; }
'''
    return html, css


ptype(key="nav", title="Navigation bar for {name}", level=1,
      brief="Build a horizontal navigation bar from an unordered list, with a logo on the left, links on the right and a highlighted current page.",
      goals=["Turn a list into a horizontal menu with Flexbox", "Mark the current page with aria-current", "Style hover and keyboard focus states"],
      elements=["header", "a", "nav", "ul", "li", "main", "h1", "p"], css=["display: flex", "justify-content", "gap", "list-style", "text-decoration", ":hover", ":focus-visible", "attribute selector"],
      steps=["Write the header with a logo link and a <nav> containing a <ul> of links.", "Add aria-current=\"page\" to the link for the current page.",
             "Make the header a flex container with space-between.", "Remove list bullets and padding; make the list itself a flex row.",
             "Give each link padding and a hover/focus background.", "Tab through the links with the keyboard and confirm the focus style is visible."],
      build=b_nav, checklist=["Links are inside <nav> with an aria-label", "Bullets removed", "Current page visibly different", "Focus visible with keyboard"],
      exercises=["Make the menu wrap into two rows on narrow screens.", "Add a dropdown sub-menu with :hover and :focus-within.", "Make the header sticky."])


def b_pricing(t):
    rows = "\n".join(f'        <tr><th scope="row">{a}</th><td>{b}</td><td class="num">{c}</td></tr>' for a, b, c in t["items"])
    html = HEAD.format(title=t["name"] + " - Prices") + f'''  <main>
    <h1>{t["name"]} price list</h1>
    <div class="table-wrapper">
      <table>
        <caption>{t["nouns"].capitalize()} and prices, 2026</caption>
        <thead>
          <tr><th scope="col">{t["noun"].capitalize()}</th><th scope="col">Description</th><th scope="col">Price</th></tr>
        </thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 50rem; margin: 2rem auto; padding: 0 1rem; }
.table-wrapper { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; }
caption { text-align: left; padding: .5rem 0; color: var(--muted); }
th, td { padding: .75rem 1rem; text-align: left; border-bottom: 1px solid var(--line); }
thead th { background: var(--brand); color: #fff; }
tbody tr:nth-child(even) { background: var(--accent); }
tbody th { font-weight: 600; }
.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
'''
    return html, css


ptype(key="pricing", title="Price table for {name}", level=1,
      brief="Present the four main offers in an accessible data table with a caption, column and row headers, zebra stripes and a scroll wrapper for phones.",
      goals=["Structure a table with caption, thead, tbody, th scope", "Collapse borders and stripe rows", "Keep tables usable on small screens"],
      elements=["table", "caption", "thead", "tbody", "tr", "th", "td", "div"], css=["border-collapse", "padding", ":nth-child(even)", "text-align", "overflow-x", "white-space"],
      steps=["Write the table markup with a caption and a thead row of th scope=\"col\".", "Add one tbody row per offer; the first cell is th scope=\"row\".",
             "Wrap the table in <div class=\"table-wrapper\">.", "Collapse borders, add padding and a bottom border to cells.", "Colour the header row and stripe the even rows.",
             "Right-align the price column and stop it wrapping."],
      build=b_pricing, checklist=["Every header cell has scope", "Caption describes the table", "Table scrolls instead of overflowing on a phone", "Numbers right-aligned"],
      exercises=["Add a tfoot row with a total.", "Highlight a row on hover.", "Make the header row sticky with position: sticky."])


def b_contact(t):
    html = HEAD.format(title=t["name"] + " - Contact") + f'''  <main>
    <h1>Contact {t["name"]}</h1>
    <form action="/contact" method="post" class="form">
      <div class="row">
        <label for="name">Your name</label>
        <input id="name" name="name" type="text" required autocomplete="name">
      </div>
      <div class="row">
        <label for="email">Email</label>
        <input id="email" name="email" type="email" required autocomplete="email">
      </div>
      <div class="row">
        <label for="topic">Topic</label>
        <select id="topic" name="topic">
{items_li(t, 4, '<option>{0}</option>')}
          <option>Something else</option>
        </select>
      </div>
      <div class="row">
        <label for="msg">Message</label>
        <textarea id="msg" name="message" rows="5" required minlength="10"></textarea>
      </div>
      <button type="submit">Send message</button>
    </form>
    <address>{t["name"]}, {t["city"]} &middot; <a href="mailto:hello@{t["slug"]}.example">hello@{t["slug"]}.example</a></address>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 36rem; margin: 2rem auto; padding: 0 1rem; }
.form { display: grid; gap: 1rem; }
.row { display: grid; gap: .3rem; }
label { font-weight: 600; }
input, select, textarea, button { font: inherit; }
input, select, textarea { padding: .6rem .8rem; border: 1px solid #bbb; border-radius: 8px; width: 100%; }
input:focus-visible, select:focus-visible, textarea:focus-visible { outline: 3px solid #ffbf47; border-color: var(--brand); }
input:user-invalid, textarea:user-invalid { border-color: #c00; }
button { justify-self: start; padding: .7rem 1.4rem; background: var(--brand); color: #fff; border: 0; border-radius: 999px; cursor: pointer; }
address { margin-top: 2rem; font-style: normal; color: var(--muted); }
'''
    return html, css


ptype(key="contact", title="Contact form for {name}", level=1,
      brief="Build a contact form with text, email, select and textarea controls, proper labels, built-in validation and a styled submit button.",
      goals=["Connect every label to its control with for/id", "Use input types and required for free validation", "Style focus and invalid states"],
      elements=["form", "label", "input", "select", "option", "textarea", "button", "address", "a"], css=["display: grid", "gap", "font: inherit", ":focus-visible", ":user-invalid", "border-radius"],
      steps=["Create the form with action and method.", "Add one .row per field: a label followed by its control; match for and id.", "Use type=\"email\", required and minlength.",
             "Add the select with one option per offer.", "Style with Grid gaps; make controls full width and inherit the page font.", "Submit the empty form and watch the browser's validation messages."],
      build=b_contact, checklist=["Clicking a label focuses its control", "Empty submit is blocked", "Focus ring visible", "Address is real contact info, not italic"],
      exercises=["Add a checkbox for newsletter consent.", "Put name and email side by side on wide screens.", "Add a pattern attribute for an Egyptian phone number."])


def b_gallery(t):
    figs = "\n".join(f'      <figure><img src="images/{t["slug"]}-{i+1}.jpg" alt="{a}" width="600" height="400" loading="lazy"><figcaption>{a}</figcaption></figure>' for i, (a, b, c) in enumerate(t["items"]))
    html = HEAD.format(title=t["name"] + " - Gallery") + f'''  <main>
    <h1>{t["name"]} gallery</h1>
    <div class="gallery">
{figs}
    </div>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 64rem; margin: 2rem auto; padding: 0 1rem; }
.gallery { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr)); }
figure { margin: 0; background: var(--accent); border-radius: 12px; overflow: hidden; }
img { display: block; width: 100%; height: auto; aspect-ratio: 3 / 2; object-fit: cover; }
figcaption { padding: .6rem .9rem; font-size: .95rem; }
figure:hover img { transform: scale(1.03); }
img { transition: transform .3s; }
'''
    return html, css


ptype(key="gallery", title="Photo gallery for {name}", level=1,
      brief="Lay out four captioned photos in a responsive grid using figure and figcaption, with lazy loading and a gentle hover zoom.",
      goals=["Use figure/figcaption for captioned images", "Reserve space with width, height and aspect-ratio", "Crop images consistently with object-fit"],
      elements=["figure", "img", "figcaption", "div", "h1"], css=["grid-template-columns", "auto-fill", "aspect-ratio", "object-fit", "overflow: hidden", "transition", "transform"],
      steps=["Create an images folder with four photos (any JPEGs, renamed).", "Write one <figure> per photo with img and figcaption.", "Give every img alt text, width, height and loading=\"lazy\".",
             "Make .gallery a grid with auto-fill columns.", "Force a 3:2 shape with aspect-ratio and object-fit: cover.", "Add the hover zoom with transition and transform."],
      build=b_gallery, checklist=["All images have meaningful alt", "No layout jump while loading", "Grid reflows on narrow screens", "Zoom does not overflow the card"],
      exercises=["Make the first image span two columns with grid-column: span 2.", "Add a lightbox using <dialog>.", "Use <picture> to serve WebP."])


def b_about(t):
    html = HEAD.format(title="About " + t["name"]) + f'''  <main class="about">
    <article>
      <h1>About {t["name"]}</h1>
      <p class="lead">{t["tagline"]}, in the heart of {t["city"]}.</p>
      <img src="images/team.jpg" alt="{t["person"]} in front of {t["name"]}" width="800" height="500">
      <h2>Our story</h2>
      <p>{t["name"]} was founded by <strong>{t["person"]}</strong> with one idea: do a few things and do them well. Today our small team offers {len(t["items"])} core {t["nouns"]} and welcomes visitors from all over {t["city"]}.</p>
      <h2>What we value</h2>
      <ul>
        <li><strong>Quality.</strong> Every {t["noun"]} is checked twice.</li>
        <li><strong>Honesty.</strong> Clear prices, no surprises.</li>
        <li><strong>Community.</strong> We support local schools and clubs.</li>
      </ul>
      <blockquote>
        <p>We treat every visitor like a neighbour, because they usually are.</p>
        <footer>&mdash; <cite>{t["person"]}</cite></footer>
      </blockquote>
    </article>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.about { max-width: 42rem; margin: 2rem auto; padding: 0 1rem; font-family: Georgia, serif; font-size: 1.1rem; }
h1, h2 { font-family: system-ui, sans-serif; color: var(--brand); }
.lead { font-size: 1.3rem; color: var(--muted); }
img { max-width: 100%; height: auto; border-radius: 12px; }
li { margin-bottom: .5rem; }
blockquote { margin: 2rem 0; padding: 1rem 1.5rem; border-left: 5px solid var(--brand); background: var(--accent); }
blockquote p { margin: 0 0 .5rem; font-style: italic; }
'''
    return html, css


ptype(key="about", title="About page for {name}", level=1,
      brief="Write a readable long-form page: lead paragraph, image, headings, a value list with strong keywords and a quotation with attribution.",
      goals=["Choose text elements by meaning (strong, cite, blockquote)", "Set comfortable reading width and line length", "Mix a serif body with sans-serif headings"],
      elements=["article", "h1", "h2", "p", "img", "ul", "li", "strong", "blockquote", "footer", "cite"], css=["max-width", "font-family", "font-size", "border-left", "font-style"],
      steps=["Write the article content first, without any CSS.", "Add the image with alt text and dimensions.", "Mark values with <strong> at the start of each list item.",
             "Add the quotation with <blockquote>, a <footer> and <cite>.", "Limit the width to 42rem and set fonts.", "Style the blockquote with a coloured left border."],
      build=b_about, checklist=["Heading order h1 then h2", "Body line length under 75 characters", "Image responsive", "Quote source in cite"],
      exercises=["Add a <details> element with 'Opening hours'.", "Add a timeline as an ordered list.", "Add a second column with an <aside> on wide screens."])


def b_menu(t):
    items = "\n".join(f'      <div class="item"><dt>{a} <span class="price">{c}</span></dt><dd>{b}</dd></div>' for a, b, c in t["items"])
    html = HEAD.format(title=t["name"] + " - Menu") + f'''  <main>
    <h1>{t["name"]}</h1>
    <p class="sub">{t["nouns"].capitalize()} and prices</p>
    <dl class="menu">
{items}
    </dl>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 36rem; margin: 2rem auto; padding: 0 1rem; }
h1 { text-align: center; color: var(--brand); margin-bottom: 0; }
.sub { text-align: center; color: var(--muted); margin-top: 0; }
.menu { margin: 0; }
.item { padding: 1rem 0; border-bottom: 1px dashed var(--line); }
dt { display: flex; justify-content: space-between; font-weight: 700; font-size: 1.1rem; }
dt::after { content: ""; order: 1; flex: 1; border-bottom: 1px dotted var(--line); margin: 0 .5rem .35rem; }
.price { order: 2; color: var(--brand); }
dd { margin: .25rem 0 0; color: var(--muted); }
'''
    return html, css


ptype(key="menu", title="Menu list for {name}", level=2,
      brief="Present offers as a description list where each term shows a name and price joined by dotted leaders, with the description below.",
      goals=["Use dl/dt/dd for name-description pairs", "Create dotted price leaders with a flex pseudo-element", "Use the order property"],
      elements=["dl", "div", "dt", "dd", "span"], css=["display: flex", "justify-content", "::after", "order", "flex: 1", "border-bottom: dotted"],
      steps=["Write the <dl>; group each dt/dd pair in a <div>.", "Put the price in a <span class=\"price\"> inside the dt.", "Make dt a flex row.",
             "Add an empty ::after with flex: 1 and a dotted bottom border - this is the leader line.", "Use order so the leader sits between the name and the price.",
             "Add a dashed separator under each item."],
      build=b_menu, checklist=["Each dt has a dd", "Price stays on the right even for long names", "Leaders do not appear when the name is very long", "Readable on a phone"],
      exercises=["Group items under h2 categories.", "Add a 'chef's choice' badge with a ::before.", "Print stylesheet: remove colours."])


def b_faq(t):
    qs = [(f"How do I book a {t['noun']}?", f"Use the contact form or call us. Popular {t['nouns']} fill up quickly."),
          ("Where are you located?", f"We are in {t['city']}. Parking is available nearby."),
          ("Do you offer discounts?", "Students and groups of four or more get 10 percent off."),
          ("Can I cancel?", "Yes, up to 24 hours before, free of charge.")]
    ds = "\n".join(f'    <details{" open" if i == 0 else ""}>\n      <summary>{q}</summary>\n      <p>{a}</p>\n    </details>' for i, (q, a) in enumerate(qs))
    html = HEAD.format(title=t["name"] + " - FAQ") + f'''  <main>
    <h1>Frequently asked questions</h1>
{ds}
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 40rem; margin: 2rem auto; padding: 0 1rem; }
details { border: 1px solid var(--line); border-radius: 10px; margin-bottom: .75rem; background: #fff; }
summary { padding: .9rem 1.1rem; cursor: pointer; font-weight: 600; list-style: none; display: flex; justify-content: space-between; }
summary::-webkit-details-marker { display: none; }
summary::after { content: "+"; color: var(--brand); font-size: 1.3rem; line-height: 1; }
details[open] summary::after { content: "\\2212"; }
details[open] summary { border-bottom: 1px solid var(--line); background: var(--accent); }
details p { padding: 0 1.1rem 1rem; margin: .75rem 0 0; }
'''
    return html, css


ptype(key="faq", title="FAQ accordion for {name}", level=2,
      brief="Build an accordion of questions and answers with no JavaScript using details and summary, with a custom plus/minus indicator.",
      goals=["Use details/summary for native disclosure", "Style the open state with the [open] attribute selector", "Replace the default marker"],
      elements=["details", "summary", "p", "h1"], css=["[open]", "::after", "content", "list-style: none", "cursor: pointer", "border-radius"],
      steps=["Write one <details> per question; the question goes in <summary>.", "Add open to the first one so it starts expanded.", "Remove the default triangle marker.",
             "Add a plus sign with summary::after and a minus when open.", "Give the open summary a background and border.", "Click and use the keyboard (Tab, Enter) to test."],
      build=b_faq, checklist=["Summary is the first child", "Works with keyboard", "Only summary is clickable, not the answer", "Indicator changes when open"],
      exercises=["Use the name attribute so only one item can be open at once.", "Animate the opening with interpolate-size or a max-height transition.", "Add a search box that filters questions with JavaScript."])


def b_card(t):
    a, b, c = t["items"][0]
    html = HEAD.format(title=a + " - " + t["name"]) + f'''  <main>
    <article class="card">
      <img src="images/{t["slug"]}-1.jpg" alt="{a}" width="600" height="400">
      <div class="body">
        <p class="kicker">{t["noun"].capitalize()}</p>
        <h1>{a}</h1>
        <p>{b}.</p>
        <p class="price">{c}</p>
        <a class="btn" href="book.html">Book now</a>
      </div>
    </article>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { min-height: 100vh; display: grid; place-items: center; background: var(--accent); padding: 1rem; }
.card { max-width: 22rem; background: #fff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgb(0 0 0 / 12%); }
.card img { display: block; width: 100%; height: auto; }
.body { padding: 1.25rem; }
.kicker { text-transform: uppercase; letter-spacing: .08em; font-size: .75rem; color: var(--muted); margin: 0; }
h1 { margin: .25rem 0 .5rem; font-size: 1.4rem; }
.price { font-size: 1.3rem; font-weight: 700; color: var(--brand); }
.btn { display: block; text-align: center; padding: .7rem; background: var(--brand); color: #fff; border-radius: 10px; text-decoration: none; }
.btn:hover { filter: brightness(.9); }
'''
    return html, css


ptype(key="card", title="Product card for {name}", level=1,
      brief="Design a single product card: image on top, small uppercase label, title, description, price and a full-width button, centred on the page.",
      goals=["Centre a component with display: grid and place-items", "Build a shadowed card with rounded corners", "Use text-transform and letter-spacing for labels"],
      elements=["article", "img", "div", "p", "h1", "a"], css=["place-items: center", "box-shadow", "border-radius", "overflow: hidden", "text-transform", "letter-spacing", "filter"],
      steps=["Write the article with the image first, then a .body div.", "Add the kicker, title, description, price and button.", "Centre the card in main with grid and place-items.",
             "Round the card corners; hide overflow so the image follows the rounding.", "Add a soft box shadow.", "Darken the button slightly on hover with filter."],
      build=b_card, checklist=["Image corners rounded with the card", "Card is centred vertically and horizontally", "Button is full width", "Text contrast passes"],
      exercises=["Turn it into a grid of four cards.", "Add a 'sold out' ribbon positioned absolutely.", "Make the image and text side by side above 600px."])


def b_footer(t):
    html = HEAD.format(title=t["name"]) + f'''  <main>
    <h1>{t["name"]}</h1>
    <p>Scroll down to see the footer.</p>
  </main>
  <footer class="site-footer">
    <div class="cols">
      <section>
        <h2>{t["name"]}</h2>
        <p>{t["tagline"]}.</p>
      </section>
      <nav aria-label="Footer">
        <h2>{t["nouns"].capitalize()}</h2>
        <ul>
{items_li(t, 4, '<li><a href="#">{0}</a></li>')}
        </ul>
      </nav>
      <section>
        <h2>Contact</h2>
        <address>{t["city"]}, Egypt<br><a href="mailto:hello@{t["slug"]}.example">hello@{t["slug"]}.example</a><br><a href="tel:+20100000000">+20 100 000 0000</a></address>
      </section>
    </div>
    <p class="legal">&copy; 2026 {t["name"]} &middot; <a href="privacy.html">Privacy</a> &middot; <a href="#top">Back to top</a></p>
  </footer>
''' + FOOT
    css = BASE_CSS.format(**t) + '''body { min-height: 100vh; display: flex; flex-direction: column; }
main { flex: 1; padding: 2rem 1rem; }
.site-footer { background: #1b2431; color: #d5dbe5; padding: 2.5rem 1rem 1rem; }
.cols { max-width: 60rem; margin: 0 auto; display: grid; gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr)); }
.site-footer h2 { color: #fff; font-size: 1rem; text-transform: uppercase; letter-spacing: .06em; margin: 0 0 .75rem; }
.site-footer ul { list-style: none; padding: 0; margin: 0; }
.site-footer li { margin-bottom: .4rem; }
.site-footer a { color: #fff; }
address { font-style: normal; line-height: 1.8; }
.legal { max-width: 60rem; margin: 2rem auto 0; padding-top: 1rem; border-top: 1px solid #334155; font-size: .85rem; text-align: center; }
'''
    return html, css


ptype(key="footer", title="Site footer for {name}", level=1,
      brief="Build a three-column footer (about, links, contact) that stays at the bottom of short pages, with a legal line underneath.",
      goals=["Make a sticky footer with flex column body", "Use address for contact details", "Lay out columns with auto-fit grid"],
      elements=["footer", "section", "nav", "h2", "ul", "li", "a", "address", "br", "p"], css=["min-height: 100vh", "flex: 1", "grid", "text-transform", "border-top", "font-size"],
      steps=["Write main content followed by <footer class=\"site-footer\">.", "Inside, add a .cols div with three blocks: section, nav, section.", "Add the legal paragraph after .cols.",
             "Make body a flex column with min-height 100vh and main flex: 1 - this pushes the footer down.", "Grid the columns.", "Style headings small and uppercase; reset list styles."],
      build=b_footer, checklist=["Footer sits at the bottom even with little content", "Links are readable on the dark background", "address not italic", "Columns stack on phones"],
      exercises=["Add social media icons as SVG links.", "Add a newsletter form in a fourth column.", "Make the 'Back to top' link smooth-scroll with scroll-behavior."])


def b_hero_img(t):
    html = HEAD.format(title=t["name"]) + f'''  <header class="hero">
    <div class="content">
      <h1>{t["name"]}</h1>
      <p>{t["tagline"]}.</p>
      <a class="btn" href="#more">Learn more</a>
    </div>
  </header>
  <main id="more">
    <h2>Why choose us</h2>
    <p>Founded in {t["city"]} by {t["person"]}, we offer {t["nouns"]} that people come back for.</p>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.hero {
  min-height: 80vh; display: grid; place-items: center; text-align: center; color: #fff; padding: 2rem 1rem;
  background: linear-gradient(rgb(0 0 0 / 45%), rgb(0 0 0 / 45%)), url("images/hero.jpg") center / cover no-repeat;
}
.hero h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0; text-shadow: 0 2px 8px rgb(0 0 0 / 40%); }
.hero p { font-size: 1.25rem; }
.btn { display: inline-block; padding: .8rem 1.6rem; background: var(--brand); color: #fff; border-radius: 999px; text-decoration: none; }
main { max-width: 50rem; margin: 0 auto; padding: 3rem 1rem; }
'''
    return html, css


ptype(key="hero", title="Full-screen hero banner for {name}", level=2,
      brief="Build a hero section that fills most of the screen with a background photo, a dark overlay for contrast, centred text and a button.",
      goals=["Layer a gradient overlay over a background image", "Size with viewport units", "Scale headings fluidly with clamp()"],
      elements=["header", "div", "h1", "p", "a", "main", "h2"], css=["background shorthand", "linear-gradient", "background-size: cover", "min-height: 80vh", "place-items", "clamp()", "text-shadow"],
      steps=["Save a wide photo as images/hero.jpg.", "Write the header with a .content block.", "Set min-height: 80vh and centre with grid/place-items.",
             "Set the background with a linear-gradient overlay first, then the image.", "Use clamp() for the h1 size.", "Check text contrast; darken the overlay if needed."],
      build=b_hero_img, checklist=["Text readable over any part of the image", "Image covers without distortion", "Heading scales between phone and desktop", "Button reachable by keyboard"],
      exercises=["Add a second button with an outline style.", "Add a scroll-down arrow animated with @keyframes.", "Use <picture> in the HTML instead of a CSS background for better loading."])


def b_team(t):
    people = [(t["person"], "Founder"), ("Nadia Fawzy", "Manager"), ("Ali Hassan", "Specialist"), ("Mona Zaki", "Customer care")]
    cards = "\n".join(f'      <li class="member"><img src="images/person-{i+1}.jpg" alt="" width="200" height="200"><h2>{n}</h2><p>{r}</p></li>' for i, (n, r) in enumerate(people))
    html = HEAD.format(title=t["name"] + " - Team") + f'''  <main>
    <h1>Meet the team</h1>
    <ul class="team">
{cards}
    </ul>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 60rem; margin: 2rem auto; padding: 0 1rem; text-align: center; }
.team { list-style: none; padding: 0; display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr)); }
.member img { width: 9rem; height: 9rem; border-radius: 50%; object-fit: cover; border: 4px solid var(--accent); }
.member h2 { font-size: 1.05rem; margin: .75rem 0 .1rem; }
.member p { margin: 0; color: var(--muted); }
'''
    return html, css


ptype(key="team", title="Team page for {name}", level=1,
      brief="Show four team members with circular photos, names and roles in a centred responsive grid.",
      goals=["Make circular avatars with border-radius: 50% and object-fit", "Use decorative empty alt when the name is next to the photo", "Centre text in a grid"],
      elements=["ul", "li", "img", "h2", "p"], css=["border-radius: 50%", "object-fit: cover", "border", "text-align: center", "grid"],
      steps=["Write a <ul class=\"team\"> with one <li> per person.", "Add square photos with alt=\"\" (the name follows as text).", "Add h2 for the name and p for the role.",
             "Grid the list with auto-fit.", "Make the images 9rem circles with object-fit: cover.", "Add a coloured ring with border."],
      build=b_team, checklist=["Photos are perfect circles even if the source is not square", "Names are headings", "Grid wraps", "Alt is empty because the name is visible text"],
      exercises=["Add a short bio with <details>.", "Add social links under each name.", "Add a hover effect that lifts the card."])


def b_testimonials(t):
    quotes = [("The best " + t["noun"] + " experience in " + t["city"] + ".", "Heba M."), ("Friendly staff and fair prices.", "Ziad K."), ("I recommend them to everyone.", "Rania S.")]
    figs = "\n".join(f'      <figure>\n        <blockquote><p>{q}</p></blockquote>\n        <figcaption>{n} <span class="stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span></figcaption>\n      </figure>' for q, n in quotes)
    html = HEAD.format(title=t["name"] + " - Reviews") + f'''  <main>
    <h1>What customers say about {t["name"]}</h1>
    <div class="quotes">
{figs}
    </div>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 60rem; margin: 2rem auto; padding: 0 1rem; }
.quotes { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); }
figure { margin: 0; padding: 1.5rem; background: var(--accent); border-radius: 14px; position: relative; }
figure::before { content: "\\201C"; position: absolute; top: -.2em; left: .4rem; font-size: 5rem; color: var(--brand); opacity: .25; font-family: Georgia, serif; }
blockquote { margin: 0 0 1rem; font-size: 1.1rem; font-style: italic; }
figcaption { font-weight: 600; }
.stars { color: #f59e0b; margin-left: .5rem; }
'''
    return html, css


ptype(key="testimonials", title="Testimonials section for {name}", level=2,
      brief="Show three customer quotes as cards with a large decorative quotation mark, the customer's name and a star rating.",
      goals=["Mark up quotes correctly with figure, blockquote and figcaption", "Position a decorative ::before", "Label icon-only content with aria-label"],
      elements=["figure", "blockquote", "p", "figcaption", "span"], css=["position: relative/absolute", "::before", "content", "opacity", "font-style", "grid"],
      steps=["Write one <figure> per review: blockquote with the text, figcaption with the name.", "Add the stars in a span with an aria-label.", "Grid the figures.",
             "Set figure position: relative.", "Add the big quotation mark with ::before positioned absolutely.", "Colour the stars."],
      build=b_testimonials, checklist=["Attribution is outside the blockquote", "Stars have a text alternative", "Quote mark does not overlap text badly", "Cards equal height"],
      exercises=["Add photos of the customers.", "Turn the section into a horizontal scroll-snap carousel.", "Add schema.org Review microdata."])


def b_signup(t):
    html = HEAD.format(title=t["name"] + " - Newsletter") + f'''  <main>
    <section class="signup">
      <h1>Get {t["name"]} news</h1>
      <p>New {t["nouns"]}, offers and events. One email a month, no spam.</p>
      <form action="/subscribe" method="post">
        <label for="email" class="sr-only">Email address</label>
        <input id="email" name="email" type="email" placeholder="you@example.com" required autocomplete="email">
        <button type="submit">Subscribe</button>
      </form>
      <p class="small">By subscribing you agree to our <a href="privacy.html">privacy policy</a>.</p>
    </section>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { min-height: 100vh; display: grid; place-items: center; padding: 1rem; background: var(--brand); }
.signup { background: #fff; padding: 2.5rem; border-radius: 18px; max-width: 30rem; text-align: center; }
form { display: flex; gap: .5rem; flex-wrap: wrap; }
input { flex: 1 1 12rem; padding: .8rem 1rem; border: 1px solid #bbb; border-radius: 999px; font: inherit; }
button { padding: .8rem 1.4rem; border: 0; border-radius: 999px; background: var(--brand); color: #fff; font: inherit; cursor: pointer; }
.small { font-size: .8rem; color: var(--muted); }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
'''
    return html, css


ptype(key="signup", title="Newsletter sign-up box for {name}", level=1,
      brief="Create a centred sign-up card with a single email field and button on one line, a visually hidden label and a privacy note.",
      goals=["Hide a label visually but keep it for screen readers", "Put input and button on one line with Flexbox and let them wrap", "Use placeholder correctly (hint, not label)"],
      elements=["section", "form", "label", "input", "button", "p", "a"], css=["flex: 1 1 12rem", "flex-wrap", ".sr-only pattern", "border-radius: 999px", "place-items"],
      steps=["Write the section with heading, text, form and note.", "Add a label with class sr-only before the input.", "Use type=\"email\" and required.",
             "Make the form a flex row that wraps.", "Give the input flex: 1 1 12rem so it grows but wraps below 12rem.", "Centre the card on a coloured page."],
      build=b_signup, checklist=["Screen reader announces 'Email address'", "Placeholder disappears when typing; label does not", "Button wraps under the input on very narrow screens", "Contrast of white card on brand colour"],
      exercises=["Add a success message with the :valid state.", "Add a checkbox for consent.", "Animate the card entrance with @keyframes."])


def b_sidebar(t):
    html = HEAD.format(title=t["name"] + " - Guide") + f'''  <div class="layout">
    <header class="top"><h1>{t["name"]} guide</h1></header>
    <nav class="side" aria-label="Sections">
      <ul>
{items_li(t, 4, '<li><a href="#s{0}">{0}</a></li>')}
      </ul>
    </nav>
    <main class="content">
{chr(10).join(f'      <section id="s{a}"><h2>{a}</h2><p>{b}. Price: {c}.</p></section>' for a, b, c in t["items"])}
    </main>
    <footer class="bottom">&copy; 2026 {t["name"]}</footer>
  </div>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.layout { min-height: 100vh; display: grid; grid-template-rows: auto 1fr auto; grid-template-columns: 1fr; grid-template-areas: "top" "side" "content" "bottom"; }
.top { grid-area: top; background: var(--brand); color: #fff; padding: 1rem 1.5rem; }
.top h1 { margin: 0; font-size: 1.3rem; }
.side { grid-area: side; background: var(--accent); padding: 1rem; }
.side ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: .5rem; }
.side a { display: block; padding: .4rem .7rem; border-radius: 6px; text-decoration: none; color: var(--ink); background: #fff; }
.content { grid-area: content; padding: 1.5rem; max-width: 50rem; }
.bottom { grid-area: bottom; padding: 1rem 1.5rem; border-top: 1px solid var(--line); color: var(--muted); }
@media (min-width: 800px) {
  .layout { grid-template-columns: 16rem 1fr; grid-template-areas: "top top" "side content" "bottom bottom"; }
  .side ul { flex-direction: column; }
  .side { position: sticky; top: 0; align-self: start; height: 100vh; }
}
'''
    return html, css


ptype(key="sidebar", title="Sidebar layout for {name}", level=2,
      brief="Build a documentation-style page: header, left sidebar of section links, content and footer, using named grid areas that rearrange at 800px.",
      goals=["Use grid-template-areas for whole-page layout", "Change the areas in a media query", "Make the sidebar sticky on wide screens"],
      elements=["div", "header", "nav", "ul", "li", "a", "main", "section", "footer"], css=["grid-template-areas", "grid-area", "@media (min-width)", "position: sticky", "align-self: start"],
      steps=["Write the four regions inside a .layout div.", "Give each region a grid-area name.", "Mobile first: one column, areas stacked.",
             "At 800px switch to two columns with side and content side by side.", "Turn the sidebar link list into a column on desktop.", "Make the sidebar sticky."],
      build=b_sidebar, checklist=["Areas string has equal columns per row", "Anchor links jump to sections", "Sticky sidebar does not cover the footer", "Mobile shows links as a wrapped row"],
      exercises=["Highlight the current section link with :target.", "Add a right column for 'on this page'.", "Collapse the sidebar with a checkbox toggle."])


def b_login(t):
    html = HEAD.format(title=t["name"] + " - Sign in") + f'''  <main>
    <form class="login" action="/login" method="post">
      <h1>Sign in to {t["name"]}</h1>
      <label for="user">Email</label>
      <input id="user" name="email" type="email" required autocomplete="username">
      <label for="pass">Password</label>
      <input id="pass" name="password" type="password" required minlength="8" autocomplete="current-password">
      <label class="check"><input type="checkbox" name="remember"> Remember me</label>
      <button type="submit">Sign in</button>
      <p><a href="forgot.html">Forgot your password?</a></p>
    </form>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { min-height: 100vh; display: grid; place-items: center; background: var(--accent); padding: 1rem; }
.login { width: min(100%, 22rem); background: #fff; padding: 2rem; border-radius: 14px; box-shadow: 0 8px 24px rgb(0 0 0 / 10%); display: grid; gap: .4rem; }
h1 { font-size: 1.3rem; margin: 0 0 1rem; text-align: center; }
label { font-weight: 600; font-size: .9rem; }
input:not([type="checkbox"]) { padding: .65rem .8rem; border: 1px solid #bbb; border-radius: 8px; font: inherit; margin-bottom: .6rem; }
.check { display: flex; align-items: center; gap: .4rem; font-weight: 400; }
button { margin-top: .5rem; padding: .75rem; border: 0; border-radius: 8px; background: var(--brand); color: #fff; font: inherit; cursor: pointer; }
p { text-align: center; font-size: .9rem; }
'''
    return html, css


ptype(key="login", title="Login form for {name}", level=1,
      brief="Build a compact sign-in card with email, password, remember-me checkbox and a link, using the correct autocomplete tokens so password managers work.",
      goals=["Use autocomplete=\"username\" and \"current-password\"", "Wrap a checkbox in its label", "Size a card with min()"],
      elements=["form", "h1", "label", "input", "button", "p", "a"], css=["width: min()", "box-shadow", ":not()", "display: flex", "align-items"],
      steps=["Write the form with labels before each input.", "Add autocomplete tokens and minlength on the password.", "Wrap the checkbox inside its label.",
             "Make the form a grid with small gaps.", "Exclude the checkbox from the input styling with :not([type=checkbox]).", "Centre the card."],
      build=b_login, checklist=["Browser offers to save the password", "Checkbox label is clickable", "Card never wider than 22rem", "Password minimum length enforced"],
      exercises=["Add a show/hide password button.", "Add a 'Sign in with...' divider using ::before/::after lines.", "Show a friendly error message region with aria-live."])


def b_timeline(t):
    events = [("2018", f"{t['person']} opens {t['name']} in {t['city']}."), ("2020", "Online ordering launched."), ("2023", f"Second location and new {t['nouns']}."), ("2026", "This website goes live.")]
    lis = "\n".join(f'      <li><time datetime="{y}">{y}</time><p>{d}</p></li>' for y, d in events)
    html = HEAD.format(title=t["name"] + " - History") + f'''  <main>
    <h1>Our history</h1>
    <ol class="timeline">
{lis}
    </ol>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 40rem; margin: 2rem auto; padding: 0 1rem; }
.timeline { list-style: none; padding: 0 0 0 2rem; margin: 0; position: relative; }
.timeline::before { content: ""; position: absolute; left: .55rem; top: .3rem; bottom: .3rem; width: 3px; background: var(--line); }
.timeline li { position: relative; padding-bottom: 1.5rem; }
.timeline li::before { content: ""; position: absolute; left: -1.85rem; top: .35rem; width: 1rem; height: 1rem; border-radius: 50%; background: var(--brand); border: 3px solid #fff; box-shadow: 0 0 0 2px var(--brand); }
time { font-weight: 700; color: var(--brand); }
.timeline p { margin: .2rem 0 0; }
'''
    return html, css


ptype(key="timeline", title="Vertical timeline for {name}", level=2,
      brief="Show the business history as an ordered list drawn as a vertical timeline with a line and dots, using only pseudo-elements.",
      goals=["Use <ol> and <time> for dated events", "Draw a line and markers with ::before", "Combine relative and absolute positioning"],
      elements=["ol", "li", "time", "p"], css=["position: relative", "position: absolute", "::before", "border-radius: 50%", "box-shadow ring"],
      steps=["Write an <ol class=\"timeline\"> with a <time> and <p> per event.", "Remove bullets and add left padding for the line.", "Draw the vertical line with .timeline::before.",
             "Draw a dot per item with li::before positioned to the left.", "Style the year.", "Check the datetime attributes are valid."],
      build=b_timeline, checklist=["Events in chronological order", "Line runs from first dot to last", "Dots centred on the line", "Works when text wraps"],
      exercises=["Alternate items left and right on wide screens.", "Animate dots appearing with animation-timeline: view().", "Add images to some events."])


def b_dashboard(t):
    stats = [("Visitors today", "1,284"), (t["nouns"].capitalize() + " sold", "57"), ("Revenue", "18,450 EGP"), ("Rating", "4.8 / 5")]
    cards = "\n".join(f'      <article class="stat"><h2>{a}</h2><p class="value">{b}</p></article>' for a, b in stats)
    html = HEAD.format(title=t["name"] + " - Dashboard") + f'''  <main>
    <h1>{t["name"]} dashboard</h1>
    <div class="stats">
{cards}
    </div>
    <section class="panel">
      <h2>Recent orders</h2>
      <table>
        <thead><tr><th>Order</th><th>{t["noun"].capitalize()}</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>#1041</td><td>{t["items"][0][0]}</td><td><span class="badge ok">Paid</span></td></tr>
          <tr><td>#1040</td><td>{t["items"][1][0]}</td><td><span class="badge wait">Pending</span></td></tr>
          <tr><td>#1039</td><td>{t["items"][2][0]}</td><td><span class="badge ok">Paid</span></td></tr>
        </tbody>
      </table>
    </section>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''body { background: #f3f4f6; }
main { max-width: 64rem; margin: 0 auto; padding: 1.5rem 1rem; }
.stats { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr)); }
.stat { background: #fff; padding: 1rem 1.25rem; border-radius: 12px; border-top: 4px solid var(--brand); }
.stat h2 { font-size: .85rem; color: var(--muted); margin: 0; text-transform: uppercase; letter-spacing: .05em; }
.value { font-size: 1.8rem; font-weight: 700; margin: .25rem 0 0; }
.panel { background: #fff; border-radius: 12px; padding: 1.25rem; margin-top: 1.5rem; }
table { width: 100%; border-collapse: collapse; }
th, td { text-align: left; padding: .6rem; border-bottom: 1px solid var(--line); }
.badge { padding: .15rem .6rem; border-radius: 999px; font-size: .8rem; font-weight: 600; }
.ok { background: #dcfce7; color: #166534; }
.wait { background: #fef9c3; color: #854d0e; }
'''
    return html, css


ptype(key="dashboard", title="Statistics dashboard for {name}", level=2,
      brief="Build an admin-style dashboard: four statistic cards with a coloured top border and a panel containing a recent-orders table with status badges.",
      goals=["Present numbers in cards with small uppercase labels", "Create pill-shaped status badges", "Combine grid cards and a table"],
      elements=["article", "h2", "p", "section", "table", "thead", "tbody", "span"], css=["border-top", "text-transform", "letter-spacing", "border-radius: 999px", "grid auto-fit"],
      steps=["Write four .stat articles inside .stats.", "Add the panel with a small table.", "Wrap statuses in <span class=\"badge ok|wait\">.",
             "Grid the cards.", "Style the badges as pills with soft background colours.", "Give the page a light grey background so white panels stand out."],
      build=b_dashboard, checklist=["Stat labels are headings", "Table has header cells", "Badge colours pass contrast", "Cards wrap on phones"],
      exercises=["Add a simple bar chart made of divs with widths in percent.", "Add a sidebar navigation.", "Add a dark theme with prefers-color-scheme."])


def b_404(t):
    html = HEAD.format(title="Page not found - " + t["name"]) + f'''  <main class="nf">
    <p class="code">404</p>
    <h1>We can't find that page</h1>
    <p>The link may be old or the address mistyped. Try one of these instead:</p>
    <ul>
      <li><a href="index.html">{t["name"]} home</a></li>
      <li><a href="{t["nouns"]}.html">All {t["nouns"]}</a></li>
      <li><a href="contact.html">Contact us</a></li>
    </ul>
    <form action="/search" role="search">
      <label for="q">Search the site</label>
      <input id="q" name="q" type="search">
      <button>Search</button>
    </form>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.nf { min-height: 100vh; display: grid; place-content: center; text-align: center; padding: 2rem 1rem; }
.code { font-size: clamp(5rem, 20vw, 10rem); font-weight: 800; color: var(--accent); -webkit-text-stroke: 2px var(--brand); margin: 0; line-height: 1; }
h1 { margin: 0 0 .5rem; }
ul { list-style: none; padding: 0; display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
form { margin-top: 1.5rem; display: flex; gap: .5rem; justify-content: center; flex-wrap: wrap; align-items: center; }
input { padding: .6rem; border: 1px solid #bbb; border-radius: 8px; }
button { padding: .6rem 1rem; border: 0; border-radius: 8px; background: var(--brand); color: #fff; }
'''
    return html, css


ptype(key="404", title="404 error page for {name}", level=1,
      brief="Design a friendly 'page not found' screen with a huge outlined 404, helpful links and a search box.",
      goals=["Centre a block with place-content", "Use huge fluid type with clamp()", "Provide useful next steps on error pages"],
      elements=["main", "p", "h1", "ul", "li", "a", "form", "label", "input", "button"], css=["place-content: center", "clamp()", "-webkit-text-stroke", "line-height", "flex-wrap"],
      steps=["Write the page: code, heading, links and search form.", "Set role=\"search\" on the form.", "Centre everything with grid and place-content.",
             "Make the 404 huge with clamp() and outline it with text-stroke.", "Lay out links and the form horizontally with wrapping.", "Name the file 404.html and configure your host to use it."],
      build=b_404, checklist=["The h1 says what happened in plain words", "Links go to real pages", "Search input has a label", "Looks fine at 320px wide"],
      exercises=["Add an illustration as inline SVG.", "Animate the 404 with a subtle float.", "Add a 'report broken link' mailto with the current URL from JavaScript."])


def b_blog(t):
    a, b, c = t["items"][0]
    html = HEAD.format(title=f"Why we love {a} - {t['name']} blog") + f'''  <main>
    <article class="post">
      <header>
        <p class="meta"><time datetime="2026-09-01">1 September 2026</time> &middot; by {t["person"]} &middot; 4 min read</p>
        <h1>Why we love {a}</h1>
        <p class="lead">{b}. Here is the story behind one of our favourite {t["nouns"]}.</p>
      </header>
      <figure>
        <img src="images/{t["slug"]}-1.jpg" alt="{a}" width="1200" height="700">
        <figcaption>{a}, photographed in {t["city"]}.</figcaption>
      </figure>
      <h2>How it started</h2>
      <p>When {t["name"]} opened, {a} was not on the list. A customer asked for it, we tried, and it has been our best seller ever since.</p>
      <h2>What makes it special</h2>
      <p>Three things: care, time and good ingredients. We never rush a {t["noun"]}.</p>
      <aside class="callout"><strong>Tip:</strong> Ask for it early in the day, it sells out by the afternoon.</aside>
      <h2>Try it yourself</h2>
      <p>{a} is available now for {c}. <a href="{t["nouns"]}.html">See all {t["nouns"]}</a>.</p>
      <footer class="tags">Tags: <a href="#">{t["slug"]}</a> <a href="#">news</a></footer>
    </article>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 44rem; margin: 2rem auto; padding: 0 1rem; }
.post { font-family: Georgia, serif; font-size: 1.1rem; }
h1, h2 { font-family: system-ui, sans-serif; line-height: 1.2; }
h1 { font-size: clamp(1.8rem, 4vw, 2.6rem); margin: .2rem 0 .5rem; }
.meta { color: var(--muted); font-family: system-ui, sans-serif; font-size: .9rem; }
.lead { font-size: 1.25rem; color: var(--muted); }
figure { margin: 2rem 0; }
img { width: 100%; height: auto; border-radius: 12px; }
figcaption { font-size: .9rem; color: var(--muted); font-family: system-ui, sans-serif; margin-top: .4rem; }
.callout { background: var(--accent); border-left: 4px solid var(--brand); padding: 1rem 1.25rem; margin: 1.5rem 0; border-radius: 0 10px 10px 0; }
.tags { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--line); font-family: system-ui, sans-serif; font-size: .9rem; }
.tags a { display: inline-block; background: var(--accent); padding: .1rem .6rem; border-radius: 999px; text-decoration: none; color: var(--ink); margin-right: .3rem; }
'''
    return html, css


ptype(key="blog", title="Blog article for {name}", level=2,
      brief="Write a full blog post with article header metadata, lead paragraph, hero figure, sections, a callout aside and tags in the footer.",
      goals=["Use article, header, footer, aside and time inside a post", "Set up readable long-form typography", "Style a callout and tag pills"],
      elements=["article", "header", "time", "h1", "p", "figure", "img", "figcaption", "h2", "aside", "strong", "footer", "a"], css=["font-family pairs", "clamp()", "border-left", "border-radius partial", "display: inline-block"],
      steps=["Write the article structure with header (meta, h1, lead).", "Add the figure with caption.", "Write two or three h2 sections.",
             "Add the callout aside and the tag footer.", "Set serif body / sans headings and a 44rem measure.", "Style the callout and tags."],
      build=b_blog, checklist=["Date has a datetime attribute", "One h1, then h2s", "Figure caption present", "Line length comfortable"],
      exercises=["Add a table of contents generated from the h2 ids.", "Add an author box with an image.", "Add 'related posts' cards at the end."])


def b_schedule(t):
    days = ["Sat", "Sun", "Mon", "Tue", "Wed"]
    rows = ""
    for i, (a, b, c) in enumerate(t["items"]):
        cells = "".join(f"<td>{a if (i + d) % 2 == 0 else ''}</td>" for d in range(5))
        rows += f'          <tr><th scope="row">{9 + i * 2}:00</th>{cells}</tr>\n'
    html = HEAD.format(title=t["name"] + " - Weekly schedule") + f'''  <main>
    <h1>Weekly schedule</h1>
    <div class="wrap">
      <table class="schedule">
        <caption>{t["nouns"].capitalize()} by day and time</caption>
        <thead><tr><th scope="col">Time</th>{"".join(f'<th scope="col">{d}</th>' for d in days)}</tr></thead>
        <tbody>
{rows}        </tbody>
      </table>
    </div>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 60rem; margin: 2rem auto; padding: 0 1rem; }
.wrap { overflow-x: auto; }
.schedule { border-collapse: separate; border-spacing: 4px; width: 100%; min-width: 36rem; }
.schedule th { background: var(--brand); color: #fff; padding: .5rem; border-radius: 6px; }
.schedule tbody th { background: var(--accent); color: var(--ink); }
.schedule td { padding: .6rem; border-radius: 6px; text-align: center; background: #f6f6f6; min-height: 3rem; }
.schedule td:not(:empty) { background: var(--accent); font-weight: 600; border: 2px solid var(--brand); }
'''
    return html, css


ptype(key="schedule", title="Weekly schedule grid for {name}", level=2,
      brief="Build a timetable as a table with separate, rounded cells where booked slots are highlighted with :not(:empty).",
      goals=["Use the separate border model with border-spacing", "Highlight cells based on content with :empty", "Keep a wide table scrollable"],
      elements=["table", "caption", "thead", "tbody", "tr", "th", "td"], css=["border-collapse: separate", "border-spacing", ":not(:empty)", "border-radius on cells", "min-width"],
      steps=["Write the header row with the days.", "Write one row per time slot; the first cell is th scope=\"row\".", "Leave empty <td></td> for free slots.",
             "Use border-collapse: separate and border-spacing so cells look like tiles.", "Style non-empty cells with :not(:empty).", "Wrap for horizontal scrolling."],
      build=b_schedule, checklist=["Every cell exists even if empty", "Row and column headers have scope", "Tiles have rounded corners", "Table scrolls on narrow screens"],
      exercises=["Add rowspan for a two-hour slot.", "Colour by category with classes.", "Make the time column sticky with position: sticky; left: 0."])


def b_cv(t):
    html = HEAD.format(title=t["person"] + " - CV") + f'''  <main class="cv">
    <header>
      <h1>{t["person"]}</h1>
      <p class="role">Founder, {t["name"]} &middot; {t["city"]}</p>
      <p class="links"><a href="mailto:{t["slug"]}@example.com">Email</a> &middot; <a href="tel:+20100000000">Phone</a> &middot; <a href="https://example.com">Website</a></p>
    </header>
    <section>
      <h2>Experience</h2>
      <article>
        <h3>Founder, {t["name"]}</h3>
        <p class="when"><time datetime="2018">2018</time> - present</p>
        <ul><li>Grew the business to {len(t["items"])} core {t["nouns"]}.</li><li>Built a loyal customer base in {t["city"]}.</li></ul>
      </article>
      <article>
        <h3>Assistant manager, Local Company</h3>
        <p class="when"><time datetime="2014">2014</time> - <time datetime="2018">2018</time></p>
        <ul><li>Managed a team of six.</li></ul>
      </article>
    </section>
    <section>
      <h2>Skills</h2>
      <ul class="skills"><li>Customer service</li><li>Planning</li><li>HTML and CSS</li><li>Arabic and English</li></ul>
    </section>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.cv { max-width: 46rem; margin: 2rem auto; padding: 0 1rem; }
header { border-bottom: 3px solid var(--brand); padding-bottom: 1rem; margin-bottom: 1.5rem; }
h1 { margin: 0; }
.role { margin: .2rem 0; color: var(--muted); }
h2 { color: var(--brand); text-transform: uppercase; font-size: 1rem; letter-spacing: .08em; margin-top: 1.5rem; }
h3 { margin: 1rem 0 0; }
.when { margin: 0; color: var(--muted); font-size: .9rem; }
.skills { list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: .5rem; }
.skills li { background: var(--accent); padding: .3rem .8rem; border-radius: 999px; }
@media print { a { color: inherit; text-decoration: none; } .cv { max-width: none; } }
'''
    return html, css


ptype(key="cv", title="CV / resume page for {person}", level=2,
      brief="Lay out a one-page CV with header, experience entries using article and time, and a skills list as pills, with a print stylesheet.",
      goals=["Structure a CV semantically", "Style skill tags with Flexbox wrapping", "Add @media print rules"],
      elements=["header", "h1", "p", "a", "section", "article", "h3", "time", "ul", "li"], css=["border-bottom", "text-transform", "letter-spacing", "flex-wrap", "@media print"],
      steps=["Write the header with name, role and contact links.", "Add an Experience section with one article per job.", "Use <time> for the years.",
             "Add a Skills list.", "Style section headings small and uppercase.", "Print preview (Ctrl+P) and adjust the print rules."],
      build=b_cv, checklist=["Contact links work (mailto, tel)", "Jobs in reverse chronological order", "Skills wrap", "Prints on one page without colours"],
      exercises=["Add a two-column layout for print with CSS columns.", "Add an Education section.", "Add a downloadable PDF link."])


def b_event(t):
    html = HEAD.format(title=t["name"] + " open day") + f'''  <main>
    <article class="event">
      <p class="date"><time datetime="2026-10-15T18:00">Thursday 15 October 2026, 18:00</time></p>
      <h1>{t["name"]} open day</h1>
      <p class="lead">Come and try our {t["nouns"]} for free, meet {t["person"]} and enjoy live music.</p>
      <dl class="facts">
        <dt>Where</dt><dd>{t["name"]}, {t["city"]}</dd>
        <dt>Price</dt><dd>Free, registration required</dd>
        <dt>Duration</dt><dd>3 hours</dd>
      </dl>
      <h2>Programme</h2>
      <ol>
        <li><b>18:00</b> Doors open</li>
        <li><b>18:30</b> Welcome talk</li>
        <li><b>19:00</b> Try the {t["nouns"]}</li>
        <li><b>20:30</b> Prize draw</li>
      </ol>
      <a class="btn" href="register.html">Register now</a>
    </article>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 44rem; margin: 2rem auto; padding: 0 1rem; }
.date { color: var(--brand); font-weight: 700; margin: 0; }
h1 { margin: .2rem 0; }
.lead { font-size: 1.2rem; }
.facts { display: grid; grid-template-columns: max-content 1fr; gap: .4rem 1.5rem; background: var(--accent); padding: 1rem 1.25rem; border-radius: 10px; }
dt { font-weight: 700; }
dd { margin: 0; }
ol { padding-left: 1.2rem; }
ol li { margin-bottom: .4rem; }
.btn { display: inline-block; padding: .8rem 1.6rem; background: var(--brand); color: #fff; border-radius: 999px; text-decoration: none; }
'''
    return html, css


ptype(key="event", title="Event page for {name}", level=1,
      brief="Announce an event with a machine-readable date, key facts in a two-column description list, a numbered programme and a register button.",
      goals=["Use <time> with a full datetime", "Lay out dl as a two-column grid", "Use ol for a sequence"],
      elements=["article", "time", "h1", "p", "dl", "dt", "dd", "h2", "ol", "li", "b", "a"], css=["grid-template-columns: max-content 1fr", "gap (two values)", "border-radius", "padding-left"],
      steps=["Write the date first with <time datetime=\"2026-10-15T18:00\">.", "Add heading and lead.", "Add the facts list and programme.",
             "Grid the dl: dt in the first column, dd in the second.", "Style the button.", "Validate the datetime format."],
      build=b_event, checklist=["datetime is ISO format", "dt/dd pairs align", "Programme is an ordered list", "Button text is an action"],
      exercises=["Add an 'Add to calendar' .ics link.", "Add a map with an iframe.", "Add a countdown with JavaScript."])


def b_invoice(t):
    rows = "\n".join(f'        <tr><td>{a}</td><td class="n">1</td><td class="n">{c}</td></tr>' for a, b, c in t["items"][:3])
    html = HEAD.format(title="Invoice 2026-041 - " + t["name"]) + f'''  <main class="invoice">
    <header>
      <div><h1>{t["name"]}</h1><p>{t["city"]}, Egypt</p></div>
      <div class="meta"><p><b>Invoice</b> 2026-041</p><p><b>Date</b> <time datetime="2026-09-11">11 Sep 2026</time></p></div>
    </header>
    <p><b>Bill to:</b> Customer name, {t["city"]}</p>
    <table>
      <thead><tr><th>Item</th><th class="n">Qty</th><th class="n">Price</th></tr></thead>
      <tbody>
{rows}
      </tbody>
      <tfoot><tr><th colspan="2">Total</th><td class="n">see items</td></tr></tfoot>
    </table>
    <p class="thanks">Thank you for your business.</p>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.invoice { max-width: 46rem; margin: 2rem auto; padding: 2rem; border: 1px solid var(--line); }
header { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 1rem; border-bottom: 3px solid var(--brand); padding-bottom: 1rem; }
h1 { margin: 0; color: var(--brand); }
.meta p { margin: .1rem 0; text-align: right; }
table { width: 100%; border-collapse: collapse; margin-top: 1.5rem; }
th, td { padding: .6rem; border-bottom: 1px solid var(--line); text-align: left; }
.n { text-align: right; font-variant-numeric: tabular-nums; }
tfoot th, tfoot td { font-weight: 700; border-top: 2px solid var(--ink); border-bottom: 0; }
.thanks { margin-top: 2rem; color: var(--muted); font-style: italic; }
@media print { .invoice { border: 0; margin: 0; max-width: none; } }
'''
    return html, css


ptype(key="invoice", title="Printable invoice for {name}", level=2,
      brief="Create a clean invoice with a header row, a table using tfoot and colspan for the total, right-aligned numbers and print styles.",
      goals=["Use tfoot and colspan", "Align numbers with tabular figures", "Design for print"],
      elements=["header", "div", "h1", "p", "b", "time", "table", "thead", "tbody", "tfoot", "th", "td"], css=["justify-content: space-between", "colspan", "font-variant-numeric", "border-top", "@media print"],
      steps=["Write the header with two blocks: seller and invoice metadata.", "Write the table with thead, tbody and a tfoot total row using colspan=\"2\".", "Add class n to numeric cells.",
             "Flex the header with space-between.", "Right-align .n cells.", "Print preview and remove the border in @media print."],
      build=b_invoice, checklist=["Numbers right-aligned", "Total row in tfoot", "Fits on one printed page", "Date has datetime"],
      exercises=["Calculate the total with JavaScript.", "Add a logo image.", "Add a QR code image for payment."])


def b_features(t):
    icons = ["&#10004;", "&#9733;", "&#9829;", "&#9992;"]
    lis = "\n".join(f'      <li><span class="icon" aria-hidden="true">{icons[i]}</span><div><h2>{a}</h2><p>{b}.</p></div></li>' for i, (a, b, c) in enumerate(t["items"]))
    html = HEAD.format(title=t["name"] + " - Features") + f'''  <main>
    <h1>What we offer</h1>
    <ul class="features">
{lis}
    </ul>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 56rem; margin: 2rem auto; padding: 0 1rem; }
.features { list-style: none; padding: 0; display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr)); }
.features li { display: flex; gap: 1rem; align-items: flex-start; }
.icon { flex: 0 0 3rem; height: 3rem; display: grid; place-items: center; background: var(--brand); color: #fff; border-radius: 12px; font-size: 1.4rem; }
.features h2 { margin: 0 0 .25rem; font-size: 1.1rem; }
.features p { margin: 0; color: var(--muted); }
'''
    return html, css


ptype(key="features", title="Feature list with icons for {name}", level=1,
      brief="Present four features as a two-column list where each item is a media object: an icon box on the left and text on the right.",
      goals=["Build the media object pattern with Flexbox", "Hide decorative icons from screen readers", "Use flex: 0 0 for fixed-size boxes"],
      elements=["ul", "li", "span", "div", "h2", "p"], css=["display: flex", "align-items: flex-start", "flex: 0 0 3rem", "place-items", "grid auto-fit"],
      steps=["Write the list; each li has an icon span and a div with h2 and p.", "Add aria-hidden=\"true\" to the icon.", "Make li a flex row.",
             "Fix the icon size with flex: 0 0 3rem and centre the glyph.", "Grid the list into two columns when wide.", "Check the text wraps under itself, not under the icon."],
      build=b_features, checklist=["Icons hidden from assistive tech", "Text does not wrap under the icon", "Two columns on desktop, one on mobile", "Headings are h2"],
      exercises=["Replace the glyphs with inline SVG icons.", "Add a hover effect on the icon box.", "Make the icon box a circle."])


def b_map_contact(t):
    html = HEAD.format(title=t["name"] + " - Find us") + f'''  <main class="find">
    <section class="info">
      <h1>Find {t["name"]}</h1>
      <address>
        <strong>{t["name"]}</strong><br>
        12 Example Street<br>
        {t["city"]}, Egypt<br>
        <a href="tel:+20100000000">+20 100 000 0000</a>
      </address>
      <h2>Opening hours</h2>
      <table>
        <tr><th scope="row">Saturday - Thursday</th><td>10:00 - 22:00</td></tr>
        <tr><th scope="row">Friday</th><td>14:00 - 22:00</td></tr>
      </table>
    </section>
    <iframe class="map" src="https://www.openstreetmap.org/export/embed.html?bbox=31.20%2C30.02%2C31.24%2C30.06&amp;layer=mapnik" title="Map showing {t["name"]} in {t["city"]}" loading="lazy"></iframe>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.find { max-width: 64rem; margin: 2rem auto; padding: 0 1rem; display: grid; gap: 2rem; grid-template-columns: 1fr; }
@media (min-width: 760px) { .find { grid-template-columns: 1fr 1.4fr; align-items: start; } }
address { font-style: normal; line-height: 1.8; margin-bottom: 1.5rem; }
table { border-collapse: collapse; }
th, td { text-align: left; padding: .4rem .8rem .4rem 0; }
.map { width: 100%; aspect-ratio: 4 / 3; border: 0; border-radius: 12px; }
'''
    return html, css


ptype(key="map", title="Find-us page with map for {name}", level=2,
      brief="Combine an address block, an opening-hours table and an embedded map iframe in a two-column responsive layout.",
      goals=["Embed a third-party map with iframe and title", "Use address correctly", "Give the iframe a responsive aspect ratio"],
      elements=["section", "h1", "address", "strong", "br", "a", "h2", "table", "tr", "th", "td", "iframe"], css=["grid-template-columns: 1fr 1.4fr", "aspect-ratio", "border: 0", "align-items: start", "@media"],
      steps=["Write the info section with address and hours table.", "Add the iframe with a descriptive title and loading=\"lazy\".", "Single column by default.",
             "Two columns above 760px.", "Make the map fill its column with width 100% and aspect-ratio.", "Remove the iframe border."],
      build=b_map_contact, checklist=["iframe has a title", "Address uses <address> without italic", "Map keeps its shape on resize", "Phone link works on mobile"],
      exercises=["Add a 'Get directions' link to a maps URL.", "Add a contact form under the address.", "Use <details> for a public transport section."])


def b_tabs(t):
    labels = [a for a, b, c in t["items"][:3]]
    inputs = "\n".join(f'    <input type="radio" name="tab" id="t{i}"{" checked" if i == 0 else ""}>' for i in range(3))
    lbls = "".join(f'<label for="t{i}">{l}</label>' for i, l in enumerate(labels))
    panels = "\n".join(f'      <section class="panel" id="p{i}"><h2>{a}</h2><p>{b}. Price: {c}.</p></section>' for i, (a, b, c) in enumerate(t["items"][:3]))
    html = HEAD.format(title=t["name"] + " - Compare") + f'''  <main class="tabs">
{inputs}
    <div class="tablist">{lbls}</div>
    <div class="panels">
{panels}
    </div>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.tabs { max-width: 40rem; margin: 2rem auto; padding: 0 1rem; }
.tabs > input { position: absolute; opacity: 0; pointer-events: none; }
.tablist { display: flex; border-bottom: 2px solid var(--line); }
.tablist label { padding: .7rem 1rem; cursor: pointer; color: var(--muted); border-bottom: 3px solid transparent; margin-bottom: -2px; }
.tabs > input:focus-visible + .tablist label { outline: 2px solid var(--brand); }
.panel { display: none; padding: 1.25rem 0; }
#t0:checked ~ .tablist label[for="t0"], #t1:checked ~ .tablist label[for="t1"], #t2:checked ~ .tablist label[for="t2"] { color: var(--brand); border-color: var(--brand); font-weight: 600; }
#t0:checked ~ .panels #p0, #t1:checked ~ .panels #p1, #t2:checked ~ .panels #p2 { display: block; }
'''
    return html, css


ptype(key="tabs", title="CSS-only tabs for {name}", level=3,
      brief="Build a tabbed interface without JavaScript using hidden radio buttons, labels as tabs and the :checked ~ sibling selector to show panels.",
      goals=["Use the :checked pseudo-class with the general sibling combinator", "Style labels as tabs", "Understand the limits of CSS-only widgets"],
      elements=["input type=radio", "label", "div", "section", "h2", "p"], css=[":checked", "~ combinator", "attribute selector", "display: none/block", "opacity: 0 hiding"],
      steps=["Put three radio inputs with the same name first inside .tabs.", "Add a .tablist of labels pointing at the radios.", "Add three panels.",
             "Hide the radios visually but keep them focusable.", "Show the panel matching the checked radio with :checked ~ .panels #pN.", "Highlight the active label the same way."],
      build=b_tabs, checklist=["Arrow keys switch tabs (radio behaviour)", "First tab open by default", "Only one panel visible", "Radios are before the labels and panels in the source"],
      exercises=["Add a fourth tab.", "Add a slide-in animation on the active panel.", "Rebuild it with buttons and JavaScript plus role=tablist for full accessibility."])


def b_modal(t):
    html = HEAD.format(title=t["name"] + " - Offer") + f'''  <main>
    <h1>{t["name"]}</h1>
    <p>{t["tagline"]}.</p>
    <button type="button" id="open">See this week's offer</button>
    <dialog id="offer">
      <form method="dialog">
        <h2>This week only</h2>
        <p><strong>{t["items"][0][0]}</strong> for {t["items"][0][2]}: 20 percent off with the code WEB20.</p>
        <button value="close">Close</button>
      </form>
    </dialog>
  </main>
  <script>
    const dlg = document.getElementById('offer');
    document.getElementById('open').addEventListener('click', () => dlg.showModal());
  </script>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 40rem; margin: 3rem auto; padding: 0 1rem; }
button { padding: .7rem 1.3rem; border: 0; border-radius: 999px; background: var(--brand); color: #fff; font: inherit; cursor: pointer; }
dialog { border: 0; border-radius: 16px; padding: 2rem; max-width: 26rem; box-shadow: 0 20px 60px rgb(0 0 0 / 30%); }
dialog::backdrop { background: rgb(0 0 0 / 50%); backdrop-filter: blur(2px); }
dialog h2 { margin-top: 0; color: var(--brand); }
'''
    return html, css


ptype(key="modal", title="Modal dialog for {name}", level=3,
      brief="Show a promotional pop-up using the native dialog element, opened with two lines of JavaScript, closed by a form with method=dialog, with a blurred backdrop.",
      goals=["Use <dialog> and showModal()", "Close a dialog with method=\"dialog\"", "Style ::backdrop"],
      elements=["button", "dialog", "form method=dialog", "h2", "p", "strong", "script"], css=["::backdrop", "backdrop-filter", "box-shadow", "border-radius"],
      steps=["Write the page with an open button and a <dialog>.", "Inside the dialog, wrap the content in <form method=\"dialog\"> with a close button.", "Add the script that calls showModal() on click.",
             "Remove the default border and round the dialog.", "Style ::backdrop.", "Test: Escape closes it; focus is trapped inside."],
      build=b_modal, checklist=["Escape key closes", "Focus moves into the dialog", "Background is not clickable", "Close button visible"],
      exercises=["Open the dialog automatically after 5 seconds, once per visit (localStorage).", "Animate the entrance with @starting-style.", "Add a form inside and read the returnValue."])


def b_search(t):
    html = HEAD.format(title=t["name"] + " - Search") + f'''  <header class="bar">
    <a class="logo" href="index.html">{t["name"]}</a>
    <search>
      <form action="/search" role="search">
        <label for="q" class="sr-only">Search {t["nouns"]}</label>
        <input id="q" name="q" type="search" placeholder="Search {t["nouns"]}" list="suggest" autocomplete="off">
        <datalist id="suggest">
{items_li(t, 4, '<option value="{0}">')}
        </datalist>
        <button>Go</button>
      </form>
    </search>
  </header>
  <main>
    <h1>Search results</h1>
    <p>3 results for <q>{t["noun"]}</q></p>
    <ol class="results">
{items_li(t, 3, '<li><a href="#">{0}</a><p>{1}.</p></li>')}
    </ol>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.bar { display: flex; gap: 1rem; align-items: center; padding: .75rem 1.5rem; background: var(--accent); flex-wrap: wrap; }
.logo { font-weight: 700; text-decoration: none; color: var(--brand); }
search { flex: 1 1 18rem; }
form { display: flex; }
input { flex: 1; padding: .6rem .9rem; border: 1px solid #bbb; border-right: 0; border-radius: 999px 0 0 999px; font: inherit; }
button { padding: .6rem 1rem; border: 0; border-radius: 0 999px 999px 0; background: var(--brand); color: #fff; font: inherit; }
main { max-width: 40rem; margin: 1.5rem auto; padding: 0 1rem; }
.results { list-style: none; padding: 0; }
.results li { padding: 1rem 0; border-bottom: 1px solid var(--line); }
.results a { font-size: 1.1rem; font-weight: 600; }
.results p { margin: .2rem 0 0; color: var(--muted); }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
'''
    return html, css


ptype(key="search", title="Search bar and results page for {name}", level=2,
      brief="Build a header search box with datalist suggestions and a joined input/button pair, plus a results list styled like a search engine.",
      goals=["Use the search element, type=search and datalist", "Join an input and button with asymmetric border-radius", "Present results as an ordered list"],
      elements=["search", "form", "label", "input type=search", "datalist", "option", "button", "ol", "li", "a", "q"], css=["flex: 1 1 18rem", "border-radius (four values)", "border-right: 0", "list-style: none"],
      steps=["Write the header with logo and <search> containing the form.", "Add a datalist with one option per offer and link it with list=.", "Add the results list.",
             "Flex the bar; let the search area grow.", "Round only the outer corners of input and button.", "Style the results."],
      build=b_search, checklist=["Typing shows suggestions", "Label exists (hidden)", "Button attached to input visually", "Results are links with descriptions"],
      exercises=["Highlight the matched word in results with <mark>.", "Add filters with checkboxes in an aside.", "Add 'no results' state styling."])


def b_progress(t):
    html = HEAD.format(title=t["name"] + " - Order status") + f'''  <main>
    <h1>Your order</h1>
    <p>Order 1042: <strong>{t["items"][0][0]}</strong></p>
    <ol class="steps">
      <li class="done">Received</li>
      <li class="done">Prepared</li>
      <li class="current" aria-current="step">On the way</li>
      <li>Delivered</li>
    </ol>
    <label for="p">Progress</label>
    <progress id="p" value="3" max="4">75%</progress>
    <h2>Rating so far</h2>
    <meter value="4.8" min="0" max="5" low="2" high="4" optimum="5">4.8 out of 5</meter> 4.8 / 5
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 40rem; margin: 2rem auto; padding: 0 1rem; }
.steps { list-style: none; padding: 0; display: flex; counter-reset: step; margin: 1.5rem 0; }
.steps li { flex: 1; text-align: center; position: relative; padding-top: 2.4rem; font-size: .9rem; color: var(--muted); }
.steps li::before { counter-increment: step; content: counter(step); position: absolute; top: 0; left: 50%; translate: -50% 0; width: 2rem; height: 2rem; border-radius: 50%; background: var(--line); color: #fff; display: grid; place-items: center; font-weight: 700; }
.steps li::after { content: ""; position: absolute; top: 1rem; left: -50%; width: 100%; height: 3px; background: var(--line); z-index: -1; }
.steps li:first-child::after { display: none; }
.steps .done::before, .steps .done::after, .steps .current::before { background: var(--brand); }
.steps .current { color: var(--brand); font-weight: 700; }
progress { width: 100%; height: 1rem; accent-color: var(--brand); }
meter { width: 12rem; }
'''
    return html, css


ptype(key="progress", title="Order progress tracker for {name}", level=3,
      brief="Show order status as a numbered step indicator built with CSS counters and pseudo-elements, plus native progress and meter elements.",
      goals=["Use counter-reset and counter-increment", "Use progress and meter", "Build connector lines with ::after"],
      elements=["ol", "li", "progress", "meter", "label", "strong"], css=["counter-reset", "counter()", "::before/::after", "translate", "accent-color", "z-index"],
      steps=["Write the ol with classes done/current and aria-current=\"step\".", "Add progress and meter elements with values.", "Flex the list; each li gets equal width.",
             "Number the circles with counters in ::before.", "Draw connector lines with ::after.", "Colour completed steps and the progress bar with accent-color."],
      build=b_progress, checklist=["Numbers generated by CSS, not typed", "Lines sit behind circles", "Current step announced with aria-current", "Progress has a label"],
      exercises=["Animate the progress bar value with a transition on width (custom bar).", "Make the tracker vertical on narrow screens.", "Add estimated times under each step."])


def b_two_col(t):
    html = HEAD.format(title=t["name"] + " - " + t["items"][0][0]) + f'''  <main class="split">
    <div class="text">
      <p class="kicker">{t["noun"].capitalize()} of the month</p>
      <h1>{t["items"][0][0]}</h1>
      <p>{t["items"][0][1]}. Available now at {t["name"]} in {t["city"]} for <strong>{t["items"][0][2]}</strong>.</p>
      <ul class="ticks">
        <li>Made with care</li>
        <li>Satisfaction guaranteed</li>
        <li>Ask us anything</li>
      </ul>
      <a class="btn" href="contact.html">Ask about it</a>
    </div>
    <img src="images/{t["slug"]}-1.jpg" alt="{t["items"][0][0]}" width="900" height="900">
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.split { min-height: 100vh; display: grid; grid-template-columns: 1fr; }
.text { padding: clamp(1.5rem, 5vw, 4rem); display: grid; align-content: center; gap: 1rem; }
img { width: 100%; height: 100%; object-fit: cover; }
@media (min-width: 800px) { .split { grid-template-columns: 1fr 1fr; } }
.kicker { text-transform: uppercase; letter-spacing: .1em; color: var(--brand); font-weight: 700; margin: 0; }
h1 { margin: 0; font-size: clamp(2rem, 4vw, 3rem); }
.ticks { list-style: none; padding: 0; margin: 0; }
.ticks li::before { content: "\\2713 "; color: var(--brand); font-weight: 700; }
.btn { justify-self: start; padding: .8rem 1.6rem; background: var(--brand); color: #fff; border-radius: 999px; text-decoration: none; }
'''
    return html, css


ptype(key="split", title="Split-screen feature section for {name}", level=2,
      brief="Create a full-height section with text on one half and a photo filling the other half, stacking on small screens.",
      goals=["Fill a grid cell with an image using object-fit", "Vertically centre content with align-content", "Use clamp() for fluid padding"],
      elements=["main", "div", "p", "h1", "strong", "ul", "li", "a", "img"], css=["grid-template-columns: 1fr 1fr", "object-fit: cover", "align-content: center", "clamp()", "::before content"],
      steps=["Write the text block and the image as the two children of .split.", "Grid with one column by default, two above 800px.", "Give the image height 100% and object-fit: cover.",
             "Centre the text vertically with align-content.", "Add tick marks to the list with ::before.", "Use clamp() for padding."],
      build=b_two_col, checklist=["Image never distorts", "Text stays readable width", "Stacks on mobile with image below", "Button aligned left, not stretched"],
      exercises=["Swap the sides with order or direction: rtl.", "Add a second split section with the image on the left.", "Use a background video instead of the image."])


def b_stats_counter(t):
    html = HEAD.format(title=t["name"] + " - In numbers") + f'''  <main>
    <h1>{t["name"]} in numbers</h1>
    <dl class="numbers">
      <div><dt>Years open</dt><dd>8</dd></div>
      <div><dt>Happy customers</dt><dd>12,000+</dd></div>
      <div><dt>{t["nouns"].capitalize()}</dt><dd>{len(t["items"])}</dd></div>
      <div><dt>Average rating</dt><dd>4.8</dd></div>
    </dl>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 60rem; margin: 3rem auto; padding: 0 1rem; text-align: center; }
.numbers { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(10rem, 1fr)); margin: 0; }
.numbers div { background: var(--brand); color: #fff; padding: 1.5rem 1rem; border-radius: 14px; display: flex; flex-direction: column-reverse; }
dd { margin: 0; font-size: 2.5rem; font-weight: 800; line-height: 1; }
dt { margin-top: .5rem; opacity: .9; }
'''
    return html, css


ptype(key="numbers", title="Statistics strip for {name}", level=1,
      brief="Show four key numbers in coloured tiles where the big number appears above its label, using flex-direction: column-reverse on a dl.",
      goals=["Use dl for label/value pairs", "Reverse visual order without changing source order", "Size big numbers with line-height 1"],
      elements=["dl", "div", "dt", "dd"], css=["flex-direction: column-reverse", "grid auto-fit", "font-weight: 800", "line-height: 1", "opacity"],
      steps=["Write the dl with a div per pair.", "Grid the dl.", "Make each div a flex column-reverse so the number shows first.",
             "Style dd large and bold.", "Colour the tiles.", "Check the reading order in a screen reader stays label then value."],
      build=b_stats_counter, checklist=["dt before dd in source", "Numbers visually above labels", "Tiles equal height", "White text contrast on brand colour"],
      exercises=["Animate the numbers counting up with JavaScript.", "Add small icons.", "Add a subtle gradient to the tiles."])


def b_breadcrumb(t):
    a = t["items"][0][0]
    html = HEAD.format(title=a + " - " + t["name"]) + f'''  <main>
    <nav aria-label="Breadcrumb">
      <ol class="crumbs">
        <li><a href="index.html">Home</a></li>
        <li><a href="{t["nouns"]}.html">{t["nouns"].capitalize()}</a></li>
        <li aria-current="page">{a}</li>
      </ol>
    </nav>
    <h1>{a}</h1>
    <p>{t["items"][0][1]}.</p>
    <nav class="pager" aria-label="Pagination">
      <a href="?page=1" aria-label="Previous page">&laquo;</a>
      <a href="?page=1">1</a>
      <a href="?page=2" aria-current="page">2</a>
      <a href="?page=3">3</a>
      <a href="?page=3" aria-label="Next page">&raquo;</a>
    </nav>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 44rem; margin: 2rem auto; padding: 0 1rem; }
.crumbs { list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: .25rem; font-size: .9rem; }
.crumbs li + li::before { content: "/"; margin: 0 .5rem; color: var(--muted); }
.crumbs a { color: var(--brand); }
.crumbs [aria-current] { color: var(--muted); }
.pager { display: flex; gap: .25rem; margin-top: 3rem; }
.pager a { min-width: 2.4rem; padding: .5rem; text-align: center; border: 1px solid var(--line); border-radius: 6px; text-decoration: none; color: var(--ink); }
.pager a:hover { background: var(--accent); }
.pager a[aria-current] { background: var(--brand); color: #fff; border-color: var(--brand); }
'''
    return html, css


ptype(key="breadcrumb", title="Breadcrumbs and pagination for {name}", level=1,
      brief="Add two navigation aids: a breadcrumb trail with CSS-generated separators and a pagination bar with a highlighted current page.",
      goals=["Use nav with aria-label for secondary navigation", "Generate separators with li + li::before", "Style the current item with [aria-current]"],
      elements=["nav", "ol", "li", "a"], css=["adjacent sibling +", "::before content", "attribute selector", "min-width", "border"],
      steps=["Write the breadcrumb ol inside a nav.", "Mark the last item with aria-current=\"page\" and no link.", "Write the pager with previous/next arrows labelled.",
             "Add separators with li + li::before so the first has none.", "Style pager links as boxes.", "Highlight the current page."],
      build=b_breadcrumb, checklist=["Both navs have distinct aria-labels", "Separators not in the HTML", "Arrows have aria-label", "Current page not a link in breadcrumb"],
      exercises=["Use an SVG chevron as the separator.", "Add schema.org BreadcrumbList microdata.", "Collapse middle crumbs on narrow screens."])


def b_alerts(t):
    html = HEAD.format(title=t["name"] + " - Messages") + f'''  <main>
    <h1>Message styles</h1>
    <p class="alert info" role="status"><strong>Info:</strong> {t["name"]} opens at 10:00 on Fridays.</p>
    <p class="alert success" role="status"><strong>Success:</strong> Your {t["noun"]} has been booked.</p>
    <p class="alert warning" role="alert"><strong>Warning:</strong> Only two {t["nouns"]} left this week.</p>
    <p class="alert error" role="alert"><strong>Error:</strong> The email address is not valid.</p>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 40rem; margin: 2rem auto; padding: 0 1rem; display: grid; gap: 1rem; }
.alert { margin: 0; padding: .9rem 1.1rem; border-radius: 10px; border: 1px solid; border-left-width: 6px; }
.info    { background: #eff6ff; border-color: #60a5fa; color: #1e3a8a; }
.success { background: #f0fdf4; border-color: #4ade80; color: #14532d; }
.warning { background: #fffbeb; border-color: #fbbf24; color: #78350f; }
.error   { background: #fef2f2; border-color: #f87171; color: #7f1d1d; }
'''
    return html, css


ptype(key="alerts", title="Alert message components for {name}", level=1,
      brief="Create four message styles (info, success, warning, error) with colour, a thick left border and a text prefix so meaning does not rely on colour alone.",
      goals=["Build reusable component classes", "Use role=status and role=alert", "Use border shorthand then override one side"],
      elements=["p", "strong"], css=["border: 1px solid", "border-left-width", "border-color", "background", "class modifiers"],
      steps=["Write four paragraphs with the shared class alert and a modifier class.", "Prefix each with a strong label.", "Add role attributes.",
             "Style .alert once with padding, radius and a 1px border.", "Set border-left-width: 6px.", "Set colours per modifier."],
      build=b_alerts, checklist=["Each message has a text label", "Contrast passes for all four", "Shared styles in one rule", "role used correctly"],
      exercises=["Add a close button that hides the alert with JavaScript.", "Add icons with ::before.", "Add a dark mode variant."])


def b_multi_step(t):
    html = HEAD.format(title=t["name"] + " - Booking") + f'''  <main>
    <h1>Book a {t["noun"]}</h1>
    <form action="/book" method="post" class="wizard">
      <fieldset>
        <legend>1. Choose a {t["noun"]}</legend>
{items_li(t, 4, '<label><input type="radio" name="item" value="{0}" required> {0} <small>{2}</small></label>')}
      </fieldset>
      <fieldset>
        <legend>2. When</legend>
        <label>Date <input type="date" name="date" required min="2026-09-11"></label>
        <label>Time <input type="time" name="time" required step="1800"></label>
        <label>People <input type="number" name="people" min="1" max="10" value="1"></label>
      </fieldset>
      <fieldset>
        <legend>3. Your details</legend>
        <label>Name <input type="text" name="name" required autocomplete="name"></label>
        <label>Phone <input type="tel" name="phone" required autocomplete="tel" inputmode="tel"></label>
        <label><input type="checkbox" name="terms" required> I agree to the cancellation policy</label>
      </fieldset>
      <button type="submit">Confirm booking</button>
    </form>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 40rem; margin: 2rem auto; padding: 0 1rem; }
.wizard { display: grid; gap: 1.5rem; }
fieldset { border: 1px solid var(--line); border-radius: 12px; padding: 1rem 1.25rem; display: grid; gap: .6rem; }
legend { font-weight: 700; color: var(--brand); padding: 0 .4rem; }
label { display: flex; align-items: center; gap: .5rem; flex-wrap: wrap; }
label small { margin-left: auto; color: var(--muted); }
input:not([type="radio"]):not([type="checkbox"]) { padding: .5rem .7rem; border: 1px solid #bbb; border-radius: 8px; font: inherit; flex: 1 1 8rem; }
button { justify-self: start; padding: .8rem 1.6rem; border: 0; border-radius: 999px; background: var(--brand); color: #fff; font: inherit; }
'''
    return html, css


ptype(key="booking", title="Booking form in three steps for {name}", level=2,
      brief="Build a longer form divided into three fieldsets: radio choice with prices, date/time/number inputs, and personal details with a required checkbox.",
      goals=["Group related controls with fieldset and legend", "Use date, time, number and tel input types with min/max/step", "Use wrapping labels"],
      elements=["form", "fieldset", "legend", "label", "input (radio, date, time, number, text, tel, checkbox)", "small", "button"], css=["fieldset border/radius", "legend", "display: flex on label", "margin-left: auto", ":not() chains"],
      steps=["Write three fieldsets with legends numbered 1 to 3.", "Step 1: radio buttons with the same name, each wrapped in a label with the price in <small>.", "Step 2: date, time and number inputs with limits.",
             "Step 3: text, tel and a required checkbox.", "Grid the form and fieldsets.", "Push prices right with margin-left: auto."],
      build=b_multi_step, checklist=["Radios share one name", "Date min prevents past dates", "Every control labelled", "Checkbox required works"],
      exercises=["Show one fieldset at a time with :has() and radio state or JavaScript.", "Add a summary panel that updates live.", "Add a progress tracker on top."])


def b_video(t):
    html = HEAD.format(title=t["name"] + " - Video tour") + f'''  <main>
    <h1>Take a tour of {t["name"]}</h1>
    <figure class="video">
      <video controls preload="metadata" poster="images/poster.jpg" width="1280" height="720">
        <source src="media/tour.webm" type="video/webm">
        <source src="media/tour.mp4" type="video/mp4">
        <track kind="captions" src="media/tour.en.vtt" srclang="en" label="English" default>
        <track kind="captions" src="media/tour.ar.vtt" srclang="ar" label="Arabic">
        <p>Your browser cannot play this video. <a href="media/tour.mp4">Download it</a> instead.</p>
      </video>
      <figcaption>A two-minute walk through our {t["city"]} location with {t["person"]}.</figcaption>
    </figure>
    <h2>Listen to our story</h2>
    <audio controls preload="none" src="media/story.mp3"></audio>
    <p><a href="media/story-transcript.html">Read the transcript</a></p>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 56rem; margin: 2rem auto; padding: 0 1rem; }
.video { margin: 0; }
video { width: 100%; height: auto; aspect-ratio: 16 / 9; background: #000; border-radius: 12px; }
figcaption { color: var(--muted); margin-top: .5rem; }
audio { width: 100%; max-width: 30rem; }
'''
    return html, css


ptype(key="video", title="Video and audio page for {name}", level=2,
      brief="Embed a video with two source formats, poster image, English and Arabic caption tracks and a fallback link, plus an audio player with a transcript link.",
      goals=["Provide multiple sources and captions", "Use preload and poster sensibly", "Keep media responsive with aspect-ratio"],
      elements=["figure", "video", "source", "track", "p", "a", "figcaption", "audio"], css=["aspect-ratio: 16 / 9", "width: 100%", "background", "border-radius", "max-width"],
      steps=["Write the video with controls, poster and dimensions.", "Add WebM then MP4 sources.", "Add caption tracks; mark one default.",
             "Add fallback content inside the video.", "Add the audio element and transcript link.", "Make the video fluid."],
      build=b_video, checklist=["Captions toggle appears in the player", "Video never wider than container", "Fallback link present", "Audio has a transcript"],
      exercises=["Add chapters with kind=\"chapters\".", "Add a custom play button overlay.", "Lazy-load the video with loading=\"lazy\" on an iframe embed instead."])


def b_cards_grid(t):
    cards = "\n".join(f'      <article class="card">\n        <img src="images/{t["slug"]}-{i+1}.jpg" alt="" width="600" height="400">\n        <div class="body">\n          <h2><a href="#">{a}</a></h2>\n          <p>{b}.</p>\n          <p class="price">{c}</p>\n        </div>\n      </article>' for i, (a, b, c) in enumerate(t["items"]))
    html = HEAD.format(title=t["name"] + " - All " + t["nouns"]) + f'''  <main>
    <h1>All {t["nouns"]}</h1>
    <div class="grid">
{cards}
    </div>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 70rem; margin: 2rem auto; padding: 0 1rem; }
.grid { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr)); }
.card { display: flex; flex-direction: column; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; background: #fff; position: relative; transition: box-shadow .2s, translate .2s; }
.card:hover { box-shadow: 0 12px 30px rgb(0 0 0 / 12%); translate: 0 -3px; }
.card img { width: 100%; height: auto; aspect-ratio: 3 / 2; object-fit: cover; }
.body { padding: 1rem 1.25rem; display: flex; flex-direction: column; flex: 1; }
h2 { font-size: 1.1rem; margin: 0 0 .3rem; }
h2 a { color: inherit; text-decoration: none; }
h2 a::after { content: ""; position: absolute; inset: 0; }   /* whole card clickable */
.body p { margin: 0 0 .5rem; color: var(--muted); }
.price { margin-top: auto !important; color: var(--brand); font-weight: 700; }
'''
    return html, css


ptype(key="cardgrid", title="Product grid with clickable cards for {name}", level=2,
      brief="List all offers as equal-height cards where the whole card is clickable via a stretched link pseudo-element and the price sticks to the bottom.",
      goals=["Make a whole card clickable accessibly (one link, stretched)", "Push an element to the bottom with margin-top: auto", "Lift cards on hover"],
      elements=["article", "img", "div", "h2", "a", "p"], css=["position: relative + ::after inset: 0", "flex-direction: column", "margin-top: auto", "transition", "translate"],
      steps=["Write one article per offer with image, heading link, text and price.", "Grid with auto-fill.", "Make card and body flex columns; body flex: 1.",
             "Push price down with margin-top: auto.", "Stretch the heading link over the card with ::after and inset: 0.", "Add the hover lift."],
      build=b_cards_grid, checklist=["Only one link per card (screen readers)", "Cards equal height in a row", "Price aligned at bottom", "Hover does not shift layout"],
      exercises=["Add a filter bar with radio buttons and :has().", "Add a 'new' badge.", "Add a sort dropdown with JavaScript."])


def b_dark(t):
    html = HEAD.format(title=t["name"] + " - Themes") + f'''  <main>
    <h1>{t["name"]}</h1>
    <p>This page follows your system theme and also lets you choose one.</p>
    <fieldset class="theme">
      <legend>Theme</legend>
      <label><input type="radio" name="theme" value="auto" checked> Auto</label>
      <label><input type="radio" name="theme" value="light"> Light</label>
      <label><input type="radio" name="theme" value="dark"> Dark</label>
    </fieldset>
    <section class="card">
      <h2>{t["items"][0][0]}</h2>
      <p>{t["items"][0][1]}. <a href="#">Read more</a></p>
    </section>
  </main>
  <script>
    document.querySelectorAll('input[name=theme]').forEach(r => r.addEventListener('change', e => {{
      document.documentElement.dataset.theme = e.target.value;
    }}));
  </script>
''' + FOOT
    css = BASE_CSS.format(**t) + ''':root { color-scheme: light dark; --bg: #fff; --fg: #1b2431; --card: #f4f4f4; }
@media (prefers-color-scheme: dark) { :root { --bg: #111827; --fg: #e5e7eb; --card: #1f2937; } }
:root[data-theme="light"] { --bg: #fff; --fg: #1b2431; --card: #f4f4f4; color-scheme: light; }
:root[data-theme="dark"]  { --bg: #111827; --fg: #e5e7eb; --card: #1f2937; color-scheme: dark; }
body { background: var(--bg); color: var(--fg); transition: background .3s, color .3s; }
main { max-width: 40rem; margin: 2rem auto; padding: 0 1rem; }
.theme { display: flex; gap: 1rem; border: 1px solid var(--line); border-radius: 10px; }
.card { background: var(--card); padding: 1.25rem; border-radius: 12px; margin-top: 1.5rem; }
a { color: var(--brand); }
'''
    return html, css


ptype(key="dark", title="Light and dark theme switcher for {name}", level=3,
      brief="Support the system colour scheme automatically and add a manual switch that sets a data attribute on the html element, all driven by custom properties.",
      goals=["Use prefers-color-scheme and color-scheme", "Theme with custom properties", "Override with a data attribute set by a few lines of JavaScript"],
      elements=["fieldset", "legend", "label", "input type=radio", "section", "script"], css=["custom properties", "@media (prefers-color-scheme)", "[data-theme]", "color-scheme", "transition"],
      steps=["Define light variables in :root and dark ones inside a prefers-color-scheme media query.", "Add [data-theme] overrides.", "Use the variables for background, colour and cards.",
             "Add the radio group.", "Add the script that copies the chosen value to html's data-theme.", "Test with your OS in dark mode."],
      build=b_dark, checklist=["Follows system setting by default", "Manual choice overrides", "Form controls also switch (color-scheme)", "Contrast good in both themes"],
      exercises=["Remember the choice in localStorage.", "Add a high-contrast theme.", "Animate the switch with a view transition."])


def b_print(t):
    html = HEAD.format(title=t["name"] + " - Voucher") + f'''  <main>
    <nav class="no-print"><a href="index.html">Back</a> &middot; <button onclick="print()">Print this voucher</button></nav>
    <article class="voucher">
      <h1>{t["name"]} gift voucher</h1>
      <p class="amount">200 EGP</p>
      <p>Valid for any {t["noun"]} until <time datetime="2027-09-11">11 September 2027</time>.</p>
      <p class="code">Code: <b>GIFT-{t["slug"].upper()[:4]}-2026</b></p>
      <p class="small">Present this voucher in {t["city"]}. Not exchangeable for cash.</p>
    </article>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 36rem; margin: 2rem auto; padding: 0 1rem; }
.voucher { border: 4px double var(--brand); padding: 2rem; text-align: center; border-radius: 8px; }
h1 { color: var(--brand); margin-top: 0; }
.amount { font-size: 3rem; font-weight: 800; margin: 0; }
.code { font-family: monospace; font-size: 1.2rem; background: var(--accent); display: inline-block; padding: .4rem 1rem; }
.small { font-size: .8rem; color: var(--muted); }
@media print {
  .no-print { display: none; }
  body { margin: 0; }
  main { max-width: none; margin: 0; }
  .voucher { border-color: #000; page-break-inside: avoid; }
  a[href]::after { content: " (" attr(href) ")"; }
}
@page { margin: 2cm; }
'''
    return html, css


ptype(key="print", title="Printable voucher for {name}", level=2,
      brief="Design a gift voucher that looks good on screen and prints cleanly: hide navigation, avoid page breaks, print link URLs and set page margins.",
      goals=["Write @media print rules", "Use @page", "Trigger printing with a button"],
      elements=["nav", "a", "button", "article", "h1", "p", "time", "b"], css=["@media print", "display: none", "page-break-inside", "attr()", "@page", "border: double"],
      steps=["Write the voucher article and a nav with a print button.", "Style the voucher with a double border.", "In @media print hide .no-print.",
             "Prevent the voucher splitting across pages.", "Print link hrefs after links.", "Set @page margins and test with print preview."],
      build=b_print, checklist=["Nav hidden in print", "Voucher on one page", "Black border when printed", "Print button works"],
      exercises=["Add a barcode-like pattern with repeating-linear-gradient.", "Add two vouchers per page with columns.", "Add a QR code image."])


def b_calendar(t):
    def cell(d):
        if d in (5, 12, 19):
            return '<td class="event">%d<span>%s</span></td>' % (d, t["noun"])
        return '<td>%d</td>' % d
    rows = ""
    cells = ["<td></td>", "<td></td>"] + [cell(d) for d in range(1, 31)]
    while len(cells) % 7:
        cells.append("<td></td>")
    for i in range(0, len(cells), 7):
        rows += "        <tr>" + "".join(cells[i:i + 7]) + "</tr>\n"
    html = HEAD.format(title=t["name"] + " - September") + f'''  <main>
    <h1>{t["name"]} calendar</h1>
    <table class="cal">
      <caption>September 2026</caption>
      <thead><tr><th>Sat</th><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th></tr></thead>
      <tbody>
{rows}      </tbody>
    </table>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 56rem; margin: 2rem auto; padding: 0 1rem; }
.cal { width: 100%; border-collapse: collapse; table-layout: fixed; }
caption { font-size: 1.3rem; font-weight: 700; padding: .5rem; }
th { padding: .5rem; background: var(--accent); }
td { height: 5rem; vertical-align: top; padding: .3rem; border: 1px solid var(--line); font-size: .9rem; }
td span { display: block; margin-top: .3rem; background: var(--brand); color: #fff; font-size: .7rem; padding: .1rem .3rem; border-radius: 4px; }
th:last-child, td:last-child { color: var(--brand); }
@media (max-width: 600px) { td { height: 3rem; } td span { font-size: 0; height: .5rem; width: .5rem; border-radius: 50%; padding: 0; } }
'''
    return html, css


ptype(key="calendar", title="Month calendar for {name}", level=3,
      brief="Draw a month grid as a table with fixed equal columns, tall cells, event labels that shrink to dots on phones and a highlighted Friday column.",
      goals=["Use table-layout: fixed for equal columns", "Use :last-child for a column", "Adapt content presentation with a media query"],
      elements=["table", "caption", "thead", "tbody", "tr", "th", "td", "span"], css=["table-layout: fixed", "vertical-align: top", "height on td", ":last-child", "@media (max-width)"],
      steps=["Write the header row with day names starting Saturday.", "Write the day cells in rows of seven, padding the first row with empty cells.", "Add a span for event labels.",
             "Fix the layout and set tall cells aligned top.", "Colour the last column.", "On narrow screens shrink event labels to dots."],
      build=b_calendar, checklist=["Seven cells in every row", "Columns equal width", "Events visible on mobile as dots", "Caption gives the month"],
      exercises=["Generate the cells with JavaScript for any month.", "Highlight today with a class.", "Make cells links to day pages."])


def b_accordion_menu(t):
    html = HEAD.format(title=t["name"] + " - Mobile menu") + f'''  <header class="top">
    <a class="logo" href="index.html">{t["name"]}</a>
    <input type="checkbox" id="menu-toggle" class="toggle" hidden>
    <label for="menu-toggle" class="burger" aria-label="Open menu">&#9776;</label>
    <nav class="menu" aria-label="Main">
      <ul>
        <li><a href="index.html">Home</a></li>
{items_li(t, 3, '<li><a href="#">{0}</a></li>')}
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
  <main><h1>Resize the window</h1><p>Below 700px the menu hides behind a button.</p></main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.top { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; padding: .75rem 1rem; background: var(--brand); color: #fff; }
.logo { color: #fff; text-decoration: none; font-weight: 700; }
.burger { font-size: 1.6rem; cursor: pointer; }
.menu { flex-basis: 100%; display: none; }
.toggle:checked ~ .menu { display: block; }
.menu ul { list-style: none; margin: .5rem 0 0; padding: 0; }
.menu a { display: block; padding: .6rem 0; color: #fff; text-decoration: none; border-top: 1px solid rgb(255 255 255 / 25%); }
@media (min-width: 700px) {
  .burger { display: none; }
  .menu { display: block; flex-basis: auto; }
  .menu ul { display: flex; gap: .5rem; margin: 0; }
  .menu a { border: 0; padding: .5rem .8rem; border-radius: 6px; }
  .menu a:hover { background: rgb(255 255 255 / 20%); }
}
main { padding: 2rem 1rem; }
'''
    return html, css


ptype(key="burger", title="Responsive hamburger menu for {name}", level=3,
      brief="Build a navigation that is a horizontal bar on desktop and collapses behind a hamburger button on phones, toggled by a hidden checkbox and no JavaScript.",
      goals=["Use the checkbox hack with :checked ~", "Switch layouts with a min-width media query", "Use flex-basis: 100% to wrap an item to its own line"],
      elements=["header", "input type=checkbox", "label", "nav", "ul", "li", "a"], css=[":checked ~", "flex-basis: 100%", "display: none/block", "@media (min-width)", "flex-wrap"],
      steps=["Write the header: logo, hidden checkbox, label as the burger, nav.", "Mobile first: hide .menu; show when the checkbox is checked.", "Make .menu take the full row with flex-basis: 100%.",
             "At 700px hide the burger and always show the menu inline.", "Style links for both modes.", "Test with keyboard: Space on the focused label toggles the checkbox."],
      build=b_accordion_menu, checklist=["Menu opens and closes on mobile", "Burger hidden on desktop", "Label has an aria-label", "No horizontal scrollbar at 320px"],
      exercises=["Animate the menu opening with grid-template-rows: 0fr to 1fr.", "Rebuild with a <button> and aria-expanded using JavaScript.", "Add a close (X) state to the burger icon."])


def b_glossary(t):
    terms = [(a, b) for a, b, c in t["items"]] + [("Booking", f"Reserving a {t['noun']} in advance."), ("Voucher", "A prepaid code exchangeable for services.")]
    terms.sort()
    groups = {}
    for a, b in terms:
        groups.setdefault(a[0].upper(), []).append((a, b))
    body = ""
    for letter in sorted(groups):
        body += f'    <section id="{letter}">\n      <h2>{letter}</h2>\n      <dl>\n' + "\n".join(f'        <dt id="{a.lower().replace(" ", "-")}">{a}</dt><dd>{b}.</dd>' for a, b in groups[letter]) + "\n      </dl>\n    </section>\n"
    letters = "".join(f'<a href="#{l}">{l}</a>' for l in sorted(groups))
    html = HEAD.format(title=t["name"] + " - Glossary") + f'''  <main>
    <h1>{t["name"]} glossary</h1>
    <nav class="letters" aria-label="Jump to letter">{letters}</nav>
{body}  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 44rem; margin: 2rem auto; padding: 0 1rem; }
.letters { display: flex; gap: .4rem; flex-wrap: wrap; position: sticky; top: 0; background: #fff; padding: .5rem 0; }
.letters a { width: 2rem; height: 2rem; display: grid; place-items: center; border: 1px solid var(--line); border-radius: 6px; text-decoration: none; color: var(--ink); }
h2 { color: var(--brand); border-bottom: 2px solid var(--accent); scroll-margin-top: 4rem; }
dt { font-weight: 700; margin-top: .8rem; scroll-margin-top: 4rem; }
dt:target { background: #fff3b0; }
dd { margin: 0; color: var(--muted); }
'''
    return html, css


ptype(key="glossary", title="Glossary with letter navigation for {name}", level=2,
      brief="Build an A-Z glossary using description lists grouped under letter headings, a sticky letter navigation and highlighted :target entries.",
      goals=["Group dl entries under sections with ids", "Use :target to highlight a linked term", "Prevent sticky headers from hiding anchors with scroll-margin-top"],
      elements=["nav", "a", "section", "h2", "dl", "dt", "dd"], css=["position: sticky", ":target", "scroll-margin-top", "place-items", "flex-wrap"],
      steps=["Sort terms alphabetically and group by first letter.", "Write one section per letter with an id and a dl.", "Give each dt an id from its name.",
             "Write the letter nav with fragment links.", "Make the nav sticky.", "Add scroll-margin-top so targets are not hidden under the nav; highlight :target."],
      build=b_glossary, checklist=["Letter links jump correctly", "Target term highlighted", "Headings not hidden under sticky bar", "dt/dd pairs valid"],
      exercises=["Add a live filter input with JavaScript.", "Link terms to each other with <a href=\"#term\">.", "Add <dfn> around each term."])


def b_comparison(t):
    html = HEAD.format(title=t["name"] + " - Compare plans") + f'''  <main>
    <h1>Compare our packages</h1>
    <div class="plans">
      <section class="plan">
        <h2>Basic</h2>
        <p class="price">{t["items"][0][2]}</p>
        <ul><li>One {t["noun"]}</li><li>Email support</li><li class="no">No priority booking</li></ul>
        <a class="btn" href="#">Choose Basic</a>
      </section>
      <section class="plan featured">
        <p class="ribbon">Most popular</p>
        <h2>Standard</h2>
        <p class="price">{t["items"][1][2]}</p>
        <ul><li>Three {t["nouns"]}</li><li>Phone support</li><li>Priority booking</li></ul>
        <a class="btn" href="#">Choose Standard</a>
      </section>
      <section class="plan">
        <h2>Premium</h2>
        <p class="price">{t["items"][3][2]}</p>
        <ul><li>Unlimited {t["nouns"]}</li><li>Personal advisor</li><li>Priority booking</li></ul>
        <a class="btn" href="#">Choose Premium</a>
      </section>
    </div>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 64rem; margin: 2rem auto; padding: 0 1rem; text-align: center; }
.plans { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); align-items: start; }
.plan { position: relative; border: 1px solid var(--line); border-radius: 16px; padding: 2rem 1.5rem; background: #fff; }
.featured { border: 2px solid var(--brand); transform: scale(1.04); box-shadow: 0 16px 40px rgb(0 0 0 / 12%); }
.ribbon { position: absolute; top: -.8rem; left: 50%; translate: -50% 0; background: var(--brand); color: #fff; font-size: .75rem; padding: .2rem .8rem; border-radius: 999px; margin: 0; }
.price { font-size: 2rem; font-weight: 800; margin: .5rem 0 1rem; }
ul { list-style: none; padding: 0; text-align: left; }
li { padding: .4rem 0; border-bottom: 1px solid var(--accent); }
li::before { content: "\\2713 "; color: var(--brand); }
li.no { color: var(--muted); }
li.no::before { content: "\\2717 "; color: #999; }
.btn { display: block; margin-top: 1.5rem; padding: .7rem; border-radius: 999px; background: var(--brand); color: #fff; text-decoration: none; }
'''
    return html, css


ptype(key="plans", title="Pricing plans comparison for {name}", level=2,
      brief="Present three packages side by side with a highlighted, slightly enlarged middle plan, a 'most popular' ribbon and tick/cross feature lists.",
      goals=["Emphasise one card with transform: scale and a border", "Position a ribbon over the card edge", "Use ::before glyphs for ticks and crosses"],
      elements=["section", "h2", "p", "ul", "li", "a"], css=["transform: scale()", "position: absolute + translate", "align-items: start", "::before content", "box-shadow"],
      steps=["Write three .plan sections; give the middle one the featured class and a ribbon p.", "Grid the plans and align them to the start.", "Scale the featured plan and add a shadow.",
             "Position the ribbon at the top centre.", "Add ticks with ::before; crosses for .no items.", "Style the buttons."],
      build=b_comparison, checklist=["Ribbon centred", "Scaled card does not overlap on narrow screens (stacking)", "Features left-aligned", "Prices large and clear"],
      exercises=["Add a monthly/yearly toggle with :checked.", "Convert to a comparison table for many features.", "Animate the featured card on hover."])


def b_recipe_steps(t):
    a, b, c = t["items"][0]
    html = HEAD.format(title=f"How we make {a} - {t['name']}") + f'''  <main>
    <article class="howto">
      <h1>How we make {a}</h1>
      <p class="lead">{b}. Here is the process, step by step, from {t["person"]}.</p>
      <section class="need">
        <h2>You will need</h2>
        <ul>
          <li>Time: about 2 hours</li>
          <li>Skill level: beginner</li>
          <li>Cost: around {c}</li>
        </ul>
      </section>
      <h2>Steps</h2>
      <ol class="steps">
        <li><h3>Prepare</h3><p>Gather everything and read the whole process once.</p></li>
        <li><h3>Start</h3><p>Begin slowly; the first step sets the quality of the rest.</p></li>
        <li><h3>Check</h3><p>Compare against our standard. Adjust if needed.</p></li>
        <li><h3>Finish</h3><p>Rest, present and enjoy your {t["noun"]}.</p></li>
      </ol>
    </article>
  </main>
''' + FOOT
    css = BASE_CSS.format(**t) + '''main { max-width: 44rem; margin: 2rem auto; padding: 0 1rem; }
.lead { font-size: 1.2rem; color: var(--muted); }
.need { background: var(--accent); padding: 1rem 1.5rem; border-radius: 12px; }
.need h2 { margin-top: 0; font-size: 1rem; text-transform: uppercase; letter-spacing: .05em; }
.steps { list-style: none; padding: 0; counter-reset: step; }
.steps li { counter-increment: step; display: grid; grid-template-columns: 3rem 1fr; gap: 0 1rem; padding: 1rem 0; border-bottom: 1px solid var(--line); }
.steps li::before { content: counter(step); grid-row: 1 / 3; width: 3rem; height: 3rem; border-radius: 50%; background: var(--brand); color: #fff; display: grid; place-items: center; font-weight: 800; font-size: 1.2rem; }
.steps h3 { margin: 0; grid-column: 2; }
.steps p { margin: .2rem 0 0; grid-column: 2; color: var(--muted); }
'''
    return html, css


ptype(key="howto", title="Step-by-step how-to page for {name}", level=2,
      brief="Write a tutorial page with a 'you will need' box and numbered steps where each number is a large circle generated by CSS counters inside a grid row.",
      goals=["Use headings inside list items", "Generate step numbers with counters", "Use a two-column grid per list item with the ::before in the first column"],
      elements=["article", "h1", "p", "section", "h2", "ul", "ol", "li", "h3"], css=["counter-reset/increment", "grid-template-columns: 3rem 1fr", "grid-row: 1 / 3", "grid-column: 2", "border-radius: 50%"],
      steps=["Write the article with lead and 'You will need' section.", "Write the ol; each li has an h3 and a p.", "Remove list numbers and reset a counter.",
             "Make each li a grid of two columns.", "Put the counter in ::before spanning two rows.", "Place h3 and p in column two."],
      build=b_recipe_steps, checklist=["Numbers generated, list still an ol", "Headings inside li are h3", "Circle stays aligned with the heading", "Readable width"],
      exercises=["Add images to steps.", "Add a 'mark as done' checkbox per step with :has() styling.", "Add schema.org HowTo microdata."])


def b_kitchen_sink(t):
    html = HEAD.format(title=t["name"] + " - Complete site") + f'''  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <a class="logo" href="index.html">{t["name"]}</a>
    <nav aria-label="Main"><ul class="nav">
      <li><a href="#offers">{t["nouns"].capitalize()}</a></li><li><a href="#about">About</a></li><li><a href="#contact">Contact</a></li>
    </ul></nav>
  </header>
  <main id="main">
    <section class="hero">
      <h1>{t["tagline"]}</h1>
      <p>Welcome to {t["name"]} in {t["city"]}.</p>
      <a class="btn" href="#offers">Explore</a>
    </section>
    <section id="offers" class="wrap">
      <h2>Our {t["nouns"]}</h2>
      <div class="grid">
{chr(10).join(f'        <article class="card"><h3>{a}</h3><p>{b}.</p><p class="price">{c}</p></article>' for a, b, c in t["items"])}
      </div>
    </section>
    <section id="about" class="wrap about">
      <h2>About us</h2>
      <p>Founded by {t["person"]}. {t["tagline"]}.</p>
      <details><summary>Opening hours</summary><p>Saturday to Thursday 10:00 to 22:00, Friday 14:00 to 22:00.</p></details>
    </section>
    <section id="contact" class="wrap">
      <h2>Contact</h2>
      <form action="/contact" method="post" class="form">
        <label for="n">Name</label><input id="n" name="name" required>
        <label for="e">Email</label><input id="e" name="email" type="email" required>
        <label for="m">Message</label><textarea id="m" name="message" rows="4" required></textarea>
        <button>Send</button>
      </form>
    </section>
  </main>
  <footer class="site-footer"><p>&copy; 2026 {t["name"]} &middot; <a href="#main">Back to top</a></p></footer>
''' + FOOT
    css = BASE_CSS.format(**t) + '''.skip { position: absolute; left: -999px; } .skip:focus { left: 1rem; top: 1rem; background: #fff; padding: .5rem; z-index: 100; }
.site-header { position: sticky; top: 0; z-index: 10; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: .5rem 1rem; padding: .75rem 1rem; background: #fff; border-bottom: 1px solid var(--line); }
.logo { font-weight: 800; color: var(--brand); text-decoration: none; }
.nav { display: flex; gap: .25rem; list-style: none; margin: 0; padding: 0; }
.nav a { padding: .4rem .8rem; border-radius: 6px; text-decoration: none; color: var(--ink); }
.nav a:hover { background: var(--accent); }
.hero { background: var(--brand); color: #fff; text-align: center; padding: 4rem 1rem; }
.hero h1 { margin: 0 0 .5rem; font-size: clamp(1.8rem, 5vw, 3rem); }
.btn { display: inline-block; padding: .7rem 1.4rem; border-radius: 999px; background: #fff; color: var(--brand); text-decoration: none; font-weight: 700; }
.wrap { max-width: 60rem; margin: 0 auto; padding: 3rem 1rem; }
.grid { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr)); }
.card { background: var(--accent); padding: 1.25rem; border-radius: 12px; }
.card h3 { margin-top: 0; }
.price { font-weight: 700; color: var(--brand); }
.about { background: #fafafa; }
details { margin-top: 1rem; } summary { cursor: pointer; font-weight: 600; }
.form { display: grid; gap: .4rem; max-width: 30rem; }
.form label { font-weight: 600; margin-top: .6rem; }
.form input, .form textarea { padding: .6rem; border: 1px solid #bbb; border-radius: 8px; font: inherit; }
.form button { justify-self: start; margin-top: 1rem; padding: .7rem 1.4rem; border: 0; border-radius: 999px; background: var(--brand); color: #fff; font: inherit; }
.site-footer { text-align: center; padding: 1.5rem; border-top: 1px solid var(--line); color: var(--muted); }
h2 { scroll-margin-top: 4rem; }
'''
    return html, css


ptype(key="onepage", title="Complete one-page website for {name}", level=3,
      brief="Combine everything into a single-page site: skip link, sticky header with anchor navigation, hero, offers grid, about with details, contact form and footer.",
      goals=["Assemble a full page from components", "Use in-page anchor navigation with scroll-margin-top", "Provide a skip link"],
      elements=["a.skip", "header", "nav", "main", "section", "h1-h3", "article", "details", "summary", "form", "label", "input", "textarea", "button", "footer"],
      css=["position: sticky", "z-index", "scroll-margin-top", "grid auto-fit", "clamp()", "focus styles for skip link"],
      steps=["Write the skeleton with four sections that have ids.", "Add the sticky header with links to those ids.", "Add a skip link as the first element in body.",
             "Style the hero, grid, about and form.", "Add scroll-margin-top to h2 so anchors are not hidden by the header.", "Validate the whole page and test keyboard navigation."],
      build=b_kitchen_sink, checklist=["Skip link appears on first Tab", "Anchor links land below the sticky header", "One h1", "Form fully labelled", "Passes the W3C validator"],
      exercises=["Add smooth scrolling with scroll-behavior: smooth (respecting reduced motion).", "Add an Arabic RTL version.", "Split into multiple pages with a shared stylesheet."])


assert len(TYPES) == 45, len(TYPES)


def all_projects():
    """Yield 1000 project dicts: for each type, one per theme."""
    out = []
    n = 0
    for tp in TYPES:
        for th in THEMES:
            n += 1
            html, css = tp["build"](th)
            out.append(dict(
                number=n, key=tp["key"], theme=th, level=tp["level"],
                title=tp["title"].format(**th), brief=tp["brief"], goals=tp["goals"], elements=tp["elements"],
                css=tp["css"], steps=tp["steps"], html=html, css_code=css, checklist=tp["checklist"], exercises=tp["exercises"],
            ))
    return out
