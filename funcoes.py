
import random

def rolar_dados(n):
    resultados = []
    for _ in range(n):
        resultados.append(random.randint(1, 6))
    return resultados
