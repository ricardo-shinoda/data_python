import random
import string

password_length = int(input('Type a desired password length: '))
option = string.ascii_letters + string.digits + string.punctuation
password = ''

for i in range(password_length):
    password += random.choice(option)

print(password)

