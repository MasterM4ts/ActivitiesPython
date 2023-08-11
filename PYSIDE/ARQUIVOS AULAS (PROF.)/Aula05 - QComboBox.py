import sys  # Importa o módulo sys para manipulação do sistema
from PySide6.QtCore import QSize  # Importa a classe QSize do PySide6 para gerenciar tamanhos
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QComboBox  # Importa classes do PySide6 para interface gráfica

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Chama o construtor da classe pai

        self.setWindowTitle("QcomboBox")  # Define o título da janela

        # Cria um QComboBox e adiciona itens a ele
        self.cb = QComboBox()
        self.cb.addItems(["item 01", "item 02", "item 03", "item 04"])

        # Conecta os sinais de mudança de índice e texto a métodos de manipulação
        self.cb.currentIndexChanged.connect(self.mundanca_indice)
        self.cb.currentTextChanged.connect(self.mudanca_texto)

        self.cb.setEditable(True)  # Permite que o QComboBox seja editável
        self.cb.setMaxCount(10)  # Define o limite máximo de itens no QComboBox

        # Configuração de modos de inserção (comentados)
        #self.cb.NoInsert  # Não permite a inserção de novos itens
        #self.cb.InsertAtTop  # Insere novos itens no topo da lista
        #self.cb.InsertAtCurrent  # Insere novos itens na posição atualmente selecionada
        #self.cb.InsertAtBottom  # Insere novos itens no final da lista
        #self.cb.InsertAfterCurrent  # Insere novos itens após o item atualmente selecionado
        #self.cb.InsertBeforeCurrent  # Insere novos itens antes do item atualmente selecionado
        #self.cb.InsertAlphabetically  # Insere novos itens na ordem alfabética da lista
        #self.setCentralWidget(self.cb)  # Define o QComboBox como widget central

    def mundanca_indice(self, i):
        print(i)  # Imprime o índice selecionado

    def mudanca_texto(self, t):
        print(t)  # Imprime o texto selecionado

        if t == "item 01":
            print('conecta ao banco e traz informações do item 01')
        elif t == 'item 02':
            print('informações item 02')

app = QApplication(sys.argv)  # Cria uma instância da aplicação Qt
w = MainWindow()  # Cria uma instância da classe MainWindow
w.show()  # Exibe a janela principal
app.exec()  # Inicia o loop de eventos da aplicação
