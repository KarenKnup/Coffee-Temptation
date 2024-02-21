# >>>>>>>>>> TELA DE OPERAÇÕES DO FUNCIONÁRIO

import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import voltar_para_login, abrir_pedido, abrir_U_pedido, abrir_D_pedido, abrir_produto, abrir_preparar
from funcoes.cardapio_atual import abrir_cardapio, abrir_menu

root = tk.Tk()
root.title("Café Temptation")
root.geometry("350x650")
root.configure(bg='light gray')

# Pega o argumento 'cargo' de abrir_tela_funcionario
cargo = sys.argv[1]
login = sys.argv[2]
senha = sys.argv[3]

# Mostra cargo no título
#tk.Label(root, text='TELA DO FUNCIONÁRIO - Cargo: ' + cargo, font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.1, anchor='n')

# Título
tk.Label(root, text='TELA DO FUNCIONÁRIO', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.025, anchor='n')

# Botão Ver Menu 
btnLogin = Button(text='Ver Menu', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=25, height=2,command=lambda:abrir_menu(root,cargo,login,senha))
btnLogin.place(relx=0.5, rely=0.13, anchor='center')

# Botão Atualizar Pedido
btnCancelar = Button(text='Atualizar Pedido', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=25, height=2,command=lambda:abrir_U_pedido(root,cargo,login,senha))
btnCancelar.place(relx=0.5, rely=0.21, anchor='center')

# Botão Preparar Pedidos
btnPreparar = Button(text='Preparar Pedidos', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=25, height=2,command=lambda:abrir_preparar(root,cargo,login,senha))
btnPreparar.place(relx=0.5, rely=0.29, anchor='center')

# Botão Adicionar Pedido
btnAdicionar = Button(text='Adicionar Pedido', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=25, height=2, command=lambda:abrir_pedido(root,cargo,login,senha))
btnAdicionar.place(relx=0.5, rely=0.37, anchor='center')

#-----------  ADMIN ----------------
if(cargo=='Administrador'):
  # Botão Adicionar Menu
  btnReg = Button(text='Gerenciar Menus', padx=6, bd=3, fg='dark blue', bg='#f3bf5f', font=('arial', 10, 'bold'), width=25, height=2, command=lambda: abrir_cardapio(root,cargo,login,senha))
  btnReg.place(relx=0.5, rely=0.45, anchor='center')

  # Botão Alterar Menu
  btnReg = Button(text='Cancelar Pedido', padx=6, bd=3, fg='dark blue', bg='#f3bf5f', font=('arial', 10, 'bold'), width=25, height=2,command=lambda:abrir_D_pedido(root,cargo,login,senha))
  btnReg.place(relx=0.5, rely=0.53, anchor='center')

  #Botão Registrar Itens 
  btnRegistrarProduto = Button(text='Gerenciar Itens do Menu', padx=6, bd=3, fg='dark blue', bg='#f3bf5f', font=('arial', 10, 'bold'), width=25, height=2, command=lambda: abrir_produto(root,cargo,login,senha)) #Registrar, Atualizar, Remover
  btnRegistrarProduto.place(relx=0.5, rely=0.61, anchor='center')

# Botão Sair
btnExit = Button(text='Sair', padx=6, bd=3, fg='dark blue', bg='dark gray', font=('arial', 10, 'bold'), width=25, height=2, command=lambda: voltar_para_login(root))
btnExit.place(relx=0.5, rely=0.69, anchor='center')

# Executando
root.mainloop()