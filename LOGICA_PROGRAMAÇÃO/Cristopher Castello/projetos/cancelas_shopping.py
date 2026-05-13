# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

veiculos = []

while True:
    print("\n==== SHOPPING - CANCELA ====")
    print("1 - Entrada de veículo")
    print("2 - Saída de veículo")
    print("3 - Relatório")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # PASSO 1 - Entrada
    if opcao == "1":
        placa = input("Digite a placa do veículo: ")

        # Verifica se já entrou
        existe = False
        for v in veiculos:
            if v["placa"] == placa and v["saida"] is None:
                existe = True

        if existe:
            print("ERRO: veículo já está no estacionamento!")
        else:
            tag = input("Possui TAG? (s/n): ")

            print("Pressione o botão para emitir ticket...")
            print("Ticket emitido com sucesso!")
    
