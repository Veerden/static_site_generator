from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter
from extract_links import split_nodes_link, split_nodes_image

def text_to_textnodes(text):
  nodes = [TextNode(text, TextType.TEXT)]

  nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)

  return nodes