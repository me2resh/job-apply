#!/usr/bin/env python3
"""Rebuild the generated files from their sources. Run from anywhere; needs Chrome (or CHROME=...).

1. Renders the example CV and letter with scripts/render_pdf.py, into the example's application
   folder and into docs/samples/.
2. Runs scripts/check_doc.py on both, against the example fact bank, and fails if either fails.
3. Regenerates agents/job-apply-reviewer.md from skills/job-apply/references/reviewer.md.
"""
import pathlib, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "job-apply"
EX = SKILL / "examples" / "isolde-brackwater"
APP = EX / "applications" / "Brindlecove-Senior-Engineering-Manager-Mobile"
SAMPLES = ROOT / "docs" / "samples"

DOCS = [("cv.md", "Isolde-Brackwater-CV.pdf"), ("cover-letter.md", "Isolde-Brackwater-Cover-Letter.pdf")]
ok = True
for src, pdf in DOCS:
    subprocess.run([sys.executable, str(SKILL / "scripts" / "render_pdf.py"), str(APP / src), str(APP / pdf),
                    "--variant", "modern"], check=True)
    r = subprocess.run([sys.executable, str(SKILL / "scripts" / "check_doc.py"), str(APP / src),
                        "--facts", str(EX / "fact-bank.md"), "--facts", str(EX / "profile.yaml"),
                        "--voice", str(EX / "voice.md"), "--pdf", str(APP / pdf)])
    ok = ok and r.returncode == 0
    SAMPLES.mkdir(parents=True, exist_ok=True)
    shutil.copy2(APP / pdf, SAMPLES / pdf)
    print("copied", SAMPLES / pdf)

FRONT = """---
name: job-apply-reviewer
description: Adversarial reviewer for job-application documents (CVs, cover letters, recruiter messages, form answers). A talent partner with 20 years in tech hiring who checks every claim against the candidate's fact bank and flags inflation, AI tells, reader-blindness and wrong tone. Returns SHIP or FIX with line-level findings and a WOULD-CHALLENGE list, never a rewrite. Called by the job-apply skill as a mandatory gate; give it the document, the JD, fact-bank.md and voice.md.
tools: Read, Grep, Glob
---

<!-- Generated from skills/job-apply/references/reviewer.md (everything after its first "---" line). Edit that file, then regenerate this one. -->

"""
ref = (SKILL / "references" / "reviewer.md").read_text(encoding="utf-8").splitlines(keepends=True)
body = "".join(ref[ref.index("---\n") + 1:])
(ROOT / "agents" / "job-apply-reviewer.md").write_text(FRONT + body, encoding="utf-8")
print("regenerated agents/job-apply-reviewer.md")
sys.exit(0 if ok else 1)
