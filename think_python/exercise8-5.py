def rotate_word(word, shift):
    rotated_word = ""
    for char in word:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            rotated_char = chr((ord(char) - base + shift) % 26 + base)
            rotated_word += rotated_char
        else:
            rotated_word += char
    return rotated_word


# Exemplo de uso:
print(rotate_word("cheer", 7))   # Saída: jolly
print(rotate_word("melon", -10))  # Saída: cubed
print(rotate_word("IBM", -1))     # Saída: HAL
