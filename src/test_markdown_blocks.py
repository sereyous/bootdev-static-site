import unittest
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks, markdown_to_html_node

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype_unordered_list(self):
        md = "- item 1\n- item 2\n- item 3"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(md))

    def test_block_to_blocktype_ordered_list(self):
        md = "1. item 1\n2. item 2\n3. item 3"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(md))

    def test_block_to_blocktype_quote(self):
        md = ">To be or not to be,\n>that is the question"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(md))

    def test_block_to_blocktype_code(self):
        md = "```print('hello, world!')\nreturn 0```"
        self.assertEqual(BlockType.CODE, block_to_block_type(md))

    def test_block_to_blocktype_heading(self):
        for i in range(1, 7):
            heading = "#" * i + f" Heading {i}"
            self.assertEqual(BlockType.HEADING, block_to_block_type(heading))

    def test_block_to_block_type_paragraph(self):
        md = "I am just a\nlowly paragraph"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(md))

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
