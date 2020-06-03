#!/usr/bin/python3
import json
""" 6-from_json_string.py """


def from_json_string(my_str):
    """change object to string

    Arguments:
        my_str {obj} -- object

    Returns:
        obj -- return a obj class
    """

    return json.loads(my_str)
