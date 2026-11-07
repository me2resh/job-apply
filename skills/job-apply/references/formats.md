# File formats

Four files hold everything about the person. The worked example in `examples/isolde-brackwater/` shows each one filled in; blank versions are in `templates/`.

## fact-bank.md

Markdown, so the user can read and edit it. Sections in this order:

1. **Front matter**: `type: fact-bank`, `owner`, `updated` (YYYY-MM-DD).
2. **Status**: current role and since when; time in role type, computed to the month with the wording to use ("four years", never "nearly five"); career length; notice; why they are looking, and whether that may be said in a document.
3. **Scale, honest largest numbers**: the biggest true figures on each axis (users, load, team, budget, money, sites), each dated and sourced. The scale gate reads this section. Say what is absent too ("no budget owned").
4. **Roles**, newest first. Heading `### <Title>, <Company> (Mon YYYY - Mon YYYY)`. One line on the company. Then reporting line, direct reports (exact, with the mix), indirect, influence without management, systems, peers. Then `#### Achievements`, each with an id:
   ```
   - **QM-01 Short name.**
     - Outcome: what changed.
     - Number / Period / Baseline: as known; write "no number" when there is none.
     - My part: what the person did.
     - Team part: what others did.
     - Evidence: where it can be checked.
     - Strength: (optional) partial, with the wording limit, e.g. "never 'in production'".
   ```
   Ids are a short company code plus a number. The mapping table and the reviewer cite them.
5. **Earlier career**: one line per job with dates. Older roles do not need achievement detail.
6. **Skills, with recency**: table of skill, first used, last used, depth.
7. **Education and certifications**, with years.
8. **Talks, writing, open source**: each with a link. Volatile numbers (stars, followers) are allowed here only as dated facts and are never printed in a document.
9. **Phrasing locks**: exact wordings the person approved for sensitive claims (team size, scope, tenure, leadership without management). Documents use these words, not paraphrases.
10. **Known gaps**: what the person has not done that their target roles often ask for. Named honestly in chat; never papered over.
11. **Change log**: newest first, `- YYYY-MM-DD: what changed and why (source)`.

## profile.yaml

```yaml
updated: YYYY-MM-DD
name: {first: , last: }
contact:
  location:                 # "City, Country"
  right_to_work_line:       # printed on the CV, verbatim
  phone:
  email:
  links: [{label: , url: }]
filters:
  location: {base: , remote: remote-only|remote-first|hybrid-ok|onsite-ok, max_office_days_per_month: , hard: }
  salary: {floor: , currency: , basis: base|total, hard: true, default_phrasing: "... {X} ..."}
  right_to_work: {countries: [], needs_sponsorship_elsewhere: }
  excluded_industries: [{name: , reason: , includes_roles_serving_them: true, hard: true}]
  excluded_employers: [{name: , reason: }]
  notice:
  available_from:
  unavailable: []           # date ranges, YYYY-MM-DD to YYYY-MM-DD
  seniority_target: []
  must_haves: []
output:
  cv_variant: editorial|modern|executive
  applications_dir: applications
```

Every filter carries `hard: true` (stop on fail) or `hard: false` (score and name the trade-off). The skill never applies a filter the user did not set.

## voice.md

Front matter, then `## How I write`, `## Writing samples` (quoted), `## Words I never use` (one per bullet; `check_doc.py --voice` fails on these), `## Language notes`.

## applications.md

```
# Applications

| Date | Company | Role | Link | Verdict | Gate notes | Status | Folder | Next step |
|---|---|---|---|---|---|---|---|---|
```

Verdict: APPLY, QUALIFY FIRST, SKIP (and "SKIP, overridden: <reason>" if the user went ahead). Status: drafted, sent, screening, interviewing, offer, rejected, withdrawn. Gate notes keep the open questions (band unknown, office days unclear) so nothing is lost between sessions.

## The application folder

`applications/<Company>-<Role-Title>/`, with hyphens for spaces and no special characters. Contents as listed in `SKILL.md`. The PDFs carry generic names (`<First>-<Last>-CV.pdf`, `<First>-<Last>-Cover-Letter.pdf`), never the company.

## CV and letter markdown

The renderer (`scripts/render_pdf.py`) reads a small, fixed subset of markdown: `#` name, `##` sections, `###` role headings, paragraphs, `-` bullets, `**bold**`, `*italic*`, links. Two conventions matter:

- The line after a role heading is `Mon YYYY - Mon YYYY | Place`. The renderer floats the dates right; the text order stays linear for an ATS.
- A role's scope line is a whole-line italic paragraph: `*Scope: ...*`.

Front matter (`type`, `company`, `role`, `date`, `variant`) is allowed and skipped by both scripts.
