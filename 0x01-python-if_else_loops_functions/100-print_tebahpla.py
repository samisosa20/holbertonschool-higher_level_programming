#!/usr/bin/python3
for str in range(122, 96, -1):
    if (str % 2 != 0):
        print(chr(str - 32), end='')
    else:
        print(chr(str), end='')
