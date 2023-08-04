import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QCheckBox, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.inicio()
        
        
    def inicio(self):
        self.setWindowTitle("INFORMAÇÔES DO USUÁRIO")
        
        
        self.label_nome = QLabel("Nome:", self)
        self.label_nome.setGeometry(26, 10, 450, 25)
        self.input_nome = QLineEdit(self)
        self.input_nome.setGeometry(100, 10, 450, 25)
        
        
        self.label_fone= QLabel("Telefone:", self)
        self.label_fone.setGeometry(12, 50, 450, 25)
        self.input_fone = QLineEdit(self)
        self.input_fone.setGeometry(100, 50, 450, 25)
        
        
        self.label_ender= QLabel("Endereço:", self)
        self.label_ender.setGeometry(10, 90, 450, 25)
        self.input_ender = QLineEdit(self)
        self.input_ender.setGeometry(100, 90, 450, 25)
        
        
        self.label_sexo = QLabel("Sexo:", self)
        self.label_sexo.setGeometry(30, 130, 80, 25)
        self.ck_masculino = QCheckBox("Masculino")
        self.ck_feminino = QCheckBox("Feminino")
        
        
        self.button = QPushButton("Cadastrar", self)
        self.button.setGeometry(500, 750, 550, 30)
        self.button.clicked.connect(self.state)   
        
        
    def state(self, m):
        if m == 2:
            self.label_sexo.setText("")
        
        
        else:
            self.label_sexo.setText("") 
                         
        
app = QApplication(sys.argv)
m = MainWindow()
m.show()
app.exec()  