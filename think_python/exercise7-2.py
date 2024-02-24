import math

# Eval take a string and avaluate using python interpretator
result = eval('1 + 2 * 3')
# print(result)

r = eval('math.sqrt(5)')
# print(r)

pi = eval('type(math.pi)')
# print(pi)


def eval_loop(data):
    while data != 'done':
        data = input('Please, informe an input: ')
        print(data)


eval_loop('data')
