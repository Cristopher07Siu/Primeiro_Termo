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

# veiculos = []

# while True:
#     print("\n==== SHOPPING - CANCELA ====")
#     print("1 - Entrada de veículo")
#     print("2 - Saída de veículo")
#     print("3 - Relatório")
#     print("4 - Sair")

#     opcao = input("Escolha uma opção: ")

#     # PASSO 1 - Entrada
#     if opcao == "1":
#         placa = input("Digite a placa do veículo: ")

#         # Verifica se já entrou
#         existe = False
#         for v in veiculos:
#             if v["placa"] == placa and v["saida"] is None:
#                 existe = True

#         if existe:
#             print("ERRO: veículo já está no estacionamento!")
#         else:
#             tag = input("Possui TAG? (s/n): ")

#             print("Pressione o botão para emitir ticket...")
#             print("Ticket emitido com sucesso!")
    
# while True:
#     print("==== Shopping - Cancela ====")
#     print("entrada = e\nsaida = s")
#     escolha0 = input("Digite sua opção: ").lower() # Transforma a resposta em minúscula
    
#     # Se escolher Entrada ou Saída
#     if escolha0 == "e" or escolha0 == "s":
#         if escolha0 == "e":
#             print("Liberação de entrada") # Ajustado para entrada
#         else:
#             print("Liberação de saída")
            
#         print("Nós cobramos R$ 9.00 por hora do veículo estacionado")
#         print("Menu de opções\nTicket = T\nCartão = C")
#         escolha = input("Qual opção você deseja?: ").lower()
#         print("___________________________________________________")

#         # Verifica a variável 'escolha' (e não escolha0)
#         if escolha == "t":
#             print("Você escolheu a opção de Ticket")
#             placa = input("Digite a placa do seu veículo: ")
#             modelo = input("Digite o modelo do seu veículo: ")
#             tempo1 = int(input("Você ficou por quantas horas? "))
#             total1 = 9 * tempo1
#             print(f"Então sua placa é {placa} e o seu veículo é um {modelo}, o valor total foi de R$ {total1:.2f}")
#             print("______________________________________________________________________________________")
#             print("Pix = P\nCartão = C\nDinheiro = D")
#             print("______________________________________________________________________________________")
#             pagamento1 = input("Qual será a forma de pagamento?: ").lower()
            
#             if pagamento1 == "p":
#                 print("QR CODE")
#                 print("Pagamento concluído")
#                 print(f"Notinha:\nO total foi de R$ {total1:.2f}")
#             elif pagamento1 == "c":
#                 Debito_credito = input("Débito = D\nou\nCrédito = C?: ").lower()
#                 if Debito_credito == "d":
#                     print("Você escolheu débito")
#                 elif Debito_credito == "c":
#                     print("Você escolheu crédito")
#                 print("Aproxime ou insira para realizar o pagamento")
#                 print("Obrigado, volte sempre!!")
#             elif pagamento1 == "d":
#                 print("Obrigado, volte sempre!!")
#             print("________________________________________________________________________________________")

#         elif escolha == "c":
#             print("Você escolheu a opção de cartão de acesso")
#             placa2 = input("Digite a placa do seu veículo: ")
#             modelo2 = input("Digite o modelo do seu veículo: ")
#             tempo2 = int(input("Você ficou por quantas horas? "))
#             total2 = 9 * tempo2
#             print(f"Então sua placa é {placa2} e o seu veículo é um {modelo2}, o valor total foi de R$ {total2:.2f}")
#             print("________________________________________________________________________________________")
#             print("Pix = P\nCartão = C\nDinheiro = D")
#             print("________________________________________________________________________________________")
#             pagamento2 = input("Qual será a forma de pagamento?: ").lower()
            
#             if pagamento2 == "p":
#                 print("QR CODE")
#                 print("Pagamento concluído")
#                 print(f"Notinha:\nO total foi de R$ {total2:.2f}")
#             elif pagamento2 == "c":
#                 Debito_credito = input("Débito = D\nou\nCrédito = C?: ").lower()
#                 if Debito_credito == "d":
#                     print("Você escolheu débito")
#                 elif Debito_credito == "c":
#                     print("Você escolheu crédito")
#                 print("Aproxime ou insira para realizar o pagamento")
#                 print("Obrigado, volte sempre!!")
#             elif pagamento2 == "d":
#                 print("Obrigado, volte sempre!!")
#             print("________________________________________________________________________________________")
        
#         else:
#             print("Opção de menu inválida.")
            
#     else:  
#         print("Isso não é uma opção válida\nRedirecionando ao menu")
#         print("____________________________________________")