# Importando as classes necessárias do módulo PySide6 para criação de interfaces gráficas
from PySide6.QtWidgets import QApplication, QWidget
# Importando o módulo 'sys' para interagir com funcionalidades do sistema
import sys

# Inicializando a aplicação
app = QApplication(sys.argv)

# Criando uma instância da classe 'QWidget' para representar a janela
janela = QWidget()

# Exibindo a janela (tornando-a visível para o usuário)
janela.show()
import site

packages = site.getsitepackages()
print(packages)

# Iniciando o loop de eventos da aplicação, onde a aplicação permanece ativa e responsiva
app.exec()
