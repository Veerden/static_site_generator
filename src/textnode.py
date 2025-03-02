from enum import Enum

class TextType(Enum):

  NORMAL_TEXT = "normal text"
  BOLD_TEXT = "bold text"
  ITALIC_TEXT = "italic text"
  CODE_TEXT = "code text"
  LINKS = "links"
  IMAGES = "images"

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other_node):
    if not isinstance(other_node, TextNode):
      return False
    
    return(
      self.text == other_node.text and
      self.text_type == other_node.text_type and 
      self.url == other_node.url
    )


  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"