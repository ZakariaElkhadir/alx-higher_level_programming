#!/usr/bin/python3
"""Class Rectangle inherits from Base """
from models.base import Base


class Rectangle(Base):
    """Class constructot"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
