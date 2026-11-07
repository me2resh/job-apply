# Examples

One invented person, end to end: Isolde Brackwater, a mobile engineering manager in Leeds, applying to Brindlecove for a Senior Engineering Manager, Mobile role. Every person, company, number and link here is invented. Each coined company and person name was checked against the web when written and matched nothing. Links point at `example.com`, and the phone number is in a range reserved for drama.

| File | What it shows |
|---|---|
| `isolde-brackwater/fact-bank.md` | The master fact bank as setup leaves it: roles, achievement ids with baselines and own-versus-team parts, phrasing locks, known gaps, change log |
| `isolde-brackwater/profile.yaml` | Contact block and her own filters (pay floor, remote, two excluded industries) |
| `isolde-brackwater/voice.md` | Writing samples and the words she never uses |
| `isolde-brackwater/applications.md` | The tracker, with an APPLY, a SKIP on an excluded industry, and a QUALIFY FIRST on an unnamed company |
| `.../Brindlecove-Senior-Engineering-Manager-Mobile/jd.md` | The ad as fetched, with the route that worked |
| `.../gate-and-mapping.md` | The gate table, the criteria, and the mapping to fact ids with strong, partial and gap |
| `.../cv.md`, `.../cover-letter.md` | The tailored documents, after review |
| `.../review.md` | Two reviewer rounds: round 1 caught two real inflation errors ("7 Android and iOS engineers" when 5 are; a cause the dates did not allow); round 2 shipped both |
| `.../form-answers.md` | Ready-to-paste answers |
| `.../Isolde-Brackwater-CV.pdf`, `...-Cover-Letter.pdf` | Rendered with `scripts/render_pdf.py --variant modern` |

Run the checks yourself, from `skills/job-apply/`:

```
E=examples/isolde-brackwater; A=$E/applications/Brindlecove-Senior-Engineering-Manager-Mobile
python3 scripts/render_pdf.py $A/cv.md $A/Isolde-Brackwater-CV.pdf --variant modern
python3 scripts/check_doc.py $A/cv.md --facts $E/fact-bank.md --facts $E/profile.yaml --voice $E/voice.md --pdf $A/Isolde-Brackwater-CV.pdf
```
