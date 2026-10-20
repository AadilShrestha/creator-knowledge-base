"""Check local Markdown link/image targets and frontmatter source paths.

Usage: python tools/kb/check_links.py knowledge-base/wiki/courses/evolve/copywriting
Ignores fenced code, inline code, external URLs, and same-page anchors.
Checks target existence, not heading anchors or factual citation accuracy.
"""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]


def destinations(text):
    text = re.sub(r"^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", text, flags=re.M | re.S)
    text = re.sub(r"`[^`\n]+`", "", text)
    for match in re.finditer(r"!?\[[^\]\n]*\]\(", text):
        start = match.end()
        if text[start:start + 1] == "<":
            end = text.find(">", start)
            if end >= 0:
                yield text[start + 1:end]
            continue
        depth, cursor = 0, start
        while cursor < len(text):
            char = text[cursor]
            if char == "\\":
                cursor += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            cursor += 1
        if cursor > start:
            yield re.sub(r"\\([() ])", r"\1", text[start:cursor])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    pages = set()
    for path in args.paths:
        if not path.exists():
            parser.error(f"Path not found: {path}")
        pages.update(path.rglob("*.md") if path.is_dir() else [path])
    failures = []
    for page in sorted(pages):
        text = page.read_text(encoding="utf-8-sig")
        for target in destinations(text):
            if re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#|//)", target):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if target and not (page.parent / target).exists():
                failures.append(f"{page}: missing link/image {target}")
        front = re.match(r"\A---\s*\n(.*?)\n---", text, re.S)
        if front:
            block = re.search(r"^sources:\s*\n((?:[ \t]+.*\n?)*)", front[1], re.M)
            if block:
                for source in re.findall(r"^\s+-\s+(.+?)\s*$", block[1], re.M):
                    source = source.strip("\"'")
                    if not re.match(r"^https?://", source) and not (ROOT / source).exists():
                        failures.append(f"{page}: missing frontmatter source {source}")
    for failure in failures:
        print(failure)
    print(f"Checked {len(pages)} Markdown files; {len(failures)} missing targets.")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
