import sqlite3
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import sys
import os

def abrir_menu(root, cargo, login, senha):
  root.destroy()  # Fecha a janela atual
  caminho_menu = os.path.join("paginas", "exibe_menu.py")
  subprocess.run(["python", caminho_menu, cargo, login, senha])

def abrir_NF(root, id_cliente):
  root.destroy()
  caminho_NF = os.path.join("paginas", "exibe_NF.py")
  subprocess.run(["python", caminho_NF, id_cliente])

def mostrarCardapio():
    # Conectar ao banco de dados
    connection = sqlite3.connect("Cafeteria.db")
    cursor = connection.cursor()

    try:
        # Obter o último cardápio registrado
        cursor.execute("SELECT nome FROM Cardapio ORDER BY ROWID DESC LIMIT 1;")
        cardapio_atual = cursor.fetchone()

        if cardapio_atual:
            cardapio_nome = cardapio_atual[0]

            # Obter todos os produtos associados a esse cardápio
            cursor.execute("SELECT nome, preco, descricao FROM Produto WHERE nomeCardapio = ?;", (cardapio_nome,))
            produtos = cursor.fetchall()

            return cardapio_nome, produtos
        else:
            return None, None
    except sqlite3.Error as e:
        # Exibir mensagem de erro em caso de falha
        print(f"Erro ao mostrar cardápio: {str(e)}")
    finally:
        # Fechar a conexão com o banco de dados
        connection.close()

def exibirCardapio():
    from funcoes.funcionario import fazer_login2
    cardapio_nome, produtos = mostrarCardapio()

    if cardapio_nome is not None and produtos is not None:
        root = tk.Tk()
        root.title("Café Temptation")
        root.geometry('500x400')
        root.configure(background='light gray')

        cargo = sys.argv[1]
        login = sys.argv[2]
        senha = sys.argv[3]

        # Título
        tk.Label(root, text=f'Cardápio: {cardapio_nome}', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').pack()

        # Lista de produtos
        lista_produtos = Listbox(root, width=50, height=10)
        lista_produtos.pack(pady=10)

        for produto in produtos:
            lista_produtos.insert(END, f"Nome: {produto[0]}, Preço: {produto[1]}, Descrição: {produto[2]}")

        # Scrollbar
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        lista_produtos.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lista_produtos.yview)

        # Botão para fechar
        btnFechar = tk.Button(root, text='Voltar', command=lambda: fazer_login2(login,senha,root))
        btnFechar.pack()

        # Executando
        root.mainloop()

    else:
        print("Nenhum cardápio encontrado.")

def fazerPedido(produto_entry, quantidade_text, cliente_text, pagamento_text):
  # Obter os valores inseridos nos campos de entrada
  produto = produto_entry
  quantidade = quantidade_text
  cliente = cliente_text
  pagamento = pagamento_text

  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Obter o último cardápio registrado
      cursor.execute("SELECT nome FROM Cardapio ORDER BY ROWID DESC LIMIT 1;")
      cardapio_atual = cursor.fetchone()[0]
      connection.commit()

      # Inserir dados na tabela Cliente
      cursor.execute("INSERT INTO Cliente (nome, metodoPagamento) VALUES (?, ?);", (cliente, pagamento))

      # Obter o ID do cliente recém-inserido
      cursor.execute("SELECT id FROM Cliente ORDER BY ROWID DESC LIMIT 1;")
      id_cliente = cursor.fetchone()[0]

      # Obter o preço unitário do produto da tabela Produto
      cursor.execute("SELECT preco FROM Produto WHERE nome = ? AND nomeCardapio = ?;", (produto, cardapio_atual))
      result = cursor.fetchone()

      if result is not None:
          preco_unitario = result[0]
          connection.commit()

          # Inserir dados na tabela Pedido
          data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          status = "PENDENTE"
          cursor.execute("INSERT INTO Pedido (dataHora, status, produto, quantidade, cardapio, cliente) VALUES (?, ?, ?, ?, ?, ?);",
                         (data_hora, status, produto, quantidade, cardapio_atual, id_cliente))
          connection.commit()

          # Inserir dados na tabela ItemPedido
          cursor.execute("INSERT INTO ItemPedido (nomeProduto, nomeCardapio, precoUnit) VALUES (?, ?, ?);",
                         (produto, cardapio_atual, preco_unitario))
          connection.commit()

          # Exibir mensagem de sucesso
          messagebox.showinfo("Sucesso", "Pedido registrado com sucesso!")
      else:
          messagebox.showerror("Erro", "Produto não encontrado no cardápio.")
  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao registrar pedido: {str(e)}")
  finally:
      # Fechar a conexão com o banco de dados
      connection.close()

