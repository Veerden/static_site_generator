import os
import shutil

def copy_static(source, destination):
  if os.path.exists(destination):
    shutil.rmtree(destination)
  os.mkdir(destination)

  for item in os.listdir(source):
    # Create full path for the source item
    source_item_path = os.path.join(source, item)
    # Create full path for the destination item
    dest_item_path = os.path.join(destination, item)
    # Check if item is a file
    if os.path.isfile(source_item_path):
      # If it's a file, copy it
      shutil.copy(source_item_path,dest_item_path)
      print(f"Copied file": {source_item_path} to {dest_item_path})
    else:
      # If it's a directory, create it and recurse
      os.mkdir(dest_item_path)
      print(f"Created directory: {dest_item_path}")
      copy_static(source_item_path, dest_item_path)

  
