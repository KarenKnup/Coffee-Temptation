import os
import subprocess

def abrir_login(root):
    root.destroy()  # Fecha a janela atual
    caminho_login = os.path.join("paginas", "login.py")
    subprocess.run(["python", caminho_login])

def abrir_cliente(root):
  root.destroy()  # Fecha a janela atual
  caminho_cliente = os.path.join("paginas", "cliente.py")
  subprocess.run(["python", caminho_cliente])

def abrir_U_cardapio(root, user, senha):
  root.destroy()  # Fecha a janela atual
  caminho_altera_cardapio = os.path.join("paginas", "altera_cardapio.py")
  subprocess.run(["python", caminho_altera_cardapio, user, senha])

def abrir_D_cardapio(root, user, senha):
  root.destroy()  # Fecha a janela atual
  caminho_deleta_cardapio = os.path.join("paginas", "deleta_cardapio.py")
  subprocess.run(["python", caminho_deleta_cardapio, user, senha])

def abrir_U_produto(root, user, senha):
  root.destroy()  # Fecha a janela atual
  caminho_altera_produto = os.path.join("paginas", "altera_produto.py")
  subprocess.run(["python", caminho_altera_produto, user, senha])

def abrir_D_produto(root, user, senha):
  root.destroy()  # Fecha a janela atual
  caminho_deleta_produto = os.path.join("paginas", "deleta_produto.py")
  subprocess.run(["python", caminho_deleta_produto, user, senha])
