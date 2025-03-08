import re
from textnode import TextType, TextNode

def extract_markdown_images(text):
  return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  
def extract_markdown_links(text):
  return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
  new_nodes = []

  for old_node in old_nodes:
    # Skip non-text nodes
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    #Extract all images from the text  
    images = extract_markdown_images(old_node.text)

    # If no images, keep the original node
    if not images:
      new_nodes.append(old_node)
      continue

    # Process the text, handling one image at a time
    remaining_text = old_node.text

    for image_alt, image_url in images:
      # Split around current image
      image_markdown = f"![{image_alt}]({image_url})"
      sections = remaining_text.split(image_markdown, 1)

      # Add text before image (if not empty)j
      if sections[0]:
        new_nodes.append(TextNode(sections[0], TextType.TEXT))

      # Add the image node
      new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

      # Update remaining text
      if len(sections) > 1:
        remaining_text = sections[1]
      else:
        remaining_text = ""

      # Add any remaining text after all images are processed
    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))

  return new_nodes


def split_nodes_link(old_nodes):
  new_nodes = []

  for old_node in old_nodes:
    # Skip non-text nodes
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    #Extract all images from the text  
    images = extract_markdown_links(old_node.text)

    # If no images, keep the original node
    if not images:
      new_nodes.append(old_node)
      continue

    # Process the text, handling one image at a time
    remaining_text = old_node.text

    for link_text, link_url in images:
      # Split around current image
      image_markdown = f"[{link_text}]({link_url})"
      sections = remaining_text.split(image_markdown, 1)

      # Add text before image (if not empty)j
      if sections[0]:
        new_nodes.append(TextNode(sections[0], TextType.TEXT))

      # Add the image node
      new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

      # Update remaining text
      if len(sections) > 1:
        remaining_text = sections[1]
      else:
        remaining_text = ""

      # Add any remaining text after all images are processed
    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))

  return new_nodes

