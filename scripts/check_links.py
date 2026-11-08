#!/usr/bin/env python3
"""Check relative links and heading anchors in all tracked Markdown files.

Usage: python3 scripts/check_links.py

Links to GitHub pages of the repository itself (../../issues, ../../discussions,
../../releases) and to external URLs are not checked. Exits with 1 when a
file link or an anchor does not resolve.
"""
import os
import re
import subprocess
import sys
from collections import defaultdict

GITHUB_PAGES = ("../../issues", "../../discussions", "../../releases", "../../pulls")


def heading_slugs(text):
    """Return the anchors GitHub generates for the headings in a Markdown file."""
    seen = defaultdict(int)
    slugs = set()
    fence = False
    for line in text.split("\n"):
        if re.match(r"^\s*(```|~~~)", line):
            fence = not fence
        if fence:
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            h = re.sub(r"<[^>]+>", "", m.group(1)).strip().lower()
            h = re.sub(r"[^\w\- ]", "", h).replace(" ", "-")
            n = seen[h]
            seen[h] += 1
            slugs.add(h if n == 0 else f"{h}-{n}")
    slugs.update(re.findall(r'<a (?:name|id)="([^"]+)"', text))
    return slugs


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    files = subprocess.check_output(["git", "ls-files"]).decode().split()
    tracked = set(files)
    cache = {}
    broken = []
    for f in files:
        if not f.endswith(".md"):
            continue
        text = open(f, encoding="utf-8").read()
        for m in re.finditer(r"\]\(([^)\s]*)\)", text):
            url = m.group(1)
            if re.match(r"^[a-z]+:", url) or url.startswith(GITHUB_PAGES):
                continue
            path, _, anchor = url.partition("#")
            target = f if not path else os.path.normpath(os.path.join(os.path.dirname(f), path)).replace("\\", "/")
            if path and target not in tracked and not any(x.startswith(target.rstrip("/") + "/") for x in tracked):
                broken.append((f, url, "missing file"))
                continue
            if anchor and target.endswith(".md"):
                if target not in cache:
                    cache[target] = heading_slugs(open(target, encoding="utf-8").read())
                if anchor not in cache[target]:
                    broken.append((f, url, "missing anchor"))
    for f, url, why in broken:
        print(f"{f}: {url} ({why})")
    print(f"{len(broken)} broken link(s)")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
