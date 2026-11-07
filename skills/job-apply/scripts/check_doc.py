#!/usr/bin/env python3
"""Check a CV, cover letter, message or form answer against the house rules (references/writing-rules.md).

Usage:
  python3 check_doc.py <doc.md> [--facts fact-bank.md] [--facts profile.yaml] [--voice voice.md]
                       [--kind cv|letter|message|form] [--pdf rendered.pdf]

Fails (exit 1) on: em or en dashes; banned AI-tell phrases (built in, plus the "Words I never use"
list in voice.md); relevance editorialising; volatile metrics (star, follower, fork counts); on a CV,
images, tables, quotes, hobbies or self-ratings; with --pdf, a heading in the last three lines of a
page, or a PDF with no text layer.
Warns on: numbers in the document that do not appear in any --facts file; sentences over 28 words;
letter or message length; CV headings an ATS will not recognise; mixed date formats; headings out of
reading order in the PDF text.

The kind is guessed from the file name (letter, message, form, else cv) when not given.
"""
import argparse, pathlib, re, shutil, subprocess, sys

DASHES = {"—": "em dash", "–": "en dash", "‒": "figure dash", "―": "horizontal bar",
          "&mdash;": "em dash entity", "&ndash;": "en dash entity"}

BANNED = [  # fail: phrases that read as generated or as filler
    r"excited to", r"thrilled", r"passionate", r"passion for", r"resonat(e|es|ed|ing)",
    r"delv(e|es|ed|ing)", r"landscape", r"leverag(e|es|ed|ing)", r"I believe that",
    r"proven track record", r"track record of success", r"world[- ]class", r"elite", r"cutting[- ]edge",
    r"best[- ]in[- ]class", r"synerg(y|ies|istic)", r"tapestry", r"testament to", r"in today'?s",
    r"fast[- ]paced", r"game[- ]changer", r"results[- ]driven", r"hit the ground running", r"go[- ]getter",
    r"rock ?star", r"ninja", r"guru", r"outside the box", r"spearhead(ed|ing|s)?", r"unwavering",
    r"I am writing to (apply|express)", r"dream (job|role|company)", r"honed",
]
EDITORIALISING = [  # fail: telling the reader why a fact matters instead of placing it well
    r"directly relevant", r"highly relevant", r"relevant to your", r"exactly what you", r"just what you need",
    r"aligns? with (your|the role|the position|the job)", r"\baligns with\b", r"makes me (a|an|the) (great|good|ideal|perfect)",
    r"perfect fit", r"ideal candidate", r"great fit for",
]
WATCH = [  # warn: often fine, often filler
    r"dynamic", r"seamless(ly)?", r"robust", r"furthermore", r"moreover", r"utili[sz]e", r"journey",
    r"I am confident", r"I feel that", r"very unique",
]
VOLATILE = r"\b\d[\d,.]*\s?[kK]?\+?\s*(GitHub\s+)?(stars?|followers?|forks?|subscribers?|watchers?|likes?|claps?)\b"
WORDNUM = {w: str(i) for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty".split())}
WORDNUM.update({"thirty": "30", "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80",
                "ninety": "90", "hundred": "100", "dozen": "12", "half": "50"})
MONTH = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
DATE_LINE = re.compile(r"^\d{1,2} (January|February|March|April|May|June|July|August|September|October|"
                       r"November|December) \d{4}$")


def strip_front_matter(text):
    m = re.match(r"\A---\n.*?\n---\n", text, re.S)
    return text[m.end():] if m else text


def plain(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"<(https?://|mailto:)[^>]+>", "", s)
    s = re.sub(r"https?://\S+", "", s)
    return re.sub(r"[*_`#>]", "", s).strip()


def numbers(text):
    """Every number-like token, normalised: 10,000 -> 10000; 2.5m -> 2.5; 'twelve' -> 12."""
    text = re.sub(r"https?://\S+|mailto:\S+|\]\([^)]*\)", " ", text)
    found = set()
    for m in re.finditer(r"(?<![\w.])\d[\d,]*(\.\d+)?", text):
        tok = m.group(0).rstrip(",").replace(",", "")
        found.add(tok)
        if "." in tok:
            found.add(tok.rstrip("0").rstrip("."))
    for w in re.findall(r"[A-Za-z]+", text):
        if w.lower() in WORDNUM:
            found.add(WORDNUM[w.lower()])
    return found


def voice_banned(path):
    words, on = [], False
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if re.match(r"^##+ ", line):
            on = "never use" in line.lower()
            continue
        m = re.match(r"^\s*[-*]\s+(.+)$", line)
        if on and m:
            w = re.sub(r"\s+\(.*\)$", "", m.group(1)).strip().strip("\"'`")
            if w:
                words.append(re.escape(w))
    return words


def pdf_lines_with_position(pdf):
    """[(page_no, page_height, line_text, y_bottom)] from pdftotext -bbox-layout, or None."""
    if not shutil.which("pdftotext"):
        return None
    r = subprocess.run(["pdftotext", "-bbox-layout", str(pdf), "-"], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    out = []
    for pn, pm in enumerate(re.finditer(r'<page width="[\d.]+" height="([\d.]+)">(.*?)</page>', r.stdout, re.S), 1):
        height = float(pm.group(1))
        for lm in re.finditer(r'<line xMin="[\d.]+" yMin="[\d.]+" xMax="[\d.]+" yMax="([\d.]+)">(.*?)</line>', pm.group(2), re.S):
            words = re.findall(r"<word[^>]*>(.*?)</word>", lm.group(2))
            out.append((pn, height, " ".join(words), float(lm.group(1))))
    return out


def pdf_text(pdf):
    if shutil.which("pdftotext"):
        r = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
    try:
        from pypdf import PdfReader  # optional
        return "\f".join(p.extract_text() or "" for p in PdfReader(str(pdf)).pages)
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("doc")
    ap.add_argument("--facts", action="append", default=[])
    ap.add_argument("--voice")
    ap.add_argument("--kind", choices=["cv", "letter", "message", "form"])
    ap.add_argument("--pdf")
    a = ap.parse_args()
    path = pathlib.Path(a.doc).expanduser()
    name = path.name.lower()
    kind = a.kind or ("letter" if "letter" in name else "message" if ("message" in name or "dm" in name)
                      else "form" if "form" in name else "cv")
    text = strip_front_matter(path.read_text(encoding="utf-8"))
    lines = text.splitlines()
    fails, warns = [], []

    # dashes, everywhere including headings and date ranges
    for i, l in enumerate(lines, 1):
        for ch, label in DASHES.items():
            if ch in l:
                fails.append(f"line {i}: {label}; use a comma, colon or full stop (plain hyphen in ranges)")

    banned = BANNED + (voice_banned(a.voice) if a.voice else [])
    for i, l in enumerate(lines, 1):
        p = plain(l)
        for pat in banned:
            m = re.search(rf"(?<!\w){pat}(?!\w)", p, re.I)
            if m:
                fails.append(f"line {i}: banned phrase '{m.group(0)}'")
        for pat in EDITORIALISING:
            m = re.search(pat, p, re.I)
            if m:
                fails.append(f"line {i}: editorialising '{m.group(0)}'; place the fact, do not explain its relevance")
                break
        for pat in WATCH:
            m = re.search(rf"\b{pat}\b", p, re.I)
            if m:
                warns.append(f"line {i}: '{m.group(0)}' is often filler; keep only if it carries meaning")
        m = re.search(VOLATILE, p, re.I)
        if m:
            fails.append(f"line {i}: volatile metric '{m.group(0)}'; describe and link the thing instead")
        if p.count("!") > 0 and kind in ("cv", "letter"):
            warns.append(f"line {i}: exclamation mark")

    # CV structure (ATS)
    heads = [(i, len(m.group(1)), m.group(2).strip()) for i, l in enumerate(lines, 1)
             for m in [re.match(r"^(#{1,3})\s+(.*)$", l)] if m]
    if kind == "cv":
        if not lines or not any(h[1] == 1 for h in heads):
            fails.append("CV needs the name as the '# ' heading")
        for i, l in enumerate(lines, 1):
            if l.lstrip().startswith("!["): fails.append(f"line {i}: image; an ATS cannot read it and CVs carry no photos")
            if re.match(r"^\s*\|.*\|\s*$", l): fails.append(f"line {i}: table; keep a CV single column, no tables")
            if l.lstrip().startswith(">"): fails.append(f"line {i}: quote block; no quotes about yourself")
            if re.search(r"[★☆●○]|\b\d\s?/\s?(5|10)\b", l):
                fails.append(f"line {i}: self-rating; drop the scale")
        h2s = [h[2] for h in heads if h[1] == 2]
        for h in h2s:
            if re.search(r"hobb|interests|personal|about me|references", h, re.I):
                fails.append(f"heading '{h}': no hobbies, personal sections or references on a CV")
        for need in ["Professional Experience", "Education"]:
            if not any(need.lower() in h.lower() for h in h2s):
                warns.append(f"no '{need}' heading; ATS parsers look for it")
        head_block = "\n".join(lines[:10])
        if "@" not in head_block:
            warns.append("no email in the first ten lines; contact details go near the top as plain text")
        styles = set()
        for i, l in enumerate(lines[:-1]):
            if l.startswith("### "):
                if re.search(r"\s-\s", l[4:]):
                    warns.append(f"line {i+1}: separate title and company with a comma, not a hyphen")
                nxt = lines[i + 1]
                if " | " in nxt:
                    d = nxt.split(" | ")[0].strip()
                    if re.fullmatch(rf"{MONTH} \d{{4}} - ({MONTH} \d{{4}}|Present)", d): styles.add("Mon YYYY")
                    elif re.fullmatch(r"\d{4} - (\d{4}|Present)", d): styles.add("YYYY")
                    else: styles.add(d); warns.append(f"line {i+2}: date '{d}' is not 'Mon YYYY - Mon YYYY'")
        if len(styles) > 1:
            warns.append(f"mixed date formats across roles: {sorted(styles)}")

    # length and rhythm
    body = " ".join(plain(l) for l in lines if l.strip() and not l.startswith("#"))
    words = len(re.findall(r"\b[\w'%.,-]+\b", body))
    if kind == "letter" and not 250 <= words <= 380:
        warns.append(f"letter is about {words} words; aim for 250 to 350 unless the format asks for more")
    if kind == "message" and words > 150:
        warns.append(f"message is about {words} words; a DM over 150 words rarely gets read")
    # sentences: per paragraph or bullet; the contact block under the name is not prose
    chunks, cur, in_contact = [], [], False
    for l in lines:
        if l.startswith("# "):
            in_contact = True; continue
        if not l.strip() or l.startswith("#") or re.match(r"^\s*[-*]\s", l):
            if cur: chunks.append(" ".join(cur)); cur = []
            if l.strip(): in_contact = False
            if re.match(r"^\s*[-*]\s", l): chunks.append(plain(l))
            continue
        if in_contact or "@" in l or DATE_LINE.match(l.strip()):
            continue
        cur.append(plain(l))
    if cur: chunks.append(" ".join(cur))
    for c in chunks:
        for s in re.split(r"(?<=[.!?:])\s+", c):
            n = len(s.split())
            if n > 28:
                warns.append(f"sentence of {n} words: '{s[:60]}...'; split it")

    # numbers must come from the fact bank
    if a.facts:
        known = set()
        for f in a.facts:
            known |= numbers(strip_front_matter(pathlib.Path(f).expanduser().read_text(encoding="utf-8")))
        for i, l in enumerate(lines, 1):
            if DATE_LINE.match(l.strip()):          # the letter's own date line
                continue
            for n in sorted(numbers(l)):
                if n in ("0", "1") or n in known:
                    continue
                warns.append(f"line {i}: number '{n}' is not in the fact bank; trace it or cut it")
    else:
        warns.append("no --facts given; numbers were not traced to the fact bank")

    # the rendered PDF: text layer, reading order, headings stranded at a page end
    if a.pdf:
        txt = pdf_text(pathlib.Path(a.pdf).expanduser())
        if txt is None:
            warns.append("no pdftotext or pypdf; PDF checks skipped (install poppler or pip install pypdf)")
        elif len(txt.strip()) < 50:
            fails.append("PDF has no text layer; an ATS will read nothing")
        else:
            norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
            htexts = [norm(plain(h[2])) for h in heads if h[1] in (2, 3)]
            pages = txt.split("\f")
            if pages and not pages[-1].strip():
                pages = pages[:-1]
            import html as _html
            placed = pdf_lines_with_position(pathlib.Path(a.pdf).expanduser())
            if placed:
                # a heading whose line ends in the bottom band of a page (about three lines above the
                # bottom margin) on any page but the last is stranded
                for pn, height, t, ybot in placed:
                    if pn >= len(pages):
                        continue
                    t = norm(_html.unescape(t))
                    for h in htexts:
                        if h and t.startswith(h[:30]) and ybot > height - 51 - 42:
                            fails.append(f"page {pn}: heading '{h[:40]}' is in the last three lines of the page; "
                                         "cut a bullet above it, or let the role before it break")
            else:
                for pn, pg in enumerate(pages[:-1], 1):
                    tail = [norm(x) for x in pg.splitlines() if x.strip()][-3:]
                    for t in tail:
                        for h in htexts:
                            if h and t.startswith(h[:30]):
                                fails.append(f"page {pn}: heading '{h[:40]}' in the last three lines; cut a bullet above it or add a break")
            flat = norm(txt)
            pos = 0
            for h in htexts:
                j = flat.find(h[:30], pos)
                if j < 0:
                    warns.append(f"heading '{h[:40]}' not found in the PDF text in reading order")
                else:
                    pos = j
            first = next((plain(h[2]) for h in heads if h[1] == 1), "")
            if first and norm(first) not in flat[:200]:
                warns.append("the name is not at the top of the PDF text")
            print(f"pdf: {len(pages)} page{'s' if len(pages) != 1 else ''}, text layer ok")

    for w in warns: print("warn:", w)
    for f in fails: print("FAIL:", f)
    print(f"{path.name}: {kind}, {words} words, {len(fails)} failures, {len(warns)} warnings")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
