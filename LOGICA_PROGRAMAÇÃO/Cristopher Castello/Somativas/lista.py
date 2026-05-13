# Exercicio 1

# print("Qual modelo do seu veículo?")
# car = str(input("Resposta 1:"))
# print("Qual a placa do seu veículo?")
# pla = str(input("Resposta 2:"))
# print("Então seu veículo é:", car)
# print("E sua placa é:", pla)
# print("OK!!! Pode passa seu veículo foi registrado no sistema")

# Exercicio 2

# L = float(input("Qual a capacidade do seu taque (em litros)?"))
# K = float(input("Qual o consumo médio do seu caminhão?"))
# total = (L / K)
# print("Então seu caminhão percorrera até:", round(total,2))

# Exercicio 3

# print("1 dolar equivale a R$5.20")
# dolar = int(input("Digite quantos dolares você converterá?"))
# total = dolar*5.20
# print("Você terá um total de:", round(total,2))

# Exercicio 4

# temp = int(input("Sua entrega chegará em torno de:"))
# mt = print("O motorista passará antes por 3 rotas diferentes")
# tt = temp/3
# print("Seu pedidio chegará daqui á:", round(tt,2))

# Exercicio 5

# peso = float(input("Qual é o peso em toneladas dos caminhões?"))
# pco = [1000, 2600]
# if peso in pco:
#     print(f"A carga está leve{peso}")
# elif 2600 > peso < 1000:
#     print(f"A carga está na medida{peso}")
# else:
#     print(f"ALERTA!!!! O PESO ESTÁ EM EXCESSO")

# Exercicio 6
# print("Codigos para carga N=Norte, S=Sul e I=Internacional")
# escolha = input("Digite uma opção:")

# if escolha == "N":
#      print("Você escolheu a região Norte")
# elif escolha == "S":
#      print("Você escolheu a região Sul")
# else:
#      print("Voce foi para região internacional")

# Exercicio 7

# print("Se não digite n\nSe sim digite s")
# Veiculo = input("O veiculo está pronto?")
# moto = input("O motorista está identificando?")
# print("Checklist:")
# if Veiculo == "N":
#     print("O veículo está pronto")
# elif Veiculo == "S":
#     print("O veiculo está pronto")

# if moto == "N":
#     print("Motorista está pronto")
# elif moto == "S":
#     print("Motorista indentificado e pronto")

# Exercicio 8

# agen = input("Qual é o total de entregas agendadas?")
# atr = input("Qual é o total de entragas realizadas com atraso?")
# if agen > "10%":
#     print("Necessario otimizar rotas")
# elif agen < "10%":
#     print("Logística Eficiente")

# Exercicio 9

# esc = int(input("Quala medida de uma carga de pressão:"))
# if 100 < esc < 110:
#     print(f"Está acima do padrão")

# else:
#     print("Está no padrão")

# Exercicio 10

# for num in range (1, 6):
#     print(f"O portão fechara em {num}")
# else: print("Portão fechado")

# Exercicio 11

#  print("Somatorio de Fretes (Acumulador)")
# faturamento_total = 0
# valor_frete = -1
# while valor_frete != 0:
#     valor_frete = float(input("Valor do Frete ou 0 para encerrar:"))
#     faturamento_total += valor_frete
#     print(f"Faturamento acumulado: R$ {faturamento_total}")
# print("Cálculo executado com sucesso")

# Exercicio 12
# for veiculos in range (1, 6):
#      input(f"Qual a quilometragem de {veiculos}?")
# print("A maior quilometragem", veiculos)

# 13.
# print("Sistema do Rastreio")
# codigo_correto = "track99"
# tentativas = 0
# max_tentativas = 1
# while tentativas < max_tentativas:
#     codigo_input = input("Código de acesso para o rastreador:")
#     if codigo_input == codigo_correto:
#         print("Acesso permitido. Iniciando rastreamento...")
#         break
#     else:
#         tentativas += 1
#         print("Acesso negado")
#         if tentativas < max_tentativas:
#             print(f"Tentativas restantes")
#             (max_tentativas-tentativas)
# else:
#     print("Rastreador Bloqueado")