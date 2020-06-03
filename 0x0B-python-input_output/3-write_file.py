#!/usr/bin/python3
""" 3-write_file.py """


def write_file(filename="", text=""):
    """write inside of a file or overwrite

    Keyword Arguments:
        filename {str} -- file's name(default: {""})
        text {str} -- text to write in the file (default: {""})

    Returns:
        [int] -- number of characters
    """
    with open(filename, mode='w', encoding="UTF8") as file:
        file.write(text)
        return len(text)
