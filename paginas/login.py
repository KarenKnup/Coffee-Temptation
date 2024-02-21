# >>>>>>>>>> TELA DE LOGIN

# BIBLIOTECAS PYTHON & GUI
import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.exit import Exit
from funcoes.funcionario import fazer_login, abrir_registrar_funcionario

root = tk.Tk()
root.title("Café Temptation")
root.geometry("350x500+0+0")
root.configure(bg='light gray')

# Título
tk.Label(root, text='TELA DE LOGIN', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.1, anchor='n')

# Login
tk.Label(root, text='Login:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.2, anchor='center')
vlogin = tk.Entry(root)
vlogin.place(relx=0.5, rely=0.25, anchor='center', width=200, height=20)

# Senha
tk.Label(root, text='Senha:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.30, anchor='center')
vsenha = tk.Entry(root)
vsenha.place(relx=0.5, rely=0.35, anchor='center', width=200, height=20)

# Botão Entrar
btnLogin = Button(text='Entrar', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=20, height=2, command=lambda: fazer_login(vlogin, vsenha, root))
btnLogin.place(relx=0.5, rely=0.45, anchor='center')

# Botão Registre-se
btnReg = Button(text='Registre-se', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=20, height=2, command=lambda: abrir_registrar_funcionario(root))
btnReg.place(relx=0.5, rely=0.55, anchor='center')

# Botão Sair
btnExit = Button(text='Sair', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=20, height=2, command=lambda: Exit(root))
btnExit.place(relx=0.5, rely=0.65, anchor='center')

# Executando
root.mainloop()