# Exercicio 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (Simulando uma falha de sensor especifica no iten 5)

# for sensor in range (1, 11):
#     if sensor == 5:
#         print(f"Sensor nº {sensor} com falha")
#     print(f"Sensor {sensor} sem falha")
#     continue
# print("FIM! :)")

# Exercicio 2
# Simule um semaforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal com ele represente uma pausa para cada cor. Use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela)

# cores = ["verde," "amarelo," "vermelho"]

# for cor in cores:
#     if cor == "Amarelo":
#         print(f"O sinal está com {cor} defeito")
#     print(f"O sinal está em funcionamento {cor}")

# Exercicio 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peças ao usuário (via input dentro do loop)
# o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa
# deve exibir o consumo total de fábrica.

# for maq in range(1, 6):
#     maquinas = float(input("Digite o valor que deseja da {maq} nº"))
#     maq = maq * maquinas
#     print(f"Total da soma de máquinas {maquinas}" )

# Exercicio 4 - Indentificador de peças defeituosas (for + if)
# Percorra uma lista de meedidas de peças:
# medidas = [50.1, 49.8, 52.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada"

# medidas = [50.1, 49.8, 52.0, 48.5]
# for med in medidas:
#     if med > 50.0:
#         print(f"Peças aceitas: {med} .")
#     elif med < 50.0:
#         print(f"Peças não aceitas: {med}")
        
# Exercicio 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos.
# O peso ideal de cada saco é de 50kg, mas o sistema aceitas variações.
# Crie um programa que peça ao usuário o peso de cada saco (via input dentro do loop) e,
# para cada um, informe se ele está "Dentro do limite" (entre 48kg e 52kg) ou "fora do limite".
# No final, exiba quantos sacos estão dentro do limite

# Escolha = float(input("Qual e o peso de cada saco?: "))
# pesos = [50.0, 48.0, 52.0]
# for peso in pesos:
#     if 48 < Escolha < 50.0:
#         print(f"peso aceito {peso}")
#         sacos_dl += 1
#     else:
#         print(f"peso fora do limite {peso}")

# O desafio: Gestão de ciclo termico
# você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# Regras do Sistema: O programa deve rodar em um loop até que 5 peças validas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual (input).
# Filtro de Erro (continue): Se o usuário digita uma temperatura negativa, exiba "Erro de leitura no sensor"
# e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergencia (break): Se a temperatura for maior que 150°C, o sistema deve ecibir "ALERTA CRITICO": Risco de Explosão!
# interromper o loop imediatamente e encerrar o programa.

