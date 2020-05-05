#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    nro_max = my_list[0]
    for n in my_list:
        if n > nro_max:
            nro_max = n
    return nro_max
