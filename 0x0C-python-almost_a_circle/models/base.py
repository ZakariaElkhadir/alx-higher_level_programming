#!/usr/bin/python3
"""base class module"""
from json import loads, dumps


class Base:
    """class method"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        from os import path
        file = f"{cls.__name__}.json"
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as file:
            return [cls.create(**z) for z in cls.from_json_string(file.read())]
