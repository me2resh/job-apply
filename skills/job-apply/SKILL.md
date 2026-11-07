---
name: job-apply
description: Tailored job applications from a master fact bank. First run builds the fact bank by interview (current CV, LinkedIn export, reviews, achievements with numbers, baselines and evidence), plus the user's hard filters and voice. After that, give it a job ad URL or pasted JD and it gates the role against the user's own filters, maps every criterion to a true fact, writes a tailored CV and cover letter, runs an adversarial review, renders ATS-safe PDFs and logs the application. Also writes recruiter replies, referral asks, cold notes and form answers. Use it when someone wants to apply for a job, tailor a CV, write a cover letter, answer an application form, reply to a recruiter, or set up or update their career facts. Trigger on "apply for this", "tailor my CV", "write a cover letter", "should I apply", "help me with this application", "update my CV facts", "set up job apply", even when the user just pastes a job link.
tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
keywords: [job application, CV, resume, cover letter, ATS, job hunt, recruiter, application form, fact bank, interview prep]
---

# Job Apply

Write job applications that are tailored to each role and true in every line. The skill keeps one master fact bank per person, built once by interview and updated after every interview or win. Each application then draws only on that bank: the CV and letter can be shaped to the job ad, but they can never say more than the bank holds.

## The idea in one paragraph

Most tailored CVs fail in one of two ways: they are generic, or they stretch the truth to fit the ad. Both are fixed by the same move: separate the facts from the writing. The fact bank holds every claim with its date, its number, its baseline, the person's own part and the evidence. The application step chooses and orders those facts for one reader, in that reader's vocabulary, and a separate reviewer attacks the result before anyone sends it. The user's own filters (pay floor, location, industries they will not work for) gate the role before a word is written, so no time goes on a job they would not take.

## Where the data lives

One folder per person, chosen at setup (suggest `~/job-apply/`). Find it in this order: the `JOB_APPLY_HOME` environment variable; the path written in `~/.config/job-apply/home`; `~/job-apply/` if it exists. If none exists, run setup.

```
<home>/
  fact-bank.md        every usable claim, dated and sourced, with a change log
  profile.yaml        contact block, hard filters, preferences, output settings
  voice.md            writing samples, words never used, language notes
  applications.md     the tracker: one row per role looked at
  sources/            copies of what the user gave at setup (old CVs, reviews, exports)
  applications/<Company>-<Role-Title>/
    jd.md                       the ad as fetched, with date, URL and how it was read
    gate-and-mapping.md         gate verdict, criteria, mapping table (private)
    cv.md, cover-letter.md      the markdown sources
    review.md                   reviewer verdicts, rounds, what was applied and why
    form-answers.md             ready-to-paste answers
    <First>-<Last>-CV.pdf
    <First>-<Last>-Cover-Letter.pdf
```

File formats are in `references/formats.md`; blank starting files are in `templates/`. A full worked example for an invented person is in `examples/isolde-brackwater/`.

## Selectors

The first word picks the job; everything after it is the JD, URL, file or context. Combine with `+` (`cv+letter <url>`). No selector means `full`.

| Selector | Produces | Gates |
|---|---|---|
| `setup` | Builds the fact bank, profile and voice by interview | none |
| `update` | Adds or corrects facts; dated change-log entry | none |
| `full` (default) | Gate, mapping, CV, letter, review, PDFs, form answers, tracker | full |
| `cv` | Tailored CV, reviewed, PDF on approval | full |
| `letter` | Cover letter, reviewed | full |
| `form` | Application-form answers | full |
| `message` | Recruiter reply or referral ask (DM voice) | quick |
| `cold` | Cold note to a named hiring manager (needs who, and why them) | quick |
| `review` | The reviewer on any existing text or file | none |
| `pdf` | Render an existing CV or letter markdown to PDF | none |

Quick gate: check the tracker for an earlier verdict and the hard filters against what is known about the company; say when a real application would need the full gate. A three-line DM does not need the full pipeline. The review applies to every generated document, messages included, and the human-pass reminder applies to everything that will be sent.

## Rules that make the output trustworthy

- **The fact bank is the only source.** Every claim in every document traces to a fact in `fact-bank.md`. If a needed fact is missing, ask the user or leave it out. Never invent, extrapolate or round up. New facts go into the bank first (via `update`), then into documents.
- **Honesty beats fit.** Durations round down or stay exact. Headcounts are stated exactly, and a single report is never pluralised. Influence is never written as line management. A recent skill is never stretched by the length of the whole career. A proof of concept is never written as production experience. When the bank has no evidence for a criterion, the documents stay silent and the chat names it as a gap.
- **Gate before writing.** The verdict (APPLY, QUALIFY FIRST, SKIP) is shown in chat before any document is written. A SKIP stops the run unless the user overrides it, and the override is logged.
- **Precedence is absolute:** honesty rules, then anti-cringe rules, then voice rules, then reviewer findings, then JD criteria. A JD criterion never licenses breaking a house rule. A reviewer suggestion that adds content is checked against the honesty and anti-cringe rules before it is applied.
- **The author never reviews its own work.** The reviewer runs as a separate agent or a fresh context (`references/reviewer.md`).
- **The user has the last word.** Nothing is sent by the skill. The user reads the final text aloud and rewrites at least one sentence in their own words.

The full writing rules are in `references/writing-rules.md`. Read them before writing any document.

## Setup

Run on first use, or when the user says `setup`. The interview script is `references/setup.md`; follow it. In outline:

