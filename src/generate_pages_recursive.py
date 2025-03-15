import os
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # List all entries in the current directory
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        # Create the full path to the entry
        entry_path = os.path.join(dir_path_content, entry)
        
        # If it's a file, check if it's a markdown file
        if os.path.isfile(entry_path) and entry.endswith('.md'):
            # Calculate the relative path from content directory
            rel_path = os.path.relpath(entry_path, dir_path_content)
            
            # Calculate the destination path, converting .md to .html
            dest_file_path = os.path.join(dest_dir_path, rel_path.replace('.md', '.html'))
            
            # Make sure the destination directory exists
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
            
            # Generate the HTML and write it to the destination
            # You'll need to use your existing generate_page function here
            
        # If it's a directory, recursively process it
        elif os.path.isdir(entry_path):
            # Calculate the corresponding destination directory
            dest_subdir = os.path.join(dest_dir_path, os.path.relpath(entry_path, dir_path_content))
            
            # Recursively process the subdirectory
            generate_pages_recursive(entry_path, template_path, dest_subdir)