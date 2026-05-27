# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

while True:
    try:
        print("Bem-vindo ao elevador")
        andar_atual = 0

        chamar = input("Você deseja chamar o elevador?: ")

        if chamar == "N" or chamar == "n":
            print("Você desejou não chamar o elevador")

        elif chamar == "S" or chamar == "s":
            print("O elevador está se locomovendo ao seu andar")

            destino = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            pergunta_andar = input("Qual andar deseja se mover?: ")
            quantidade = int(input("Quantas pessoas estão entrando?: "))

            if quantidade > 5:
                print("O peso está acima da capacidade\nO elevador deve fazer uma parada")

            elif quantidade <= 5:
                print("A capacidade está ok")

                if int(pergunta_andar) in destino:

                    print(f"O elevador está subindo do {andar_atual}º andar até o {pergunta_andar}º andar")
                    print("Tela de Andar atual:")

                    for andar in range(0, int(pergunta_andar) + 1):
                        print(f"Andar {andar}º")

                    print("Você chegou ao seu destino")

                else:
                    print("Andar inválido")

    except:
        print("Ocorreu um erro")
