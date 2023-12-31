#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 4-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[i])]
        for i in range(0, self.__size):
            [print("", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for l in range(0, self.__size)]
            print("")

    @property
    def position(self):
        """position fun """
        return self.__position

    @position.setter
    def position(self, value):
        """pisition fun"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(num >= 0)for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
