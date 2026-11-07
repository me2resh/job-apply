# Writing rules

These rules apply to every document the skill writes: CVs, cover letters, messages, cold notes and form answers. When two rules pull in different directions, precedence is absolute:

**honesty > anti-cringe > voice > reviewer findings > JD criteria**

A JD criterion never licenses breaking a house rule. A reviewer finding that adds content is checked against the honesty and anti-cringe rules before it is applied, and is rejected the same way an honesty violation would be, even if a second reviewer agrees with it.

`scripts/check_doc.py` enforces the mechanical parts. The rest is judgement, and the reviewer checks it.

## 1. Honesty (never broken, even when it weakens the application)

- Every claim traces to a fact in `fact-bank.md`. If a needed fact is missing, ask or leave it out.
- Use the fact bank's phrasing locks word for word for team size, scope and tenure.
- Durations round down or stay exact. Four years and seven months is "four years", never "nearly five" and never "five".
- Headcount is exact. One report stays singular. A team of 7 with 5 engineers is "a team of 7, including 5 engineers", never "7 engineers".
- Influence is never written as line management. Leading as a tech lead, through a guild, or through standards is written as exactly that.
- A recent skill is not stretched by the length of the whole career. "14 years building software" and "two years of X" are different sentences.
- A proof of concept is a proof of concept. A pilot is a pilot. An integration is not platform ownership.
- Credit is split as the fact bank splits it. The user's part is "I"; the team's part is "we" or "the team".
- A cause is claimed only when the fact bank records it, and the dates must allow it.
- When the bank has no evidence for a criterion, the documents stay silent and the chat names it as a gap.

## 2. Anti-cringe

- Never editorialise relevance: no "directly relevant to", "this aligns with your", "exactly what you need". Placing the fact prominently is the argument.
- No superlatives about self or teams: "world-class", "elite", "cutting-edge", "best-in-class".
- No hobbies, lifestyle, health habits, photos, soft-skill self-ratings or quotes about oneself on a CV. This holds even when the JD lists personal passion or commitment as an essential criterion: that evidence goes to the letter or the interview, never the CV.
- Never tell readers what they already know: their own company, their own ad, their own org chart, their own job title.
- No flattery paragraph about the company.
- No planted imperfections. A deliberate typo reads as careless, not human. Authenticity comes from the user's own voice, specific numbers, and the sentence they rewrite in the human pass.
- No volatile metrics: star counts, follower counts, anything that drifts stale between writing and reading. Describe the thing and link it; the link carries the live number.

## 3. Voice

- Simple, direct English. Short sentences. The document must sound like the user (read `voice.md`), not like a template.
- No em dashes and no en dashes, anywhere, including headings. Use commas, colons or full stops in prose and plain hyphens in ranges: "Jan 2025 - Nov 2025", "12-18 months".
- Banned, as AI tells: "excited to", "thrilled", "passionate", "resonates", "aligns with", "delve", "landscape", "leverage" as a verb, "I believe that", "proven track record", "spearheaded", "honed", "testament to", "fast-paced", "results-driven", rule-of-three adjective stacks, and every word in the user's "Words I never use".
- Vary sentence length. Uniform rhythm is a tell.
- One conversational touch per document, at most ("actually", "in my own time", one dry line). Never two.
- Close directly: state the interest or the ask plainly, and stop.
- Write numbers as digits for outcomes; spell out small counts in prose where the user would ("two engineers").

## 4. CV content

- Bullets lead with the outcome or the value to the organisation. Process counts (tickets, surveys, tools, meetings) appear only as supporting evidence of scale, never as the achievement.
- Stack-agnostic, senior framing: name a technology only where it carries the point. No technology lists in bullets and no skills-keyword block.
- Earlier career is compressed to one line per job, with dates.
- Key Achievements is ordered by the JD's own priority order, and page 1 answers the JD's top three criteria.
- No hobbies, photos, self-ratings, quotes or references section.
- Never explain why a bullet matters to this employer.

## 5. ATS rules (built into the markdown, so every export parses)

- Single column, linear reading order. No tables, text boxes, columns, icons, images or graphics.
- Standard headings that parsers recognise: "Professional Experience", "Education", "Certifications". "Key Achievements" sits under the profile.
- Every role heading is **Job Title, Company**, separated by a comma (never a dash). The next line is the dates and place: `Jan 2025 - Nov 2025 | City, Country`. One date format everywhere.
- Mirror the JD's exact keyword forms where they are honestly true. When the JD uses an abbreviation, write it once with its expansion so both forms parse: "SRE (Site Reliability Engineering)", "CI/CD", "A/B tests".
- Contact details are plain text at the top, never in a page header or footer.
- Sanity check after rendering: the text copied out of the PDF reads in order. `check_doc.py --pdf` does this.

## 6. CV skeleton (in this order)

1. **Name** (`# First Last`), then the contact block on two or three lines: location and the right-to-work line from `profile.yaml` (verbatim; recruiters and filters scan for "sponsorship"), phone and email, links.
2. **Profile**: four or five lines answering "why credible for this role", in the JD's own vocabulary. No adjective without evidence.
3. **Key Achievements**: four to six bullets mapped to the JD's essential criteria, quantified from the fact bank, in the JD's priority order. This section wins the sift.
4. **Professional Experience**, newest first. Each role: heading, dates line, then an italic scope line (`*Scope: ...*`: what it covers, headcount stated exactly, reporting line, budget where known), then three to six achievement bullets chosen for this JD. Cut bullets that do not serve it.
5. **Earlier Career**: one line per job with dates.
6. **Talks, writing, open source**: short, described and linked, no volatile numbers. Move it higher only when the JD is centred on it.
7. **Education** and **Certifications**, with years.

Length: two to three pages. When a CV runs long, trim the bullets that serve this JD least before shrinking the type.

## 7. Cover letter

250 to 350 words, unless the format asks for something else (a public-sector statement of suitability: map to their criteria headings explicitly).

1. One or two lines on who the user is, anchored in the employer's problem.
2. The strongest JD-relevant story, with numbers and the baseline.
3. The differentiator: the one thing other candidates are unlikely to have, from the fact bank.
4. A direct close: availability and the ask. No begging, no paragraph of flattery about the company.

Name the company once. Do not repeat the job title back to the reader in place of the company.

## 8. Messages and cold notes

- Short: a recruiter reply or referral ask fits on a phone screen without scrolling (under about 120 words).
- One ask per message.
- Never tell the reader what they already know. Before showing a draft, re-read it as the recipient and delete every sentence they could have written themselves.
- Informal channel voice: first names, no "Dear", no sign-off block.
- A cold note says why this person, in one line, with a fact only someone who looked would know.
- Do not volunteer disqualifiers in a first contact (notice periods, gaps, constraints) unless asked.

## 9. Form answers

- Right to work, notice and availability: from `profile.yaml`, verbatim.
- Salary: the profile's phrasing with the number from the gate analysis, never below the floor.
- Team size and scope: the fact bank's phrasing locks.
- Motivation or "why us" boxes: the letter's rules, at the box's length. One concrete reason, tied to a fact.

## 10. The human pass

Before anything is sent, the user reads the final text aloud once and rewrites at least one sentence in their own words. A sentence they stumble over gets cut or simplified. Remind them every time documents are finished; it is the one gate only they can run.
