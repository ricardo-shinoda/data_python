import math


def estimate_pi():
    """
    Estima o valor de π usando a série de Ramanujan.
    Retorna a estimativa de π.
    """
    k = 0
    sum_term = 0
    while True:
        term = (math.factorial(4*k) * (1103 + 26390*k)) / \
            ((math.factorial(k) ** 4) * (396 ** (4*k)))
        sum_term += term
        if term < 1e-15:
            break
        k += 1
    return 1 / ((2 * math.sqrt(2) / 9801) * sum_term)


# Teste da função
pi_estimate = estimate_pi()
print("Estimativa de pi:", pi_estimate)
print("Valor de math.pi:", math.pi)
