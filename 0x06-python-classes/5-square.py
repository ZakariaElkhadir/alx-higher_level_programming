#!/usr/bin/python3
class Square:
    """Private instance attribute"""
    def __init__(self, size=0) -> None:
        self.__size = size
        """if else statment"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        """area function with parameter(self)"""
    def area(self):
        """return area value"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    """size function"""
    @size.setter
    def size(self, value):
        """if else statment"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """my_print fun"""
    def my_print(self):
        """ printing a square pattern of '#' characters"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='\n' if j is self.size - 1 and i != j else "")
        print()
