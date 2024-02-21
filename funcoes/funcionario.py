from tkinter import *
from tkinter import messagebox
import subprocess
import sqlite3
import os
from datetime import datetime
import tkinter as tk
import sys


def abrir_tela_funcionario(root, cargo, usuario, senha):
    root.destroy()  # Fecha a janela de login
    caminho_funcionario = os.path.join("paginas", "funcionario.py")
    subprocess.run(["python", caminho_funcionario, cargo, usuario, senha])
    return

def fazer_login(vlogin, vsenha, root):
    usuario = vlogin.get()
    senha = vsenha.get()

    # Conectar ao banco de dados
    connection = sqlite3.connect("Cafeteria.db")
    cursor = connection.cursor()

    # Consultar o banco de dados para encontrar o usuário e senha correspondentes
    cursor.execute("SELECT login, senha, cargo FROM Funcionarios;")
    resultados = cursor.fetchall()

    for resultado in resultados:
        login_salvo, senha_salva, cargo_salvo = resultado

        if usuario == login_salvo and senha == senha_salva:
            #messagebox.showinfo("Login", "Login bem-sucedido!")
            abrir_tela_funcionario(root, cargo_salvo, usuario, senha)  
            return  # Importante: encerrar a função aqui para evitar o retorno abaixo

    # Fechar a conexão
    connection.close()

    messagebox.showerror("Erro de Login", "Credenciais inválidas")

def fazer_login2(vlogin, vsenha, root):#usado para retornar para a tela de funcionario.py
  usuario = vlogin
  senha = vsenha

  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  # Consultar o banco de dados para encontrar o usuário e senha correspondentes
  cursor.execute("SELECT login, senha, cargo FROM Funcionarios;")
  resultados = cursor.fetchall()

  for resultado in resultados:
      login_salvo, senha_salva, cargo_salvo = resultado

      if usuario == login_salvo and senha == senha_salva:
          abrir_tela_funcionario(root, cargo_salvo, usuario, senha)  
          return  # Importante: encerrar a função aqui para evitar o retorno abaixo

  # Fechar a conexão
  connection.close()

  messagebox.showerror("Erro de Login", "Credenciais inválidas")

def abrir_registrar_funcionario(root):
  root.destroy()  # Fecha a janela de login
  caminho_registra_funcionario = os.path.join("paginas", "registra_funcionario.py")
  subprocess.run(["python", caminho_registra_funcionario])

# Função para voltar para o login.py
def voltar_para_login(root):
    root.destroy()  # Fechar a janela atual após redirecionar
    os.system("python paginas/login.py")


def abrir_pedido(root, cargo, login, senha):
  root.destroy()  # Fecha a janela atual
  caminho_registra_pedido = os.path.join("paginas", "registra_pedido.py")
  subprocess.run(["python", caminho_registra_pedido, cargo, login, senha])

def abrir_U_pedido(root, cargo, login, senha):
  root.destroy()  # Fecha a janela atual
  caminho_altera_pedido = os.path.join("paginas", "altera_pedido.py")
  subprocess.run(["python", caminho_altera_pedido, cargo, login, senha])

def abrir_D_pedido(root, cargo, login, senha):
  root.destroy()  # Fecha a janela atual
  caminho_deleta_pedido = os.path.join("paginas", "deleta_pedido.py")
  subprocess.run(["python", caminho_deleta_pedido, cargo, login, senha])

