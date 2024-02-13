def is_power(a, b):
    if a == b:  # Caso base: Se 'a' é igual a 'b', então 'a' é uma potência de 'b'
        return True
    elif a % b == 0:  # Se 'a' é divisível por 'b'
        return is_power(a / b, b)  # Verifique se a/b é uma potência de 'b'
    else:
        return False


result = is_power(3, 2)
print(result)  # Saída: True
