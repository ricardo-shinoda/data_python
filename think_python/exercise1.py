# Errors analysis

# Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?

# print hello world

# Response: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?


############################

# Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?

# print('hello world)

# response: SyntaxError: unterminated string literal (detected at line 14)

# 3

# Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?

print(2++2)

# response: 4

###########################

#Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?

# print(02)

# response: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

#############################

# O que acontece se você tiver dois valores sem nenhum operador entre eles?

print(2 4)

# response: SyntaxError: invalid syntax. Perhaps you forgot a comma?

