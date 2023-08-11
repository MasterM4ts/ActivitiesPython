import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

# Criação da aplicação
app = QApplication(sys.argv)

# Criação da janela principal
window = QMainWindow()
window.setWindowTitle("Exemplo de QListWidget")
window.setGeometry(100, 100, 400, 300)  # Define a posição e tamanho da janela

# Criação do QListWidget
list_widget = QListWidget()

# Adicionando itens ao QListWidget
item1 = QListWidgetItem("Item 1")
item2 = QListWidgetItem("Item 2")
item3 = QListWidgetItem("Item 3")
list_widget.addItem(item1)
list_widget.addItem(item2)
list_widget.addItem(item3)

# Configurando layout
layout = QVBoxLayout()
layout.addWidget(list_widget)

# Criando um widget para conter o QListWidget e definindo o layout
container = QWidget()
container.setLayout(layout)
window.setCentralWidget(container)

# Exibindo a janela
window.show()

# Execução da aplicação
sys.exit(app.exec_())
