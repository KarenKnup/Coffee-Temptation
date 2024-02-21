import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcoes.funcionario import prepararPedidos

# Chamando a função para exibir pedidos pendentes
prepararPedidos()
