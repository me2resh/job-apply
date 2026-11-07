#!/usr/bin/env python3
"""Render a CV or cover letter written in markdown to an ATS-safe A4 PDF with headless Chrome.

Usage:
  python3 render_pdf.py <in.md> <out.pdf> [--kind cv|letter] [--variant editorial|modern|executive]
                        [--keep-html] [--strict-roles]

No Python packages needed: the converter below handles the subset of markdown the skill writes
(headings, paragraphs, bullets, bold, italic, links). Chrome, Chromium, Edge or Brave must be
installed; set CHROME=/path/to/browser to choose one.

--kind     cv or letter. Guessed from the file name ("letter" in it means letter), else cv.
--variant  print style; see references/print-styles.md. Default editorial.
--strict-roles  never let a role split across pages, even a long one (default: roles with more
           than five bullets may break between bullets, with the heading kept on its first bullet).
--keep-html     also write the intermediate HTML next to the PDF, for debugging the layout.

Prints the page count. Warns when a CV runs past 3 pages or a letter past 1.
"""
import html, os, pathlib, platform, re, shutil, subprocess, sys, tempfile

VARIANTS = {
    # name: (body font stack, heading font stack, accent colour, heading extras)
    "editorial": ('Charter, "Bitstream Charter", Georgia, serif',
                  '"Avenir Next", Avenir, "Helvetica Neue", Arial, sans-serif', "#24425c", "font-variant:small-caps;"),
    "modern": ('"Avenir Next", Avenir, "Helvetica Neue", Arial, sans-serif',
               '"Avenir Next", Avenir, "Helvetica Neue", Arial, sans-serif', "#14524f",
               "border-left:3px solid #14524f;padding-left:6pt;border-bottom:0;"),
    "executive": ('Georgia, "Times New Roman", serif', 'Georgia, "Times New Roman", serif', "#5e1f2e",
                  "border-bottom:1.5px solid #5e1f2e;"),
}


def find_chrome():
    env = os.environ.get("CHROME")
    if env and pathlib.Path(env).exists():
        return env
    system = platform.system()
    candidates = []
    if system == "Darwin":
        for app in ["Google Chrome", "Chromium", "Microsoft Edge", "Brave Browser"]:
            candidates.append(f"/Applications/{app}.app/Contents/MacOS/{app}")
            candidates.append(str(pathlib.Path.home() / f"Applications/{app}.app/Contents/MacOS/{app}"))
    elif system == "Windows":
        for base in [os.environ.get("PROGRAMFILES", r"C:\Program Files"),
                     os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)"),
                     os.environ.get("LOCALAPPDATA", "")]:
            if not base:
                continue
            candidates += [os.path.join(base, r"Google\Chrome\Application\chrome.exe"),
                           os.path.join(base, r"Microsoft\Edge\Application\msedge.exe"),
                           os.path.join(base, r"Chromium\Application\chrome.exe")]
    for c in candidates:
        if pathlib.Path(c).exists():
            return c
    for name in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
                 "microsoft-edge", "brave-browser", "chrome", "msedge"]:
        p = shutil.which(name)
        if p:
            return p
    return None


# ---------- a small markdown converter for CVs and letters ----------

def inline(text):
    """Escape HTML, then apply links, bold and italic. Autolinks <https://...> become links."""
    out, pos = [], 0
    token = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)|<(https?://[^>\s]+|mailto:[^>\s]+)>")
    for m in token.finditer(text):
        out.append(_emph(html.escape(text[pos:m.start()], quote=False)))
        if m.group(1) is not None:
            out.append(f'<a href="{html.escape(m.group(2))}">{_emph(html.escape(m.group(1), quote=False))}</a>')
        else:
            url = m.group(3)
            label = url[7:] if url.startswith("mailto:") else url
            out.append(f'<a href="{html.escape(url)}">{html.escape(label)}</a>')
        pos = m.end()
    out.append(_emph(html.escape(text[pos:], quote=False)))
    return "".join(out)


def _emph(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s


def md_to_html(md):
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)       # YAML front matter
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)                # comments
    lines = md.splitlines()
    blocks, para, items = [], [], []
    after_h3 = False

    def flush():
        nonlocal para, items
        if para:
            blocks.append(("p", para)); para = []
        if items:
            blocks.append(("ul", items)); items = []

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush(); after_h3 = False; continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            flush()
            blocks.append((f"h{len(m.group(1))}", m.group(2).strip()))
            after_h3 = len(m.group(1)) == 3
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            if para:
                blocks.append(("p", para)); para = []
            items.append(m.group(1)); after_h3 = False; continue
        if items and raw.startswith("  "):                      # continuation of a bullet
            items[-1] += " " + line.strip(); continue
        if after_h3 and " | " in line and not para:             # "Mar 2021 - Present | Bristol, UK"
            dates, place = line.split(" | ", 1)
            blocks.append(("meta", (dates.strip(), place.strip()))); after_h3 = False; continue
        after_h3 = False
        if items:
            blocks.append(("ul", items)); items = []
        para.append(line.strip())
    flush()
    return blocks


def render_blocks(blocks, kind, strict_roles):
    out = []
    i = 0
    while i < len(blocks):
        tag, val = blocks[i]
        if tag == "h3" and kind == "cv":
            # a role: the h3 and everything up to the next h2 or h3
            j = i + 1
            while j < len(blocks) and blocks[j][0] not in ("h2", "h3"):
                j += 1
            role = blocks[i:j]
            bullets = sum(len(v) for t, v in role if t == "ul")
            cls = "role" if (strict_roles or bullets <= 5) else "role long"
            out.append(f'<div class="{cls}">' + "".join(_block(t, v) for t, v in role) + "</div>")
            i = j
            continue
        out.append(_block(tag, val))
        i += 1
    return "\n".join(out)


