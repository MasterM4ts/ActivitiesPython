import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSpinBox, QVBoxLayout, QWidget

# Função chamada quando o valor do QSpinBox é alterado
def value_changed(value):
    label.setText(f"Valor selecionado: {value}")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Exemplo de QSpinBox")
window.setGeometry(100, 100, 300, 150)

layout = QVBoxLayout()  # Criação de um layout vertical

spin_box = QSpinBox()  # Criação do QSpinBox
spin_box.setMinimum(0)  # Define o valor mínimo
spin_box.setMaximum(100)  # Define o valor máximo
spin_box.setSingleStep(1)  # Define o incremento/decremento em 1
#spin_box.setPrefix('R$')
#spin_box.setSuffix(' kg')

spin_box.valueChanged.connect(value_changed)  # Conecta o sinal 'valueChanged' à função 'value_changed'

label = QLabel("Valor selecionado: 0")  # Criação de um QLabel inicializado com um texto

layout.addWidget(spin_box)  # Adiciona o QSpinBox ao layout
layout.addWidget(label)  # Adiciona o QLabel ao layout

container = QWidget()  # Criação de um widget para conter o layout
container.setLayout(layout)  # Define o layout para o widget container
window.setCentralWidget(container)  # Define o widget container como o conteúdo central da janela

window.show()  # Exibe a janela

sys.exit(app.exec_())  # Inicia o loop de eventos da aplicação
