from funcoes import *

def jogo():
    cartela = {
        'regra_simples': {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},
        'regra_avancada': {
            'sem_combinacao':-1,
            'quadra':-1,
            'full_house':-1,
            'sequencia_baixa':-1,
            'sequencia_alta':-1,
            'cinco_iguais':-1
        }
    }

    imprime_cartela(cartela)

    for _ in range(12):

        dados_guardados = []
        dados_rolados = rolar(dados_guardados)
        rerrolagens = 0
        exibir = True

        while True:
            if exibir:
                print("Dados rolados:", dados_rolados)
                print("Dados guardados:", dados_guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

            exibir = True
            opcao = input()

            if opcao == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                i = int(input())
                if 0 <= i < len(dados_rolados):
                    dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, i)

            elif opcao == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                i = int(input())
                if 0 <= i < len(dados_guardados):
                    dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, i)

            elif opcao == "3":
                if rerrolagens >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    dados_rolados = rolar(dados_guardados)
                    rerrolagens += 1

            elif opcao == "4":
                imprime_cartela(cartela)

            elif opcao == "0":
                print("Digite a combinação desejada:")
                while True:
                    cat = input()

                    if cat in ["1","2","3","4","5","6"]:
                        if cartela['regra_simples'][int(cat)] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            break
                    elif cat in cartela['regra_avancada']:
                        if cartela['regra_avancada'][cat] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            break
                    else:
                        print("Combinação inválida. Tente novamente.")

                cartela = faz_jogada(dados_rolados + dados_guardados, cat, cartela)
                break

            else:
                print("Opção inválida. Tente novamente.")
                exibir = False

    imprime_cartela(cartela)

    total = sum(v for v in cartela['regra_simples'].values() if v != -1) + \
            sum(v for v in cartela['regra_avancada'].values() if v != -1)

    if sum(v for v in cartela['regra_simples'].values() if v != -1) >= 63:
        total += 35

    print("Pontuação total:", total)

jogo()