1. Ask where to keep the folder (suggest `~/job-apply/`), create it, and write the path to `~/.config/job-apply/home`.
2. Ask for every resource at once: current CV in any format, LinkedIn profile text or data export, performance reviews, promotion cases, portfolio, GitHub, talks, writing, certificates, references. Copy what they give into `sources/`. Read all of it before asking questions, so the interview only asks what the documents do not answer.
3. Walk the roles in reverse order. For each: dates (month and year), exact title, company and what it does, reporting line, direct and indirect headcount stated exactly, budget, systems. Then each achievement: the outcome, the number, the baseline, the period, the user's own part against the team's, and the evidence. Push for numbers; accept "no number" and record it as such.
4. Ask the filters and preferences: location and remote, salary floor and currency (and whether it is hard), right to work and visa needs, industries or employers they will not work for and why, notice and availability, seniority target, must-haves.
5. Ask for voice: two or three writing samples they are happy with, words they never use, language notes.
6. Write `fact-bank.md`, `profile.yaml`, `voice.md` and an empty `applications.md` from `templates/`. Show the user the fact bank and the phrasing locks, and fix anything they correct. Close by naming the known gaps the bank revealed.

## Update

`update <what changed>`: after an interview, a new achievement, a correction, a new number. Ask the same per-achievement questions as setup, write the fact into the right role, and add a dated line to the change log at the bottom of the fact bank. When a correction changes a number that already went into sent documents, say which applications in the tracker used it.

## Apply

`apply <URL or pasted JD>` (or `full`). Read `fact-bank.md`, `profile.yaml`, `voice.md` and `applications.md` first.

1. **Tracker check.** If the company and role are already in `applications.md`, show the earlier verdict and ask before redoing work.
2. **Fetch the JD.** Follow the fallbacks in `references/gates.md`: the page, then the applicant-tracking system's public JSON, then an archived copy, then a search snippet marked as such, then ask the user to paste it. Save it as `jd.md` with the URL, the date and the route that worked.
3. **Gate check.** Run every gate in `references/gates.md` against `profile.yaml`: tracker, excluded industries and employers (including roles whose work mainly serves them), salary floor, right to work, location and office days, seniority and must-haves, the scale ratio, culture and office signals. Show the verdict and the per-gate table in chat before writing anything. Stop on SKIP.
4. **Criteria.** List the JD's essential and desirable criteria in the ad's own words, and classify the role type, which sets the emphasis.
5. **Persona.** Before writing, take on the vocabulary and altitude of the ideal candidate for this role. Same facts, different lens: product language for a product role, delivery and organisation language for an engineering leadership role, the competency framework for public sector.
6. **Mapping.** Map each criterion to fact-bank ids with a strength: strong, partial or gap. Write it to `gate-and-mapping.md`. State the gaps plainly in chat. Never paper over a gap in a document.
7. **Write the CV** to the skeleton in `references/writing-rules.md`, then **the cover letter**.
8. **Check.** Run `python3 scripts/check_doc.py <doc.md> --facts <home>/fact-bank.md --facts <home>/profile.yaml --voice <home>/voice.md` on each document and fix every failure. Warnings about numbers mean a claim may not trace to the bank: trace it or cut it.
9. **Adversarial review.** Send each document, with the JD, the fact bank and the voice file, to the reviewer. Apply the findings that are clearly right; keep the original where a finding conflicts with a house rule, and note why. If the verdict is FIX, review again after fixing, at most two rounds, then show the user what is unresolved. Save every round to `review.md`. Always show the user the verdict, the READ TEST line, the findings applied and rejected, and the WOULD-CHALLENGE list, which is their interview prep.
10. **PDFs**, after the user approves the markdown: `python3 scripts/render_pdf.py cv.md "<folder>/<First>-<Last>-CV.pdf" --variant <variant>` and the same for the letter, then `check_doc.py ... --pdf <the pdf>` for page-end headings and the text layer. Filenames stay generic: the reader sees the filename, and a company name in it advertises per-company tailoring. Variant choice and page-break rules: `references/print-styles.md`.
11. **Form answers** to `form-answers.md`: right to work, notice and availability, salary (from the profile's phrasing and the gate analysis), team size in the bank's phrasing lock, and the motivation box written to the same rules as the letter.
12. **Close in chat:** the verdict, the two or three things to lead with, the honest gaps, the reviewer verdicts, the paths of the PDFs, and the human-pass reminder: read it aloud once, and rewrite at least one sentence in your own words. A sentence you stumble over gets cut.
13. **Tracker.** Offer once to log the role in `applications.md`: date, company, role, link, verdict, gate notes (band, office days, open questions), status, folder, next step.

## Messages and cold notes

`message` and `cold` use the DM rules in `references/writing-rules.md`: short, one ask, and never tell the reader what they already know (their own company, their own ad, their own org). Before showing a draft, re-read it as the recipient and delete every sentence they could have written themselves. A cold note needs a named person and a real reason for writing to them; if either is missing, ask.

## Pitfalls learned the hard way

- Careers pages often block scripts; the applicant-tracking system behind them usually has public JSON. See `references/gates.md`.
- A JD that asks for personal passion or lifestyle evidence does not make it CV content. That evidence goes to the letter or the interview, never the CV.
- A fast-moving hiring manager is reacting to competition, not to fit. Keep the gates in order.
- When the gate says weak fit, the next step is three disqualifying questions in writing (band, office days, authority over hiring and budget), not interview prep.
- Volatile numbers (stars, followers) go stale between writing and reading. The bank keeps them as dated facts; documents link the thing instead.
- When a CV runs long, let a long role break between bullets rather than leaving half a page blank, and trim to two or three pages. Check that no heading sits in the last three lines of a page.
- Create the application folder before rendering; the renderer does, but a hand-run Chrome command does not.
- Never plant typos or fake errors to look human. Authenticity comes from the user's own sentence in the human pass.
