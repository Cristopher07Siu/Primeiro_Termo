# 🐍 Lógica de Programação com Python

## 📑 1. Conteúdo de Aula
*   **Introdução à Lógica:** O que é um algoritmo e como estruturar o pensamento lógico para resolver problemas.
*   **Estruturas Fundamentais:**
    *   **Variáveis e Tipos de Dados:** Armazenamento de informações na memória.
    *   **Operadores:** Aritméticos (soma, subtração), relacionais (maior, menor) e lógicos (e, ou, não).
    *   **Estruturas de Decisão:** Controle de fluxo condicional com base em critérios.
    *   **Estruturas de Repetição:** Loops para automação e execução contínua de blocos de código.

---

## 💻 2. Implementação em Python
*   **Sintaxe Limpa:** Linguagem de alto nível focada em legibilidade, que dispensa o uso de ponto e vírgula e chaves.
*   **Indentação Obrigatória:** O recuo do texto define o escopo dos blocos de código (condicionais, loops e funções).
*   **Tipagem Dinâmica:** O Python identifica o tipo da variável automaticamente no momento da atribuição.

### Exemplos Práticos de Código

#### Variáveis, Entrada e Saída
```python
# Entrada de dados do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Saída de dados formatada
print(f"Olá {nome}, você tem {idade} anos.")
```

#### Estrutura Condicional (Se / Senão)
```python
nota = 7.5

if nota >= 7.0:
    print("Aluno Aprovado!")
elif nota >= 5.0:
    print("Recuperação.")
else:
    print("Aluno Reprovado.")
```

#### Estrutura de Repetição (Loops)
```python
# Loop 'for' (Contagem de 1 a 5)
for i in range(1, 6):
    print(f"Número: {i}")

# Loop 'while' (Condicional)
contador = 0
while contador < 3:
    print("Executando...")
    contador += 1
```
