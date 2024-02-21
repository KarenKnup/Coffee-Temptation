import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from funcoes.funcionario import fazer_login2
from funcoes.cardapio_atual import atualizarCardapio

# CRIANDO UMA JANELA
root = tk.Tk()
root.title("Café Temptation")
root.geometry('260x300')
root.configure(background='light gray')

login = sys.argv[1]
senha = sys.argv[2]

tk.Label(root, text='ALTERAR UM MENU', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.1, anchor='n')

tk.Label(root, text='Título do Cardápio a ser alterado:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.30, anchor='center')
titulo = tk.Entry(root)
titulo.place(relx=0.5, rely=0.40, anchor='center', width=200, height=20)

tk.Label(root, text='Novo título do Cardápio:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.47, anchor='center')
novo_titulo = tk.Entry(root)
novo_titulo.place(relx=0.5, rely=0.55, anchor='center', width=200, height=20)

tk.Label(root, text='Nova descrição do Cardápio:', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.63, anchor='center')
nova_descricao = tk.Text(root, height=4, width=50)
nova_descricao.place(relx=0.5, rely=0.70, anchor='center', width=200, height=20)

btnEnviar = tk.Button(root, text='Enviar', command=lambda: atualizarCardapio(titulo.get(), novo_titulo.get(), nova_descricao.get("1.0", "end-1c"))).place(relx=0.5, rely=0.78, anchor='center', width=70, height=20)

# Botão para voltar
btnVoltar = tk.Button(root, text='Voltar', command=lambda: fazer_login2(login,senha,root))
btnVoltar.place(relx=0.5, rely=0.90, anchor='center', width=150, height=20)

# Executando
root.mainloop()
