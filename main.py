import tkinter as tk
from tkinter import *
from funcoes.exit import Exit
from funcoes.login import abrir_login, abrir_cliente
from funcoes.tabelas import criar_tabelas

# Iniciar a criação das tabelas antes de iniciar o loop principal - SQLite3
criar_tabelas()

# Iniciar a GUI
root = tk.Tk()
root.title("Café Temptation")
root.geometry("350x350")
root.configure(bg='light gray')

# Título
tk.Label(root, text='TELA INICIAL', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.1, anchor='n')

# Botão Funcionário
btnLogin = Button(text='Funcionário', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=20, height=2, command=lambda: abrir_login(root))
btnLogin.place(relx=0.5, rely=0.3, anchor='center')

# Botão Cliente
btnReg = Button(text='Cliente', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=20, height=2,command=lambda: abrir_cliente(root))
btnReg.place(relx=0.5, rely=0.5, anchor='center')

# Botão Sair
btnExit = Button(text='Sair', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=20, height=2, command=lambda: Exit(root))
btnExit.place(relx=0.5, rely=0.7, anchor='center')

# Executando
root.mainloop()
