import sys
import os

# Adiciona o caminho do diretório pai ao PythonPath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcoes.cardapio_atual import exibirCardapio

exibirCardapio()

