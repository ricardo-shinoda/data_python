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


# Incremental development


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquare = dx**2 + dy**2
    result = math.sqrt(dsquare)
    return result


distance_result = distance(1, 2, 4, 6)
print(distance_result)

# ? Bulding Hypotenusa in an incremental development


def hypotenuse(c1, c2):
    """ A soma do quadrado dos catetos é igual ao quadrado da hipotenusa"""
    cat_sum = c1**2 + c2**2
    return cat_sum


hypotenuse_result = hypotenuse(3, 2)
print('Hypotenuse must be: ', hypotenuse_result)


# Boolean functions


def is_divisible(x, y):
    return x % y == 0


divi_result = is_divisible(4, 2)
print('is x divisible by y ? ', divi_result)

# exercise


def is_between(x, y, z):
    return x <= y <= z


is_between_result = is_between(2, 5, 4)
print('Is between resul: ', is_between_result)

# Factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


fac_result = factorial(3)
print(fac_result)

# Fibonacci recursive math function


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibo = fibonacci(6)
print(fibo)

# Adding another layer of refactor on the Factorial code


def factorial2(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


fac_result2 = factorial2(-4)
print(fac_result2)
