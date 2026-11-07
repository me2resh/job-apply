# Print styles

`scripts/render_pdf.py` embeds the CSS; this file says which variant to pick and what the layout rules are. Every variant has the same ATS-safe structure: one column, real text, no tables, images or icons, A4, no page header or footer.

## Variant by company type

Ask the user when the choice is unclear, offering the two closest. The default lives in `profile.yaml` (`output.cv_variant`).

| Company or role type | Variant | Look |
|---|---|---|
| B2B software, scale-ups, general tech (default) | `editorial` | Charter serif body, Avenir Next small-caps headings, ink blue |
| AI-native, developer tools, product-led, consumer apps | `modern` | Avenir Next throughout, teal, left-bar headings |
| Public sector, boards, investor-backed, traditional companies | `executive` | Georgia throughout, burgundy, heavier rules |

Fonts fall back to Georgia or Helvetica Neue and Arial where the named fonts are missing (Linux, Windows). The structure does not change.

## Shared rules

- `@page { size: A4; margin: 18mm 20mm }`.
- Body 10 to 10.8pt, line height about 1.4, near-black on white.
- The name is the largest text, in the accent colour. Section headings use the accent colour. The accent never colours body text.
- Role headers: title and company bold, then a line with the place on the left and the dates floated right with tabular figures. The float keeps the text order linear, so an ATS reads title, dates, place in order.
- Scope lines are italic and grey; bullets have 3pt spacing.
- Links print as plain text in the body colour: the URL or label is readable on paper and clickable in the PDF.

## Page-break rules

- A heading never sits at the bottom of a page: `h2, h3 { break-after: avoid }`, and the dates and scope lines stay with the heading.
- `p, li { orphans: 3; widows: 3 }`.
- A role of five bullets or fewer never splits across pages.
- A longer role may break between bullets, with its heading kept on its first bullet. This avoids leaving half a page blank when a CV runs long. `--strict-roles` turns this off.
- After rendering, run `check_doc.py <cv.md> --pdf <cv.pdf>`. It fails when a heading falls in the last three lines of a page, and checks that the text layer reads in order. Then look at the PDF: each page should end at a natural boundary.
- When a CV runs past three pages, cut the bullets that serve this JD least and render again. Do not shrink the type below 10pt.

## Filenames

`<First>-<Last>-CV.pdf` and `<First>-<Last>-Cover-Letter.pdf`, in the application's folder. Never add the company: the hiring team sees the filename. The PDF's title metadata is set from the name heading for the same reason.
