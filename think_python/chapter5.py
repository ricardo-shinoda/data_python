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
number5 = 100 % 1000

dividable = number1 % number2
# print(dividable)
print('This is number3:', number3)
print('This is number4:', number4)
print('This is number5:', number5)
