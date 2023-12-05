#!/usr/bin/python3
"""defining from json string function"""

import json

def from_json_string(my_str):
    """return json string"""
    return json.loads(my_str)