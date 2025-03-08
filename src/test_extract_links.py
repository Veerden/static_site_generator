import unittest
from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

class TestExtractLInk(unittest.TestCase):
  def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_extract_markdown_links(self):
    matches = extract_markdown_links("This is text with a link [to canda](https://www.candaequipment.net)")
    self.assertListEqual([("to canda", "https://www.candaequipment.net")], matches)

  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

  def test_split_links(self):
    node = TextNode(
        "This is text with an [link](https://www.google.com) and another [second link](https://www.udemy.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://www.udemy.com"
            ),
        ],
        new_nodes,
    )