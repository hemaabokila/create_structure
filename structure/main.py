import os
import argparse
from pathlib import Path

def create(file_path):
    root_folder = Path.cwd()
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    current_dir = ""
    for line in lines:
        line = line.strip()
        if line.endswith(("\\", "/")):
            current_dir = line.rstrip("\\/")
        else:
            file_path = Path(root_folder, current_dir, line)
            create_file(file_path)
    
    generate_init_files(root_folder)
    generate_setup_file(root_folder)
    generate_license_file(root_folder)
    generate_readme_file(root_folder)

def create_file(file_path):
    if file_path:
        if not file_path.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w') as f:
                if file_path.suffix == '.py' and "__init__" not in file_path.name:
                    class_name = file_path.stem.capitalize()
                    f.write(f"class {class_name}:\n    pass\n")
        print(f'File created: {file_path}')
    else:
        print(f"Empty file path encountered: {file_path}")

def generate_init_files(root_folder):
    for dirpath, _, filenames in os.walk(root_folder):
        python_files = [f for f in filenames if f.endswith('.py') and f != '__init__.py']
        if python_files:
            init_file_path = Path(dirpath, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                for py_file in python_files:
                    class_name = Path(py_file).stem.capitalize()
                    init_file.write(f"from .{Path(py_file).stem} import {class_name}\n")
            print(f"__init__.py created in: {dirpath}")

def generate_setup_file(root_folder):
    setup_file_path = root_folder / "setup.py"
    setup_content = '''from setuptools import setup, find_packages
description = "A simple Create Structure tool."
setup(
    name="project",
    version="1.0.0",
    author="your_name",
    author_email="your_email",
    description="A simple Create Structure tool.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_github/project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'main=main:main',
        ],
    },
    include_package_data=True,
)
'''
    if not setup_file_path.exists():
        with open(setup_file_path, 'w') as setup_file:
            setup_file.write(setup_content)
        print(f"Setup file created: {setup_file_path}")

def generate_license_file(root_folder):
    license_file_path = root_folder / "LICENSE"
    license_content = '''
The MIT License (MIT)
Copyright © 2024 (your name)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
    if not license_file_path.exists():
        with open(license_file_path, 'w') as license_file:
            license_file.write(license_content)
        print(f"LICENSE file created: {license_file_path}")

def generate_readme_file(root_folder):
    readme_file_path = root_folder / "README.md"
    readme_content = '''
# Create Structure tool
### Author: Ibrahem abo kila
### Email: ibrahemabokila@gmail.com
'''
    if not readme_file_path.exists():
        with open(readme_file_path, 'w') as readme_file:
            readme_file.write(readme_content)
        print(f"README file created: {readme_file_path}")

def main():
    parser = argparse.ArgumentParser(description="Create directories and files based on the outline in a text file.")
    parser.add_argument('file', help="Path to the outline text file")
    args = parser.parse_args()

    if not args.file:
        print(parser.usage)
        exit(1)
    else:
        try:
            create(args.file)
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
