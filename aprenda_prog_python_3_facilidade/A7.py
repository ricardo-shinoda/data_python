# Lust and tuple
# List can change, while tuple can´t

# Tupla
month = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(type(month))

# list
students = ['ricardo', 'lucas', 'luísa', 'ana_paula']

print(type(students))

# To change a item on a list
students[2] = "luisa"

print(students)

# To add an item to the end of the list

students.append('mariana')

print(students)

# To add an item choosing the index/where we want to add then

students.insert(4, 'ana')
print(students)


# To order in alphabetical

students.sort()
print(students)

# To remove an item from the list
# just choose the index
students.pop(1)
print(students)


# remove by name
students.remove('mariana')
print(students)

# Concatenate

teachers = ['pedro', 'paulo', 'gabriel']
total = students + teachers
print(total)


# Exercise


month = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

date_of_birth = input(
    'What is your date of birht? Please type it in DD-MM-AAAA format ')

date = date_of_birth[3:5]
index = int(date)
# print(type(date))
# print(date)
birth_month = month[index-1]

print('You month of birth is: ', birth_month)
