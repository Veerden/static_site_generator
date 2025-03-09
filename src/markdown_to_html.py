import re
from markdown_to_blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from split_delimiter import split_nodes_delimiter

def markdown_to_html_node(markdown):
  #create a parent div node
  parent = ParentNode("div", [], None)

  #Split markdown into blocks
  blocks = markdown_to_blocks(markdown)

  #process each block and add to parent
  for block in blocks:
    #Determine block type
    type = block_to_block_type(block)

    #Create appropriate HTML node based on type
    if type == BlockType.PARAGRAPH:
      # For paragraphs, convert the text to children nodes (handles inline markdown)
      children = text_to_children(block)
      paragraph_node = ParentNode("p", children, None)
      parent.children.append(paragraph_node)

    elif type.startswith(BlockType.HEADING):
      # Process heading blocks
      content, heading_level = extract_heading_content(block)
      children = text_to_children(content)
      heading_tag = f"h{heading_level}"
      heading_node = ParentNode(heading_tag, children, None)
      parent.children.append(heading_node)

    elif type == BlockType.UNORDERED_LIST:
      # Process unordered list blocks
      list_items = process_list_items(block, BlockType.UNORDERED_LIST)
      ul_node = ParentNode("ul", list_items, None)
      parent.children.append(ul_node)

    elif type == BlockType.ORDERED_LIST:
      # Process ordered list blocks
      list_items = process_list_items(block, BlockType.ORDERED_LIST)
      ol_node = ParentNode("ol", list_items, None)
      parent.children.append(ol_node)
        
    elif type == BlockType.CODE:
      # Process code blocks
      code_content = extract_code_content(block)
      text_node = TextNode(code_content, TextType.TEXT)
      code_node = text_node_to_html_node(text_node)
      pre_node = ParentNode("pre", [ParentNode("code", [code_node], None)], None)

      parent.children.append(pre_node)
    
    elif type == BlockType.QUOTE:
      # Remove the '>' characters at the beginning of each line
      # Join the cleaned lines back together
      quote_content = re.sub(r"^>\s*", "", block, flags=re.MULTILINE)

      # Parse the quote content for inline markdown
      quote_children = text_to_children(quote_content)

      # Create a blockquote node
      blockquote_node = ParentNode("blockquote", quote_children, None)

      parent.children.append(blockquote_node)

  return parent

#Helper functions you'll need:
def text_to_children(text):
  # First create a TextNode with the raw text
  nodes = [TextNode(text, TextType.TEXT)]

  # Convert to a list of TextNodes with inline markdown parsed
  # You'll need to use your existing functions for this
  nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)


  # Convert each TextNode to an HTMLNode
  html_nodes = []
  # Convert each parsed text node to an HTML node
  for node in nodes:
    html_node = text_node_to_html_node(node)
    html_nodes.append(html_node)

  return html_nodes

def extract_heading_content(block):
    """Extract content from a heading block and determine its level."""
    heading_level = 0
    for char in block:
        if char == '#':
            heading_level += 1
        else:
            break
    
    # Skip the #s and the space after them
    content = block[heading_level:].strip()
    return content, heading_level

def process_list_items(block, list_type):
    """Process items in a list block and return list item nodes."""
    list_items = []
    lines = block.split("\n")
    
    for line in lines:
        if not line.strip():
            continue  # Skip empty lines
            
        if list_type == BlockType.UNORDERED_LIST:
            # Remove the list marker (-, *, or +) and convert the rest
            content = line.strip()[2:]  # Skip the marker and the space after it
        else:  # ORDERED_LIST
            # Find where the actual content starts after the number, period, and space
            content_start = 0
            for i, char in enumerate(line.strip()):
                if char == '.' and i > 0 and line.strip()[i+1:i+2] == ' ':
                    content_start = i + 2
                    break
            content = line.strip()[content_start:]
            
        children = text_to_children(content)
        li_node = ParentNode("li", children, None)
        list_items.append(li_node)
        
    return list_items

def extract_code_content(block):
    """Extract content from a code block, preserving newlines."""
    lines = block.split("\n")
    # Skip the first and last lines (which contain the ```)
    # and join the rest with newlines
    return "\n".join(lines[1:-1])