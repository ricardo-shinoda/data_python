
# Transforma float and int

numero = 3.999999
print(int(numero))

# Transforma número em float
outro = 32
print(float(outro))

# Converter o argumento em string

print(str(outro))

# Como acrescentar funções dentro de funções


def first_setense():
    print("This is the first sentense")


def second_sentense():
    print("This is the second sentense")


def both_sentense():
    first_setense()
    second_sentense()


both_sentense()
