#!/usr/bin/python3
""" 7-from_json_string.py """
import json


def save_to_json_file(my_obj, filename):
    """save to json file

    Arguments:
        my_obj {obs} -- obj class
        filename {str} -- file's name
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
