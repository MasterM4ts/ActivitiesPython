# Importando o módulo 'sys' para interagir com funcionalidades do sistema
import sys
# Importando as classes necessárias do módulo PySide6 para criação de interfaces gráficas
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap

# Definindo a classe da janela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicialização da classe pai (QMainWindow)
        
        self.setWindowTitle("Image")  # Definindo o título da janela
        
        # Criando um rótulo QLabel e configurando-o com uma imagem
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap("chess.gif"))  # Configurando a imagem no rótulo
        self.lbl.setScaledContents(True)  # Redimensionamento da imagem para preencher o rótulo
        
        self.setCentralWidget(self.lbl)  # Definindo o rótulo como widget central da janela

# Inicializando a aplicação
app = QApplication(sys.argv)
# Criando uma instância da classe MainWindow
window = MainWindow()
# Exibindo a janela principal
window.show()
# Iniciando o loop de eventos da aplicação
app.exec()
