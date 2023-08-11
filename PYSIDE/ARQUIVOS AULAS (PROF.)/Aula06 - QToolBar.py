import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

# Importar os módulos necessários

def on_button_click():
    status_bar.showMessage("Botão clicado!")  # Mostra a mensagem na barra de status

# Definir a função que será chamada quando o botão for clicado

app = QApplication(sys.argv)

# Inicializar a aplicação

main_window = QMainWindow()
main_window.setWindowTitle("Exemplo de QToolBar e QStatusBar")

# Criar a janela principal e definir o título

toolbar = QToolBar()
main_window.addToolBar(toolbar)

# Criar uma barra de ferramentas e adicioná-la à janela

button_action = QAction(QIcon('balance.png'),"Clique aqui", main_window)
button_action.triggered.connect(on_button_click)
button_action.setStatusTip("Clica logo")  # Dica de status exibida na barra de status ao passar o mouse
button_action.setCheckable(True)  # Permite que a ação seja alternada (pressionada e solta)

toolbar.setIconSize(QSize(24, 24))  # Define o tamanho dos ícones na barra de ferramentas
toolbar.addAction(button_action)

toolbar.addSeparator()

# Criar uma ação (botão) e conectá-la à função de clique, em seguida, adicionar à barra de ferramentas

status_bar = QStatusBar()
main_window.setStatusBar(status_bar)

# Criar uma barra de status e associá-la à janela

main_window.show()

# Mostrar a janela

sys.exit(app.exec_())

# Executar a aplicação e gerenciar sua execução
