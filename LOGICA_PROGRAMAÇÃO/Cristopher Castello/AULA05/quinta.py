# Revisão de conteúdo:
# print = "função de saída de dados para o console"
# input = "função de entrada de dados do usúario via teclado"
# if = "Estrutura de decisão para executar código condicionalmente"
#   elif = "Combinação de else + if para verificar múltiplicas condições"
#   else = "Parte opcional de um if que executa código quando a condição do if é falsa"
# for = "laço de repetição para iterar sobre uma sequência de elementos"
# while = "laço de repetição para executar código enquanto uma condição for verdadeira"
# operadores matemáticos: +, -, *, /, //, %, **
# operadores de comparação: ==, |=, >, <, >=, <=
# variavel = "Exemplo de variavel para armazenar dados"
# print(variavel)

# Exemplo 1: com print e input
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}! Bem-Vindo à aula de Python para Desenvolvimento de Sistemas!")

# Exemplo 2: com if, elif e else
# nota = float(input("Digite a nota do aluno: "))
# if nota >= 7:
#     print("Aluno aprovado!")
# elif nota >= 5:
#     print("Aluno em recuperação.")
# else:
#     print("Aluno reprovado.")
    
# Exemplo 3: com for
# materials = ["metal," "plastico," "vidro"]
# for material in materials:
#     print(f"Processando material: {material}.")
#     print(f"Material {material}")
# print ("Fim do processamento de materiais.")

# 2. O laço while (Repetições Indeterminadas)
# Use o while quando você não quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de temperatura (Loop infinito Controlado)
# Repete enquanto a temperatura estiver segura
import time
temperatura = 25
while temperatura < 40:
    print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
    time.sleep(1)
    temperatura += 3 # Simulando o aquecimento de máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Lista de temperaturas lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]
# for temp in leituras:
#     while temp > 100:
#         print(f"CRÍTICO: {temp}°C. detectado! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
#     print("Sistema desligado. Aguardado manutenção.")

# # Produção de peças com controle de material usando continue
# materiais = ["metal," "metal," "plastico," "metal," "vidro," "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#         continue # Pula o restante do código abaixo e vai para a próxima peça
#     # Este código só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")
# print("Fim do lote de produção")

