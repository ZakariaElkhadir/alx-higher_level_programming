#!/usr/bin/python3
'''Rectangle class Module'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method for area of square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns string'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
