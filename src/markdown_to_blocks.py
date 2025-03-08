from enum import Enum
import re

class BlockType(Enum):

  PARAGRAPH = 0
  HEADING = 1
  CODE = 2
  QUOTE = 3
  UNORDERED_LIST = 4
  ORDERED_LIST = 5



def markdown_to_blocks(markdown):
  blocks = [block.strip() for block in markdown.split("\n\n") if block.strip()]
  return blocks

def block_to_block_type(block):
  # Check for heading (starts with 1-6 # characters followed by a space)
  if block.startswith('#'):
    # Make sure it's a valid heading (1-6 # followed by space)
    heading_match = re.match(r'^#{1,6} ', block)
    if heading_match:
      return BlockType.HEADING
    
  # Check for code block (starts and ends with ```)
  if block.startswith('```') and block.endswith('```'):
    return BlockType.CODE
  
  # Check for quote block (every line starts with >)
  lines = block.split('\n')
  if all(line.startswith('>') for line in lines):
    return BlockType.QUOTE
  
  # Check for unordered list (every line starts with - followed by space)
  if all(line.startswith('- ') for line in lines):
    return BlockType.UNORDERED_LIST
  
  # Check for ordered list (every line starts with a number, then . then space)
  # This is more complex = need to check numbers are sequential starting from 1
  if lines and lines[0].startswith('1. '):
    is_ordered_list = True
    for i, line in enumerate(lines, 1):
      if not line.startswith(f"{i}. "):
        is_ordered_list = False
        break
    if is_ordered_list:
      return BlockType.ORDERED_LIST
    
  # Default case - it's a paragraph
  return BlockType.PARAGRAPH

  

