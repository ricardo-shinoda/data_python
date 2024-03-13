fruit = 'banana'

first = fruit[0:5:2]
print(first)

reverse = fruit[::-1]
print(reverse)


def is_palindrome(a, b):
    rev = b[::-1]
    if a == rev:
        print('Is Palindrome')
    else:
        print('This is not a palindrome')


is_palindrome('carro', 'orrac')
