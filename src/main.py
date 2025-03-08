from textnode import TextNode, TextType


def main():
  node = TextNode("Hello World", TextType.ITALIC_TEXT, "https://www.candaequipment.net")
  print(node)

if __name__ == "__main__":
  main()