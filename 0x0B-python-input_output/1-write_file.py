#!/usr/bin/python3
"""write file method"""


def write_file(filename="", text=""):
    """read file with utf-8"""
    with open(filename,'w', encoding="utf-8", ) as file:
        return file.write(text)
