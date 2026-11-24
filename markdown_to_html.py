#!/usr/bin/env python3
"""Convert Markdown to HTML from a file or stdin."""

import argparse
import sys
from pathlib import Path

import markdown


def convert(md_text: str) -> str:
    """Convert Markdown text to an HTML fragment."""
    return markdown.markdown(md_text, extensions=["fenced_code", "tables"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML.")
    parser.add_argument("input", nargs="?",
                        help="Input .md file (omit or use '-' to read from stdin)")
    parser.add_argument("-o", "--output",
                        help="Output .html file (default: write to stdout)")
    args = parser.parse_args()

    if args.input and args.input != "-":
        md_text = Path(args.input).read_text(encoding="utf-8")
    else:
        md_text = sys.stdin.read()

    html = convert(md_text)

    if args.output:
        Path(args.output).write_text(html, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(html)


if __name__ == "__main__":
    main()
