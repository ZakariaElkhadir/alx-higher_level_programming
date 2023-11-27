#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """ rectangle representation"""
    def __init__(self, width=0, height=0):
        """initializes width and height"""
        self.height = height
        self.width = width
    @property
    def width(self):
        """Private instance attribute: width"""
        return self.__width
    @width.setter
    def width(self, value):
        """Laws of rectangle width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Private instance attribute: height"""
        return self.__height
    @height.setter
    def height(self, value):
        """Laws of rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0 :
            raise ValueError("height must be >= 0")
        self.__height = value
