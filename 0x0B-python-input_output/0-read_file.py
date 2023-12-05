#!/usr/bin/python3
"""read file method."""


def read_file(filename=""):
    """function that read file content"""
    with open(filename, encoding="utf-8") as file:
        print(file.read())
