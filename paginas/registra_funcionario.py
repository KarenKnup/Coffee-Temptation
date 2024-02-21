import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from funcoes.funcionario import gravar_funcionario
from funcoes.funcionario import voltar_para_login

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('250x500')
root.configure(background='light gray')

# Labels e Entradas para o ADMINISTRADOR
tk.Label(root, text='Login do ADMINISTRADOR:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.10, anchor='center')
vlogin_admin = tk.Entry(root)
vlogin_admin.place(relx=0.5, rely=0.15, anchor='center', width=200, height=20)

tk.Label(root, text='Senha do ADMINISTRADOR:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.20, anchor='center')
vsenha_admin = tk.Entry(root)
vsenha_admin.place(relx=0.5, rely=0.25, anchor='center', width=200, height=20)

# Labels e Entradas para o novo funcionário
tk.Label(root, text='Login do novo funcionário:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.30, anchor='center')
vlogin = tk.Entry(root)
vlogin.place(relx=0.5, rely=0.35, anchor='center', width=200, height=20)

tk.Label(root, text='Senha do novo funcionário:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.40, anchor='center')
vsenha = tk.Entry(root)
vsenha.place(relx=0.5, rely=0.45, anchor='center', width=200, height=20)

tk.Label(root, text='Nome do novo funcionário:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.50, anchor='center')
vnome = tk.Entry(root)
vnome.place(relx=0.5, rely=0.55, anchor='center', width=200, height=20)

tk.Label(root, text='Cargo do novo funcionário:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.60, anchor='center')
vcargo = tk.Entry(root)
vcargo.place(relx=0.5, rely=0.65, anchor='center', width=200, height=20)

tk.Label(root, text='Salário do novo funcionário:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.70, anchor='center')
vsalario = tk.Entry(root)
vsalario.place(relx=0.5, rely=0.75, anchor='center', width=200, height=20)

# Botão para enviar
btnEnviar = tk.Button(root, text='Enviar', command=lambda: gravar_funcionario(vlogin_admin,vsenha_admin,vlogin,vsenha, vnome, vcargo, vsalario))
btnEnviar.place(relx=0.5, rely=0.82, anchor='center')

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar', command=lambda: voltar_para_login(root))
btnVoltar.place(relx=0.5, rely=0.90, anchor='center', width=150, height=20)

# Executando
root.mainloop()
