#!/usr/bin/python3
""" 2-read_lines.py """


def read_lines(filename="", nb_lines=0):
    """read x lines of a file

    Keyword Arguments:
        filename {str} -- file's name (default: {""})
        nb_lines {int} -- how many lines to read (default: {0})
    """

    with open(filename, mode='r', encoding="UTF8") as file:
        if (nb_lines <= 0):
                print(file.read(), end="")
        else:
            i = 0
            while (i < nb_lines):
                print(file.readline(), end='')
                i += 1
