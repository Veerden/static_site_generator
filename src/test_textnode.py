import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("I am a test", TextType.ITALIC, url = "https://www.candaequipment.net")
        node2 = TextNode("I am not a test", TextType.ITALIC, url = "https://www.candaequipment.net")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("url's the same?", TextType.BOLD, url=None)
        node2 = TextNode("url's the same?", TextType.BOLD, url="https://www.notthesame.com")
        self.assertNotEqual(node, node2)

    def test_text_typ_not_eq(self):
        node = TextNode("we are the droids you're looking for", TextType.BOLD, url=None)
        node2 = TextNode("we are the droids you're looking for", TextType.NORMAL, url=None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()