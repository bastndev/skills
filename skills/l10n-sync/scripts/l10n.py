#!/usr/bin/env python3
"""l10n-sync — propagate English README.md edits into README_<LANG>.md translations.

Division of labor:
  * The MODEL translates natural language. It only ever sees the blocks that
    actually changed (via git), never the whole file, never code/URLs.
  * THIS SCRIPT owns structure. It parses the markdown into ordered blocks,
    figures out what changed, splices the model's translations back into the
    exact same positions, and verifies nothing was dropped.

Never invents filenames or languages: it writes only to files that already
exist (folder mode) or that the caller names explicitly.

Subcommands
-----------
  plan   --source README.md (--dir DIR | --file F [F ...]) [--base REF] --work W
         Resolves targets, computes per-file deltas, writes:
           W/jobs.json   -> blocks the model must translate (small)
           W/state.json  -> splice plan the `apply` step replays (machine)
         Prints a compact summary table.

  apply  --work W
         Reads W/state.json + W/results.json (the model's translations),
         writes every target file, then verifies. Prints a status table.

  verify --source README.md (--dir DIR | --file F [F ...])
         Structural parity report only (no writes).
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

# --------------------------------------------------------------------------- #
# language map — extensible, NON-gating. Suffix of README_<SUFFIX>.md -> lang.
# Add rows freely; unknown suffixes are still processed (model infers the lang).
# --------------------------------------------------------------------------- #

LANG_NAMES = {
    "ar": "Arabic", "de": "German", "es": "Spanish", "fr": "French",
    "hi": "Hindi", "ja": "Japanese", "ko": "Korean", "pt": "Portuguese",
    "pt-br": "Brazilian Portuguese", "ru": "Russian", "vi": "Vietnamese",
    "zh": "Simplified Chinese", "zh-cn": "Simplified Chinese",
    "zh-tw": "Traditional Chinese", "it": "Italian", "nl": "Dutch",
    "tr": "Turkish", "pl": "Polish", "id": "Indonesian", "th": "Thai",
    "uk": "Ukrainian", "cs": "Czech", "ro": "Romanian", "el": "Greek",
    "sv": "Swedish", "da": "Danish", "fi": "Finnish", "no": "Norwegian",
    "hu": "Hungarian", "he": "Hebrew", "fa": "Persian", "ur": "Urdu",
    "bn": "Bengali", "ta": "Tamil", "fil": "Filipino", "ms": "Malay",
}
RTL = {"ar", "he", "fa", "ur"}


def lang_of(suffix: str) -> tuple[str, str, bool]:
    """(code, language name, rtl) from a filename suffix like 'AR' or 'zh-cn'."""
    code = suffix.strip().lower().replace("_", "-")
    name = LANG_NAMES.get(code, f"the '{code}' language")
    return code, name, code in RTL


# --------------------------------------------------------------------------- #
# markdown parsing — text -> ordered slots
# --------------------------------------------------------------------------- #
# A slot is one of:
#   {"k": "v",   "lines": [...]}                      verbatim (copied as-is)
#   {"k": "x",   "tpl": {...}, "en": str, "inv": []}  one translatable line
#   {"k": "row", "cells": [...]}                      one table data row
# Every slot maps to one or more output lines, so reassembly is exact.

CODE_RE = re.compile(r"`[^`]+`")
# URL stops at real delimiters (quote, backtick, paren, angle bracket, bracket,
# whitespace) — NOT greedy \S+, which used to swallow trailing sentence
# punctuation and adjacent HTML tags and produce false "invariant lost" reports.
URL_RE = re.compile(r"(?:https?://|mailto:|www\.)[^\s\"'`)<>\]]+")
_URL_TRAIL = ".,;:!?"
PLACEHOLDER_RE = re.compile(r"\{[a-zA-Z0-9_]+\}|%[sdifx]|\$\{[^}]+\}")
HTML_RE = re.compile(r"</?[a-zA-Z][^>]*>")
IMG_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")
LINK_TARGET_RE = re.compile(r"\]\(([^)]+)\)")
LETTER_RE = re.compile(r"[^\W\d_]", re.UNICODE)

_STRIP_FOR_TEST = [IMG_RE, LINK_RE, CODE_RE, URL_RE, PLACEHOLDER_RE, HTML_RE]


def _strip_invariants(text: str) -> str:
    for pat in _STRIP_FOR_TEST:
        text = pat.sub(" ", text)
    return text


def _has_translatable(text: str) -> bool:
    return LETTER_RE.search(_strip_invariants(text)) is not None


def _prose_words(text: str) -> int:
    """Word count of the visible prose only (invariants stripped)."""
    return len([w for w in _strip_invariants(text).split() if LETTER_RE.search(w)])


def _invariants(text: str) -> list[str]:
    """Distinctive substrings that MUST survive translation unchanged.
    Kept precise on purpose: only code spans, URL cores, placeholders, HTML tags,
    and link targets — never trailing sentence punctuation (which is localized)."""
    found: list[str] = []
    found += CODE_RE.findall(text)
    found += [u.rstrip(_URL_TRAIL) for u in URL_RE.findall(text)]
    found += PLACEHOLDER_RE.findall(text)
    found += HTML_RE.findall(text)
    found += LINK_TARGET_RE.findall(text)  # link/image targets ( [txt](THIS) )
    # de-dup preserving order
    seen, out = set(), []
    for f in found:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out


def _v(lines: list[str]) -> dict:
    return {"k": "v", "lines": lines}


def _x(tpl: dict, en: str) -> dict:
    return {"k": "x", "tpl": tpl, "en": en, "inv": _invariants(en)}


def _is_table_row(line: str) -> bool:
    return "|" in line and line.strip() != ""


def _table_sep(line: str) -> bool:
    return "|" in line and bool(re.match(r"^\s*\|?[\s:\-|]+\|?\s*$", line)) and "-" in line


def _row_slot(line: str) -> dict:
    raw = line.strip()
    inner = raw[1:] if raw.startswith("|") else raw
    inner = inner[:-1] if inner.endswith("|") else inner
    cells = []
    for cell in inner.split("|"):
        c = cell.strip()
        if c and _has_translatable(c):
            cells.append({"t": "tr", "en": c, "inv": _invariants(c)})
        else:
            cells.append({"t": "lit", "v": c})
    return {"k": "row", "cells": cells}


def parse(text: str) -> list[dict]:
    lines = text.split("\n")
    slots: list[dict] = []
    i, n = 0, len(lines)

    while i < n:
        line = lines[i]
        s = line.strip()

        # frontmatter (only at very top)
        if i == 0 and s == "---":
            j = i + 1
            while j < n and lines[j].strip() != "---":
                j += 1
            j = j if j < n else n - 1
            slots.append(_v(lines[i:j + 1]))
            i = j + 1
            continue

        # fenced code block
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            fence = m.group(1)[0]
            j = i + 1
            while j < n and not re.match(rf"^\s*{re.escape(fence)}{{3,}}\s*$", lines[j]):
                j += 1
            j = j if j < n else n - 1
            slots.append(_v(lines[i:j + 1]))
            i = j + 1
            continue

        # blank
        if s == "":
            slots.append(_v([line]))
            i += 1
            continue

        # horizontal rule
        if re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", line):
            slots.append(_v([line]))
            i += 1
            continue

        # table (header row + separator + data rows)
        if _is_table_row(line) and i + 1 < n and _table_sep(lines[i + 1]):
            slots.append(_row_slot(line))
            slots.append(_v([lines[i + 1]]))
            i += 2
            while i < n and _is_table_row(lines[i]) and not _table_sep(lines[i]):
                slots.append(_row_slot(lines[i]))
                i += 1
            continue

        # heading
        m = re.match(r"^(\s*#{1,6})\s+(.*?)\s*$", line)
        if m:
            marker, txt = m.group(1), m.group(2)
            slots.append(_x({"type": "heading", "marker": marker}, txt)
                         if _has_translatable(txt) else _v([line]))
            i += 1
            continue

        # list item
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*?)\s*$", line)
        if m:
            indent, mk, txt = m.group(1), m.group(2), m.group(3)
            slots.append(_x({"type": "list", "indent": indent, "marker": mk}, txt)
                         if _has_translatable(txt) else _v([line]))
            i += 1
            continue

        # blockquote
        m = re.match(r"^(\s*>\s?)(.*?)\s*$", line)
        if m:
            marker, txt = m.group(1), m.group(2)
            slots.append(_x({"type": "quote", "marker": marker}, txt)
                         if _has_translatable(txt) else _v([line]))
            i += 1
            continue

        # paragraph
        txt = line.rstrip()
        slots.append(_x({"type": "para"}, txt) if _has_translatable(txt) else _v([line]))
        i += 1

    return slots


# --------------------------------------------------------------------------- #
# rendering — slot + translated text -> output line(s)
# --------------------------------------------------------------------------- #

def render_x(tpl: dict, text: str) -> str:
    t = tpl["type"]
    if t == "heading":
        return f"{tpl['marker']} {text}".rstrip()
    if t == "list":
        return f"{tpl['indent']}{tpl['marker']} {text}".rstrip()
    if t == "quote":
        return f"{tpl['marker']}{text}".rstrip()
    return text  # para


def render_row(cells: list[dict], lookup) -> str:
    # emit-plan cells are {"lit": text} or {"id": job_id} (see build_emit)
    out = []
    for c in cells:
        if "id" in c:
            out.append(lookup(c["id"]))
        else:
            out.append(c.get("lit", ""))
    return "| " + " | ".join(out) + " |"


# --------------------------------------------------------------------------- #
# signatures for diffing old vs new source
# --------------------------------------------------------------------------- #

def sig(slot: dict):
    if slot["k"] == "v":
        return ("v", tuple(slot["lines"]))
    if slot["k"] == "x":
        return ("x", slot["en"])
    parts = tuple((c["v"] if c.get("t") == "lit" else ("tr", c["en"])) for c in slot["cells"])
    return ("row", parts)


# --------------------------------------------------------------------------- #
# git baseline
# --------------------------------------------------------------------------- #

def git_old_source(source: Path, base: str) -> str | None:
    """Return the committed text of `source` at `base`, or None if unavailable."""
    try:
        root = subprocess.run(
            ["git", "-C", str(source.resolve().parent), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        rel = source.resolve().relative_to(Path(root))
        r = subprocess.run(
            ["git", "-C", root, "show", f"{base}:{rel.as_posix()}"],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            return None
        return r.stdout
    except Exception:
        return None


# --------------------------------------------------------------------------- #
# planning
# --------------------------------------------------------------------------- #

def build_emit(new_slots, old_slots, tgt_slots, jobs, next_id, force_full=False):
    """Return (emit_plan, mode). Appends translate jobs to `jobs`."""
    emit: list[dict] = []

    def emit_new(slot):
        if slot["k"] == "v":
            for ln in slot["lines"]:
                emit.append({"lit": ln})
        elif slot["k"] == "x":
            jid = next_id()
            emit.append({"x": {"id": jid, "tpl": slot["tpl"]}})
            jobs.append({"id": jid, "text": slot["en"], "keep": slot["inv"]})
        else:  # row
            cells = []
            for c in slot["cells"]:
                if c.get("t") == "lit":
                    cells.append({"lit": c["v"]})
                else:
                    jid = next_id()
                    cells.append({"id": jid})
                    jobs.append({"id": jid, "text": c["en"], "keep": c["inv"]})
            emit.append({"row": {"cells": cells}})

    aligned = (
        not force_full
        and old_slots is not None
        and tgt_slots is not None
        and len(tgt_slots) == len(old_slots)
        and all(a["k"] == b["k"] for a, b in zip(old_slots, tgt_slots))
    )

    if not aligned:
        # full retranslate — establishes / re-establishes a clean baseline
        for slot in new_slots:
            emit_new(slot)
        return emit, "full"

    # incremental: diff old source -> new source, replay ops onto the target
    a = [sig(s) for s in old_slots]
    b = [sig(s) for s in new_slots]
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i1, i2):
                for ln in tgt_slots[k]["lines_raw"]:
                    emit.append({"lit": ln})
        elif tag == "delete":
            continue
        else:  # replace / insert -> take new source slots
            for k in range(j1, j2):
                emit_new(new_slots[k])
    return emit, "incremental"


def attach_raw_lines(slots: list[dict], text: str) -> list[dict]:
    """Record the exact source lines each slot occupies, for verbatim copying."""
    lines = text.split("\n")
    pos = 0
    for slot in slots:
        if slot["k"] == "v":
            count = len(slot["lines"])
            slot["lines_raw"] = lines[pos:pos + count]
            pos += count
        else:
            slot["lines_raw"] = [lines[pos]]
            pos += 1
    return slots


def find_targets(source: Path, dir_: Path | None, files: list[Path] | None) -> list[Path]:
    if files:
        return files
    targets = []
    src_name = source.name
    for f in sorted(dir_.glob("*.md")):
        if f.name == src_name:
            continue
        if re.match(r"^README[_-].+\.md$", f.name, re.IGNORECASE):
            targets.append(f)
    return targets


def suffix_of(target: Path, source: Path) -> str:
    m = re.match(r"^" + re.escape(source.stem) + r"[_-](.+)$", target.stem, re.IGNORECASE)
    if m:
        return m.group(1)
    m = re.match(r"^README[_-](.+)$", target.stem, re.IGNORECASE)
    return m.group(1) if m else target.stem


def cmd_plan(args) -> int:
    source = args.source
    if not source.exists():
        print(json.dumps({"error": f"source not found: {source}"}))
        return 1
    new_text = source.read_text(encoding="utf-8")
    new_slots = parse(new_text)

    old_text = git_old_source(source, args.base)
    if old_text is not None and old_text == new_text and args.base == "HEAD":
        # edit already committed — compare against the previous commit instead
        prev = git_old_source(source, "HEAD~1")
        if prev is not None:
            old_text = prev
    old_slots = parse(old_text) if old_text is not None else None

    targets = find_targets(source, args.dir, args.file)
    work = args.work
    work.mkdir(parents=True, exist_ok=True)

    counter = [0]
    def next_id():
        counter[0] += 1
        return counter[0]

    state_targets = []
    jobs_targets = []
    summary = []

    for tgt in targets:
        counter[0] = 0  # ids are per-file
        code, name, rtl = lang_of(suffix_of(tgt, source))
        if tgt.exists():
            tgt_text = tgt.read_text(encoding="utf-8")
            tgt_slots = attach_raw_lines(parse(tgt_text), tgt_text)
        else:
            tgt_slots = None
        jobs: list[dict] = []
        emit, mode = build_emit(new_slots, old_slots, tgt_slots, jobs, next_id,
                                force_full=args.full)

        state_targets.append({"file": str(tgt), "emit": emit})
        if jobs:
            jobs_targets.append({
                "file": str(tgt), "lang": code, "language": name,
                "rtl": rtl, "mode": mode, "blocks": jobs,
            })
        summary.append({"file": str(tgt), "lang": code, "mode": mode,
                        "blocks": len(jobs)})

    (work / "state.json").write_text(
        json.dumps({"source": str(source), "targets": state_targets},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    (work / "jobs.json").write_text(
        json.dumps({
            "source": str(source),
            "instructions": (
                "Translate each block's 'text' into the file's 'language'. "
                "Copy every substring in 'keep' (code, URLs, paths, placeholders, "
                "HTML) verbatim. Do not add notes or change structure. "
                "Write results to results.json as {file: {id: translation}} — or, "
                "when splitting work across agents, one partial-<lang>.json per "
                "language as {id: translation}, then run the 'merge' command. "
                "Output must be valid JSON: escape double quotes inside "
                "translations, and validate every file you write with "
                "`python3 -m json.tool <file>` before finishing."
            ),
            "targets": jobs_targets,
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "targets": len(targets),
        "to_translate": [s for s in summary if s["blocks"]],
        "up_to_date": [s["file"] for s in summary if not s["blocks"]],
        "jobs_file": str(work / "jobs.json"),
    }, ensure_ascii=False, indent=2))
    return 0


# --------------------------------------------------------------------------- #
# merge — combine per-language partial-<lang>.json files (written by parallel
# translation agents) into results.json. Validates every partial first, so one
# agent's malformed JSON is reported precisely instead of stalling the run.
# --------------------------------------------------------------------------- #

def cmd_merge(args) -> int:
    work = args.work
    jobs_path = work / "jobs.json"
    if not jobs_path.exists():
        print(json.dumps({"error": f"no jobs.json in {work} — run plan first"}))
        return 1
    jobs = json.loads(jobs_path.read_text(encoding="utf-8"))
    by_lang = {t["lang"]: t for t in jobs["targets"]}

    results: dict = {}
    report: list[dict] = []
    errors = 0
    seen: set[str] = set()
    for part in sorted(work.glob("partial-*.json")):
        lang = part.stem[len("partial-"):]
        t = by_lang.get(lang)
        if t is None:
            report.append({"partial": part.name, "ok": False,
                           "error": f"no planned target with lang '{lang}'"})
            errors += 1
            continue
        seen.add(lang)
        try:
            data = json.loads(part.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            report.append({"partial": part.name, "ok": False,
                           "error": f"invalid JSON: {e} — rewrite this file "
                                    "(double quotes inside translations must be "
                                    "escaped as \\\")"})
            errors += 1
            continue
        expected = {str(b["id"]) for b in t["blocks"]}
        missing = sorted(expected - {str(k) for k in data}, key=int)
        if missing:
            report.append({"partial": part.name, "ok": False,
                           "error": f"missing block id(s): {', '.join(missing)}"})
            errors += 1
            continue
        results[t["file"]] = {str(k): str(v) for k, v in data.items()}
        report.append({"partial": part.name, "ok": True,
                       "file": t["file"], "blocks": len(data)})

    missing_partials = sorted(set(by_lang) - seen)
    ok = not errors and not missing_partials
    if ok:
        (work / "results.json").write_text(
            json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"merged": report, "missing_partials": missing_partials,
                      "results_written": ok}, ensure_ascii=False, indent=2))
    return 0 if ok else 2


# --------------------------------------------------------------------------- #
# apply
# --------------------------------------------------------------------------- #

def cmd_apply(args) -> int:
    work = args.work
    state = json.loads((work / "state.json").read_text(encoding="utf-8"))
    results_path = work / "results.json"
    results = json.loads(results_path.read_text(encoding="utf-8")) if results_path.exists() else {}
    source = Path(state["source"])

    report = []
    for t in state["targets"]:
        file = t["file"]
        res = results.get(file, {})
        blanks = []

        def lookup(jid, _res=res, _blanks=blanks):
            v = _res.get(str(jid), "")
            if not v:
                _blanks.append(jid)
            return v

        out = []
        for e in t["emit"]:
            if "lit" in e:
                out.append(e["lit"])
            elif "x" in e:
                out.append(render_x(e["x"]["tpl"], lookup(e["x"]["id"])))
            else:
                out.append(render_row(e["row"]["cells"], lookup))

        target = Path(file)
        # only write if there is something to write (avoid clobbering with blanks
        # when the model produced no results for a file that needed translation)
        needs = any(("x" in e) or ("row" in e and any("id" in c for c in e["row"]["cells"]))
                    for e in t["emit"])
        wrote = False
        if not needs or res:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("\n".join(out), encoding="utf-8")
            wrote = True

        v = verify_pair(source, target) if target.exists() else {"error": "not written"}
        report.append({"file": file, "wrote": wrote, "blanks": blanks, **v})

    ok = all(r.get("ok") for r in report)
    if getattr(args, "json", False):
        print(json.dumps({"applied": report}, ensure_ascii=False, indent=2))
    else:
        wrote_n = sum(1 for r in report if r.get("wrote"))
        print(f"Applied to {wrote_n}/{len(report)} file(s).\n")
        print(render_report(report))
        print("\n" + ("All files OK." if ok else
                      "Some files need fixing — edit those blocks and re-run apply."))
    return 0 if ok else 2


# --------------------------------------------------------------------------- #
# verify
# --------------------------------------------------------------------------- #

def _snip(text: str, n: int = 90) -> str:
    text = " ".join(text.split())
    return text if len(text) <= n else text[:n] + "…"


def verify_pair(source: Path, target: Path) -> dict:
    src = parse(source.read_text(encoding="utf-8"))
    tgt = parse(target.read_text(encoding="utf-8"))
    issues: list[str] = []
    details: list[dict] = []   # actionable: what to fix and where

    if len(src) != len(tgt):
        return {"ok": False, "src_slots": len(src), "tgt_slots": len(tgt),
                "issues": [f"slot count {len(src)} vs {len(tgt)} — structure drifted; "
                           "re-run plan --full for this file"], "details": []}

    def cell_text(c: dict) -> str:
        return c["en"] if c.get("t") == "tr" else c.get("v", "")

    untranslated = 0
    missing_inv = lit_changed = emptied = 0
    line = 1
    for a, b in zip(src, tgt):
        at = line
        line += len(a["lines"]) if a["k"] == "v" else 1
        if a["k"] != b["k"]:
            issues.append(f"kind mismatch {a['k']}/{b['k']}")
            continue
        if a["k"] == "v":
            if a["lines"] != b["lines"]:
                details.append({"line": at, "type": "verbatim_block_changed",
                                "expected": _snip("\\n".join(a["lines"])),
                                "got": _snip("\\n".join(b["lines"]))})
        elif a["k"] == "x":
            for inv in a["inv"]:
                if inv not in b["en"]:
                    missing_inv += 1
                    details.append({"line": at, "type": "invariant_lost",
                                    "expected": inv, "en": _snip(a["en"]),
                                    "got": _snip(b["en"])})
            # soft hint: real prose (>=3 visible words) left identical to English.
            # single words (nav names, brand headings) are intentionally the same.
            if a["en"] == b["en"] and _prose_words(a["en"]) >= 3:
                untranslated += 1
        else:  # row
            if len(a["cells"]) != len(b["cells"]):
                issues.append(f"table column count changed (line {at})")
                continue
            for idx, (ca, cb) in enumerate(zip(a["cells"], b["cells"])):
                bt = cell_text(cb)
                if ca.get("t") == "tr":
                    for inv in ca["inv"]:
                        if inv not in bt:
                            missing_inv += 1
                            details.append({"line": at, "type": "invariant_lost",
                                            "col": idx, "expected": inv,
                                            "en": _snip(ca["en"]), "got": _snip(bt)})
                    if ca["en"].strip() and not bt.strip():
                        emptied += 1
                        details.append({"line": at, "type": "cell_emptied",
                                        "col": idx, "expected": _snip(ca["en"])})
                elif ca.get("v", "").strip() and ca["v"] != bt:
                    lit_changed += 1
                    details.append({"line": at, "type": "verbatim_cell_changed",
                                    "col": idx, "expected": ca["v"], "got": bt})

    if missing_inv:
        issues.append(f"{missing_inv} invariant(s) (code/URL/placeholder) lost")
    if lit_changed:
        issues.append(f"{lit_changed} verbatim table cell(s) changed/dropped")
    if emptied:
        issues.append(f"{emptied} table cell(s) emptied")
    return {
        "ok": not issues, "src_slots": len(src), "tgt_slots": len(tgt),
        "possibly_untranslated": untranslated, "issues": issues, "details": details,
    }


def render_report(rows: list[dict]) -> str:
    """Human-readable, directly actionable report (no JSON parsing needed)."""
    out = []
    for r in rows:
        name = Path(r["file"]).name
        if r.get("ok"):
            note = "" if not r.get("possibly_untranslated") else \
                f"  ({r['possibly_untranslated']} line(s) same as English — check if intended)"
            out.append(f"  ✓ {name}{note}")
            continue
        out.append(f"  ✗ {name}  —  {'; '.join(r.get('issues', []))}")
        for d in r.get("details", []):
            loc = f"line {d['line']}" + (f", col {d['col']}" if "col" in d else "")
            if d["type"] == "invariant_lost":
                out.append(f"      {loc}: keep `{d['expected']}` verbatim — it is missing")
                out.append(f"        en : {d['en']}")
                out.append(f"        got: {d['got']}")
            elif d["type"] == "cell_emptied":
                out.append(f"      {loc}: table cell emptied — should be: {d['expected']}")
            elif d["type"] == "verbatim_cell_changed":
                out.append(f"      {loc}: restore verbatim cell → {d['expected']}  (got: {d['got']})")
            elif d["type"] == "verbatim_block_changed":
                out.append(f"      {loc}: code/verbatim block changed → {d['expected']}")
    return "\n".join(out) if out else "  (no files)"


def cmd_verify(args) -> int:
    targets = find_targets(args.source, args.dir, args.file)
    report = [{"file": str(t), **(verify_pair(args.source, t) if t.exists()
              else {"ok": False, "issues": ["missing"], "details": []})} for t in targets]
    ok = all(r.get("ok") for r in report)
    if args.json:
        print(json.dumps({"verify": report}, ensure_ascii=False, indent=2))
    else:
        print(render_report(report))
        print("\n" + ("All files OK." if ok else "Some files need fixing (see above)."))
    return 0 if ok else 2


# --------------------------------------------------------------------------- #
# repair — restore verbatim structure (code / links / table cells) from the
# English source WITHOUT retranslating: keeps every existing translation, only
# rewrites the parts that must be identical to English. Costs zero model tokens.
# Requires the target to still line up slot-for-slot with the source; if it has
# drifted structurally, use plan/apply instead.
# --------------------------------------------------------------------------- #

def repair_pair(source: Path, target: Path) -> dict:
    src = parse(source.read_text(encoding="utf-8"))
    tgt = parse(target.read_text(encoding="utf-8"))
    if len(src) != len(tgt) or any(a["k"] != b["k"] for a, b in zip(src, tgt)):
        return {"file": str(target), "repaired": False,
                "issues": [f"not aligned with source ({len(src)} vs {len(tgt)} slots) "
                           "— run plan/apply instead"]}

    out: list[str] = []
    fixes = 0
    for a, b in zip(src, tgt):
        if a["k"] == "v":
            if a["lines"] != b["lines"]:
                fixes += 1
            out.extend(a["lines"])              # source verbatim wins
        elif a["k"] == "x":
            out.append(render_x(a["tpl"], b["en"]))   # keep translation, source structure
        else:  # row
            if len(a["cells"]) != len(b["cells"]):
                return {"file": str(target), "repaired": False,
                        "issues": ["table column count differs — run plan/apply instead"]}
            cells = []
            for ca, cb in zip(a["cells"], b["cells"]):
                bt = cb["en"] if cb.get("t") == "tr" else cb.get("v", "")
                if ca.get("t") == "tr":
                    cells.append(bt)                        # keep translation
                else:
                    if ca.get("v", "") != bt:
                        fixes += 1
                    cells.append(ca["v"])                   # source verbatim wins
            out.append("| " + " | ".join(cells) + " |")

    target.write_text("\n".join(out), encoding="utf-8")
    return {"file": str(target), "repaired": True, "fixes": fixes,
            **verify_pair(source, target)}


def cmd_repair(args) -> int:
    targets = find_targets(args.source, args.dir, args.file)
    report = [repair_pair(args.source, t) if t.exists()
              else {"file": str(t), "repaired": False, "issues": ["missing"]}
              for t in targets]
    print(json.dumps({"repair": report}, ensure_ascii=False, indent=2))
    return 0 if all(r.get("repaired") for r in report) else 2


# --------------------------------------------------------------------------- #
# cli
# --------------------------------------------------------------------------- #

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="l10n")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("plan")
    p.add_argument("--source", type=Path, default=Path("README.md"))
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--dir", type=Path)
    g.add_argument("--file", type=Path, nargs="+")
    p.add_argument("--base", default="HEAD")
    p.add_argument("--full", action="store_true",
                   help="force a full retranslate of every target (re-baseline)")
    p.add_argument("--work", type=Path, required=True)

    p = sub.add_parser("merge")
    p.add_argument("--work", type=Path, required=True)

    p = sub.add_parser("apply")
    p.add_argument("--work", type=Path, required=True)
    p.add_argument("--json", action="store_true", help="machine-readable output")

    for name in ("verify", "repair"):
        p = sub.add_parser(name)
        p.add_argument("--source", type=Path, default=Path("README.md"))
        g = p.add_mutually_exclusive_group(required=True)
        g.add_argument("--dir", type=Path)
        g.add_argument("--file", type=Path, nargs="+")
        p.add_argument("--json", action="store_true", help="machine-readable output")

    args = ap.parse_args(argv)
    if args.cmd == "plan":
        return cmd_plan(args)
    if args.cmd == "merge":
        return cmd_merge(args)
    if args.cmd == "apply":
        return cmd_apply(args)
    if args.cmd == "verify":
        return cmd_verify(args)
    if args.cmd == "repair":
        return cmd_repair(args)
    ap.error("unknown command")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