def fazerPedido(produto_entry, quantidade_text, cliente_text, pagamento_text):
    # Obter os valores inseridos nos campos de entrada
    produto = produto_entry.get()
    quantidade = quantidade_text.get("1.0", "end-1c")
    cliente = cliente_text.get("1.0", "end-1c")
    pagamento = pagamento_text.get("1.0", "end-1c")

    # Conectar ao banco de dados
    connection = sqlite3.connect("Cafeteria.db")
    cursor = connection.cursor()

    try:
        # Obter o último cardápio registrado
        cursor.execute("SELECT nome FROM Cardapio ORDER BY ROWID DESC LIMIT 1;")
        cardapio_atual = cursor.fetchone()[0]
        connection.commit()

        # Verificar se o produto existe na tabela Produto
        cursor.execute("SELECT preco FROM Produto WHERE nome = ? AND nomeCardapio = ?;", (produto, cardapio_atual))
        result = cursor.fetchone()

        if result is not None:
            preco_unitario = result[0]

            # Inserir dados na tabela Cliente
            cursor.execute("INSERT INTO Cliente (nome, metodoPagamento) VALUES (?, ?);", (cliente, pagamento))
            connection.commit()

            # Obter o ID do cliente recém-inserido
            cursor.execute("SELECT id FROM Cliente ORDER BY ROWID DESC LIMIT 1;")
            id_cliente = cursor.fetchone()[0]

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



def alteraPedido(id_pedido, produto, quantidade, cliente, pagamento):

  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Obter o último cardápio registrado
      cursor.execute("SELECT nome FROM Cardapio ORDER BY ROWID DESC LIMIT 1;")
      cardapio_atual = cursor.fetchone()[0]

      # Obter o ID do cliente
      cursor.execute("SELECT cliente FROM Pedido WHERE id = ?;", (id_pedido,))
      result = cursor.fetchone()

      if result is not None:
          id_cliente = result[0]

          # Atualizar dados na tabela Cliente
          cursor.execute("UPDATE Cliente SET nome=?, metodoPagamento=? WHERE id=?;", (cliente, pagamento, id_cliente))
          connection.commit()

          # Obter o preço unitário do produto da tabela Produto
          cursor.execute("SELECT preco FROM Produto WHERE nome = ? AND nomeCardapio = ?;", (produto, cardapio_atual))
          result = cursor.fetchone()

          if result is not None:
              preco_unitario = result[0]
              connection.commit()

              # Atualizar dados na tabela Pedido
              data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              cursor.execute("UPDATE Pedido SET dataHora=?, status=?, produto=?, quantidade=?, cardapio=?, cliente=? WHERE id=?;",
                             (data_hora, "PENDENTE", produto, quantidade, cardapio_atual, id_cliente, id_pedido))
              connection.commit()

              # Atualizar dados na tabela ItemPedido
              cursor.execute("UPDATE ItemPedido SET nomeProduto=?, nomeCardapio=?, precoUnit=? WHERE id=?;",
                             (produto, cardapio_atual, preco_unitario, id_pedido))
              connection.commit()

              # Exibir mensagem de sucesso
              messagebox.showinfo("Sucesso", "Pedido alterado com sucesso!")
          else:
              messagebox.showerror("Erro", "Produto não encontrado no cardápio.")
      else:
          messagebox.showerror("Erro", "Cliente não encontrado.")
  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao alterar pedido: {str(e)}")
  finally:
      # Fechar a conexão com o banco de dados
      connection.close()


def cancelarPedido(id_pedido):
  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Verificar se o pedido com o ID fornecido existe
      cursor.execute("SELECT * FROM Pedido WHERE id = ?;", (id_pedido,))
      result = cursor.fetchone()

      if result is not None:
          # Obter o ID do cliente associado ao pedido
          id_cliente = result[6]  # Assuming the index 6 corresponds to the 'cliente' column

          # Remover dados da tabela ItemPedido
          cursor.execute("DELETE FROM ItemPedido WHERE id = ?;", (id_pedido,))
          connection.commit()

          # Remover dados da tabela Pedido
          cursor.execute("DELETE FROM Pedido WHERE id = ?;", (id_pedido,))
          connection.commit()

          # Remover dados da tabela Cliente
          cursor.execute("DELETE FROM Cliente WHERE id = ?;", (id_cliente,))
          connection.commit()

          # Exibir mensagem de sucesso
          messagebox.showinfo("Sucesso", "Pedido cancelado com sucesso!")
      else:
          messagebox.showerror("Erro", "Pedido não encontrado.")
  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao cancelar pedido: {str(e)}")
  finally:
      # Fechar a conexão com o banco de dados
      connection.close()


