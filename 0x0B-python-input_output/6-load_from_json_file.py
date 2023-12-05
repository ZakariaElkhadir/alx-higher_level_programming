#!/usr/bin/python3
"""define load_from_json_file function"""


import json


def load_from_json_file(filename):
    """creates an object json from file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
