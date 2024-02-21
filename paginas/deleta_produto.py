import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import fazer_login2, removerProduto

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('260x300')
root.configure(background='light gray')

login = sys.argv[1]
senha = sys.argv[2]

tk.Label(root, text='REMOVER PRODUTO', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.05, anchor='n')

tk.Label(root, text='Título do Cardápio:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.20, anchor='center')
cardapio = tk.Entry(root)
cardapio.place(relx=0.5, rely=0.28, anchor='center', width=200, height=20)

tk.Label(root, text='Nome do Produto a ser removido:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.36, anchor='center')
nome = tk.Text(root, height=4, width=50)
nome.place(relx=0.5, rely=0.44, anchor='center', width=200, height=20)

btnEnviar = tk.Button(root, text='Enviar', command=lambda:removerProduto(cardapio,nome)).place(relx=0.5, rely=0.55, anchor='center', width=70, height=20)

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar', command=lambda: fazer_login2(login,senha,root))
btnVoltar.place(relx=0.5, rely=0.80, anchor='center', width=150, height=20)

# Executando
root.mainloop()
