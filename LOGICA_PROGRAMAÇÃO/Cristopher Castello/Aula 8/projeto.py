print("Entre no Estacionamente")
print("Menu de opções")
print("Escolha uma das opções")
print(f"Ticket T e Caso possuir TAG G e Caso queira sair digite X")
escolha = input("Digite uma opção:")

if escolha == "T":
     print("Você escolheu: Ticket")
elif escolha == "G":
     print("Você Possui: TAG")
else:
     print("Voce saiu do programa")

print("Registro de Veículo")
modelo = input("Digite o modelo de veículos:")
placa = input("Digite a placa do veículo:")
print(f"Veículo {modelo} de placa {placa} registrado no sistema. ")

horario = input("Qual horario você dejesa ficar no shopping? ")
