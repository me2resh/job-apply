---
name: Job Apply
description: Tailored job applications that are true in every line.
colors:
  review-indigo: "#3b33a6"
  review-indigo-hover: "#4a42b8"
  review-paper: "#f2f1f7"
  review-sheet: "#fcfcff"
  ink: "#1c1a35"
  ink-quiet: "#4b4868"
  rule: "#d8d6e6"
  rule-strong: "#b9b6cf"
  on-indigo: "#ffffff"
  on-indigo-quiet: "#d6d3f7"
  struck-rose-bg: "#fbe4e8"
  struck-rose: "#99152f"
  traced-mint-bg: "#dcf2e4"
  traced-mint: "#12633a"
  partial-amber-bg: "#fbeecb"
  partial-amber: "#734700"
  lit-lilac: "#e6e3fb"
  night-paper: "#14131d"
  night-sheet: "#1b1a28"
  night-ink: "#ebe9f7"
  night-rail: "#2b2575"
  night-indigo-text: "#bcb6ff"
  night-ink-quiet: "#b4b1cd"
  night-rule: "#312f47"
  night-rule-strong: "#4a4766"
  night-on-indigo-quiet: "#cdc9f5"
  night-rail-hover: "#3a3394"
  struck-rose-rule: "#efb3bf"
  traced-mint-rule: "#9fd6b3"
  partial-amber-rule: "#e8c77a"
  night-struck-rose-bg: "#3b1620"
  night-struck-rose: "#ffb3c0"
  night-struck-rose-rule: "#6b2a3a"
  night-traced-mint-bg: "#10301f"
  night-traced-mint: "#91e4b0"
  night-traced-mint-rule: "#2a5e40"
  night-partial-amber-bg: "#33270b"
  night-partial-amber: "#f3c96d"
  night-partial-amber-rule: "#66501d"
  night-lit-lilac: "#2c2856"
typography:
  display:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2.6rem, 1.2rem + 3.9vw, 4.75rem)"
    fontWeight: 850
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2rem, 1.3rem + 2.4vw, 3.25rem)"
    fontWeight: 800
    lineHeight: 1.04
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 750
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  code:
    fontFamily: "Martian Mono, ui-monospace, SF Mono, Menlo, monospace"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.6
    fontVariation: "'wdth' 87.5"
  verdict:
    fontFamily: "Martian Mono, ui-monospace, monospace"
    fontSize: "clamp(5rem, 2rem + 11vw, 9.5rem)"
    fontWeight: 800
    lineHeight: 0.8
    letterSpacing: "-0.04em"
    fontVariation: "'wdth' 112.5"
  lede:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1.1875rem"
    fontWeight: 400
    lineHeight: 1.6
  body-small:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.55
  caption:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
  wordmark:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 800
  chain:
    fontFamily: "Schibsted Grotesk, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 700
  code-small:
    fontFamily: "Martian Mono, ui-monospace, monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "Martian Mono, ui-monospace, monospace"
    fontSize: "0.6875rem"
    fontWeight: 700
    letterSpacing: "0.04em"
rounded:
  focus: "3px"
  token: "4px"
  hunk: "6px"
  control-inner: "7px"
  control: "8px"
  verdict: "10px"
  pill: "999px"
spacing:
  row: "28px"
  inset: "16px"
  gutter-mobile: "16px"
  gutter-desktop: "56px"
  section: "112px"
components:
  command-copy:
    backgroundColor: "{colors.review-indigo}"
    textColor: "{colors.on-indigo}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "44px"
  command-copy-hover:
    backgroundColor: "{colors.review-indigo-hover}"
  verdict-fix:
    backgroundColor: "{colors.struck-rose-bg}"
    textColor: "{colors.struck-rose}"
    typography: "{typography.label}"
    rounded: "{rounded.token}"
  verdict-ship:
    backgroundColor: "{colors.traced-mint-bg}"
    textColor: "{colors.traced-mint}"
    typography: "{typography.label}"
    rounded: "{rounded.token}"
  verdict-partial:
    backgroundColor: "{colors.partial-amber-bg}"
    textColor: "{colors.partial-amber}"
    typography: "{typography.label}"
    rounded: "{rounded.token}"
  hunk:
    backgroundColor: "{colors.review-sheet}"
    textColor: "{colors.ink}"
    typography: "{typography.code}"
    rounded: "{rounded.hunk}"
  rail:
    backgroundColor: "{colors.review-indigo}"
    textColor: "{colors.on-indigo-quiet}"
    width: "232px"
