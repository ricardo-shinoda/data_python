# Divisão por piso

time = 105
hour = int(time // 60)
minutes = int(time - hour * 60)

print(hour, ":", minutes)

# Como tirar o resto || how to get the remaining

remaining = time - hour * 60
print(remaining)


# Another way
remaining2 = time % 60
print(remaining2)

# The module % is also usefull to see if a number is dividable by another if it returns 0 the answer is yes.

number1 = 4
number2 = 2

number3 = 10 % 10
number4 = 100 % 100
number5 = 3 % 4

dividable = number1 % number2
# print(dividable)
print('This is number3:', number3)
print('This is number4:', number4)
print('This is number5:', number5)

x = 6
y = 5
print(not (x > y))

if x > y:
    print("X is bigger than y")

# Instruction PASS do nothing on the code

if x < y:
    pass

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

if x > y:
    print('X is greater then y')
elif x < y:
    print('X is less then y')
else:
    print('X is equal to y')

# 3 ways to do the same

if 0 < x:
    if x < 10:
        print('X is positive single-digit number')

if 0 < x and x < 10:
    print('X is positive single-digit number with AND')

if 0 < x < 10:
    print('X is a positove single-digit number - concise')


# Recursiveness - Function that call itself


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


countdown(3)


def print_n(s, n):
    def do_n(f, n):
        for _ in range(n):
            f()

    def print_s():
        print(s)

    do_n(print_s, n)


print_n('Hello', 4)

# Input

name = input('What is your name?\n')
print('The name is: ', name)

horas = (10 // 3)
horas2 = (10 / 3)
horas3 = (10 % 3)
print(horas)
print(horas2)
print(horas3)
