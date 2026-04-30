
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

def calcula_pontos_sequencia_alta(dados):
    unicos = sorted(set(dados))
    for i in range(len(unicos) - 4):
        if unicos[i+4] - unicos[i] == 4:
            return 30
    return 0

def calcula_pontos_full_house(dados):
    contagem = {}
    for d in dados:
        contagem[d] = contagem.get(d, 0) + 1
    
    valores = sorted(contagem.values())
    
    if valores == [2, 3]:
        total = 0
        for d in dados:
            total += d
        return total
    
    return 0

def calcula_pontos_quadra(dados):
    contagem = {}
    for d in dados:
        contagem[d] = contagem.get(d, 0) + 1
    for v in contagem.values():
        if v >= 4:
            total = 0
            for d in dados:
                total += d
            return total
    return 0

def calcula_pontos_quina(dados):
    contagem = {}
    for d in dados:
        contagem[d] = contagem.get(d, 0) + 1
    for v in contagem.values():
        if v >= 5:
            return 50
    return 0

def calcula_pontos_sequencia_baixa(dados):
    unicos = sorted(set(dados))
    for i in range(len(unicos) - 3):
        if unicos[i+3] - unicos[i] == 3:
            return 15
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def faz_jogada(dados, categoria, cartela_de_pontos):
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancada = calcula_pontos_regra_avancada(dados)
    
    if categoria in cartela_de_pontos['regra_avancada']:
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancada[categoria]
    else:
        categoria_int = int(categoria)
        cartela_de_pontos['regra_simples'][categoria_int] = pontos_simples[categoria_int]
    
    return cartela_de_pontos