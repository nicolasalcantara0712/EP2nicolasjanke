
import random

def rolar_dados(n):
    resultados = []
    for _ in range(n):
        resultados.append(random.randint(1, 6))
    return resultados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    
    nova_lista = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            nova_lista.append(dados_rolados[i])
    
    return [nova_lista, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado)
    
    nova_lista = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            nova_lista.append(dados_no_estoque[i])
    
    return [dados_rolados, nova_lista]

def calcula_pontos_regra_simples(dados):
    resultado = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    for d in dados:
        if d == 1:
            resultado[1] += 1
        if d == 2:
            resultado[2] += 2
        if d == 3:
            resultado[3] += 3
        if d == 4:
            resultado[4] += 4
        if d == 5:
            resultado[5] += 5
        if d == 6:
            resultado[6] += 6
    
    return resultado

def calcula_pontos_soma(dados):
    soma = 0
    for d in dados:
        soma += d
    return soma