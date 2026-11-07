---
name: Job Apply
description: Tailored job applications that are true in every line.
colors:
  ink: "#14202c"
  paper: "#e9edf0"
  raised: "#f6f8fa"
  muted: "#5b6977"
  rule: "#c9d1d8"
  code: "#dfe4e8"
  fix-red: "#a3382e"
  strong-green: "#2e7a4e"
  partial-amber: "#9a6416"
  gap-grey: "#6e7781"
  sheet: "#ffffff"
  sheet-rule: "#d7dde3"
  sheet-link: "#0f4c75"
  night-paper: "#0f161d"
  night-raised: "#16202a"
  night-ink: "#e6ebf0"
  night-muted: "#98a4b0"
  night-rule: "#2a3642"
  night-code: "#1b2631"
  night-fix-red: "#e07a6c"
  night-strong-green: "#6fcf8b"
  night-partial-amber: "#e0a93a"
  night-gap-grey: "#9aa3ad"
typography:
  display:
    fontFamily: "Bricolage Grotesque, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(40px, 8.5vw, 84px)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "-0.035em"
    fontVariation: "'opsz' 96"
  headline:
    fontFamily: "Bricolage Grotesque, Helvetica Neue, Arial, sans-serif"
    fontSize: "30px"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Bricolage Grotesque, Helvetica Neue, Arial, sans-serif"
    fontSize: "20px"
    fontWeight: 600
  brand:
    fontFamily: "Bricolage Grotesque, Helvetica Neue, Arial, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    letterSpacing: "-0.01em"
  tag:
    fontFamily: "Bricolage Grotesque, Helvetica Neue, Arial, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  sheet-body:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "15.5px"
    lineHeight: 1.55
  label:
    fontFamily: "Bricolage Grotesque, Helvetica Neue, Arial, sans-serif"
    fontSize: "13px"
    fontWeight: 700
  note:
    fontFamily: "Bricolage Grotesque, Helvetica Neue, Arial, sans-serif"
    fontSize: "14px"
    fontWeight: 400
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "13.5px"
    lineHeight: 1.5
rounded:
  focus: "2px"
  sheet: "2px"
  button: "4px"
  code: "6px"
  mark: "50%"
spacing:
  gutter: "20px"
  column-gap: "40px"
  section: "48px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.button}"
    padding: "12px 18px"
  button-primary-hover:
    backgroundColor: "{colors.fix-red}"
    textColor: "{colors.sheet}"
  button-quiet:
    textColor: "{colors.ink}"
    rounded: "{rounded.button}"
    padding: "12px 18px"
  button-quiet-hover:
    backgroundColor: "{colors.raised}"
  sheet:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    typography: "{typography.sheet-body}"
    rounded: "{rounded.sheet}"
    padding: "44px 52px 36px"
  code-block:
    backgroundColor: "{colors.code}"
    typography: "{typography.code}"
    rounded: "{rounded.code}"
    padding: "14px 16px"
---

# Design System: Job Apply

## Overview

**Creative North Star: "The Cold Read family"**

Job Apply's page follows the system of the Cold Read project page (`cold-read/docs/index.html`), so the author's skill pages read as one family. Same fonts, same cool grey ground and ink, same spacing, the same top nav, the same hero (heavy headline and short sans intro on the left with two buttons, a ruled evidence table on the right), serif body text in sections, thin dividers between sections, and white paper sheets for finished documents. When Cold Read's system changes, this page follows it.

