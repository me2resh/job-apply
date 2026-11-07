# Setup: building the fact bank by interview

The fact bank is only as good as the interview that built it. Ask for documents first and read them, so the questions fill gaps instead of repeating what the CV already says. Ask in small batches (one role, or one block of filters, at a time), never as a single wall of forty questions.

## 1. The folder

> Where should I keep your job-apply folder? It will hold your fact bank, your settings, a tracker, and one folder per application. I suggest `~/job-apply/`.

Create it, create `sources/` and `applications/` inside it, and write the absolute path to `~/.config/job-apply/home` (create the parent folder). Tell the user they can move it later by editing that file or setting `JOB_APPLY_HOME`.

## 2. Resources

Ask for everything at once and say why each one helps:

> Send or point me at anything you have. The more I read now, the fewer questions I ask.
> - Your current CV, in any format (PDF, Word, Google Doc export, text), and older versions if you have them. Older CVs often hold numbers you have since cut.
> - Your LinkedIn profile: paste the text, or the data export (Settings, Data privacy, Get a copy of your data).
> - Performance reviews and promotion cases. These hold dated numbers with evidence.
> - Portfolio, GitHub, personal site, talks, articles, podcasts.
> - Certificates and degrees, with years.
> - Anything else that records what you did: launch posts, internal write-ups, award citations, references.

Copy files into `sources/` (or note their paths). Read all of them. Draft the role list and every candidate fact you can find, each with the document it came from. Facts from a CV the user wrote are claims, not evidence: mark them "from CV" until the user confirms the number and its basis.

## 3. Roles, newest first

For each role, confirm or ask:

| Ask | Record as |
|---|---|
| Start and end month and year | `Mon YYYY - Mon YYYY` or `Present` |
| Exact title, and any title changes inside the role | separate entries for a promotion |
| Company: what it does in one line, rough size, location, remote or not | one line |
| Who did you report to? | title, not name |
| Direct reports: how many, which roles? | an exact number; "1 direct report" stays singular |
| Indirect reports, through managers or leads | exact, and through whom |
| People you led without managing (tech lead, guilds, programmes) | written as influence, never as reports |
| Budget you owned or influenced | owned versus input, and the amount |
| Systems, products, customers, scale | what it is and the numbers that describe it, with dates |

Then, for each achievement:

| Ask | Why |
|---|---|
| What changed, in one sentence? | the outcome leads every bullet |
| What is the number? | a checkable figure beats an adjective |
| What was it before? | a number without a baseline is a boast |
| Over what period, and when? | dates make it checkable and stop it drifting |
| What was your part, and what was the team's? | stops "I" claims for team work |
| What is the evidence, and where would someone find it? | a review, a dashboard, a post, a release note |
| Who would confirm it if asked? | role only, for the user's own reference |

Accept "I do not have a number". Record the achievement without one and say so; never estimate one for them. If the user gives a range or "about", keep it as given.

Probe for the facts people forget: promotions they caused, hires they made, things they stopped, money saved, incidents avoided, standards that others adopted, talks, open source, mentoring that led to promotions.

## 4. Skills, with recency

For each skill that matters to their target roles: first used, last used, depth (deep, working, past). This is what stops "15 years of experience" being read as 15 years of a skill picked up last year.

## 5. Filters and preferences

Ask each and whether it is hard (stop on fail) or a preference (score it):

- Location and remote: base, remote-only or remote-first or hybrid, the most office days they will accept.
- Salary floor: amount, currency, base or total, and the phrasing they use when asked ("GBP X base, flexible depending on the overall package").
- Right to work: where they can work without sponsorship, and the exact line they want on the CV.
- Industries they will not work for, and why. Ask whether the rule also covers roles at other companies whose work mainly serves that industry (an agency whose biggest client is one, a platform built for one).
- Employers they will not work for, and why.
- Notice period and earliest start; any dates they are unavailable.
- Seniority target and titles they would accept.
- Must-haves beyond pay: authority over hiring, budget, a product area, travel limits.

## 6. Voice

- Two or three pieces of writing they are happy with: an email, a post, a past cover letter they liked.
- Words and phrases they never use.
- Language notes: first or second language, British or American spelling, how formal they are, how they sign off.
- One question: "Read this sentence aloud. Would you say it?" with a sample line from their CV. Their answer calibrates everything after.

## 7. Write and confirm

Write `fact-bank.md`, `profile.yaml`, `voice.md` and `applications.md` from `templates/`, in the formats in `formats.md`. Then show the user:

- The roles and the achievement ids, one line each.
- The phrasing locks you propose (team size, scope, tenure), for them to approve word for word.
- The known gaps the interview revealed.
- The filters, read back as rules ("I will stop on any role under GBP X base").

Fix what they correct. Add the first change-log line: the date, "first version", and what it was built from.
