from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt5.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def _init_(self):
        
        super()._init_()
        self.setWindowTitle("Hello World!!!")
        self.setFixedSize(600,400)
        self.lbl = QLabel("Oiee mundo")
        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)
        
        
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()    