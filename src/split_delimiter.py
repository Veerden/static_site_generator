from textnode import TextType, TextNode



def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    text = old_node.text

    if delimiter not in text:
      new_nodes.append(old_node)
      continue

    first_delimiter_pos = text.find(delimiter)

    second_delimiter_pos = text.find(delimiter, first_delimiter_pos + len(delimiter))

    if second_delimiter_pos == -1:
      raise Exception(f"Invalid markdown: opening delimiter '{delimiter}' without closing delimiter")
    
    before_text = text[:first_delimiter_pos]

    between_text = text[first_delimiter_pos + len(delimiter):second_delimiter_pos]

    after_text = text[second_delimiter_pos + len(delimiter):]

    if before_text:
      new_nodes.append(TextNode(before_text, TextType.TEXT))

    new_nodes.append(TextNode(between_text, text_type))

    if after_text:
      after_node = TextNode(after_text, TextType.TEXT)
      result_nodes = split_nodes_delimiter([after_node], delimiter, text_type)
      new_nodes.extend(result_nodes)

  return new_nodes

