#!/usr/bin/env python
import os
import argparse
from colorama import Fore, Style
def create(file_path):
    root_folder = os.getcwd()
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if "." in line and "    " not in line: 
            line2 = ""
        line = line.strip()
        if line.endswith('\\') or line.endswith('/'): 
            line2 = line.rstrip('\\').rstrip('/')
        else:
            file_path = os.path.join(root_folder, line2, line)
            create_file(file_path)
    generate_init_files(root_folder)

def create_file(file_path):
    if file_path:
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                if file_path.endswith('.py') and "__init__" not in file_path:
                    class_name = os.path.basename(file_path).replace('.py', '').capitalize()
                    f.write(f"class {class_name}:\n    pass\n")
    else:
        print(f"Empty file path encountered: {file_path}")
    print(f'File created: {file_path}')

def generate_init_files(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder): 
        python_files = [f for f in filenames if f.endswith('.py') and f != '__init__.py']
        if python_files:
            init_file_path = os.path.join(dirpath, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                for py_file in python_files:
                    class_name = py_file.replace('.py', '').capitalize()
                    init_file.write(f"from .{py_file.replace('.py', '')} import {class_name}\n")

def main():
    parser = argparse.ArgumentParser(description="Create directories and files based on the outline in a text file.")
    parser.add_argument('file', help="Path to the outline text file")
    parser.parse_args()
    args = parser.parse_args()
    if not args.file:
        print(parser.usage)
    else:
        create(args.file)

if __name__ == "__main__":
    main()

