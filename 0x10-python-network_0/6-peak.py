#!/usr/bin/python3
""" function find_peak """


def find_peak(list_of_integers):
    """[summary]

    Args:
        list_of_integers ([type]): [description]

    Returns:
        [type]: [description]
    """
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    maximo = list_of_integers[-1]
    return maximo
