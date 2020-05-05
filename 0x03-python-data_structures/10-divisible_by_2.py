#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in range(0, len(my_list)):
        if (my_list[i] % 2 == 0):
            result.append(1)
        else:
            result.append(0)
    return result