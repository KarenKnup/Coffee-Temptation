import sqlite3

def criar_tabelas():
  # Conectar ao banco de dados (ou criar se não existir)
  connection = sqlite3.connect("Cafeteria.db")
  cursor = connection.cursor()

  cursor.execute("CREATE TABLE IF NOT EXISTS Funcionarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cargo TEXT, salario TEXT, login TEXT, senha TEXT);") #FEITO

  cursor.execute("CREATE TABLE IF NOT EXISTS Cliente(nome TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT, metodoPagamento TEXT);")

  cursor.execute("CREATE TABLE IF NOT EXISTS Pedido(id INTEGER PRIMARY KEY AUTOINCREMENT, dataHora DATETIME, status TEXT, produto TEXT, quantidade INTEGER, cardapio TEXT, cliente INTEGER, FOREIGN KEY (produto) REFERENCES Produto(nome), FOREIGN KEY (cardapio) REFERENCES Cardapio(nome), FOREIGN KEY (cliente) REFERENCES Cliente(id));")#FEITO

  cursor.execute("CREATE TABLE IF NOT EXISTS Cardapio(nome TEXT PRIMARY KEY, descricao TEXT);") #FEITO

  cursor.execute("CREATE TABLE IF NOT EXISTS Produto(nome TEXT PRIMARY KEY, preco FLOAT, descricao TEXT, nomeCardapio TEXT, FOREIGN KEY (nomeCardapio) REFERENCES Cardapio(nome));") #FEITO

  cursor.execute("CREATE TABLE IF NOT EXISTS ItemPedido(id INTEGER PRIMARY KEY AUTOINCREMENT, nomeProduto TEXT, nomeCardapio TEXT, precoUnit FLOAT, FOREIGN KEY (nomeProduto) REFERENCES Produto(nome), FOREIGN KEY (nomeCardapio) REFERENCES Cardapio(nome));")#FEITO

  #Teste do Banco de Dados:
  #cursor_object = connection.execute("SELECT * FROM Cliente")
  #print(cursor_object.fetchall())

  # Verificar se a tabela está vazia
  cursor.execute("SELECT COUNT(*) FROM Funcionarios;")
  num_registros = cursor.fetchone()[0]

  # Se a tabela estiver vazia, execute o INSERT
  if num_registros == 0:
      exemplo_insert = "INSERT INTO Funcionarios (nome, cargo, salario,login,senha) VALUES (?, ?, ?, ?, ?);"
      dados_funcionario = ("Admin", "Administrador", "0.0", "admin", "admin123")

      # Executar o INSERT
      cursor.execute(exemplo_insert, dados_funcionario)

      # Commit para salvar as alterações
      connection.commit()

  # Fechar a conexão
  connection.close()