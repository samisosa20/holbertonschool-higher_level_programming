#!/usr/bin/python3
"""Write full name."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Arguments:
        first_name {str} -- first Name to print

    Keyword Arguments:
        last_name {str} -- last Name to print (default: {""})

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
