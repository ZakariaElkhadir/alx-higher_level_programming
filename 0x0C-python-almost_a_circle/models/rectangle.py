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
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area method"""
        return self.height * self.width

    def display(self):
        """ prints rectangle as a # """
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')


    def __str__(self):


        """__str__ function that returns a string"""
        return "[Rectangle] ({id}) {x}/{y} - {width}/{height}".format(
         id=self.id, x=self.x, y=self.y, width=self.width, height=self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id != None:
            self.id = id
        if width != None:
            self.width = width
        if height != None:
            self.height = height
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, *args, **kwargs):
        """args and kwargs fun"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
    