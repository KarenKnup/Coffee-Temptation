import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
from funcoes.login import abrir_cliente

root = tk.Tk()  
root.title("Café Temptation")
root.geometry('400x500')
root.configure(background='light gray')

id_cliente = sys.argv[1]
id_cliente = int(id_cliente)  # Converta para inteiro

connection = sqlite3.connect("Cafeteria.db")
cursor = connection.cursor()

# Consultar o nome do cliente
cursor.execute("SELECT nome FROM Cliente WHERE id = ?;", (id_cliente,))
result = cursor.fetchone()

if result is not None:
    nome = result[0]

    # Mostra cargo no título
    tk.Label(root, text='NOTA FISCAL DO PEDIDO', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').place(relx=0.5, rely=0.1, anchor='center')

    tk.Label(root, text='Cliente: ' + nome, background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.20, anchor='center')

    tk.Label(root, text='ID do PEDIDO: ' + str(id_cliente), background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.25, anchor='center')

    # Consultar os pedidos do cliente
    cursor.execute("SELECT produto, quantidade, dataHora FROM Pedido WHERE cliente = ?;", (id_cliente,))
    resultados = cursor.fetchall()

    # Mostrar os resultados
    x = 0.30
    total = 0.0
    if resultados:
        for resultado in resultados:
            produto, quantidade, dataHora = resultado
            cursor.execute("SELECT preco FROM Produto where nome = ?;", (produto,))
            r = cursor.fetchone()[0]
            total = total + r * quantidade
            connection.commit()
            tk.Label(root, text=f'{produto} x {quantidade} unidades = R$ {r} às {dataHora}', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=x, anchor='center')
            x = x + 0.05
            tk.Label(root, text=f'às {dataHora}', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=x, anchor='center')
            x = x + 0.05

        tk.Label(root, text='----------------------------------------------------------', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=x + 0.05, anchor='center')

        tk.Label(root, text='Valor total: R$ ' + str(total), background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=x + 0.05, anchor='center')

    else:
        tk.Label(root, text='Nenhum pedido encontrado para este cliente.', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=x + 0.05, anchor='center')

    btnVoltar = tk.Button(root, text='Finalizar sessão', command=lambda: abrir_cliente(root))
    btnVoltar.place(relx=x + 0.05 * 2, rely=0.92, anchor='center', width=150, height=20)

else:
    tk.Label(root, text='Cliente não encontrado.', background='light gray', foreground='midnight blue', anchor=tk.W).place(relx=0.5, rely=0.20, anchor='center')
    btnVoltar = tk.Button(root, text='Finalizar sessão', command=lambda: abrir_cliente(root))
    btnVoltar.place(relx=0.5, rely=0.92, anchor='center', width=150, height=20)

# Fechar a conexão
connection.close()

# Executando
root.mainloop()
