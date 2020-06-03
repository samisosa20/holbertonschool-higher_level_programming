#!/usr/bin/python3
""" 5-to_json_string.py """
import json


def to_json_string(my_obj):
    """change object to string

    Arguments:
        my_obj {obj} -- object

    Returns:
        str -- return a str class
    """

    return json.dumps(my_obj)
