#!/usr/bin/python3
""" rectangle.py """
from models.base import Base


class Rectangle(Base):
    """Class rectangle

    Args:
        Base (class): imherits class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
            Calculates area
        """
        return self.width * self.height

    def display(self):
        """
            displays
        """
        print('\n' * self.y, end="")
        for i in range(0, self.height):
            print(' ' * self.x, end="")
            for j in range(0, self.width):
                print('#', end="")
            print()

    def to_dictionary(self):
        """
            to dict
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        attr = ["id", "width", "height", "x", "y"]
        if args:
            for index, value in enumerate(args):
                setattr(self, attr[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary representation of a Rectangle """
        self_dict = dict(self.__dict__)
        for key in self_dict:
            new_key = key.replace("_Rectangle__", "")
            self_dict[new_key] = self_dict.pop(key)
        return self_dict
