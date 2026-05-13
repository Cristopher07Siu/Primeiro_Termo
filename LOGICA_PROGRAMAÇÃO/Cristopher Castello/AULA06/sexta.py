#  1.
# print("Registro de Veículo")
# modelo = input("Digite o modelo de veículos:")
# placa = input("Digite a placa do veículo:")
# print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa Viagem!!!")

# 2.
# print("Cálculo de Autonomia")
# tanque = float(input("Qual a capacidade do seu tanque em Litros:"))
# consumo = float(input("Digite o consumo do seu caminhão:"))
# total = tanque / consumo
# print(f"Seu caminhão pode percorrer: {total:.2f}")
# print(f"Seu caminhão pode percorrer:", round(total,2), "em Km/L")

# 3.
# print(f"Conversor de Moeda (Frete Internacional)")
# valor = float(input("Qual é o valor em reais que será convertido?..."))
# taxa_dolar = float(input("Qual é o valor da taxa:"))
# total = valor / taxa_dolar
# print(f"O valor total convertido é... {total:.2f}")

# 4.
# print(f"Média de Entrega")
# tempo1 = int(input("Qual foi o tempo para concluir a rota 1 em horas"))
# tempo2 = int(input("Qual foi o tempo para concluir a rota 2 em horas"))
# tempo3 = int(input("Qual foi o tempo para concluir a rota 3 em horas"))
# media = (tempo1 + tempo2 + tempo3) / 3
# print(f"A média {media:.2f} de tempo das entregas")

# 5.
# print(f"Monitor de carga")
# peso = float(input("Qual é o peso atual do seu caminhão?..."))

# if peso <10:
#     print("Carga leve")
# elif peso <= 25:
#     print("Carga padrão")
# else:
#     print("Alerta execesso de peso")

# 6.
# print("Classificador de Destinos")
# print("Regiões = N - Região Norte, S - Região Sul, Qualquer Outra - Internacional")
# regiao = input("Inserir o código da Região:").lower()
# if regiao == "N".upper() or regiao == "n".lower():
#     print("Região Norte")
# elif regiao == "S":
#     print("Região Sul")
# else:
#     print("Região Internacional")

# 7.
# print("Liberação de Saída")
# checklist = input("O checklist foi concluido? [Concluido ou Não Concluido]")
# motorista = input("O motorista foi indentificado? [Sim ou Não]")
# if checklist == "concluido" and motorista == "Sim":
#     print("Veículo autorizado a iniciar a rota.")
# else:
#     print("Veículo NÃO autorizado a iniciar a rota. Verificar checklst e indentificação do motorista.")

# 8.
# print("Cálculo de Atrasos")
# total_entregas = int(input("Total de entregas Agendadas:..."))
# total_atrasos = int(input("Total de Entregas em Atrasos:..."))
# if total_atrasos > total_entregas * 0.1:
#     print("Necessario otimizar rotas")
# else:
#     print("Logistica Eficiente")

# 9.
# print("Validação de Calibragem")
# pressao = float(input("Digite a pressão do pneu em PSI:..."))
# if 100 <= pressao < 100:
#     print("Dentro do padrão")
# elif pressao < 100:
#     print("Abaixo do recomendado")
# else:
#     print("Acima do recomendado")

# 10.
# print("Contagem de Embarque")
# import time
# for contagem in range (5,0 -1):
#     time.sleep(1)
#     print(contagem)
# print("Portão Trancado!!!!!!")

# 11.
# print("Somatorio de Fretes (Acumulador)")
# faturamento_total = 0
# valor_frete = -1
# while valor_frete != 0:
#     valor_frete = float(input("Valor do Frete ou 0 para encerrar:"))
#     faturamento_total += valor_frete
#     print(f"Faturamento acumulado: R$ {faturamento_total}")
# print("Cálculo executado com sucesso")

# 12.
# print("Monitoramento de Frota")
# maior_ka = 0
# for frota in range(1,6):
#     km = float(input(f"Digite a quilometragem do veículo {frota}:"))
#     if km > maior_ka:
#         maior_ka = km
# print(f"A maior quilometragem registrada é: {maior_ka} km.")

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
