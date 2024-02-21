import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import fazer_login2, alterarProduto

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('260x350')
root.configure(background='light gray')

login = sys.argv[1]
senha = sys.argv[2]

tk.Label(root, text='ALTERAR PRODUTO', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.05, anchor='n')

tk.Label(root, text='Título do Cardápio:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.18, anchor='center')
cardapio = tk.Entry(root)
cardapio.place(relx=0.5, rely=0.24, anchor='center', width=200, height=20)

tk.Label(root, text='Nome do Produto a ser alterado:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.30, anchor='center')
nome = tk.Text(root, height=4, width=50)
nome.place(relx=0.5, rely=0.36, anchor='center', width=200, height=20)

tk.Label(root, text='Novo nome do Produto:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.42, anchor='center')
novo_nome = tk.Text(root, height=4, width=50)
novo_nome.place(relx=0.5, rely=0.48, anchor='center', width=200, height=20)

tk.Label(root, text='Nova descrição do Produto:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.54, anchor='center')
descricao = tk.Text(root, height=4, width=50)
descricao.place(relx=0.5, rely=0.60, anchor='center', width=200, height=20)

tk.Label(root, text='Novo preço do Produto:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.66, anchor='center')
preco = tk.Text(root, height=4, width=50)
preco.place(relx=0.5, rely=0.72, anchor='center', width=200, height=20)

btnEnviar = tk.Button(root, text='Enviar',command=lambda:alterarProduto(cardapio,nome,novo_nome,descricao,preco)).place(relx=0.5, rely=0.78, anchor='center', width=70, height=20)

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar',command=lambda: fazer_login2(login,senha,root))
btnVoltar.place(relx=0.5, rely=0.90, anchor='center', width=150, height=20)

# Executando
root.mainloop()
