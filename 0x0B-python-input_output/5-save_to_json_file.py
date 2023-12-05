#!/usr/bin/python3
"""defin save to json function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