def cancelarPedido2(id_pedido):
  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Verificar se o pedido com o ID fornecido existe
      cursor.execute("SELECT * FROM Pedido WHERE id = ?;", (id_pedido,))
      result = cursor.fetchone()

      if result is not None:
          # Obter o ID do cliente associado ao pedido
          id_cliente = result[6]  # Assuming the index 6 corresponds to the 'cliente' column

          # Remover dados da tabela ItemPedido
          cursor.execute("DELETE FROM ItemPedido WHERE id = ?;", (id_pedido,))
          connection.commit()

          # Remover dados da tabela Pedido
          cursor.execute("DELETE FROM Pedido WHERE id = ?;", (id_pedido,))
          connection.commit()

          # Remover dados da tabela Cliente
          cursor.execute("DELETE FROM Cliente WHERE id = ?;", (id_cliente,))
          connection.commit()

  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao cancelar pedido: {str(e)}")
  finally:
      # Fechar a conexão com o banco de dados
      connection.close()

def abrir_produto(root, cargo, login, senha):
  root.destroy()  # Fecha a janela atual
  caminho_registra_produto = os.path.join("paginas", "registra_produto.py")
  subprocess.run(["python", caminho_registra_produto, cargo, login, senha])

def registrarProduto(cardapio_entry, nome_text, descricao_text, preco_text):
  # Obter os valores inseridos nos campos de entrada
  cardapio = cardapio_entry.get()
  nome = nome_text.get("1.0", "end-1c")
  descricao = descricao_text.get("1.0", "end-1c")
  preco = float(preco_text.get("1.0", "end-1c"))

  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Verificar se o cardápio existe na tabela Cardapio
      cursor.execute("SELECT COUNT(*) FROM Cardapio WHERE nome = ?;", (cardapio,))
      cardapio_exists = cursor.fetchone()[0]

      if cardapio_exists > 0:
          # Inserir dados na tabela Produto
          cursor.execute("INSERT INTO Produto (nome, descricao, preco, nomeCardapio) VALUES (?, ?, ?, ?);", (nome, descricao, preco, cardapio))
          connection.commit()

          # Exibir mensagem de sucesso
          messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
      else:
          # Exibir mensagem de erro se o cardápio não existe
          messagebox.showerror("Erro", "O cardápio especificado não existe!")
  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao cadastrar produto: {str(e)}")
  finally:
      # Fechar a conexão com o banco de dados
      connection.close()

def alterarProduto(cardapio_entry, nome_text, novo_nome_text, descricao_text, preco_text):
  # Obter os valores inseridos nos campos de entrada
  cardapio = cardapio_entry.get()
  nome = nome_text.get("1.0", "end-1c")
  novo_nome = novo_nome_text.get("1.0", "end-1c")
  descricao = descricao_text.get("1.0", "end-1c")
  preco = float(preco_text.get("1.0", "end-1c"))

  # Conectar ao banco de dados
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Verificar se o cardápio existe na tabela Cardapio
      cursor.execute("SELECT COUNT(*) FROM Cardapio WHERE nome = ?;", (cardapio,))
      cardapio_exists = cursor.fetchone()[0]

      if cardapio_exists > 0:
          # Verificar se o produto existe na tabela Produto
          cursor.execute("SELECT COUNT(*) FROM Produto WHERE nome = ? AND nomeCardapio = ?;", (nome, cardapio))
          produto_exists = cursor.fetchone()[0]

          if produto_exists > 0:
              # Atualizar dados na tabela Produto
              cursor.execute("UPDATE Produto SET nome = ?, descricao = ?, preco = ? WHERE nome = ? AND nomeCardapio = ?;",
                             (novo_nome, descricao, preco, nome, cardapio))
              connection.commit()

              # Exibir mensagem de sucesso
              messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")
          else:
              # Exibir mensagem de erro se o produto não existe
              messagebox.showerror("Erro", "O produto especificado não existe no cardápio!")
      else:
          # Exibir mensagem de erro se o cardápio não existe
          messagebox.showerror("Erro", "O cardápio especificado não existe!")
  except sqlite3.Error as e:
      # Exibir mensagem de erro em caso de falha
      messagebox.showerror("Erro", f"Erro ao alterar produto: {str(e)}")
  finally:
      # Fechar a conexão com o banco de dados
      connection.close()


