#!/usr/bin/python3
"""Rectangle Module."""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """laws of width rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """laws of height rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method"""
        return self.width * self.height

    def perimeter(self):
        """Public instance method"""
        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """create a rectangle with '#' """
        str = ""
        if self.width != 0 or self.height != 0:
            str += "\n".join("#" * self.width for i in range(self.height))

        return str
