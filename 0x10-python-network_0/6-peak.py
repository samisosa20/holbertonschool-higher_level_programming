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
    maximo = list_of_integers[0]
    for i in list_of_integers:
        if i > maximo:
            maximo = i
    return maximo