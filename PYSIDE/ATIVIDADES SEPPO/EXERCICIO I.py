from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Exercicio I!!")
        self.setFixedSize(600,400)
        self.lbl = QLabel("Hello World")
        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()    