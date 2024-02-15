def countdown(n):
    """“Enquanto n for maior que 0, mostre o valor de n e então decremente n. Quando chegar a 0, mostre a palavra Blastoff!”"""
    while n > 0:
        print(n)
        n = n - 1
    print('Done!')


countdown(10)


def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1


sequence(10)
