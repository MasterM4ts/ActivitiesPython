from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Imagem")
        self.label = QLabel()
        self.label.setPixmap(QPixmap("PYSIDE/QPIXMAP/imagem.jpg"))
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)
        
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()   