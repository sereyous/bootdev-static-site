import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("no header found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, os.path.dirname(dest_dir_path), "index.html")
        return

    for file in os.listdir(dir_path_content):
        if os.path.isfile(file):
            generate_page(dir_path_content, template_path, os.path.dirname(dest_dir_path), "index.html")
        else:
            new_dest = os.path.dirname(os.path.join(dest_dir_path, file))
            os.makedirs(new_dest)
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, new_dest)
