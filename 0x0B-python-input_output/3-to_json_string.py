#!/usr/bin/pyhton3
"""define json string fun"""


import json
    
def to_json_string(my_obj):
    """returns json represintation of an object"""
    return json.dumps(my_obj)
