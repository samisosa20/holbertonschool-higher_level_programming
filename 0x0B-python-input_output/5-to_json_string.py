#!/usr/bin/python3
import json
""" 5-to_json_string.py """


def to_json_string(my_obj):
    """change object to string

    Arguments:
        my_obj {obj} -- object

    Returns:
        str -- return a str class
    """

    return json.dumps(my_obj)
