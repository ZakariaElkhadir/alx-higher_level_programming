#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """ if the object is an instance of a class return true"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
