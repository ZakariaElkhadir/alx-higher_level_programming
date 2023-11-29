#!/usr/bin/python3
"""Rectangle Module."""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    """int: the number of active instances"""
    print_symbol = '#'
    """print sumbol"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        """Return string representation """
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print a message for every deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """8-rectange"""
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger of two rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
