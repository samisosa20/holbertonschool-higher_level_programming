#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the Rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return the current perimeter of the Rectangle."""
        if (self.__height == 0 or self.__width == 0):
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        string = "{}".format('\n'.join(
            ['#' * self.__width for row in range(0, self.__height)]))
        return string