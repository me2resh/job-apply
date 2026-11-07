# Fetching the JD, and the gate check

## Fetching the JD

Try in this order. Save the result as `jd.md` with the URL, the date and the route that worked (`fetch_route` in the front matter).

1. **The page itself.** Fetch the URL. Many careers pages render the ad with JavaScript or return 403 to scripts; if the text is missing or blocked, go on.
2. **The applicant-tracking system's public JSON.** Most careers pages sit on an ATS with a public endpoint. Work out the system from the URL, the page source, or the "apply" link.

   | System | How to spot it | Public endpoint |
   |---|---|---|
   | Greenhouse | `boards.greenhouse.io/<org>`, `job-boards.greenhouse.io`, `gh_jid=` in the URL | `https://boards-api.greenhouse.io/v1/boards/<org>/jobs/<id>` (one job) or `/jobs?content=true` (all) |
   | Lever | `jobs.lever.co/<org>/<id>` | `https://api.lever.co/v0/postings/<org>/<id>` or `https://api.lever.co/v0/postings/<org>?mode=json` |
   | Ashby | `jobs.ashbyhq.com/<org>` | `https://api.ashbyhq.com/posting-api/job-board/<org>?includeCompensation=true` |
   | Workable | `apply.workable.com/<org>` | `https://apply.workable.com/api/v3/accounts/<org>/jobs` (POST) |
   | SmartRecruiters | `jobs.smartrecruiters.com/<org>` | `https://api.smartrecruiters.com/v1/companies/<org>/postings/<id>` |
   | Teamtailor | `<org>.teamtailor.com` | `https://<org>.teamtailor.com/jobs.rss`; each job page carries JSON-LD |
   | Personio | `<org>.jobs.personio.de` | `https://<org>.jobs.personio.de/xml` |
   | Recruitee | `<org>.recruitee.com` | `https://<org>.recruitee.com/api/offers/` |

   Job pages often embed a `JobPosting` JSON-LD block (`<script type="application/ld+json">`) with the full text, dates, location and sometimes pay, even when the visible page is blank.
3. **An archived copy.** `https://web.archive.org/web/2026*/<url>` or the availability API `https://archive.org/wayback/available?url=<url>`. Say which date's copy was read. Archived ads are also how the office-days check finds what an older version of the ad said.
4. **A search snippet** for the exact title and company on job aggregators. Mark the text as a snippet; do not treat it as the full ad.
5. **Ask the user to paste it.** Say what was tried. Never guess an ad's content.

A LinkedIn job view is behind a login. Ask the user to paste it rather than fetch it.

## The gate check

Run every gate before writing anything, against the user's own `profile.yaml`. Never apply a filter the user did not set. Show the result in chat as a table, then the verdict.

| Gate | What to check | On fail |
|---|---|---|
| Already tracked | `applications.md` for the company and role, including roles ruled out before | show the earlier verdict; ask before redoing |
| Excluded industries | The company's core business, and what the role's labour directly serves. When `includes_roles_serving_them` is set, a role at a supplier, agency or platform whose main customers are in the excluded industry also fails. | hard: SKIP. If the company is unnamed (a recruiter ad), say the gate cannot run and recommend getting the name first. |
| Excluded employers | Name, parent company, recent acquirer | hard: SKIP |
| Salary floor | The band in the ad against the floor, in the same currency and basis (base against base) | hard and below floor: SKIP. Not stated: proceed and flag "band unknown, qualify before investing interview time". |
| Right to work | Location of the role against the user's right-to-work countries; sponsorship offered or not | SKIP when the user needs sponsorship and the ad says none |
| Location and office days | Remote, hybrid or on site; days per week or month; read every live and archived version of the ad, because the office line changes | preference: name the trade-off. Five days on site against a remote-first preference: recommend SKIP unless something exceptional. |
| Seniority and must-haves | Title, reporting line, and whether the role owns real scope (hiring, budget, a product area) | name what is missing |
| Scale | Their scale claims against the user's largest honest numbers (the fact bank's Scale section), on the axis the role is about | see below |
| Culture and office signals | Review sites (the user pastes them if the pages block automated reads) and every ad's office line | report red flags in the table |

**Scale gate.** Compare the company's own scale words (users, devices, sites, events a day, engineers, "tens of millions", "a hundred engineers") with the user's largest true numbers from the fact bank. Say the ratio out loud. When theirs is ten times or more beyond the user's on the axis the role is about, it is a stretch role: the verdict is at best QUALIFY FIRST, and say the odds plainly. Lead and head roles at fast-growing companies are often decided on this axis in the first technical round. In interview, the user names the gap once and moves to the mechanism that transfers; never inflate to close it.

**Culture red flags.** Hiring commitments not kept (offers below an agreed figure, hybrid overturned after joining); a founder or CEO described as running every team; five days on site in the ads against a hybrid line on the careers page; positive reviews clustered by date and role.

## Verdicts

- **APPLY**: every hard gate passes and the mapping has strong evidence for most essential criteria.
- **QUALIFY FIRST**: a hard gate cannot be checked (band unknown, company unnamed, office days unclear), or the role is a stretch on scale. The next step is the three disqualifying questions in writing: the band, the office days, and the role's authority over hiring and budget. Prepare interview material only after the answers clear the filters.
- **SKIP**: a hard gate fails. Stop. If the user overrides, log "SKIP, overridden: <reason>" in the tracker and carry on.

Show with the verdict: the per-gate table, a realistic read of competitiveness, and two or three things to lead with, each tied to a fact-bank id.

Urgency is not fit. A hiring manager who speeds up because the user has another process is reacting to competition, not to evidence. Note it and keep the gates in order.

If the Cold Read skill is installed, offer a join-lens read of the company before the first interview. The research belongs in the interview, not in the letter.
