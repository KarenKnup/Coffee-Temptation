import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import fazer_login2, registrarProduto
from funcoes.login import abrir_U_produto, abrir_D_produto

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('260x320')
root.configure(background='light gray')

cargo = sys.argv[1]
login = sys.argv[2]
senha = sys.argv[3]

tk.Label(root, text='CADASTRAR PRODUTO', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.05, anchor='n')

tk.Label(root, text='Título do Cardápio a ser inserido:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.18, anchor='center')
cardapio = tk.Entry(root)
cardapio.place(relx=0.5, rely=0.24, anchor='center', width=200, height=20)

tk.Label(root, text='Nome do Produto:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.30, anchor='center')
nome = tk.Text(root, height=4, width=50)
nome.place(relx=0.5, rely=0.36, anchor='center', width=200, height=20)

tk.Label(root, text='Descrição do Produto:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.42, anchor='center')
descricao = tk.Text(root, height=4, width=50)
descricao.place(relx=0.5, rely=0.48, anchor='center', width=200, height=20)

tk.Label(root, text='Preço do Produto:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.54, anchor='center')
preco = tk.Text(root, height=4, width=50)
preco.place(relx=0.5, rely=0.60, anchor='center', width=200, height=20)

btnEnviar = tk.Button(root, text='Enviar',command=lambda:registrarProduto(cardapio,nome,descricao,preco)).place(relx=0.5, rely=0.68, anchor='center', width=70, height=20)

btnAltera = tk.Button(root, text='Alterar produto em um menu', bg='#f3bf5f', command=lambda:abrir_U_produto(root,login,senha)).place(relx=0.5, rely=0.77, anchor='center', width=220, height=20)

btnRemove = tk.Button(root, text='Remover produto em um menu', bg='#f3bf5f', command=lambda:abrir_D_produto(root,login,senha)).place(relx=0.5, rely=0.84, anchor='center', width=220, height=20)

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar', command=lambda: fazer_login2(login,senha,root))
btnVoltar.place(relx=0.5, rely=0.93, anchor='center', width=150, height=20)

# Executando
root.mainloop()
