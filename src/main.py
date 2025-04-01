import argparse
from utilities import copy_static_to_output_dir
from html_pages import generate_pages_recursive

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-dir', help="file locations relative to project root", default="public")
    parser.add_argument('-p', '--base-path', help="url base path", default="/")
    args = parser.parse_args()

    copy_static_to_output_dir(args.output_dir)
    generate_pages_recursive("content", "template.html", args.output_dir, args.base_path)


main()

