def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Exemplo de uso
print(gcd(4, 3))  # Saída: 6
