# it gives an area form a circle with a given ratio

import math


def area(radius):
    a = math.pi * radius**2
    return a


result = area(4)
print(result)


def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1


output = compare(3, 4)
print(output)
