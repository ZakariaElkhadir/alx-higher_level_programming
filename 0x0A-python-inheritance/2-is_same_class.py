#!/usr/bin/python3
"""function returns True """


def is_same_class(obj, a_class):
    """if the object is exactly an instance of the specified class"""
    if type(obj) == a_class:
        return True

    else:
        """ otherwise False."""
        return False


"""another way"""
"""
return type(obj) == a_class
"""
