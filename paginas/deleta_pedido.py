import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import fazer_login2, cancelarPedido

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('260x400')
root.configure(background='light gray')

senha = sys.argv[3]
cargo = sys.argv[1]
login = sys.argv[2]

# Considerar o último cardápio registrado sempre

tk.Label(root, text='CANCELAR PEDIDO', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.05, anchor='n')

tk.Label(root, text='ID do Pedido:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.25, anchor='center')
id_pedido = tk.Entry(root)
id_pedido.place(relx=0.5, rely=0.35, anchor='center', width=200, height=20)

btnEnviar = tk.Button(root, text='Enviar', command=lambda: cancelarPedido(id_pedido.get())).place(relx=0.5, rely=0.50, anchor='center', width=150, height=20)

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar',command=lambda: fazer_login2(login, senha, root))
btnVoltar.place(relx=0.5, rely=0.60, anchor='center', width=150, height=20)

# Executando
root.mainloop()
