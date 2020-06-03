#!/usr/bin/python3
""" 0-read_file.py """


def read_file(filename=""):
    """read a file

    Keyword Arguments:
        filename {str} -- name of a file (default: {""})
    """

    with open(filename, encoding="UTF8", mode='r') as file:
        for line in file:
            print(line, end='')
