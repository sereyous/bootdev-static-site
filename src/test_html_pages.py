import unittest
from html_pages import extract_title

class TestHtmlPages(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Here is a title

and a paragraph here with some **bold** text

## and a subheading
"""

        self.assertEqual("Here is a title", extract_title(md))

