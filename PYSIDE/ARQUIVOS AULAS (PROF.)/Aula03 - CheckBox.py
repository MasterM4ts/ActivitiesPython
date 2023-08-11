import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget

# Definindo a classe da janela principal
class MainWindown(QMainWindow):
    def __init__(self):
        super().__init__()  # Inicialização da classe pai (QMainWindow)

        self.setWindowTitle("CheckBox")  # Definindo o título da janela

        self.lbl = QLabel("Voce Fuma ?")  # Criando um rótulo com texto
        self.ck = QCheckBox("SIM")  # Criando um checkbox com texto
        self.ck.setTristate(True)  # Permitindo três estados no checkbox
        self.lbl2 = QLabel()  # Criando um segundo rótulo vazio

        layout = QVBoxLayout()  # Criando um layout vertical
        layout.addWidget(self.lbl)  # Adicionando o rótulo ao layout
        layout.addWidget(self.ck)  # Adicionando o checkbox ao layout
        layout.addWidget(self.lbl2)  # Adicionando o segundo rótulo ao layout

        container = QWidget()  # Criando um widget container
        container.setLayout(layout)  # Definindo o layout para o widget container

        self.setCentralWidget(container)  # Definindo o widget container como central

        self.ck.stateChanged.connect(self.state)  # Conectando o sinal de mudança de estado ao método 'state'

    def state(self, s):
        print(s)  # Imprimindo o estado do checkbox
        if s == 2:
            self.lbl2.setText("Pare de fumar.")  # Definindo o texto do segundo rótulo
        else:
            self.lbl2.setText("")  # Limpando o texto do segundo rótulo

app = QApplication(sys.argv)  # Inicializando a aplicação
w = MainWindown()  # Criando a janela principal
w.show()  # Exibindo a janela principal
app.exec()  # Iniciando o loop de eventos da aplicação
