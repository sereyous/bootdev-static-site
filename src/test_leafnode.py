import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_paragraph_node(self):
        expected = "<p>Hello, world!</p>"
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(expected, node.to_html())

    def test_paragraph_node_with_attributes(self):
        expected = "<p class=\"paragraph-sm\">Hello, world!</p>"
        node = LeafNode("p", "Hello, world!", {"class": "paragraph-sm"})
        self.assertEqual(expected, node.to_html())

    def test_anchor_tag(self):
        expected = '<a href="https://www.google.com">Click me!</a>'
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), expected)

