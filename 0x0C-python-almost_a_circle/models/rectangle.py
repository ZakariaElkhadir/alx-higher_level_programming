#!/usr/bin/python3
"""Class Rectangle inherits from Base """
from models.base import Base


class Rectangle(Base):
    """Class constructot"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Rectangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Rectangle y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value, eq=True):
        "Value validation method"

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")
        
    def area(self):
        """area method"""
        return self.height * self.width

    def display(self):
        """ prints rectangle as a # """
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    