def exibirCardapio2():
  cardapio_nome, produtos = mostrarCardapio()

  if cardapio_nome is not None and produtos is not None:
      root = tk.Tk()
      root.title("Café Temptation")
      root.geometry('500x700')
      root.configure(background='light gray')

      # Título
      tk.Label(root, text=f'Cardápio: {cardapio_nome}', font=('arial', 14, 'bold'), background='light gray',
               foreground='midnight blue').pack()

      # Lista de produtos
      lista_produtos = Listbox(root, width=50, height=10)
      lista_produtos.pack(pady=10)

      for produto in produtos:
          lista_produtos.insert(END, f"Nome: {produto[0]}, Preço: {produto[1]}, Descrição: {produto[2]}")

      # Scrollbar
      scrollbar = Scrollbar(root)
      scrollbar.pack(side=RIGHT, fill=Y)
      lista_produtos.config(yscrollcommand=scrollbar.set)
      scrollbar.config(command=lista_produtos.yview)

      tk.Label(root, text='Nome do Cliente:', background='light gray', foreground='midnight blue').pack()
      nome = tk.Text(root, height=1, width=30)
      nome.pack()

      tk.Label(root, text='Método de pagamento:', background='light gray', foreground='midnight blue').pack()
      pagamento = tk.Text(root, height=1, width=30)
      pagamento.pack(pady=10)

      tk.Label(root, text='Produto desejado:', background='light gray', foreground='midnight blue').pack()
      produto = tk.Entry(root)
      produto.pack(pady=10)

      tk.Label(root, text='Quantidade de unidades:', background='light gray', foreground='midnight blue').pack()
      quantidade = tk.Text(root, height=1, width=30)
      quantidade.pack(pady=10)

      def realizarPedido():
          fazerPedido(produto.get(), quantidade.get("1.0", "end-1c"), nome.get("1.0", "end-1c"),
                      pagamento.get("1.0", "end-1c"))
          btnFechar['state'] = tk.NORMAL  # Habilitar o botão "Encerrar" após realizar o pedido

      btnEnviar = tk.Button(root, text='Realizar pedido', command=realizarPedido)
      btnEnviar.pack()

      # Obter o último cardápio registrado
      connection = sqlite3.connect("Cafeteria.db")
      cursor = connection.cursor()

      try:
          cursor.execute("SELECT id FROM Cliente ORDER BY ROWID DESC LIMIT 1;")
          result = cursor.fetchone()

          if result is not None:
              id_cliente = result[0]
          else:
              # Definir id_cliente como 0 por padrão se não houver nenhum cliente ainda
              id_cliente = 0

          # Incrementar o ID do cliente
          id_cliente += 1

          # Botão para fechar
          btnFechar = tk.Button(root, text='Encerrar', bg='#f3bf5f', state=tk.DISABLED,
                                  command=lambda: abrir_NF(root, str(id_cliente)))  # Nota Fiscal
          btnFechar.pack()

          # Executando
          root.mainloop()

      except sqlite3.Error as e:
          print(f"Erro ao obter ID do cliente: {str(e)}")
      finally:
          # Fechar a conexão com o banco de dados
          connection.close()

  else:
      print("Nenhum cardápio encontrado.")



def abrir_cardapio(root, cargo, login, senha):
  root.destroy()  # Fecha a janela atual
  caminho_registra_cardapio = os.path.join("paginas", "registra_cardapio.py")
  subprocess.run(["python", caminho_registra_cardapio, cargo, login, senha])

def registrarCardapio(titulo_entry, descricao_text):
    # Obter os valores inseridos nos campos de entrada
    titulo = titulo_entry.get()
    descricao = descricao_text.get("1.0", "end-1c")

    # Conectar ao banco de dados
    connection = sqlite3.connect("Cafeteria.db")
    cursor = connection.cursor()

    try:
        # Verificar se o título já existe na tabela Cardapio
        cursor.execute("SELECT COUNT(*) FROM Cardapio WHERE nome = ?;", (titulo,))
        existing_titles_count = cursor.fetchone()[0]

        if existing_titles_count == 0:
            # Inserir dados na tabela Cardapio
            cursor.execute("INSERT INTO Cardapio (nome, descricao) VALUES (?, ?);", (titulo, descricao))
            connection.commit()

            # Exibir mensagem de sucesso
            messagebox.showinfo("Sucesso", "Cardápio cadastrado com sucesso!")

            # Limpar campos após o cadastro
            titulo_entry.delete(0, 'end')
            descricao_text.delete("1.0", "end")
        else:
            # Exibir mensagem de erro se o título já existe
            messagebox.showerror("Erro", "Já existe um cardápio com esse título!")
    except sqlite3.Error as e:
        # Exibir mensagem de erro em caso de falha
        messagebox.showerror("Erro", f"Erro ao cadastrar cardápio: {str(e)}")

    # Fechar a conexão com o banco de dados
    connection.close()

def removerCardapio(nome_cardapio):
  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Verificar se o título existe na tabela Cardapio
      cursor.execute("SELECT COUNT(*) FROM Cardapio WHERE nome = ?;", (nome_cardapio,))
      existing_titles_count = cursor.fetchone()[0]

      if existing_titles_count > 0:
          # Remover dados da tabela Cardapio
          cursor.execute("DELETE FROM Cardapio WHERE nome = ?;", (nome_cardapio,))
          connection.commit()

          # Exibir mensagem de sucesso
          messagebox.showinfo("Sucesso", f"Cardápio '{nome_cardapio}' removido com sucesso!")
      else:
          # Exibir mensagem de erro se o título não existe
          messagebox.showerror("Erro", f"Não existe um cardápio com o título '{nome_cardapio}'!")
  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao remover cardápio: {str(e)}")

  # Fechar a conexão com o banco de dados
  connection.close()


def atualizarCardapio(titulo_atual, novo_titulo, nova_descricao):
  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Verificar se o título atual existe na tabela Cardapio
      cursor.execute("SELECT * FROM Cardapio WHERE nome = ?;", (titulo_atual,))
      existing_cardapio = cursor.fetchone()

      if existing_cardapio:
          # Atualizar dados na tabela Cardapio
          cursor.execute("UPDATE Cardapio SET nome = ?, descricao = ? WHERE nome = ?;",
                         (novo_titulo, nova_descricao, titulo_atual))
          connection.commit()

          # Exibir mensagem de sucesso
          messagebox.showinfo("Sucesso", f"Cardápio '{titulo_atual}' atualizado com sucesso!")
      else:
          # Exibir mensagem de erro se o título atual não existe
          messagebox.showerror("Erro", f"Não existe um cardápio com o título '{titulo_atual}'!")
  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao atualizar cardápio: {str(e)}")

  # Fechar a conexão com o banco de dados
  connection.close()