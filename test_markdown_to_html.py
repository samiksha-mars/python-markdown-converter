import unittest

from markdown_to_html import convert


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


if __name__ == "__main__":
    unittest.main()
