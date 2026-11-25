#!/usr/bin/env python3
"""Convert Markdown to HTML from a file or stdin."""

import argparse
import sys
from pathlib import Path

import markdown


def convert(md_text: str) -> str:
    """Convert Markdown text to an HTML fragment."""
    return markdown.markdown(md_text, extensions=["fenced_code", "tables"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML.")
    parser.add_argument("input", nargs="?",
                        help="Input .md file (omit or use '-' to read from stdin)")
    parser.add_argument("-o", "--output",
                        help="Output .html file (default: write to stdout)")
    args = parser.parse_args(argv)

    from_file = bool(args.input) and args.input != "-"
    try:
        md_text = Path(args.input).read_text(encoding="utf-8") if from_file else sys.stdin.read()
    except (OSError, UnicodeDecodeError) as exc:
        reason = getattr(exc, "strerror", None) or exc
        print(f"Error: cannot read {args.input if from_file else 'stdin'}: {reason}", file=sys.stderr)
        return 1

    html = convert(md_text)

    if args.output:
        try:
            Path(args.output).write_text(html, encoding="utf-8")
        except OSError as exc:
            print(f"Error: cannot write {args.output}: {exc.strerror or exc}", file=sys.stderr)
            return 1
        print(f"Wrote {args.output}")
    else:
        print(html)
    return 0


if __name__ == "__main__":
    sys.exit(main())
