#!/usr/bin/python3
string = ""
for str in range(122, 96, -1):
    if (str % 2 != 0):
        string += chr(str - 32)
    else:
        string += chr(str)
print(string, end='')
