import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import fazer_login2, fazerPedido

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('260x320')
root.configure(background='light gray')

cargo = sys.argv[1]
login = sys.argv[2]
senha = sys.argv[3]

#Considerar o último cardápio registrado sempre

tk.Label(root, text='REGISTRAR PEDIDO', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.05, anchor='n')

tk.Label(root, text='Produto do Cardápio atual:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.20, anchor='center')
produto = tk.Entry(root)
produto.place(relx=0.5, rely=0.28, anchor='center', width=200, height=20)

tk.Label(root, text='Quantidade de unidades:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.36, anchor='center')
quantidade = tk.Text(root, height=4, width=50)
quantidade.place(relx=0.5, rely=0.44, anchor='center', width=200, height=20)

tk.Label(root, text='Nome do Cliente:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.52, anchor='center')
cliente = tk.Text(root, height=4, width=50)
cliente.place(relx=0.5, rely=0.60, anchor='center', width=200, height=20)

tk.Label(root, text='Método de pagamento:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.68, anchor='center')
pagamento = tk.Text(root, height=4, width=50)
pagamento.place(relx=0.5, rely=0.76, anchor='center', width=200, height=20)

btnEnviar = tk.Button(root, text='Enviar',command=lambda:fazerPedido(produto,quantidade,cliente,pagamento)).place(relx=0.5, rely=0.84, anchor='center', width=150, height=20)

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar',command=lambda: fazer_login2(login,senha,root))
btnVoltar.place(relx=0.5, rely=0.92, anchor='center', width=150, height=20)

# Executando
root.mainloop()
