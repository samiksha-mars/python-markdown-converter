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

Notes:

- The output is an HTML fragment (no `<html>`, `<head>` or `<body>` wrapper), ready to be
  embedded in a page or template.
- Input and output files are read and written as UTF-8. If the input can't be read or the
  output can't be written, an error is printed and the exit status is 1.
- Raw HTML in the Markdown is passed through unchanged, so don't use this to render
  untrusted input in a web page without sanitizing the result.

## Tests

With the dependencies from `requirements.txt` installed (see Setup):

```bash
python3 -m unittest test_markdown_to_html.py
```
