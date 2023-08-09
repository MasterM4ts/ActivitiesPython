import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit, QHBoxLayout, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.tela_principal()
    
    
    def tela_principal(self):
        self.setWindowTitle("Tela Principal")
        self.setGeometry(100, 100, 300, 200)
        
        
        layout = QVBoxLayout()
        self.label_text = QLabel("Escolha o Tipo de Cálculo:")
        layout.addWidget(self.label_text) 
        
        
        self.retangulo_button = QPushButton("Área do Retângulo")
        self.retangulo_button.clicked.connect(self.calculo_retangulo)
        
        
        self.circulo_button = QPushButton("Área do Círculo")
        self.circulo_button.clicked.connect(self.calculo_circulo)
        
        
        layout.addWidget(self.retangulo_button)
        layout.addWidget(self.circulo_button)
        
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)