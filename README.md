# Job Apply

**Tailored job applications that are true in every line.**

Job Apply is an add-on for Claude Code, Codex and Cursor (and anything else that reads the Agent Skills format, with a rule file for GitHub Copilot). The first time you run it, it builds your master fact bank by interview: it reads your CV, LinkedIn export and reviews, then asks for the numbers, baselines, your part against the team's, and the evidence. After that, give it a job ad and it checks the role against your own filters, maps every criterion to a true fact, writes a tailored CV and cover letter, has a separate reviewer attack them, and renders ATS-safe PDFs. Nothing it writes says more than your fact bank can back.

Site: https://me2resh.github.io/job-apply/ (placeholder until published)

## What it does

| Command | What you get |
|---|---|
| `setup` | Your fact bank, profile and voice file, built by interview from your CV, LinkedIn, reviews and your answers |
| `update` | A new or corrected fact, with a dated change-log line |
| `apply <URL or pasted ad>` | Gate verdict, criteria mapped to your facts, tailored CV and letter, reviewer verdicts, PDFs, form answers, tracker row |
| `cv`, `letter`, `form` | One piece of the above |
| `message`, `cold` | A recruiter reply, referral ask or cold note, short and reviewed |
| `review` | The reviewer on any text you already have |
| `pdf` | A markdown CV or letter rendered to an ATS-safe A4 PDF |

## How an application runs

1. **Fetch the ad.** The page, then the hiring system's public JSON when the careers page blocks scripts, then an archived copy, then it asks you to paste it.
2. **Gate.** Your own filters, set at setup: pay floor, location and office days, right to work, industries and employers you will not work for, seniority, must-haves. Plus a scale check: their numbers against your largest true ones. You see APPLY, QUALIFY FIRST or SKIP before a word is written.
3. **Map.** Each criterion in the ad against your fact ids, marked strong, partial or gap. Gaps are told to you plainly and never papered over in the documents.
4. **Write.** A CV to a fixed, ATS-safe skeleton and a 250 to 350 word letter, in your voice, using the ad's vocabulary where it is honestly true.
5. **Check and review.** A script fails the documents on dashes, banned phrases, star counts and untraced numbers. Then a separate reviewer, a cynical talent partner, returns SHIP or FIX with line-level findings and the questions an interviewer would ask. Up to two rounds.
6. **Render.** PDFs with generic filenames (`First-Last-CV.pdf`), one folder per application, a tracker row, and a reminder: read it aloud and rewrite one sentence in your own words.

## Rules the skill enforces

- Every claim traces to your fact bank. A missing fact is asked for or left out.
- Durations round down. Headcounts are exact. Influence is never written as line management. A recent skill is not stretched by the length of your career.
- The gate runs before any writing, and only on filters you set.
- No em or en dashes, no AI-tell phrases, no flattery about the company, no telling readers what they already know.
- No hobbies, photos, self-ratings or star counts on a CV, even when the ad asks for "passion".
- Precedence: honesty, then anti-cringe, then voice, then reviewer findings, then the ad.
- The author never reviews its own work.
- It never sends anything. You do, after the human pass.

## Your data

Everything lives in one folder you choose at setup (suggested `~/job-apply/`): `fact-bank.md`, `profile.yaml`, `voice.md`, `applications.md`, and `applications/<Company>-<Role>/` for each role. Plain markdown and YAML, so you can read and edit all of it. Nothing leaves your machine except the job-ad fetches.

## Install

Claude Code, one line:

```
/plugin install job-apply --marketplace me2resh/job-apply
```

Older Claude Code, two steps: `/plugin marketplace add me2resh/job-apply`, then `/plugin install job-apply@job-apply`. From the shell: `claude plugin install job-apply --marketplace me2resh/job-apply`. The skill then answers to `/job-apply` (or `/job-apply:job-apply`), and the plugin adds the `job-apply-reviewer` agent.

Codex and other agents that read the Agent Skills format: clone the repo and run `./install.sh codex` (copies `skills/job-apply/` into `~/.codex/skills/`), or `./install.sh /path/to/your/agent/skills`. Cursor: copy `.cursor/rules/job-apply.mdc` into your project. Copilot: copy `.github/copilot-instructions.md`. Anything else: add `AGENTS.md` to its instructions and keep `skills/job-apply/` readable. Without the plugin agent, the reviewer runs as a fresh context with `references/reviewer.md` as its brief.

Then ask: *"Set up job apply"*, and later *"Apply for this: https://..."* or *"Reply to this recruiter: ..."*.

**Needs:** Python 3 (standard library only) and Chrome, Chromium, Edge or Brave for the PDFs (`CHROME=/path` to pick one). `pdftotext` (poppler) or `pip install pypdf` enables the PDF page-end and text-layer checks.

## The scripts

```
python3 skills/job-apply/scripts/render_pdf.py cv.md out/First-Last-CV.pdf --variant editorial|modern|executive
python3 skills/job-apply/scripts/check_doc.py cv.md --facts fact-bank.md --facts profile.yaml --voice voice.md --pdf out/First-Last-CV.pdf
```

`render_pdf.py` turns the CV or letter markdown into an A4 PDF with embedded print CSS, creates the output folder, lets a long role break between bullets instead of leaving half a page blank, and reports the page count. `check_doc.py` fails on em and en dashes, banned phrases, relevance editorialising, star and follower counts, CV images, tables and hobbies, and headings stranded at a page end; it warns on numbers that are not in the fact bank, long sentences, and letter length. Both run green on the example: `python3 docs/build/build_samples.py`.

## Example

`skills/job-apply/examples/isolde-brackwater/` follows one invented person from fact bank to sent application, including two reviewer rounds in which the first caught two real inflation errors. The rendered [CV](docs/samples/Isolde-Brackwater-CV.pdf) and [cover letter](docs/samples/Isolde-Brackwater-Cover-Letter.pdf) are in `docs/samples/`.

## Repository

```
.claude-plugin/plugin.json             plugin manifest
.claude-plugin/marketplace.json        this repo is also its own marketplace
agents/job-apply-reviewer.md           the reviewer as a Claude Code agent (generated from references/reviewer.md)
skills/job-apply/SKILL.md              the skill (Agent Skills format)
skills/job-apply/references/           setup interview, file formats, gates, writing rules, reviewer, print styles
skills/job-apply/templates/            blank fact bank, profile, voice file, tracker
skills/job-apply/examples/             one invented person, end to end
skills/job-apply/scripts/              render_pdf.py, check_doc.py
docs/build/build_samples.py            renders and checks the example, regenerates the reviewer agent
docs/samples/                          the example PDFs
AGENTS.md                              generic agent instructions (Codex and others)
.cursor/rules/                         Cursor rule
.github/copilot-instructions.md
docs/                                  the website
install.sh                             copies the skill for agents without plugins
```

## Licence

MIT.
