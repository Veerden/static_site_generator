import unittest
from markdown_to_html import markdown_to_html_node, text_to_children, extract_heading_content, process_list_items, extract_code_content


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

def test_headers(self):
    md = """
# Heading 1

## Heading 2

### Heading 3
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>"
    )

def test_ordered_lists(self):
    md = """
1. First item
2. Second item
3. Third item with **bold**
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>First item</li><li>Second item</li><li>Third item with <b>bold</b></li></ol></div>"
    )

def test_unordered_lists(self):
    md = """
- First item
- Second item with _italic_
- Third item with `code`
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>First item</li><li>Second item with <i>italic</i></li><li>Third item with <code>code</code></li></ul></div>"
    )