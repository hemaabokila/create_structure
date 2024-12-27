import os
import argparse
def create(file_path):
    root_folder = os.getcwd()
    with open(file_path, 'r') as file:
        lines = file.readlines()
    line2 = ""
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
    generate_setup_file(root_folder)
    generate_License_file(root_folder)
    generate_readme_file(root_folder)

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

def generate_setup_file(root_folder):
    setup_file_name = "setup.py"
    setup_file_path = os.path.join(root_folder, setup_file_name)
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
    if not os.path.exists(setup_file_path):
        with open(setup_file_path, 'w') as setup_file:
            setup_file.write(setup_content)
        print(f"setup File created: {setup_file_path}")
    else:
        print(f"setup.py already exists: {setup_file_path}")

def generate_License_file(root_folder):
    License_file_name = "LICENSE"
    License_file_path = os.path.join(root_folder, License_file_name)
    License_content = '''
The MIT License (MIT)
Copyright © 2024 (your name)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
    
    if not os.path.exists(License_file_path):
        with open(License_file_path, 'w') as License_file:
            License_file.write(License_content)
        print(f"LICENSE File created: {License_file_path}")
    else:
        print(f"LICENSE already exists: {License_file_path}")
def generate_readme_file(root_folder):
    readme_file_name = "README.md"
    readme_file_path = os.path.join(root_folder, readme_file_name)
    readme_content = '''
# Create Structure tool
### author Ibrahem abo kila
### author email ibrahemabokila@gmail.com 
'''
    if not os.path.exists(readme_file_path):
        with open(readme_file_path, 'w') as readme_file:
            readme_file.write(readme_content)
        print(f"README File created: {readme_file_path}")
    else:
        print(f"README already exists: {readme_file_path}")



def main():
    parser = argparse.ArgumentParser(description="Create directories and files based on the outline in a text file.")
    parser.add_argument('file', help="Path to the outline text file")
    parser.parse_args()
    args = parser.parse_args()
    if not args.file:
        print(parser.usage)
        exit(1)
    else:
        create(args.file)

if __name__ == "__main__":
    main()

