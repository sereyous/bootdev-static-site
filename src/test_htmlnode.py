import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = { "href": "https://www.google.com", "target": "_blank" }
        html_node = HTMLNode("a", props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, html_node.props_to_html())

    def test_props_to_html_when_props_is_none(self):
        html_node = HTMLNode()
        expected = ""
        self.assertEqual(expected, html_node.props_to_html())

    def test_props_to_html_when_props_is_empty_dict(self):
        html_node = HTMLNode(props={})
        expected = ""
        self.assertEqual(expected, html_node.props_to_html())

