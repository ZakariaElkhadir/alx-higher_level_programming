#!/usr/bin/python3
"""Module that that prints a square with the character #."""


def print_square(size):
    """print_square function"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    print((('#' * size + "\n") * size), end='')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
