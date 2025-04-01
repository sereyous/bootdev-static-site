import re
from enum import Enum
from inline_markdown import text_to_textnodes, text_node_to_html_node
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    line_count = len(lines)

    if line_count == 1:
        heading = r"^#{1,6}\s(.*)"
        if re.search(heading, block):
            return BlockType.HEADING

    code_block = r"^```(.*?)```$"
    if re.search(code_block, block, re.DOTALL):
        return BlockType.CODE

    is_unordered_list = len(list(filter(lambda line: line.startswith("- "), lines))) == line_count
    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    is_quote = len(list(filter(lambda line: line.startswith(">"), lines))) == line_count
    if is_quote:
        return BlockType.QUOTE

    is_ordered_list = True
    for i in range(line_count):
        if not lines[i].startswith(f"{i + 1}. "):
            is_ordered_list = False

    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        cleaned_blocks.append(block)
    return cleaned_blocks


def text_to_children(text):
    print("text_to_children")
    print(text)
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                paragraph = " ".join(lines)
                node = ParentNode("p", text_to_children(paragraph))
            case BlockType.QUOTE:
                lines = block.split("\n")
                new_lines = []
                for line in lines:
                    if not line.startswith(">"):
                        raise ValueError("invalid block quote")
                    new_lines.append(line.lstrip(">").strip())
                content = " ".join(new_lines)
                children = text_to_children(content)
                node = ParentNode("blockquote", children)
            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                html_items = []
                for item in items:
                    text = item[3:]
                    children = text_to_children(text)
                    html_items.append(ParentNode("li", children))
                node = ParentNode("ol", html_items)
            case BlockType.UNORDERED_LIST:
                print(block_type)
                items = block.split("\n")
                html_children = []
                for item in items:
                    print(f"item {item}")
                    text = item[2:]
                    children = text_to_children(text)
                    html_children.append(ParentNode("li", children))
                node = ParentNode("ul", html_children)
            case BlockType.HEADING:
                level = 0
                for char in block:
                    if "#" == char:
                        level += 1
                    else:
                        break
                if level + 1 >= len(block):
                    raise ValueError(f"invalid heading level {level}")
                text = block[level+1:]
                children = text_to_children(text)
                node = ParentNode(f"h{level}", children)
            case BlockType.CODE:
                if not block.startswith("```") or not block.endswith("```"):
                    raise ValueError("invalid code block")
                text = block[4:-3]
                raw_text_node = TextNode(text, TextType.TEXT)
                child = text_node_to_html_node(raw_text_node)
                code = ParentNode("code", [child])
                node = ParentNode("pre", [code])
            case _:
                raise ValueError("unsupported block type")
        child_nodes.append(node)
        print(child_nodes)
    return ParentNode("div", child_nodes)

