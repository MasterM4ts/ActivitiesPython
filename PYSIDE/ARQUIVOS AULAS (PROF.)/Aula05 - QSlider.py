import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget
from PySide6.QtCore import  Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowTitle("Exemplo de QSlider")
        self.setGeometry(100, 100, 300, 200)

        # Cria um layout vertical
        layout = QVBoxLayout()

        # Cria um slider horizontal (QSlider)
        self.slider = QSlider()

        # Configura o slider para ajustar valores inteiros dentro do intervalo de 0 a 100
        self.slider.setOrientation(Qt.Horizontal)  # Define a orientação horizontal
        self.slider.setMinimum(0)  # Valor mínimo
        self.slider.setMaximum(100)  # Valor máximo

        # Adiciona o slider ao layout
        layout.addWidget(self.slider)

        # Cria um widget para conter o layout e define-o como o widget central da janela
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        # Conecta o sinal de alteração de valor do slider a um método
        self.slider.valueChanged.connect(self.slider_value_changed)

    # Método chamado quando o valor do slider é alterado
    def slider_value_changed(self, value):
        print("Valor selecionado:", value)

# Cria uma instância da aplicação
app = QApplication(sys.argv)

# Cria uma instância da janela personalizada
window = MyWindow()

# Exibe a janela
window.show()

# Inicia o loop de eventos da aplicação
sys.exit(app.exec_())
