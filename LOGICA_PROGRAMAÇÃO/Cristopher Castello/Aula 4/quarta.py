# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 censores ou processar uma lista de peças)
# Exemplo: Relatorio de produção Diaria
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número:{lote}...\n")
#     print("Quantidade Verificada. [OK]")
#     print("Produção do dia finalizada!")

# Exemplo 2
# for b in range(10):
#     print(f"Quantidade total {b} foi...")


# Exemplo 3
# imagine o seguinte cenário, iremo produzir 20 discos de vinil
# for vinil in range(1,21):
#     print(f"Produção de: {vinil} diaria \n")
#     print("Quantidade Produzidas. [OK]")
#     print("Produção finalizada!")

# Exemplo 4
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda"]
# itempecas = ["Cilindrica", "Duplo", "Cronica", "Prego", "Orelha", "Redondo", "Phillips", "Universal"]

# for item in pecas:
#     print(f"Item em estoque: {item} e {itempecas}")

# Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você e a partir da seleção ele liberar os produtos

# print("Menu de Opção")
# print("Escolha uma das opções:")
# print("Jogos J e X para Sair")


# escolha = input("Digite uma opção:")
 
# if escolha == "J":
#      print("Você escolheu Jogos")
#      jogo = ["The Last Of Us", "God Of War(2018)", "Uncharted 4", "Death Stranding"]
# for jogo in jogo:
#       print(f"Jogos Para Venda! {jogo}")

# else:
#      print("Você saiu do programa")

# 
