#!/usr/bin/python3
""" 4-append_write.py """


def append_write(filename="", text=""):
    """append inside of a file

    Keyword Arguments:
        filename {str} -- file's name(default: {""})
        text {str} -- text to write in the file (default: {""})

    Returns:
        [int] -- number of characters
    """

    with open(filename, mode='a', encoding="UTF8") as file:
        file.write(text)
        return len(text)
