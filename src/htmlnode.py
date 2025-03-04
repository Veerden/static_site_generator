from enum import Enum

class HTMLNode:
  def __init__(self,tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    
  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    if not self.props:
      return ""
    props_str = ""
    for key, value in self.props.items():
      props_str += f' {key}="{value}"'
    return props_str
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, children=None, props=props)
    self.value = value
    self.tag = tag
    self.props = props

  def to_html(self):
    if self.value == None:
      raise ValueError("Leaf nodes must have a value")
    if self.tag is None:
      return self.value
    html = "<" + self.tag

    if self.props:
      for prop_name, prop_value in self.props.items():
        html += f' {prop_name}="{prop_value}"'
    html += ">" + self.value + "</" + self.tag + ">"

    return html
  
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, children, props=props)
    self.tag = tag
    self.children = children
    self.props = props

  def to_html(self):
    if self.tag is None:
        raise ValueError("Parent nodes must have a tag")
    if self.children is None:
        raise ValueError("Parent nodes must have children")
    
    # Start with the opening tag
    html = f"<{self.tag}"
    
    # Add any properties if they exist
    if self.props:
        props_html = self.props_to_html()
        html += props_html
    
    # Close the opening tag
    html += ">"
    
    # Add all children's HTML
    for child in self.children:
        html += child.to_html()
    
    # Add the closing tag
    html += f"</{self.tag}>"
    
    return html
