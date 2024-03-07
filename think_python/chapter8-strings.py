fruit = 'banana'
letter = fruit[1]

print(letter)

# len

comprimento = len(fruit)
print(comprimento)


# to get the last letter

last = fruit[comprimento - 1]
print(last)

# Loop while

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# Loop for
word = 'Pearl Jam'
for i in word:
    print(i)


# Make way for Ducklings

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for i in prefixes:
    print(i + suffix)

# Slicing strings


s = "Pearl-Jam"
r = s[3:]
print(r)

# Kind of rewriting a string

greeting = 'Hello World'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

# What does this function do?


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


resu = find('text', 'e')
print(resu)

# Loop and counting

word = 'apartamento'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Word Finding

palavra = 'pessego'
index = palavra.find('g')
print(index)

index_second = palavra.find('g', 1)
print(index_second)

# IN operator

response = 'a' in 'banana'
print(response)

next_response = 'seed' in 'banana'
print(next_response)


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


test = in_both('apples', 'oranges')
print(test)

# Comparison

if word == 'banana':
    print('All right, bananas')

if word < 'banana':
    print("Your word, " + word + ", comes before banana.")
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana')
else:
    print('All good, bananas')


# Depuração

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True


a = is_reverse('pots', 'spot')
print(a)
