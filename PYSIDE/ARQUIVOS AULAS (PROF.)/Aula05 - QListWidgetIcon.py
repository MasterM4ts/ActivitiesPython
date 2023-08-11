import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon


app = QApplication(sys.argv)  # Criação da instância da aplicação

window = QMainWindow()  # Criação da janela principal
window.setWindowTitle("Exemplo de QListWidget")  # Define o título da janela
window.setGeometry(100, 100, 400, 300)  # Define a posição e tamanho da janela

list_widget = QListWidget()  # Criação do QListWidget

item1 = QListWidgetItem("Item 1")  # Criação de um item
item1.setIcon(QIcon("chess.gif"))  # Define um ícone para o Item 1
item2 = QListWidgetItem("Item 2")  # Criação de outro item
item2.setIcon(QIcon("picachu.jpg"))  # Define um ícone para o Item 2
item3 = QListWidgetItem("Item 3")  # Criação de mais um item
item3.setIcon(QIcon("chess.gif"))  # Define um ícone para o Item 3

list_widget.addItem(item1)  # Adiciona o Item 1 ao QListWidget
list_widget.addItem(item2)  # Adiciona o Item 2 ao QListWidget
list_widget.addItem(item3)  # Adiciona o Item 3 ao QListWidget

layout = QVBoxLayout()  # Criação de um layout vertical
layout.addWidget(list_widget)  # Adiciona o QListWidget ao layout vertical

container = QWidget()  # Criação de um widget para conter o layout
container.setLayout(layout)  # Define o layout para o widget container
window.setCentralWidget(container)  # Define o widget container como o conteúdo central da janela
# Função a ser chamada quando um item for clicado
def item_clicked(item):
    print("Ícone clicado:", item.text())  # Imprime o texto do item clicado
    
# Conectar o sinal 'itemClicked' à função 'item_clicked'
#list_widget.itemClicked.connect(item_clicked)
list_widget.itemDoubleClicked.connect(item_clicked)


window.show()  # Exibe a janela

sys.exit(app.exec_())  # Inicia o loop de eventos da aplicação
