from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A simple Create Structure tool."

setup(
    name="create_structure",
    version="1.0.0",
    author="Ibrahem abo kila",
    author_email="ibrahemabokila@gmail.com",
    description="A simple Create Structure tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hemaabokila/create_structure",
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'creates=structure.main:main',  
        ],
    },
    include_package_data=True,
)
