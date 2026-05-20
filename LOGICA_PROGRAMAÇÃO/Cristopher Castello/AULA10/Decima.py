# Tratamento de Erros e Depuração
# try e execpt são usados para lídar com erros de forma controlada, evitando que o programa quebre. O código dentro do bloco try é executado normalmente,
# mas se ocorrer um erro, o controle é passado para o bloco expect, onde podemos lidar com a situação de forma apropriada.

# try:
#     numero = int(input("Digite um número: "))
#     resultado = 10 / numero
#     print("O resultado é:", resultado)

# except ValueError:
#     print("Erro: você deve digiar um número válido")

# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero")

# except KeyboardInterrupt:
#     print("\n programa interronpido")

# except TypeError:
#     print("Erro: Tipo de dado inválido.")

# except Exception as erro:
#     print("Erro inesperado:", erro)

# Exercicios 1 
# Escreva um programa que solicite ao usuário calcule a medía de três números.
# O programa deve lidar com possíveis erros, como a entrada de valores não númericos ou a divisão por zero
# while True:
#  try:
#      numero1 = int(input("digite o numero: "))
#      numero2 = int(input("digite o numero: "))
#      numero3 = int(input("digite o numero: "))
#      resultado = 2 / numero1 + numero2 + numero3
#      print("O resultado é: ", resultado)
#  except ZeroDivisionError:
#      print("Você não deve dividir um nimero por zero")
#  except ValueError:
#     print("Você deve digitar um número válido.")

# Explicação de def: A palavra-chave "def" é usada para definir uma função em python. Uma função é um bloco de código reutilizar que realiza uma tarefa específica.
# Return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada.
# O valor retornado pode ser usado posteriormente no codigo

# def nome_da_função(parametro1, parametro2):
    # Corpo da função (codigo que será executado)
    # resultado = parametro1 + parametro2
    # return resultado
# Exemplo 1
# def saudação(nome):
#     nome = input("Digite seu nome: ")
#     idade = int(input("Digite sua idade: "))
#     return f"Olá, {nome}, {idade}!"
# print(saudação("" ""))

# Exemplo 2
# def calcular_media(num1, num2, num3):
#  try:
#     media = (num1 + num2 + num3) / 3
#     return media
#  except TypeError:
#     return "Erro: Todos os valores devem ser números."
#  except ZeroDivisionError:
#     return "Erro: Não é possivel deividir por zero"

# print(f"calcular_media ((calcular_media(10,20,30)))")

# # Exemplo 3
# def valores():
#    print("Digite três valores: ")
#    a = int(inpu("Digite o primeiro valor: "))
#    b = int(input("Digite o segundo valor: "))
#    c = int(input("Digite o terceiro valor: "))
#    return a,b,c
# print(f"O valor é: {max(valores())}")

# Exemplo 4:
# Calcule o dobro de um número fornecido pelo úsuario, tratando erros de entrada inválido.
def calcular_dobro():
    try:
        valor_digitando = int(input("Digite o valor que deseja: "))
        total_dobro = valor_digitando *2
        return total_dobro

    except ValueError:
        print("Digite um número válido")
print(f"O calculo é: {calcular_dobro()}")
    