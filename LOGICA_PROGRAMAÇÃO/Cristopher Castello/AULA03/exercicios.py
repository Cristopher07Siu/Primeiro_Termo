# Exercicios
# 1 Criar um algoritmo para realizar a locação de filmes ou séries seguir o modelo anterior. Ao escolher a opção você deverá pergurtar o nome do cliente do filme ou série e quantidaade que deseja assim como o valor de aluguel.
# Para filmes R$5,00 e para séries R$ 10,00



# print("Voce esta ma sessão Filmes")
# nome = input("Digite seu nome:")
# filmes = input("Qual filme deseja?")
# qtde = int(input("Qual quantidade deseja?"))
# valor = 5
# total = qtde * valor
# print("Parabéns pela sua locação de filmes", nome,"E seu filme foi:", filmes,"A quantidade foi", qtde, "E, sua locação custou", valor)

# serie = input("Qual serie deseja?")
# qtde = int(input("Qual quantidade deseja?"))
# valor = 10
# total = qtde * valor
# print("Parabéns pela sua locação de filmes", nome,"E sua serie foi:", serie,"A quantidade foi", qtde, "E, sua locação custou", valor)

# Exercicio 2
# Loja de Comida e Doces
# Criar um algoritmo para compra de produtos
# 1 - Comida
# 2 - Bebida
# 3 - Doces
# Ao escoler as opções cada um terá um valor de porcentegem, comida = 10%, bebida = 5%, Doces = 2%

# print("Bem-Vindo a nossa loja de conveniencias")
# print("Temos, Comida, Bebida e Doces")
# print("Digite a opção que dejesa para iniciar")
# print("Comida - Digite 1")
# print("Bebida - Digite 2")
# print("Doces - Digite 3")

# opcao = int(input("Digite sua opção:"))
# if opcao == 1:
#    print("Você está em Comida")
#    print("Temos PF , La Carte")
#    comida = input("O que deseja? ")
#    valor = float(input("Digite o valor da comida:"))
#    desconto = valor * (10 / 100)
#    total = valor - desconto
#    print("Sua compra total foi de: ", total)

# if opcao == 2:
#    print("Você está em Doces")
#    print("Temos Brigadeiro , beijinho")
#    comida = input("O que deseja? ")
#    valor = float(input("Digite o valor do doce:"))
#    desconto = valor * (2 / 100)
#    total = valor - desconto
#    print("Sua compra total foi de: ", total)

# if opcao == 3:
#    print("Você está em Bebidas")
#    print("Temos Coca cola 600ml , Pepsi 300ml")
#    comida = input("O que deseja? ")
#    valor = float(input("Digite o valor da bebida:"))
#    desconto = valor * (5 / 100)
#    total = valor - desconto
#    print("Sua compra total foi de: ", total)

# Exercico 3
# Calcular com operadores
# sua calculadora deverá perguntar qual operador ele deseja e calcular os valores desejados

# print("Qual valor você deseja colocar?")
# print("Qual outro valor você dejesa colocar?")

# opcao1 = int(input("Digite seu primeiro valor:"))
# opcao2 = int(input("Digite seu segundo valor:"))

# escolha = input("Operador:")

# if  escolha == ("+"):
#     ptotal = (opcao1 + opcao2)
#     print("o valor é: \n", round(ptotal,2))

# if  escolha == ("-"):
#     ptotal = (opcao1 + opcao2)
#     print("o valor é: \n", round(ptotal,2))

# if  escolha == ("*"):
#     ptotal = (opcao1 + opcao2)
#     print("o valor é: \n", round(ptotal,2))

# if  escolha == ("/"):
#     ptotal = (opcao1 + opcao2)
#     print("o valor é: \n", round(ptotal,2))

# # else:
#     print("Isso não e um operador")

# Exercicio 4 
# Calculo de notas
# Nossas atividades são por base de calculo em somativa 1 e somativa 2, no final temos um media. Acima ou igual a 50 o aluno será apovado caso contrario reprovado o programa deverá perguntar o nome e as notas e apresentar o resultado final do aluno

# nota1 = float(input("digite sua nota do primeira somativa: \n"))
# nota2 = float(input("digite sua nota do segunda somativa: \n"))
# ptotal = (nota1 + nota2) / 2
# print ("As somativas  são: \n", round(ptotal,2))

# if ptotal >= 50:
#    print("Sua somativa está na media")

# elif ptotal <= 50:
#      print("Sua somativa está abaixo da meida")

# Exercicio 5 
# Criar um algoritimo para calcular uma viagem de carro, obinus e avião
# viagem de carro: dece ser feito um abastecimento e deve cobrar o valor de pedagio
# onibus: deve ser cobrado o valor do seguro de 3,88
# avião: Cobrar o valor da viagem e valor da taxa de embarque 55,28