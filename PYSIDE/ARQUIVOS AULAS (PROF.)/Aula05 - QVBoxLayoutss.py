import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

def button_clicked():
    print("Botão clicado!")

app = QApplication(sys.argv)

# Cria a janela principal
window = QMainWindow()
window.setWindowTitle("Exemplo de QVBoxLayout")

# Cria um widget central para a janela
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Cria um layout vertical
layout = QVBoxLayout()
central_widget.setLayout(layout)


# Cria dois botões e os adiciona ao layout
button1 = QPushButton("Botão 1")
button1.clicked.connect(button_clicked)
layout.addWidget(button1)


button2 = QPushButton("Botão 2")
button2.clicked.connect(button_clicked)
layout.addWidget(button2)

button3 = QPushButton("Botão 3")
button3.clicked.connect(button_clicked)
layout.addWidget(button3)
# Mostra a janela
window.show()

sys.exit(app.exec_())
