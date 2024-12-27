# Create Structure Tool

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

## About the Project

`Create Structure` is a Python tool designed to help developers quickly generate file and folder structures based on an outline provided in a text file. It simplifies the process of organizing projects, creating Python classes, and generating `__init__.py` files automatically.

With this tool, you can easily:
- Generate a project structure with folders and files.
- Automatically create Python class files with a basic class template.
- Generate `__init__.py` files that import classes for easier module management.
- Creating a `setup.py` file.
- Creating a `README.md` file.
- Creating a `LICENSE` file.

---

## Features

- **Flexible Input:** Provide a text file that outlines the structure of your project.
- **Automatic Class Creation:** Automatically creates Python class templates in `.py` files.
- **Init File Generation:** Automatically generates `__init__.py` files for importing modules.
- **Setup File Generation:** Automatically generates `setup.py` file, The file is generated with ready-to-use content for installation.
- **Cross-Platform:** Works on Windows, Linux, and macOS.

---

## Installation

You can install the tool directly from source or by using `pip`.

### From Source:
```bash
git clone https://github.com/hemaabokila/create_structure.git
cd create_structure
python install .
```
### From PyPI (Coming Soon):
```python
pip install create_struc
```
## Usage
After installing the tool, you can run it directly from the command line.

Syntax:
```bash
ceartes <path_to_outline_file>
```
1- Example:
Create a text file, e.g., structure.txt:
```bash
src/
    main.py
    utils.py
tests/
    test_main.py
    test_utils.py
```
2-  Run the command:
```bash
ceartes structure.txt
```
3- The tool will generate the following structure:
```bash
├── src/
│   ├── main.py
│   ├── utils.py
│   └── __init__.py
├── tests/
│   ├── test_main.py
│   ├── test_utils.py
│   └── __init__.py
├── README.md
├── setup.py
└── LICENSE
```
## Arguments
file (Required): Path to the outline text file that specifies the project structure.
### Example Command:
```bash
ceartes my_structure.txt
```
## How It Works
1- Reads the outline from a text file.

2- Creates directories and files based on the provided structure.

3- For Python files:
- Adds a basic class template.
- Generates __init__.py files for importing classes in submodules.
## File Structure
If you clone or download the repository, here’s what the directory structure looks like:
```bash
create_structure/
├── structure/                # Core functionality of the tool
│   ├── main.py               # Main entry point of the tool
│   └── __init__.py
├── setup.py                  # Setup script for packaging
├── LICENSE                   # MIT License file
├── README.md                 # Documentation file
└── tests/                    # Unit tests for the tool
```
## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more details.

## Author
Developed by Ibrahem abo kila.

