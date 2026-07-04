#!/usr/bin/env python3
"""
l10n-sync extractor / reassembler / checker.

Subcommands:
  extract           .md  -> flat per-lang payload templates
  reassemble        .md  payload -> docs/{lang}/README.md
  check             .md  parity (line count + untranslated)
  extract-nls       package.nls.json -> per-lang payload (drift-only)
  reassemble-nls    merge payload into package.nls.{lang}.json
  check-nls         key-count parity across package.nls.*.json
  extract-bundle    l10n/bundle.l10n.en.json -> per-lang payload (drift-only)
  reassemble-bundle merge payload into l10n/bundle.l10n.{lang}.json
  check-bundle      key-count parity across l10n/bundle.l10n.*.json

See future-skill/SKILL.md and future-skill/references/reassembly-spec.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SUPPORTED = ["es", "zh-cn", "de", "fr", "ja", "ko", "pt-br", "ru", "vi", "hi", "ar"]

PREFIXES = ("[My Skills]", "[My Memory]", "[MySkills]", "[My CLI]")
PLACEHOLDER_RE = re.compile(r"\{[a-zA-Z0-9_]+\}|%[sd]|\{[a-zA-Z0-9_ ]*\}")
URL_RE = re.compile(r"https?://\S+|mailto:\S+|vscode-webview://\S+|file://\S+")
CODE_SPAN_RE = re.compile(r"`[^`]+`")
HTML_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")


# --------------------------------------------------------------------------- #
# .md extraction
# --------------------------------------------------------------------------- #

def _split_prefix(text: str) -> tuple[str, str]:
    for p in PREFIXES:
        if text.startswith(p):
            return p, text[len(p):]
    return "", text


def _unwrap_placeholders(text: str) -> str:
    return re.sub(r"«([^»]+)»", r"\1", text)


def _wrap_invariants(text: str) -> str:
    """Wrap placeholders, URLs, inline code spans and HTML tags in sentinels
    so the model leaves them verbatim. Reassembler strips the sentinels."""
    text = PLACEHOLDER_RE.sub(lambda m: f"«{m.group(0)}»", text)
    text = URL_RE.sub(lambda m: f"«{m.group(0)}»", text)
    text = CODE_SPAN_RE.sub(lambda m: f"«{m.group(0)}»", text)
    text = HTML_TAG_RE.sub(lambda m: f"«{m.group(0)}»", text)
    return text


def _is_invariant_segment(text: str) -> bool:
    t = text.strip()
    if not t:
        return True
    if CODE_SPAN_RE.fullmatch(t):
        return True
    if HTML_TAG_RE.fullmatch(t):
        return True
    if URL_RE.fullmatch(t):
        return True
    if PLACEHOLDER_RE.fullmatch(t):
        return True
    # emoji-only or single-char tokens stay verbatim
    return False


def extract_md(source: Path, out_dir: Path) -> dict:
    lines = source.read_text(encoding="utf-8").splitlines()
    skeleton = []          # list of dicts: {id?, verbatim, prefix, kind, line}
    payload_template = {}  # {id: english_value}  -- filled once, copied per lang

    in_frontmatter = False
    in_code = False

    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")

        # code fence
        if stripped.lstrip().startswith("```"):
            in_code = not in_code
            skeleton.append({"id": None, "verbatim": line, "kind": "codefence", "line": i})
            continue
        if in_code:
            skeleton.append({"id": None, "verbatim": line, "kind": "code", "line": i})
            continue

        # frontmatter
        if i == 1 and stripped.strip() == "---":
            in_frontmatter = True
            skeleton.append({"id": None, "verbatim": line, "kind": "frontmatter", "line": i})
            continue
        if in_frontmatter:
            if stripped.strip() == "---":
                in_frontmatter = False
            skeleton.append({"id": None, "verbatim": line, "kind": "frontmatter", "line": i})
            continue

        # blank
        if not stripped.strip():
            skeleton.append({"id": None, "verbatim": line, "kind": "blank", "line": i})
            continue

        # table separator
        if re.match(r"^\s*\|?[\s\-:|]+\|?\s*$", stripped) and "|" in stripped:
            skeleton.append({"id": None, "verbatim": line, "kind": "tablesep", "line": i})
            continue

        # table row
        if stripped.lstrip().startswith("|") or stripped.rstrip().endswith("|"):
            cells = [c.strip() for c in stripped.strip().strip("|").split("|")]
            row = {"id": None, "verbatim": line, "kind": "table", "line": i, "cells": []}
            translated_cells = []
            for idx, cell in enumerate(cells):
                if _is_invariant_segment(cell):
                    row["cells"].append({"idx": idx, "verbatim": cell, "id": None})
                else:
                    prefix, rest = _split_prefix(cell)
                    cid = f"markdown:{i}:cell:{idx}"
                    val = _wrap_invariants(rest.strip())
                    row["cells"].append({"idx": idx, "verbatim": None, "id": cid, "prefix": prefix})
                    translated_cells.append((cid, val))
            skeleton.append(row)
            for cid, val in translated_cells:
                payload_template[cid] = val
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            marker, text = m.group(1), m.group(2)
            if _is_invariant_segment(text):
                skeleton.append({"id": None, "verbatim": line, "kind": "heading-static", "line": i})
            else:
                cid = f"markdown:{i}:heading"
                prefix, rest = _split_prefix(text)
                skeleton.append({"id": cid, "prefix": prefix, "marker": marker, "kind": "heading", "line": i})
                payload_template[cid] = _wrap_invariants(rest.strip())
            continue

        # list item
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", stripped)
        if m:
            indent, marker, text = m.group(1), m.group(2), m.group(3)
            if _is_invariant_segment(text):
                skeleton.append({"id": None, "verbatim": line, "kind": "list-static", "line": i})
            else:
                cid = f"markdown:{i}:list"
                prefix, rest = _split_prefix(text)
                skeleton.append({"id": cid, "prefix": prefix, "indent": indent, "marker": marker, "kind": "list", "line": i})
                payload_template[cid] = _wrap_invariants(rest.strip())
            continue

        # list continuation: indented prose directly after a list/cont slot (no marker)
        if skeleton and skeleton[-1].get("kind") in ("list", "list-static", "cont", "cont-static"):
            m_cont = re.match(r"^(\s+)(\S.*)$", stripped)
            if m_cont and not re.match(r"^[-*+]|\d+\.", m_cont.group(2)) and not stripped.lstrip().startswith(">"):
                indent, text = m_cont.group(1), m_cont.group(2)
                if _is_invariant_segment(text):
                    skeleton.append({"id": None, "verbatim": line, "kind": "cont-static", "line": i})
                else:
                    cid = f"markdown:{i}:cont"
                    prefix, rest = _split_prefix(text)
                    skeleton.append({"id": cid, "prefix": prefix, "indent": indent, "kind": "cont", "line": i})
                    payload_template[cid] = _wrap_invariants(rest.strip())
                continue

        # blockquote
        m = re.match(r"^(\s*>\s?)(.*)$", stripped)
        if m:
            marker, text = m.group(1), m.group(2)
            if _is_invariant_segment(text):
                skeleton.append({"id": None, "verbatim": line, "kind": "quote-static", "line": i})
            else:
                cid = f"markdown:{i}:quote"
                prefix, rest = _split_prefix(text)
                skeleton.append({"id": cid, "prefix": prefix, "marker": marker, "kind": "quote", "line": i})
                payload_template[cid] = _wrap_invariants(rest.strip())
            continue

        # link-only line [text](url): keep verbatim
        if re.match(r"^\s*\[[^\]]*\]\([^)]*\)\s*$", stripped):
            skeleton.append({"id": None, "verbatim": line, "kind": "link", "line": i})
            continue

        # paragraph
        if _is_invariant_segment(stripped):
            skeleton.append({"id": None, "verbatim": line, "kind": "para-static", "line": i})
        else:
            cid = f"markdown:{i}:para"
            prefix, rest = _split_prefix(stripped)
            skeleton.append({"id": cid, "prefix": prefix, "kind": "para", "line": i})
            payload_template[cid] = _wrap_invariants(rest.strip())

    # write skeleton + per-lang templates
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "skeleton.json").write_text(
        json.dumps(skeleton, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    for lang in SUPPORTED:
        (out_dir / f"payload.{lang}.json").write_text(
            json.dumps(payload_template, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    return {"segments": len(payload_template), "lines": len(lines)}


# --------------------------------------------------------------------------- #
# .md reassemble
# --------------------------------------------------------------------------- #

def reassemble_md(source: Path, payload_path: Path, out: Path) -> dict:
    work_dir = payload_path.parent
    skeleton_path = work_dir / "skeleton.json"
    if not skeleton_path.exists():
        return {"error": f"skeleton not found at {skeleton_path}; run extract first"}
    skeleton = json.loads(skeleton_path.read_text(encoding="utf-8"))
    payload = json.loads(payload_path.read_text(encoding="utf-8"))

    blanks = []
    rendered = []
    for slot in skeleton:
        kind = slot["kind"]
        if slot.get("id") is None and kind != "table":
            rendered.append(slot["verbatim"])
            continue

        if kind == "table":
            # reconstruct: prefix + | cells |
            cells_out = []
            for c in slot["cells"]:
                if c["id"] is None:
                    cells_out.append(c["verbatim"])
                else:
                    val = payload.get(c["id"], "")
                    if not val:
                        blanks.append(c["id"])
                    cells_out.append((c.get("prefix", "") + _unwrap_placeholders(val)).strip())
            rendered.append("| " + " | ".join(cells_out) + " |")
            continue

        val = payload.get(slot["id"], "")
        if not val:
            blanks.append(slot["id"])
            val = ""  # leave blank so checker detects it
        body = (slot.get("prefix", "") + _unwrap_placeholders(val))
        if kind == "heading":
            rendered.append(f"{slot['marker']} {body}".rstrip())
        elif kind == "list":
            rendered.append(f"{slot['indent']}{slot['marker']} {body}".rstrip())
        elif kind == "quote":
            rendered.append(f"{slot['marker']}{body}".rstrip())
        elif kind == "cont":
            rendered.append(f"{slot['indent']}{body}".rstrip())
        else:  # para
            rendered.append(body.rstrip() if body else "")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(rendered) + "\n", encoding="utf-8")
    src_lines = len(source.read_text(encoding="utf-8").splitlines())
    out_lines = len(rendered)
    return {
        "written": str(out),
        "src_lines": src_lines,
        "out_lines": out_lines,
        "parity": abs(src_lines - out_lines) <= 1,
        "blanks": blanks,
    }


# --------------------------------------------------------------------------- #
# .md check
# --------------------------------------------------------------------------- #

def check_md(source: Path, target: Path) -> dict:
    if not target.exists():
        return {"error": f"{target} does not exist"}
    src = source.read_text(encoding="utf-8").splitlines()
    tgt = target.read_text(encoding="utf-8").splitlines()
    blanks = sum(1 for ln in tgt if not ln.strip() and False)  # placeholder
    # crude untranslated detector: count target lines identical to source line
    identical = 0
    for s, t in zip(src, tgt):
        if s == t and s.strip() and not _is_invariant_segment(s):
            identical += 1
    return {
        "target": str(target),
        "src_lines": len(src),
        "tgt_lines": len(tgt),
        "parity": abs(len(src) - len(tgt)) <= 1,
        "possibly_untranslated": identical,
    }


# --------------------------------------------------------------------------- #
# nls (package.nls.*.json)
# --------------------------------------------------------------------------- #

def _load_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def extract_nls(source: Path, missing: Path | None, out: Path) -> dict:
    src = _load_json(source)
    miss = _load_json(missing) if missing and missing.exists() else {}
    payload = {}
    for k, v in src.items():
        # drift == value in the lang file still equals English, or key absent
        cur = miss.get(k)
        if cur is None or cur == v:
            payload[k] = v
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"keys_total": len(src), "keys_to_translate": len(payload)}


def reassemble_nls(source: Path, payload: Path, out: Path) -> dict:
    src = _load_json(source)
    pl = _load_json(payload)
    existing = _load_json(out) if out.exists() else {}
    merged = dict(src)  # English keys as base order
    for k in src:
        if k in pl:
            merged[k] = pl[k]
        elif k in existing:
            merged[k] = existing[k]
        else:
            merged[k] = src[k]  # fallback to English if never translated
    blanks = [k for k in src if not merged.get(k)]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"written": str(out), "keys": len(merged), "blanks": blanks}


def check_nls(source: Path, lang_glob_dir: Path) -> list[dict]:
    src = _load_json(source)
    results = []
    for f in sorted(lang_glob_dir.glob("package.nls.*.json")):
        tgt = _load_json(f)
        results.append({
            "file": f.name,
            "src_keys": len(src),
            "tgt_keys": len(tgt),
            "parity": set(src.keys()) == set(tgt.keys()),
            "missing": sorted(set(src) - set(tgt)),
            "extra": sorted(set(tgt) - set(src)),
        })
    return results


# --------------------------------------------------------------------------- #
# bundle.l10n.*.json
# --------------------------------------------------------------------------- #

def _load_bundle_source(source: Path) -> dict:
    """Load the English source bundle. If the file doesn't exist, synthesize
    an identity map {key: key} from the union of keys across all existing
    bundle.l10n.*.json files in the same directory (bundle keys ARE the
    English source strings)."""
    if source.exists():
        return _load_json(source)
    keys: list[str] = []
    seen = set()
    for f in sorted(source.parent.glob("bundle.l10n.*.json")):
        for k in _load_json(f).keys():
            if k not in seen:
                seen.add(k)
                keys.append(k)
    return {k: k for k in keys}


def extract_bundle(source: Path, missing: Path | None, out: Path) -> dict:
    src = _load_bundle_source(source)
    miss = _load_json(missing) if missing and missing.exists() else {}
    payload = {}
    for k, _ in src.items():
        cur = miss.get(k)
        if cur is None or cur == k or cur == "":
            payload[k] = ""  # value empty = needs translation; key is English source
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"keys_total": len(src), "keys_to_translate": len(payload)}


def reassemble_bundle(source: Path, payload: Path, out: Path) -> dict:
    src = _load_bundle_source(source)
    pl = _load_json(payload)
    existing = _load_json(out) if out.exists() else {}
    # base = existing order; add new src keys at the end
    merged = dict(existing)
    for k in src:
        if k in pl and pl[k]:
            merged[k] = pl[k]
        elif k not in merged:
            merged[k] = ""  # blank -> checker flags
    # strip stale keys not in source
    merged = {k: v for k, v in merged.items() if k in src}
    blanks = [k for k, v in merged.items() if not v]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"written": str(out), "keys": len(merged), "blanks": blanks}


def check_bundle(source: Path, lang_glob_dir: Path) -> list[dict]:
    src = _load_bundle_source(source)
    results = []
    for f in sorted(lang_glob_dir.glob("bundle.l10n.*.json")):
        tgt = _load_json(f)
        results.append({
            "file": f.name,
            "src_keys": len(src),
            "tgt_keys": len(tgt),
            "parity": set(src.keys()) == set(tgt.keys()),
            "missing": sorted(set(src) - set(tgt)),
            "extra": sorted(set(tgt) - set(src)),
            "blanks": sum(1 for v in tgt.values() if not v),
        })
    return results


# --------------------------------------------------------------------------- #
# cli
# --------------------------------------------------------------------------- #

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="l10n-sync")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("extract")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)

    p = sub.add_parser("reassemble")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--payload", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)

    p = sub.add_parser("check")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--target", type=Path, required=True)

    p = sub.add_parser("extract-nls")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--missing", type=Path)
    p.add_argument("--out", type=Path, required=True)

    p = sub.add_parser("reassemble-nls")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--payload", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)

    p = sub.add_parser("check-nls")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--dir", type=Path, required=True)

    p = sub.add_parser("extract-bundle")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--missing", type=Path)
    p.add_argument("--out", type=Path, required=True)

    p = sub.add_parser("reassemble-bundle")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--payload", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)

    p = sub.add_parser("check-bundle")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--dir", type=Path, required=True)

    args = ap.parse_args(argv)
    out = sys.stdout

    if args.cmd == "extract":
        r = extract_md(args.source, args.out)
    elif args.cmd == "reassemble":
        r = reassemble_md(args.source, args.payload, args.out)
    elif args.cmd == "check":
        r = check_md(args.source, args.target)
    elif args.cmd == "extract-nls":
        r = extract_nls(args.source, args.missing, args.out)
    elif args.cmd == "reassemble-nls":
        r = reassemble_nls(args.source, args.payload, args.out)
    elif args.cmd == "check-nls":
        r = check_nls(args.source, args.dir)
    elif args.cmd == "extract-bundle":
        r = extract_bundle(args.source, args.missing, args.out)
    elif args.cmd == "reassemble-bundle":
        r = reassemble_bundle(args.source, args.payload, args.out)
    elif args.cmd == "check-bundle":
        r = check_bundle(args.source, args.dir)
    else:
        ap.error(f"unknown cmd {args.cmd}")
        return 2

    out.write(json.dumps(r, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))