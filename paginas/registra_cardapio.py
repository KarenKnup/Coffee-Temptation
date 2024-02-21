import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import fazer_login2
from funcoes.cardapio_atual import  registrarCardapio
from funcoes.login import abrir_U_cardapio, abrir_D_cardapio

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('260x300')
root.configure(background='light gray')

cargo = sys.argv[1]
login = sys.argv[2]
senha = sys.argv[3]

tk.Label(root, text='CRIAR NOVO MENU', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.1, anchor='n')

tk.Label(root, text='Título do Cardápio:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.23, anchor='center')
titulo = tk.Entry(root)
titulo.place(relx=0.5, rely=0.30, anchor='center', width=200, height=20)

tk.Label(root, text='Descrição do Cardápio:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.38, anchor='center')
descricao = tk.Text(root, height=4, width=50)
descricao.place(relx=0.5, rely=0.50, anchor='center', width=200, height=20)

btnEnviar = tk.Button(root, text='Enviar', command=lambda: registrarCardapio(titulo,descricao)).place(relx=0.5, rely=0.60, anchor='center', width=70, height=20)

btnAltera = tk.Button(root, text='Alterar Menu', bg='#f3bf5f', command=lambda:abrir_U_cardapio(root,login,senha)).place(relx=0.5, rely=0.73, anchor='center', width=150, height=20)

btnRemove = tk.Button(root, text='Remover Menu', bg='#f3bf5f', command=lambda: abrir_D_cardapio(root,login,senha)).place(relx=0.5, rely=0.81, anchor='center', width=150, height=20)

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar', command=lambda: fazer_login2(login,senha,root))
btnVoltar.place(relx=0.5, rely=0.92, anchor='center', width=150, height=20)

# Executando
root.mainloop()
