#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number = number * -1
if (number % 10 < 6 and number % 10 > 0):
    str = "and is less than 6 and not 0"
elif (number % 10 > 5):
    str = "and is greater than 5"
else:
    str = "and is 0"
print("Last digit of {} is {} {}".format(number, number % 10, str))
