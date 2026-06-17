# import tkinter as tk
# from tkinter import messagebox, ttk

# # Função
# def biblioteca():
#     tipo_usuario = combo_usuario.get()
#     titulo = titulo_livro.get()
#     nome = nome_usuario.get()
#     categoria = combo_categoria.get()
#     dias = aluno_emprestimo.get()

#     if tipo_usuario == "" or titulo == "" or nome == "" or categoria == "" or dias == "":
#         messagebox.showwarning("Aviso", "Preencha todos os campos!")
#     else:
#         messagebox.showinfo(
#             "Empréstimo",
#             f"""Olá, {nome}!

# Tipo de usuário: {tipo_usuario}
# Livro: {titulo}
# Categoria: {categoria}
# Dias de empréstimo: {dias}
# """
#         )

# # Janela
# janela_biblioteca = tk.Tk()
# janela_biblioteca.title("Biblioteca")
# janela_biblioteca.geometry("900x400")

# # Labels
# tk.Label(janela_biblioteca, text="Tipo de Usuário:").grid(row=0, column=1, padx=10, pady=10)

# tk.Label(janela_biblioteca, text="Título do Livro:").grid(row=1, column=1, padx=10, pady=10)

# tk.Label(janela_biblioteca, text="Nome do Usuário:").grid(row=2, column=1, padx=10, pady=10)

# tk.Label(janela_biblioteca, text="Categoria do Livro:").grid(row=0, column=3, padx=10, pady=10)

# tk.Label(
#     janela_biblioteca,
#     text=(
#         "Regras de Negócio\n"
#         "Alunos: até 14 dias de graça\n"
#         "Comunidade: até 7 dias de graça\n"
#         "Taxa adicional: R$ 5,00 por dia extra\n"
#         "Livros raros: apenas para alunos"
#     ),
# ).grid(row=2, column=3, padx=10, pady=10)

# tk.Label(janela_biblioteca, text="Dias de Empréstimo:").grid(row=1, column=3, padx=10, pady=10)

# # Entrys
# titulo_livro = tk.Entry(janela_biblioteca, font=("Arial", 12), width=20)
# titulo_livro.grid(row=1, column=2, padx=10, pady=10)

# nome_usuario = tk.Entry(janela_biblioteca, font=("Arial", 12), width=20)
# nome_usuario.grid(row=2, column=2, padx=10, pady=10)

# aluno_emprestimo = tk.Entry(janela_biblioteca, font=("Arial", 12), width=20)
# aluno_emprestimo.grid(row=1, column=4, padx=10, pady=10)

# # Combobox
# combo_usuario = ttk.Combobox(
#     janela_biblioteca,
#     values=["Aluno", "Comunidade"],
#     width=20
# )
# combo_usuario.grid(row=0, column=2, padx=10, pady=10)

# combo_categoria = ttk.Combobox(
#     janela_biblioteca,
#     values=["Comum", "Raro"],
#     width=20
# )
# combo_categoria.grid(row=0, column=4, padx=10, pady=10)

# # Botões
# btn_enviar = tk.Button(
#     janela_biblioteca,
#     text="Enviar Mensagem",
#     command=biblioteca,
#     bg="#9dfff0"
# )
# btn_enviar.grid(row=3, column=1, padx=10, pady=10)

# btn_fechar = tk.Button(
#     janela_biblioteca,
#     text="Fechar Janela",
#     command=janela_biblioteca.destroy,
#     bg="#ff0000"
# )
# btn_fechar.grid(row=3, column=2, padx=10, pady=10)

# janela_biblioteca.mainloop()