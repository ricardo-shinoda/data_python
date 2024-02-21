# import math

# # a = 4
# x = 4


# def my_sqrt(a):
#     x = 4
#     while True:
#         print(x)
#         y = (x + a / x) / 2
#         if y == x:
#             break
#         x = y


# def math_square(a):
#     return math.sqrt(a)


#     # print('This is the result of math: ', result)
# a = 4
# sqr_from_math = math_square(a)
# print('The square from math: ', sqr_from_math)


# one = sqr_from_math
# two = my_sqrt
# final = (one - two)
# print('Diff: ', final)

# # math(4)
# my_sqrt(4)


import math


def mysqrt(a):
    """
    Função para estimar a raiz quadrada de um número a.

    Argumentos:
    a (float ou int): O número do qual estimar a raiz quadrada.

    Retorna:
    float: Estimativa da raiz quadrada de a.
    """
    x = a / 2    # Escolha inicial de x
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < 0.0000001:  # Critério de parada
            return y
        x = y


def test_square_root():
    """
    Função para testar a função mysqrt e compará-la com math.sqrt.
    Exibe uma tabela com os resultados.
    """
    print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
    print("-\t---------\t------------\t----")
    for a in range(1, 10):
        my_sqrt = mysqrt(a)
        math_sqrt = math.sqrt(a)
        diff = abs(my_sqrt - math_sqrt)
        print(f"{a}\t{my_sqrt}\t{math_sqrt}\t{diff}")


# Teste da função
test_square_root()
