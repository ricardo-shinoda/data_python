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

word = 'bananaaaaaaaaaaaaaaaaaa'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Word Finding

palavra = 'pessego'
index = palavra.find('g')
print(index)
