# Product

## Register
Read, leaning Persuade: the project page of an open-source add-on. The visitor should understand what it does in one screen, trust that it will not lie for them, and know how to install it.

## What it is
Job Apply is an open-source add-on for Claude Code, Codex, Cursor and GitHub Copilot. It builds a master fact bank by interview (CV, LinkedIn export, reviews, then questions about numbers, baselines and the person's own part), then turns any job ad into a gated, tailored CV and cover letter, reviewed by a separate cynical reviewer and rendered to ATS-safe PDFs. Promise: tailored job applications that are true in every line.

## Surface
`docs/index.html`, served by GitHub Pages. One page. Sections: what it is, how an application runs (fetch, gate, map, write, check and review, render; this is a real sequence), the rules it enforces, the sample (Isolde Brackwater's CV, letter and reviewer verdict, from `docs/samples/` and `skills/job-apply/examples/isolde-brackwater/`), install for each tool (from README.md and install.sh), licence and author.

## Users
Experienced professionals applying for senior roles who already work with a coding agent: engineers, engineering managers, product and design leads. Sceptical of AI-written applications; they have read too many.

## Brand commitments
- Content comes only from README.md, SKILL.md, the references and the Isolde Brackwater example. No real person's data: no CV facts, employers or numbers from the author. The author appears only as a one-line credit with the repo link.
- No invented testimonials, user counts, stars or metrics. No prices.
- Plain short English, active voice, no em or en dashes, no marketing language ("supercharge", "effortless", "AI-powered").
- Show, do not claim: the reviewer's real FIX findings from the example (the "7 engineers when 5 of the 7 are" catch) are the strongest proof on the page.
- Standalone HTML, inline CSS and JS, works at 390 px and 1440 px with no sideways scroll, respects prefers-reduced-motion and dark mode, 4.5:1 contrast.
