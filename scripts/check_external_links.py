#!/usr/bin/env python3
"""Check that external links in Markdown files still resolve.

Usage: python3 scripts/check_external_links.py [FILE ...]

With no arguments, checks docs/REFERENCES.md. Placeholder hosts (example.com,
169.254.169.254, *.amazonaws.com endpoints in code samples) are skipped.
Prints links that fail or redirect, and exits with 1 if any link fails.
Redirects are reported but do not fail the run.
"""
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

SKIP = re.compile(r"example\.com|169\.254\.|amazonaws\.com|\.on\.aws|<|\.\.\.")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; saa-c03-link-check)"}


def collect(paths):
    urls = []
    for path in paths:
        text = open(path, encoding="utf-8").read()
        for url in re.findall(r"\]\((https?://[^)\s]+)\)", text):
            if not SKIP.search(url) and url not in urls:
                urls.append(url)
    return urls


def check(url):
    last = None
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return url, resp.status, resp.geturl()
        except urllib.error.HTTPError as err:
            last = err.code
        except Exception as err:  # noqa: BLE001 - report any network failure
            last = type(err).__name__
    return url, last, ""


def main():
    paths = sys.argv[1:] or ["docs/REFERENCES.md"]
    urls = collect(paths)
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, urls))
    failed = [r for r in results if r[1] != 200]
    moved = [r for r in results if r[1] == 200 and r[2].split("#")[0].rstrip("/") != r[0].split("#")[0].rstrip("/")]
    for url, status, _ in failed:
        print(f"FAIL {status} {url}")
    for url, _, final in moved:
        print(f"MOVED {url} -> {final}")
    print(f"{len(urls)} links, {len(failed)} failed, {len(moved)} redirected")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
