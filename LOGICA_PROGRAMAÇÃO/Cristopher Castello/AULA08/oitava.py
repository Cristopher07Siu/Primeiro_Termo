# Tratamento de Erros e Execuções
# valor = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# resultado = valor / valor2
# print(f"O resultado da divisão é de: {resultado}")
# O código acima pode gerar um erro de divisão por zero se o usuário digitar 0 para o segundo valor. Para tratar esse erro, podemos usar um bloco try-except:
# Exemplo 1: Tratamento de divisão por zero
# try:
#     valor = int(input("Digite o primeito valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero.")

# Exemplo 2: Tratamento de entrada inválida
# try:
#     valor = int(input(f"Digite o primeiro valor: "))
#     valor2 = int(input(f"Digite o segundo valor: "))
#     resultado = valor / valor2
#     print(f"O resultado da divisao é de : {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Ocorreu um erro: {e}")

# Exemplo 3: Uso do bloco finally
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é de: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de value: Por favor, digite um número inteiro válido. {e} ou Erro: Não é possivel dividir por zero. {e}")
# finally:
#     print("Bloco finally executado.")

# Exemplo 5: TypeError
# try:
#     resultado = "5" + 10
# except TypeError as e:
#     print(f"Erro de tipo {e}")

# Pojeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado 
# As entrada deverão ser registradas por placa. 
# 
# Passo 1:
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado 
# Se possuir erros informar ao usuario

# Passo 2:
# Verificar tempo de permanencia
# Valor a ser cobrado

# Passo 3:
# Saida como será?
# Calcular tempo de permanencia
# Se for tag gerar na fatura da tag
# Pagar ticket
# Devolver ticket na saida

# Passo 4:
# Gerar relatorio de entradas e saidas
# Tratamento de Erros
# Revisão do código
