from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt5.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Exercicio 2!!!")
        
        self.button= QPushButton(" Botão",self)
        self.button.setGeometry(190,10,100,70)
        self.result_label=QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        
        self.button.clicked.connect(self.imprimir)
     
    def imprimir(self):
        numero = 1
        if numero % 2==0:
            self.result_label.setText(f"Este número {numero} é Par")    
            
        else:
             self.result_label.setText(f"Este número {numero} é Impar")
     
                                       
app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()    