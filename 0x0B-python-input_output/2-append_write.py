#!/usr/bin/python3
"""define append_write"""


def append_write(filename="", text=""):
    """append file with utf-8"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