---

# Design System: Job Apply

## Overview

**Creative North Star: "The Review Diff"**

The page is a code review of a job application. Claims are diff lines; every line carries a blame column that names the fact it rests on, and the reviewer's comments sit on the lines they caught. The visitor reads it the way an engineer reads a pull request: the struck line, the true line beneath it, the reason in between.

The ground is a cool violet-grey review paper with white sheets for every file, diff and comment. One indigo owns structure: the full-height rail that carries navigation, the copy action, step markers and fact ids. Everything else is ink. Colour beyond that is state and nothing else.

Density sits between documentation and a review tool: large confident grotesk headings, generous section spacing, and mono only where the content is code, data, file names or verdicts.

**Key Characteristics:**
- A full-height indigo rail on desktop that becomes a top bar on phones.
- Diff hunks with line numbers, a sign column and a blame column as the main content surface.
- Review comments as the only lifted surfaces.
- Verdict tokens (FIX, SHIP, APPLY, SKIP, QUALIFY FIRST, strong, partial, gap) in a fixed colour law.
- One display-scale verdict, set once.

## Colors

A restrained ground with one structural indigo and three state colours that each mean exactly one thing.

### Primary
- **Review Indigo** (#3b33a6): the rail, the copy button, step markers, blame text, the first link in the precedence chain, pressed fact ids, focus rings and link text in light mode. On the dark theme the rail deepens to Night Rail (#2b2575), buttons and markers use Review Indigo Hover (#4a42b8), and indigo text becomes Night Indigo Text (#bcb6ff).

### Neutral
- **Review Paper** (#f2f1f7): page ground. Night Paper (#14131d) in dark.
- **Review Sheet** (#fcfcff): files, hunks, comments, command boxes, cards. Night Sheet (#1b1a28) in dark.
- **Ink** (#1c1a35): headings and body. Night Ink (#ebe9f7) in dark.
- **Ink Quiet** (#4b4868): secondary text, ledes, blame text, line numbers (7.7:1 on paper).
- **Rule** (#d8d6e6) and **Rule Strong** (#b9b6cf): 1px hairlines between rows and around sheets.
- **Lit Lilac** (#e6e3fb): the highlight on a line and fact when a fact id is chosen.

### State
- **Struck Rose** (#99152f on #fbe4e8): removed lines, FIX, SKIP, gap.
- **Traced Mint** (#12633a on #dcf2e4): added lines, SHIP, APPLY, strong, Applied.
- **Partial Amber** (#734700 on #fbeecb): partial, QUALIFY FIRST.

### Named Rules
**The Colour Law Rule.** Rose only for what may not be written, mint only for what traces and ships, amber only for partial and QUALIFY FIRST. No state colour ever decorates.

**The One Indigo Rule.** Indigo is structure and action, never a background wash for content.

## Typography

**Display Font:** Schibsted Grotesk (with ui-sans-serif, system-ui)
**Body Font:** Schibsted Grotesk
**Label/Mono Font:** Martian Mono, set at 87.5% width (112.5% for the verdict), self-hosted from `docs/fonts/`

**Character:** A newsroom grotesk for the claims and a wide engineering mono for the evidence. The grotesk is set heavy and tight; the mono is condensed so diff lines keep a readable measure.

### Hierarchy
- **Display** (850, clamp(2.6rem, 1.2rem + 3.9vw, 4.75rem), 0.98, -0.04em): the page promise only.
- **Headline** (800, clamp(2rem, 1.3rem + 2.4vw, 3.25rem), 1.04, -0.03em): section heads.
- **Title** (750, 1.25rem, 1.25): step and sub-section heads.
- **Body** (400, 1.0625rem, 1.6): prose, held to 65ch. Ledes at 1.1875rem in Ink Quiet.
- **Code** (Martian Mono 400, 0.75 to 0.875rem, 1.6 to 1.75): diff lines, files, commands, fact ids.
- **Label** (Martian Mono 700, 0.6875rem, 0.04em): verdict tokens and WHY labels.
- **Verdict** (Martian Mono 800 at 112.5% width, clamp(5rem, 2rem + 11vw, 9.5rem)): the single FIX.

### Named Rules
**The Evidence Is Mono Rule.** Mono is for code, file names, fact ids, commands and verdicts. Claims, headings and explanations stay in the grotesk.

## Layout

Desktop (960px and up): a fixed 232px rail on the left; content in a column capped at 1120px with 56px side padding. Below 960px the rail becomes a top bar with wrapping section links. Below 720px side padding drops to 16px, diff blame columns move above their line, and two-column blocks stack. Sections are separated by 112px; section heads sit 44px above their content. Steps in the flow are full-width rows: marker, text, then the file that step leaves. Nothing scrolls sideways; long commands and diff lines wrap.

## Elevation & Depth

Flat by default. Depth comes from paper against sheet and 1px rules. The only shadow is on review comments.

### Shadow Vocabulary
- **Comment lift** (`box-shadow: 0 10px 28px -12px rgba(28, 26, 53, 0.28), 0 2px 6px -2px rgba(28, 26, 53, 0.12)`): reviewer comments anchored under a line.

### Named Rules
**The Only The Reviewer Floats Rule.** A review comment is the one surface that lifts off the sheet.

## Shapes

Small, square-ish corners from the review world: 3px on focus rings, 4px on tokens and fact ids, 6px on hunks and files, 8px on command boxes, comments and sample links (7px inside the joined copy button), 10px on the display-scale verdict, full pills only for the precedence chain. Borders are 1px. Step markers are circles.

## Components

### Buttons
- **Shape:** joined to its command box, right corners 7px.
- **Primary (Copy):** Review Indigo with white text, 44px tall, 16px side padding, drawn copy icon that swaps to a check and the word "Copied".
- **Hover / Focus:** Review Indigo Hover; 2px indigo focus ring offset 2px.

### Chips
- **Verdict tokens:** mono 700 at 0.6875rem, state background, state text, matching 1px border, 4px radius.
- **Fact ids:** outlined mono buttons; hover and pressed fill with indigo.

### Cards / Containers
- **Hunks and files:** Review Sheet, 1px Rule Strong border, 6px radius, a mono header strip with the file name in Ink and context in Ink Quiet.
- **Sample links:** Review Sheet, 8px radius, indigo underlined title, lift 2px on hover.

### Navigation
- **Rail:** section links in the grotesk, no numbering; current section filled with Review Indigo Hover and set bold; white focus ring. On phones, a top bar with wrapping links.
- **Tabs:** underline tabs with a 3px indigo bar on desktop; outlined segments under 600px.

### Diff Line (signature)
A grid of line number, sign, text and blame. Removed lines are Struck Rose with the text struck through; added lines are Traced Mint. The blame column names the fact file and fact, always in indigo ink, so the indigo line runs through the evidence. On phones the blame sits under its line, never above it. Choosing a fact id lights every line and fact that share it in Lit Lilac.

## Do's and Don'ts

### Do:
- **Do** trace every visible claim in a demo to a file in the example and label invented material as invented.
- **Do** keep state colours to their law: rose (#99152f) removed and FIX, mint (#12633a) added and SHIP, amber (#734700) partial.
- **Do** draw icons as SVG with a 1.5px stroke.
- **Do** keep the strike-through draw as the only entrance motion, and switch it off under reduced motion.

### Don't:
- **Don't** use em or en dashes anywhere in copy.
- **Don't** set prose, headings or explanations in mono.
- **Don't** add shadows to anything but review comments.
- **Don't** use counts, stars, testimonials or prices as proof.
