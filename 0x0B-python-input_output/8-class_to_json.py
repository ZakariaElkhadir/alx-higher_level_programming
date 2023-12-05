#!/usr/bin/python3
"""class to json function"""


def class_to_json(obj):
    """returns the dictionnary description"""
    return obj.__dict__