def removerProduto(cardapio_entry, nome_text):
  # Get values from input fields
  cardapio = cardapio_entry.get()
  nome_produto = nome_text.get("1.0", "end-1c")

  # Connect to the database
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  try:
      # Check if the cardapio exists in the Cardapio table
      cursor.execute("SELECT COUNT(*) FROM Cardapio WHERE nome = ?;", (cardapio,))
      cardapio_exists = cursor.fetchone()[0]

      if cardapio_exists > 0:
          # Check if the product exists in the Produto table for the given cardapio
          cursor.execute("SELECT COUNT(*) FROM Produto WHERE nome = ? AND nomeCardapio = ?;", (nome_produto, cardapio))
          produto_exists = cursor.fetchone()[0]

          if produto_exists > 0:
              # Delete the product from the Produto table
              cursor.execute("DELETE FROM Produto WHERE nome = ? AND nomeCardapio = ?;", (nome_produto, cardapio))
              connection.commit()

              # Show success message
              messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
          else:
              # Show error if the product doesn't exist
              messagebox.showerror("Erro", "O produto especificado não existe no cardápio!")
      else:
          # Show error if the cardapio doesn't exist
          messagebox.showerror("Erro", "O cardápio especificado não existe!")
  except sqlite3.Error as e:
      # Show error in case of failure
      messagebox.showerror("Erro", f"Erro ao remover produto: {str(e)}")
  finally:
      # Close the database connection
      connection.close()


def abrir_preparar(root, cargo, login, senha):
  root.destroy()  # Fecha a janela atual
  caminho_preparar = os.path.join("paginas", "preparar.py")
  subprocess.run(["python", caminho_preparar, cargo, login, senha])

def mostrarPedidosPendentes(lista_pedidos):
    # Conectar ao banco de dados
    connection = sqlite3.connect("Cafeteria.db")
    cursor = connection.cursor()

    try:
        # Obter pedidos com status PENDENTE
        cursor.execute("SELECT id, produto, quantidade, cliente FROM Pedido WHERE status = 'PENDENTE';")
        pedidos_pendentes = cursor.fetchall()

        # Limpar a lista atual
        lista_pedidos.delete(0, END)

        if pedidos_pendentes:
            for pedido in pedidos_pendentes:
                lista_pedidos.insert(END, f"ID: {pedido[0]}, Produto: {pedido[1]}, Quantidade: {pedido[2]}, Cliente: {pedido[3]}")

    except sqlite3.Error as e:
        # Exibir mensagem de erro em caso de falha
        print(f"Erro ao mostrar pedidos pendentes: {str(e)}")
    finally:
        # Fechar a conexão com o banco de dados
        connection.close()

    # Atualizar novamente após 5000 milissegundos (5 segundos)
    lista_pedidos.after(5000, lambda: mostrarPedidosPendentes(lista_pedidos))

