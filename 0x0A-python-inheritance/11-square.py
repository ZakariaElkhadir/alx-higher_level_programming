#!/usr/bin/python3
"""Rectangle class method/"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        """area for square"""
        return self.__size ** 2

    def __str__(self):
        """returns string """

        return "[Square] " + str(self.__size) + "/" + str(self.__size)
