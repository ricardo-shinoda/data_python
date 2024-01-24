
# Transforma float and int

numero = 3.999999
print(int(numero))

# Transforma número em float
outro = 32
print(float(outro))

# Converter o argumento em string

print(str(outro))


# ? Como acrescentar funções dentro de funções

# first function


def first_setense():
    print("This is the first sentense")

# second function


def second_sentense():
    print("This is the second sentense")

# function calling both


def both_sentense():
    first_setense()
    second_sentense()


# calling function
both_sentense()


# ? Functions with arguments

def print_arg(name):
    print(name)


print_arg("Argument given")


# ? Variaveis e parametros locais


def local_var(num1, num2):
    sum = num1 + num2
    print(sum)


local_var(2, 4)
