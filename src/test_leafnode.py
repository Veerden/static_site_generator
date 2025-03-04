import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_a_with_href(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Just some text")
    self.assertEqual(node.to_html(), "Just some text")

  def test_leaf_to_html_no_value(self):
    with self.assertRaises(ValueError):
      node = LeafNode("p", None)
      node.to_html()

if __name__ == "__main__":
  unittest.main()