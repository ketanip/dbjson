from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'JsonDBB - JSON Database Something'
SHORT_DESCRIPTION = """
    This is a simple flat file database which stores its data in a JSON file.
    It is NOT INTENTED TO USE IN PRODUCTION.
    It can be used times when you are too lazy to write a schema and do other stuff for a ORM like SQLAlchemy.
    Data is structured in simple format of collections and records ( key-value pairs ).
    """


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbjson", # Replace with your own username
    version="0.0.2",
    author="Ketan Iralepatil",
    author_email="",
    description=SHORT_DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KetanIP/jsondbb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

