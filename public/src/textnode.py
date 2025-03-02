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