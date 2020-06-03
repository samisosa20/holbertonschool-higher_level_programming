#!/usr/bin/python3
""" 6-from_json_string.py """
import json
write_file = __import__('3-write_file').write_file


def save_to_json_file(my_obj, filename):
    """save to json file

    Arguments:
        my_obj {obs} -- obj class
        filename {str} -- file's name
    """

    write_file(filename, json.dumps(my_obj))
