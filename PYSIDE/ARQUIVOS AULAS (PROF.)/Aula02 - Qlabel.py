# Importando o módulo 'sys' para interagir com funcionalidades do sistema
import sys
# Importando as classes necessárias do módulo PySide6 para criação de interfaces gráficas
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# Definindo a classe da janela principal
class MainWindown(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicialização da classe pai (QMainWindow)

        self.setWindowTitle("Meu programa")  # Definindo o título da janela
        self.setFixedSize(QSize(600, 400))  # Definindo o tamanho fixo da janela

        # Criando um rótulo QLabel com texto e configurações de fonte e alinhamento
        self.lbl = QLabel("Meu primeiro programa")
        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(self.lbl)  # Definindo o rótulo como widget central da janela

# Inicializando a aplicação
app = QApplication(sys.argv)
# Criando uma instância da classe MainWindown
w = MainWindown()
# Exibindo a janela principal
w.show()
# Iniciando o loop de eventos da aplicação
app.exec()