def prepararPedidos():
    from funcoes.funcionario import fazer_login2
    root = tk.Tk()
    root.title("Café Temptation")
    root.geometry('500x400')

    cargo = sys.argv[1]
    login = sys.argv[2]
    senha = sys.argv[3]
    root.configure(background='light gray')

    # Título
    tk.Label(root, text='Pedidos Pendentes', font=('arial', 14, 'bold'), background='light gray', foreground='midnight blue').pack()

    # Lista de pedidos
    lista_pedidos = Listbox(root, width=50, height=10)
    lista_pedidos.pack(pady=10)

    # Preencher a lista com pedidos pendentes
    mostrarPedidosPendentes(lista_pedidos)

    def cancelarPedidoSelecionado():
        # Obter o índice do item selecionado
        selected_index = lista_pedidos.curselection()

        if selected_index:
            # Obter o ID do pedido a partir do texto do item selecionado
            pedido_id = lista_pedidos.get(selected_index[0]).split(":")[1].split(",")[0].strip()

            # Chamar a função para cancelar o pedido
            cancelarPedido2(pedido_id)

            # Atualizar a lista de pedidos
            mostrarPedidosPendentes(lista_pedidos)

    # Botão "OK"
    btnOK = tk.Button(root, text='OK', command=cancelarPedidoSelecionado)
    btnOK.pack()

    # Botão para fechar
    btnFechar = tk.Button(root, text='Voltar', command=lambda: fazer_login2(login, senha, root))
    btnFechar.pack()

    # Executando
    root.mainloop()


def gravar_funcionario(vlogin_admin, vsenha_admin, vlogin, vsenha, vnome, vcargo, vsalario):
    # Verifica se algum campo está vazio
    if not vlogin_admin.get() or not vsenha_admin.get() or not vlogin.get() or not vsenha.get() or not vcargo.get() or not vsalario.get() or not vnome.get():
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    # Conectar ao banco de dados
    connection = sqlite3.connect("Cafeteria.db")
    cursor = connection.cursor()

    # Verifica se as credenciais do administrador estão corretas
    cursor.execute("SELECT login, senha, cargo FROM Funcionarios WHERE cargo = 'Administrador';")

    admin_credentials = None

    # Itera sobre os resultados e verifica se há uma correspondência com as credenciais fornecidas
    for row in cursor.fetchall():
        if vlogin_admin.get() == row[0] and vsenha_admin.get() == row[1]:
            admin_credentials = row
            break

    if admin_credentials:
        # Verifica se o cargo é 'Administrador'
        if admin_credentials[2] == 'Administrador':
            # Verifica se o login já existe no banco de dados
            cursor.execute("SELECT COUNT(*) FROM Funcionarios WHERE login = ?;", (vlogin.get(),))
            existing_login_count = cursor.fetchone()[0]

            if existing_login_count == 0:
                try:
                    insert = "INSERT INTO Funcionarios(nome, cargo, salario, login, senha) VALUES (?, ?, ?, ?, ?);"
                    dados = (vnome.get(), vcargo.get(), vsalario.get(), vlogin.get(), vsenha.get())
                    cursor.execute(insert, dados)
                    connection.commit()
                    messagebox.showinfo("MENSAGEM IMPORTANTE", "Informações gravadas com sucesso!")

                    # Limpa os campos de entrada
                    vlogin.delete(0, tk.END)
                    vsenha.delete(0, tk.END)
                    vnome.delete(0, tk.END)
                    vcargo.delete(0, tk.END)
                    vsalario.delete(0, tk.END)
                    vlogin.focus()
                except sqlite3.Error as e:
                    messagebox.showerror("Erro", f"Erro ao inserir no banco de dados: {str(e)}")
            else:
                # Se o login já existe, exibe uma mensagem de erro
                messagebox.showerror("Erro", "Já existe um funcionário com esse login!")
        else:
            # Se o cargo não for 'Administrador', exibe uma mensagem de erro
            messagebox.showerror("Erro", "Apenas administradores podem cadastrar outros administradores!")
    else:
        # Se as credenciais do administrador estiverem incorretas, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Credenciais do administrador incorretas!")

    # Fecha a conexão com o banco de dados
    connection.close()

