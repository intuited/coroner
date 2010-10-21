try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from textwrap import dedent, fill

def format_desc(desc):
    if len(desc) > 200:
        raise ValueError("Description cannot exceed 200 characters.")
    return fill(dedent(desc), 200)

def format_classifiers(classifiers):
    return dedent(classifiers).strip().split('\n')

def split_keywords(keywords):
    return dedent(keywords).strip().replace('\n', ' ').split(' ')

def file_contents(filename):
    with open(filename) as f:
        return f.read()

setup(
    name = "coroner",
    version = "0.2.1",
    author = "Ted Tibbetts",
    author_email = "intuited@gmail.com",
    url = "http://github.com/intuited/coroner",
    description = format_desc("""
        Wraps python invocations in code to do post-mortem debugging
        and sundry usefulnesses.
        """),
    long_description = file_contents('README.txt'),
    classifiers = format_classifiers("""
        Development Status :: 2 - Pre-Alpha
        Intended Audience :: Developers
        License :: OSI Approved :: BSD License
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 2
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Utilities
        Topic :: Software Development :: Debuggers
        """),
    keywords = split_keywords("""
        xml grainery odt openoffice
        """),
    py_modules = ['coroner']
    )
