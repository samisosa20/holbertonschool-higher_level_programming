#!/usr/bin/python3
"""module: 8-base_geometry"""


class BaseGeometry():
    """class BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method: area"""
        return self.__width * self.__height

    def __str__(self):
        """method: str"""
        s = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return s
