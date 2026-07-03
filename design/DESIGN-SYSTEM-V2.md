# FPS Contracting — "Bespoke v2" Design System (APPROVED)

Approved by Anthony for the homepage + projects/portfolio redesign.
Interactive mockups: `mockup-homepage-v2.html`, `mockup-projects-v2.html`
(self-contained; open in any browser — images embedded as data URIs).

## Design tokens
```css
--ink:   #12161C;   /* primary dark (softened from pure black) */
--navy:  #0C2D4E;   /* brand navy — buttons, dark surfaces */
--blue:  #0F6EBF;   /* brand blue — DEMOTED to links only */
--paper: #FAF9F6;   /* warm paper page ground (replaces white/#F1F4F7) */
--stone: #F2F0EB;   /* warm alt-section ground */
--hair:  #E7E4DD;   /* hairline dividers (replaces boxes/borders) */
--gray:  #6B7280;   /* body gray */
--brass: #A98D5F;   /* THE accent — used rarely: eyebrow rules,
                       active filter tick, hover underlines */
```

## Typography (real build uses existing Archivo + Libre Franklin)
- Display: Archivo **weight 300**, tight tracking (-.025em), large clamp sizes;
  `<em>` inside headings = weight 600 for emphasis words. NEVER 900 for big headings.
- Labels ("caps"): 9.5–10.5px, weight 600, letter-spacing .28–.34em, uppercase.
- Serif accent: Georgia italic — mission line, pull quotes, featured-work caption. Sparingly.
- Body: Libre Franklin 300, 13.5–15.5px.

## Signature elements
- 26px × 1px **brass rule** before eyebrow labels.
- **Underline reveal** links: 28px brass underline grows to 100% on hover
  (background-size transition). No arrows-in-circles, no pills.
- Cards: NO boxes/borders — image with caption BELOW on the page ground;
  meta line "SECTOR · LOCATION" small-caps with brass middot; title 600;
  one-line summary; "View Case Study" underline link.
- Image hover: slow zoom `transform 1.1s cubic-bezier(.2,.6,.2,1)` scale(1.035).
- Images get `filter:saturate(.94)` for cohesion.
- Hairline (`--hair`) dividers structure sections; generous 110–130px section padding.

## Page structures
### Homepage (mockup-homepage-v2.html)
1. Hero: slideshow, scrim, caps eyebrow "NEW YORK GENERAL CONTRACTOR — EST. 1983",
   H1 light "Driven by quality. / *Defined by results.*", positioning line,
   sub line, [Request a Project Review] solid btn + "View Our Work" underline link.
   Right column: serif-italic "Featured Work" caption tied to slides. Brass dots.
2. Proof band: hairline-bounded row — 40+ / 500+ / 50+ / 6 / NYC / occupied-healthcare.
3. Mission: two-col; H2 light w/ 600 em; serif italic mission copy.
4. Featured Projects (stone bg): 3 editorial cards (4:5), captions below, View All btn.
5. Sector index: two-column hairline list (ToC style) → deep-links to portfolio filters.
6. Quote band (ink bg): serif italic large quote, Avi Kahn.
7. CTA: light section, H2 light+em, contact facts as hairline rows.
8. Compact footer.

### Projects page (mockup-projects-v2.html)
1. Hero (66vh): image + scrim, "Projects that shape *New York* spaces."
2. Serif-italic intro line.
3. Sticky left sector rail (plain text + counts, brass tick on active);
   mobile: horizontal scroll row with brass underline active state.
4. Editorial grid: 2-col, 64px row gaps, captions below.
5. Case-study modal: 21:9 hero, meta, light title, Overview/Challenge/Solution/Result
   with brass-tick section headers, Scope list in hairline right column, gallery strip,
   related projects, ink CTA band w/ serif line.
6. Lightbox: near-black, thin chevrons, counter, Esc/arrows/swipe.

## Sectors (9 filters)
All · Healthcare · Commercial Interiors · Institutional · Supportive Housing ·
Luxury Residential · Kitchens & Baths · Roofing & Waterproofing · Occupied Renovations
(projects can belong to multiple sectors)

## Implementation notes
- Static HTML/CSS/JS only — no frameworks. Keep existing nav/footer/contact/fonts.
- All 28 existing projects carry over; each needs: sector(s), one-line summary,
  and (for case studies) Overview/Challenge/Solution/Result — DRAFT copy exists in the
  mockup PROJECTS array for 9 projects; facts must be reviewed by FPS before launch.
- Homepage keeps 4-slide hero + progress bar from live site, restyled.
- Blueprint watermark: keep, but consider reducing opacity on paper ground.
- OPEN QUESTION (user hasn't decided): brass accent is new to brand —
  fallback is swapping brass → navy hairlines if they want strictly on-brand.

---
# V3 ADDENDUM (pending approval — supersedes v2 structures if approved)
Same tokens/typography as v2. New in v3 (`mockup-*-v3.html`):
- PROJECTS: full-page case-study OVERLAY replaces modal — 82vh cinematic hero
  (image settles from scale 1.06), fixed index badge "04 / 09" + round close btn,
  facts bar (Sector/Location/Setting/Scope count), serif lede, chapters with brass-tick
  headers, TWO full-bleed images inline between chapters, 3-col gallery -> lightbox,
  ink CTA row, full-width "Next Project" teaser (cycles projects).
- PROJECTS grid: 12-col staggered editorial pattern (pos-a 1/8 4:3, pos-b 8/13
  portrait +96px offset, pos-c 1/6 portrait, pos-d 6/13 16:10 +56px), index numbers
  01/02..., pattern reassigned by JS after each filter. Mobile: single col, offsets off.
- Mobile filters: sticky swipeable row under nav (not left rail).
- HOMEPAGE: cinematic full-vh hero w/ Ken Burns slides, slide index "01 — 03",
  animated brass progress line, serif caption per slide; centered statement section;
  proof band w/ count-up stats in hairline columns; featured work as ALTERNATING
  editorial rows (7/5 grid, mirrored); sector index w/ sticky hover image PREVIEW
  column (desktop); serif quote on ink; closing spread "Let's build." (huge light
  type) + contact hairline rows + slim footer merged.
- Motion: IntersectionObserver reveals, count-ups, Ken Burns, slide progress —
  all gated by prefers-reduced-motion.
