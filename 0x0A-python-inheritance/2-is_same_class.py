#!/usr/bin/python3
"""Module with is_same_class function"""


def is_same_class(obj, a_class):
    """function to look if is same class"""
    if (type(obj) is a_class):
        return True
    else:
        return False
