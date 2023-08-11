import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit, QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.inicio()
        
        
    def inicio(self):
        self.setWindowTitle("Cadastro")
        
        
        self.button = QPushButton("Concluido")
        self.check_masculino = QCheckBox("Masculino")
        self.check_feminino = QCheckBox("Feminino")
        
        
        self.label_nome = QLabel("Nome:", self)
        self.label_nome.setGeometry(10, 10, 100, 20)
        self.label_fone = QLabel("Telefone:", self)
        self.label_fone.setGeometry(10, 40, 100, 20)
        self.label_endereco = QLabel("Endereço:", self)
        self.label_endereco.setGeometry(10, 70, 100, 20)
        self.label_sexo = QLabel("Sexo:", self)
        self.label_sexo.setGeometry(10,100,100,20)
        
        
        self.input_nome = QLineEdit(self)
        self.input_nome.setGeometry(70, 10, 500, 20)
        self.input_fone = QLineEdit(self)
        self.input_fone.setGeometry(70, 40, 500, 20)
        self.input_endereco = QLineEdit(self)
        self.input_endereco.setGeometry(70, 70, 500, 20)
        
        
        layout = QVBoxLayout()
        h = QHBoxLayout()
        layout.addSpacing(120)
        h.addWidget(self.check_masculino)
        h.addWidget(self.check_feminino)
        layout.addLayout(h)
        layout.addSpacing(500)
        layout.addWidget(self.button)
        
        
        self.setLayout(layout)
        self.check_masculino.stateChanged.connect(self.check_homem)
        self.check_feminino.stateChanged.connect(self.check_mulher)
        self.button.clicked.connect(self.concluir)
    
    
    def check_homem(self,c):
        if c == self.check_masculino.setChecked:
            self.check_feminino.setChecked(True)
            
            
        else:
            self.check_feminino.setChecked(False)
            self.sexo = "Masculino"
         
            
    def check_mulher(self,c):
        if c == self.check_feminino.setChecked:
            self.check_masculino.setChecked(True)
            
            
        else:
            self.check_masculino.setChecked(False)
            self.sexo = "Feminino"
            
    
    def concluir(self):
        self.nome = self.input_nome.text()
        self.fone = self.input_fone.text()
        self.endereco = self.input_endereco.text()
        
        
        info = QHBoxLayout()
        try:
            self.label_info = QLabel(f"Informações\nNome: {self.nome}\nSexo: {self.sexo}\nTelefone: {self.fone}\nEndereço: {self.endereco}")
        
        
        except:
            self.sexo = "INDEFINIDO"
            self.label_info = QLabel(f"Informações\nNome: {self.nome}\nSexo: {self.sexo}\nTelefone: {self.fone}\nEndereço: {self.endereco}")
            
            
        self.image_label = QLabel(self)
        
        
        if self.sexo == "Masculino":
            self.image_label.setPixmap(QPixmap("PYSIDE/ATIVIDADE CADASTRO/M.png"))
        
        
        else:
            self.image_label.setPixmap(QPixmap("PYSIDE/ATIVIDADE CADASTRO/F.png"))
        
        
        self.label_info.setAlignment(Qt.AlignCenter)
        
        
        info.addWidget(self.image_label)
        info.addWidget(self.label_info)
        
        
        self.tela_info = QWidget()
        self.tela_info.setWindowTitle("Informações do Usuário")
        self.tela_info.setLayout(info)
        self.tela_info.setFixedSize(400, 300)
        self.tela_info.show()    
           
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()  