The one difference Job Apply takes, as Tayyib does with its green, is its accent: a brick red (#a3382e) where Cold Read uses amber for hover, focus and the selected tab. It is the colour of the reviewer's FIX. The three marks keep the family's meaning: green for strong, amber for partial, grey for gap.

**Key Characteristics:**
- Name left, plain links right; links hide on phones.
- The hero table, "What the ad asks" against "What the fact bank shows", is the page's one visual event, with round marks that stamp in.
- Sections are separated by 1px rules and set in Source Serif 4; headings and interface text are Bricolage Grotesque.
- Finished documents (reviewer rounds, the sample application) sit on white sheets that stay light in dark mode.

## Colors

The family's cool grey paper and dark slate ink, three mark colours, and one accent of Job Apply's own.

### Primary
- **Slate Ink** (#14202c): text, the dark Install button, the hero table's top rule.
- **FIX Red** (#a3382e): primary button hover, focus rings, the selected tab, struck draft lines and FIX or SKIP labels.

### Neutral
- **Cool Grey Paper** (#e9edf0): page ground. **Raised** (#f6f8fa): quiet button hover. **Muted** (#5b6977): ledes, notes, source lines. **Rule** (#c9d1d8): dividers. **Code** (#dfe4e8): command blocks.
- **Sheet** (#ffffff) with **Sheet Rule** (#d7dde3): paper documents, always light.

### Marks
- **Strong Green** (#2e7a4e), **Partial Amber** (#9a6416), **Gap Grey** (#6e7781). Amber is a shade darker than Cold Read's (#b4761a) so it passes 4.5:1 as small text on a white sheet.

### Named Rules
**The Family Rule.** Tokens come from Cold Read. Job Apply changes only the accent.

**The Three Marks Rule.** ✓ green strong, ~ amber partial, ? grey gap. Nothing else uses those colours.

## Typography

**Display Font:** Bricolage Grotesque (with Helvetica Neue, Arial)
**Body Font:** Source Serif 4 (with Georgia)
**Mono:** the system monospace stack, for commands only

**Character:** a heavy, optically sized grotesque for headlines and interface, a calm serif for reading.

### Hierarchy
- **Display** (700, clamp(40px, 8.5vw, 84px), 0.95, -0.035em): the hero headline only.
- **Headline** (600, 30px, 1.1): section heads.
- **Title** (600, 16 to 20px): sub-heads, step names, sheet titles.
- **Body** (Source Serif 4, 17px, 1.6): prose, held to 66ch. Ledes in Muted.
- **Tag** (Bricolage, 19px, 1.4): the hero intro.
- **Note and label** (Bricolage, 13 to 14px): source lines, captions, mark labels.

## Layout

A single 1080px column with 20px side padding. The hero is a 5:6 grid with a 40px gap; it stacks under 860px. Sections have 48px vertical padding and a 1px top rule. Steps are a ruled list in three columns (name, what it does, what it left in the example) that stacks on phones. Uses and rules are two columns that stack on phones. Install is two columns: the tabbed command on the left, the things to ask on the right.

## Elevation & Depth

Flat, except for paper. Sheets carry the family's paper shadow.

### Shadow Vocabulary
- **Paper on a desk** (`box-shadow: 0 1px 0 rgba(0,0,0,.06), 0 12px 32px rgba(0,0,0,.18)`): white sheets only.

## Shapes

Nearly square: 2px on sheets and focus rings, 4px on buttons, 6px on code blocks. Marks are 34px circles with a 1.5px border in the mark colour.

## Components

### Buttons
- **Primary:** Slate Ink fill, paper text, 4px radius, 12px by 18px; hover fills FIX Red.
- **Quiet:** 1.5px ink outline; hover fills Raised.
- **Copy:** small outlined button in the corner of each command block; hover inverts to ink.

### Tabs
Text tabs on a 1px rule; the selected tab is ink with a 3px FIX Red underline. Arrow keys move between them.

### The ledger (signature)
A 2px ink top rule, a muted header row, then rows of quote (italic serif), fact (serif) with a small source line, and a round mark. Marks stamp in one after another; with reduced motion they are simply there.

### Reviewer finding
On a sheet: a label column (Draft, Reviewer or Why, Shipped) and a text column. Drafts are struck in FIX Red, shipped lines are bold in Strong Green, and the lead finding carries the reviewer's comment behind a 2px red rule.

## Do's and Don'ts

### Do:
- **Do** copy new family tokens from Cold Read before inventing any.
- **Do** keep sheets white in both themes.
- **Do** give every claim in a demo a source line and label invented material as invented.

### Don't:
- **Don't** use em or en dashes in copy.
- **Don't** add a second accent; FIX Red is the only one.
- **Don't** use the mark colours for anything but the three marks and their verdict labels.
