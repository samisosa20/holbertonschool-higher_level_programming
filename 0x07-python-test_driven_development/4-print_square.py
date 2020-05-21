#!/usr/bin/python3
"""prints a square with the character #."""


def print_square(size):
    """function that prints a square

    Arguments:
        size {int} -- The height/width of the square.

    Raises:
        TypeError: if size is not int
        ValueError: if size < 0
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
