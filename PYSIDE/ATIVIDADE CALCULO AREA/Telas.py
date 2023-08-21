import sys
from Retangulo import*
from Circulo import*
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QTextBrowser


class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Principal")
        self.setFixedSize(190, 150)

        
        layout = QVBoxLayout()


        self.label_text = QLabel("Escolha Qual Calculo Deseja Efetuar")
        layout.addWidget(self.label_text)
        
        
        botao_tela_retang = QPushButton("Calcular Área Retângulo")
        botao_tela_retang.clicked.connect(self.ir_tela_retangulo)
        layout.addWidget(botao_tela_retang)

        
        botao_tela_circ = QPushButton("Calcular Área Círculo")
        botao_tela_circ.clicked.connect(self.ir_tela_circulo)
        layout.addWidget(botao_tela_circ)

    
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def ir_tela_retangulo(self):
        self.tela1 = Tela_Retangulo()
        self.tela1.show()


    def ir_tela_circulo(self):
        self.tela2 = Tela_Circulo()
        self.tela2.show()


class Tela_Retangulo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Retângulo")
        self.setFixedSize(500, 350)
        
        layout = QVBoxLayout()
        
        
        self.label_base = QLabel("Base:")
        self.input_base = QLineEdit(self)
        layout.addWidget(self.label_base)
        layout.addWidget(self.input_base)
        
        
        self.label_altura = QLabel("Altura:")
        self.input_altura = QLineEdit(self)
        layout.addWidget(self.label_altura)
        layout.addWidget(self.input_altura)
        
        
        self.label_cor = QLabel("Cor:")
        self.input_cor = QLineEdit(self)
        layout.addWidget(self.label_cor)
        layout.addWidget(self.input_cor)
        
        
        self.button_calcular = QPushButton("Calcular", self)
        self.button_calcular.clicked.connect(self.calcular_area)
        layout.addWidget(self.button_calcular)
        
        
        self.result_display = QTextBrowser()
        layout.addWidget(self.result_display)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    
    def calcular_area(self):
        base = float(self.input_base.text())
        altura = float(self.input_altura.text())
        color = self.input_cor.text()
        
        shape = Retangulo(base, altura, color)
        area = shape.calcular_area()
        self.result_display.append(f"Área Calculada do Retângulo ({color}): {area}")
        
        
class Tela_Circulo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Círculo")
        self.setFixedSize(500, 350)
        
        layout = QVBoxLayout()
        
        
        self.label_raio = QLabel("Raio:")
        self.input_raio = QLineEdit(self)
        layout.addWidget(self.label_raio)
        layout.addWidget(self.input_raio)
        
        
        self.label_cor = QLabel("Cor:")
        self.input_cor = QLineEdit(self)
        layout.addWidget(self.label_cor)
        layout.addWidget(self.input_cor)
        
        
        self.button_calcular = QPushButton("Calcular", self)
        self.button_calcular.clicked.connect(self.calcular_area)
        layout.addWidget(self.button_calcular)
        
        
        self.result_display = QTextBrowser()
        layout.addWidget(self.result_display)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    
    def calcular_area(self):
        raio = float(self.input_base.text())
        color = self.input_cor.text()
        
        shape = Circulo(raio, color)
        area = shape.calcular_area()
        self.result_display.append(f"Área Calculada do Círculo ({color}): {area}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_principal = TelaPrincipal()
    tela_principal.show()
    sys.exit(app.exec_())