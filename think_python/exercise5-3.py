def is_triangle(a, b, c):
    if a == b == c:
        print('Yes')
    else:
        print('no')


def call():
    number1 = int(input('Please, type number one: '))
    number2 = int(input('Please, type number two: '))
    number3 = int(input('Please, type number three: '))
    is_triangle(number1, number2, number3)


call()
