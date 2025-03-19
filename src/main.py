import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page
from pathlib import Path
from generate_recursive import generate_pages_recursive

basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages recursively...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath )


main()
