#!/usr/bin/python3
""" 1-number_of_line.py """


def number_of_lines(filename=""):
    """read number of line has a file

    Keyword Arguments:
        filename {str} -- name of a file (default: {""})
    Returns:
        int -- how many line has the file
    """

    i = 0
    with open(filename, encoding="UTF8", mode='r') as file:
        return len(file.readlines())
