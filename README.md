# Python Markdown to HTML Converter

A small command-line tool that converts Markdown to HTML using the
[`markdown`](https://python-markdown.github.io/) library, with support for fenced
code blocks and tables.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Convert a file and print HTML to stdout
python3 markdown_to_html.py sample.md

# Convert a file and write to an HTML file
python3 markdown_to_html.py sample.md -o sample.html

# Convert from stdin
echo "# Hello" | python3 markdown_to_html.py
```

## Tests

```bash
python3 -m unittest test_markdown_to_html.py
```
