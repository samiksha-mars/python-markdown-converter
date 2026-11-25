import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

from markdown_to_html import convert, main


class ConvertTest(unittest.TestCase):

    def test_heading(self):
        self.assertIn("<h1>", convert("# Hello"))
        self.assertIn("Hello", convert("# Hello"))

    def test_bold(self):
        self.assertIn("<strong>bold</strong>", convert("**bold**"))

    def test_link(self):
        html = convert("[Example](https://example.com)")
        self.assertIn('<a href="https://example.com">Example</a>', html)

    def test_fenced_code_block(self):
        html = convert("```python\nprint('hi')\n```")
        self.assertIn("<code", html)
        self.assertIn("language-python", html)

    def test_table(self):
        html = convert("| A | B |\n|---|---|\n| 1 | 2 |")
        self.assertIn("<table>", html)


class MainTest(unittest.TestCase):

    def run_main(self, argv, stdin=""):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err), mock.patch("sys.stdin", io.StringIO(stdin)):
            code = main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_reads_stdin_by_default(self):
        code, out, _ = self.run_main([], stdin="# Hello")
        self.assertEqual(code, 0)
        self.assertIn("<h1>Hello</h1>", out)

    def test_file_to_output_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "in.md"
            target = Path(tmp) / "out.html"
            source.write_text("**hi**", encoding="utf-8")
            code, out, _ = self.run_main([str(source), "-o", str(target)])
            self.assertEqual(code, 0)
            self.assertIn("Wrote", out)
            self.assertIn("<strong>hi</strong>", target.read_text(encoding="utf-8"))

    def test_missing_input_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out, err = self.run_main([str(Path(tmp) / "missing.md")])
        self.assertEqual(code, 1)
        self.assertEqual(out, "")
        self.assertIn("cannot read", err)

    def test_unwritable_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "no-such-dir" / "out.html"
            code, _, err = self.run_main(["-o", str(target)], stdin="# Hi")
        self.assertEqual(code, 1)
        self.assertIn("cannot write", err)


if __name__ == "__main__":
    unittest.main()