def _block(tag, val):
    if tag in ("h1", "h2", "h3"):
        return f"<{tag}>{inline(val)}</{tag}>"
    if tag == "meta":
        dates, place = val
        return f'<p class="meta"><span class="dates">{inline(dates)}</span>{inline(place)}</p>'
    if tag == "ul":
        return "<ul>" + "".join(f"<li>{inline(x)}</li>" for x in val) + "</ul>"
    if tag == "p":
        cls = ' class="scope"' if len(val) == 1 and re.match(r"^\*[^*].*\*$", val[0]) else ""
        return f"<p{cls}>" + "<br>".join(inline(x) for x in val) + "</p>"
    return ""


def css(kind, variant):
    body, head, accent, h2x = VARIANTS[variant]
    base = f"""
@page{{size:A4;margin:18mm 20mm}}
*{{box-sizing:border-box}}
body{{font-family:{body};font-size:10pt;line-height:1.42;color:#1a1a1a;background:#fff;margin:0}}
h1{{font:600 24pt {head};color:{accent};margin:0 0 3pt;letter-spacing:.01em}}
h1 + p{{color:#444;font-size:9.5pt;line-height:1.5;margin:0 0 8pt}}
h2{{font:600 12.5pt {head};color:{accent};letter-spacing:.03em;border-bottom:1px solid #d8dee6;padding-bottom:2pt;margin:13pt 0 5pt;break-after:avoid;{h2x}}}
h3{{font:600 10.8pt {body};margin:10pt 0 1pt;break-after:avoid}}
p{{margin:0 0 6pt;orphans:3;widows:3}}
p.meta{{color:#666;font-size:9.5pt;margin:0 0 3pt;break-after:avoid}}
p.meta .dates{{float:right;font-variant-numeric:tabular-nums}}
p.scope{{color:#555;font-size:9.6pt;margin:0 0 4pt;break-after:avoid}}
ul{{margin:0 0 6pt;padding-left:15pt}}
li{{margin:0 0 3pt;orphans:3;widows:3}}
em{{color:#555}}
a{{color:#1a1a1a;text-decoration:none}}
.role{{break-inside:avoid}}
.role.long{{break-inside:auto}}
.role.long ul li:first-child{{break-before:avoid}}
"""
    if kind == "letter":
        base += """
body{font-size:10.8pt;line-height:1.5}
h1{font-size:20pt}
p{margin:0 0 10pt}
"""
    return base


def page_count(pdf_bytes):
    return len(re.findall(rb"/Type\s*/Page[^s]", pdf_bytes))


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--kind", choices=["cv", "letter"])
    ap.add_argument("--variant", choices=list(VARIANTS), default="editorial")
    ap.add_argument("--keep-html", action="store_true")
    ap.add_argument("--strict-roles", action="store_true")
    a = ap.parse_args()
    src, out = pathlib.Path(a.src).expanduser(), pathlib.Path(a.out).expanduser()
    kind = a.kind or ("letter" if "letter" in src.name.lower() else "cv")
    variant = a.variant
    flags = (["--keep-html"] if a.keep_html else []) + (["--strict-roles"] if a.strict_roles else [])
    if not src.exists():
        sys.exit(f"not found: {src}")
    chrome = find_chrome()
    if not chrome:
        sys.exit("No Chrome, Chromium, Edge or Brave found. Install one, or set CHROME=/path/to/browser.")

    blocks = md_to_html(src.read_text(encoding="utf-8"))
    name = next((v for t, v in blocks if t == "h1"), "Document")
    title = re.sub(r"[*_\[\]]", "", name) + (" Cover Letter" if kind == "letter" else " CV")
    body = render_blocks(blocks, kind, "--strict-roles" in flags)
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f"<style>{css(kind, variant)}</style></head><body>{body}</body></html>")

    out.parent.mkdir(parents=True, exist_ok=True)                 # the output folder may not exist yet
    with tempfile.TemporaryDirectory() as tmp:
        hp = pathlib.Path(tmp) / (out.stem + ".html")
        hp.write_text(page, encoding="utf-8")
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--no-first-run",
               f"--user-data-dir={tmp}/profile", f"--print-to-pdf={out}", hp.as_uri()]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if not out.exists():
            sys.exit(f"Chrome did not write the PDF.\n{r.stderr[-800:]}")
    if "--keep-html" in flags:
        out.with_suffix(".html").write_text(page, encoding="utf-8")

    pages = page_count(out.read_bytes())
    print(f"{out}: {pages} page{'s' if pages != 1 else ''}, {out.stat().st_size} bytes, {kind}, {variant}")
    if kind == "cv" and pages > 3:
        print("warn: CV is over 3 pages; cut the bullets that serve this JD least and render again")
    if kind == "cv" and pages == 1:
        print("warn: a one-page CV at senior level usually leaves evidence out; check the mapping")
    if kind == "letter" and pages > 1:
        print("warn: letter is over one page; aim for 250 to 350 words")
    print("next: python3 check_doc.py <the .md> --pdf", out, "(page-end headings, text layer)")


if __name__ == "__main__":
    main()
