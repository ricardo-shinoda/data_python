# Dealiing with strings | Slicing

name = 'joao'
midle_name = 'garcia'
last_name = 'pereira'

print(name[0])
print(name[1])
print(name[2])
print(name[3])


# Slicing - taking a amount of letter al together
print(name[0:3])

# using slicing and concatenation to take the initial letters

print('Initial my initials are: ', name[0] + midle_name[0] + last_name[0])

company = 'technology'
name = 'lucas'
family_name = 'shinoda'

print('My email address is: ', name + '.' +
      family_name + '@' + company + '.com')
