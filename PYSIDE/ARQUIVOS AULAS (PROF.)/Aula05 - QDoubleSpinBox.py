import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDoubleSpinBox, QVBoxLayout, QWidget

def value_changed(value):
    label.setText(f"Valor selecionado: {value:.2f}")  # Exibe o valor com duas casas decimais

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Exemplo de QDoubleSpinBox")
window.setGeometry(100, 100, 300, 150)

layout = QVBoxLayout()

double_spin_box = QDoubleSpinBox()  # Criação do QDoubleSpinBox
double_spin_box.setMinimum(0.0)  # Valor mínimo
double_spin_box.setMaximum(100.0)  # Valor máximo
double_spin_box.setSingleStep(0.1)  # Incremento/decremento de 0.1
double_spin_box.setDecimals(2)  # Define duas casas decimais

double_spin_box.textChanged.connect(value_changed)
double_spin_box.valueChanged.connect(value_changed)

label = QLabel("Valor selecionado: 0.00")

layout.addWidget(double_spin_box)
layout.addWidget(label)

container = QWidget()
container.setLayout(layout)
window.setCentralWidget(container)

window.show()

sys.exit(app.exec_())
