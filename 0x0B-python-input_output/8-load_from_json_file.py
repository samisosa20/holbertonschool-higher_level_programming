#!/usr/bin/python3
""" 6-from_json_string.py """
import json


def load_from_json_file(filename):
    """[summary]

    Arguments:
        filename {str} -- file's name

    Returns:
        [obj] -- obj or json data
    """

    with open(filename, encoding="UTF8", mode='r') as file:
        return json.loads(file.read())
