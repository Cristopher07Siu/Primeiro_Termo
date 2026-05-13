# Clean Code - Aula 7
# para que usar?
# como usar?
# print("Clean Code - Aula 7")
# aula = 7
# print(f"Estamos na aula {aula} de clean code")

# 1.
# seu_nickname = input("Insira seu nickname:")
# nivel_do_jogador = input("Qual seu nivel:")
# print(f"O Jogador {seu_nickname} está no nivel {nivel_do_jogador} e pronto para a partida!!!")

# 2.
# valor_da_mesada = int(input("Digite o valor da sua mesada:"))
# total_da_mesada = valor_da_mesada * 4
# print("Então no final do mês você terá", total_da_mesada)

# Manipulação de arquivos e texto
# manipular_Texto = " Python é Muito legal! "
# print(manipular_Texto.strip().upper()) # "Python"
# print(manipular_Texto.strip().lower) # "python"
# print(manipular_Texto.strip().startswith("A")) # "Começar com Letras iniciais"
# print(manipular_Texto.strip().capitalize()) # "Letra inicial"
# print(manipular_Texto.strip().title()) # "Titulo"
# print(manipular_Texto.strip().replace(" ", " ")) # "Preencher vazios"
# print(manipular_Texto.strip().split()) # "Separar palavras"

# Exercicio 1.
# Crie um progama que peça ai usúario para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações;
# - Deixe o texto em letras minúsculas
# texto = input("insira o texto:")
# print(texto.strip().lower())

# Manipular arquivos:
# Escrevendo
# with open("notas.txt", "w", encoding="utf-8") as texto:
#     texto.write("Estudar Python hoje!")
#     texto.write("\nLer sobre Clean Code.")
#     texto.write("\n Estamos evolvidos")

# Lendo
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python"
# aparece no arquivo. Exiba o resultado para o usúario.
# print("Contagem de palavras em arquivo")
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#      conteudo = texto.read()
#      contagem = conteudo.count("Python")
#      contagem = conteudo.upper().count("Python") # Contar a palavra
#     #  palavra "python"
#      contagem = conteudo.lower().count("python")
#      print(f"A contagem de palavras {contagem} é de...")
     
# Interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))

# Criar pastas

# os.mkdir("Cris")
# Criar arquivos

# Renomear pastas
# os.rename("Cris", "Minha_Pasta")

# Apagar pastas
# os.rmdir("Minha_Pasta")