#!/usr/bin/python3
"""module: 100-my_int"""


class MyInt(int):
    """class: MyInt"""
    def __init__(self, value):
        """init"""
        self.__value = value

    def __eq__(self, other):
        """overriding eq"""
        if type(self.__value) is int:
            return False

    def __ne__(self, other):
        """overriding ne"""
        if type(self.__value) is int:
            return True
