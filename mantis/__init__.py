"""
Mantis - A Minimalist Database Toolkit for Python

@author: Clivern U{hello@clivern.com}
"""


__VERSION__ = "1.0.0"

def read_file(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content