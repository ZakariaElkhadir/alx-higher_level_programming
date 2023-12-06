#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
