#!/usr/bin/env python3

import argparse
import sys

import freeplane
import mdutils


ICON_MAP = {
    'button_cancel': '❌',
    'button_ok': '✅',
    'help': '❓',
    'idea': '💡',
    'messagebox_warning': '⚠️',
    'yes': '❗',
}
ICON_NOT_FOUND = '[ICON NOT FOUND: %s]'


def convert(filename: str, max_heading_levels: int):
    mm = freeplane.Mindmap(filename)
    md = mdutils.MdUtils(file_name='dummy.md')  # Will not use the file.
    md.new_list(tree_to_nested_list(md, mm.rootnode, 1, max_heading_levels))
    print(md.get_md_text())    


def tree_to_nested_list(
        md: mdutils.MdUtils,
        node: freeplane.Node,
        level: int,
        max_heading_levels: int):
    items = []
    for c in node.children:
        items.append(format_node(md, c, level, max_heading_levels))
        items.append(tree_to_nested_list(md, c, level + 1, max_heading_levels))
    return items


def format_node(
        md: mdutils.MdUtils,
        node: freeplane.Node,
        level: int,
        max_heading_levels: int):
    h = '#' * level + ' ' if level <= max_heading_levels else ''
    icons = ''.join([ICON_MAP.get(i, ICON_NOT_FOUND % i) for i in node.icons])
    if icons:
        icons += ' '
    text = md.new_inline_link(link=node.hyperlink, text=node.plaintext) \
        if node.hyperlink else node.plaintext
    return h + icons + text


def main(args: argparse.Namespace):
    convert(args.filename, args.max_heading_levels)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert a Freeplane mindmap to Markdown')
    parser.add_argument('filename', type=str, help='File to convert')
    parser.add_argument(
        '--max_heading_levels',
        type=int,
        default=2,
        help='Max number of heading levels')

    args = parser.parse_args()
    sys.exit(main(args))
