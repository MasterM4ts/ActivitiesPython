import typing
from PyQt5 import QtCore
import brazilcep
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Busca CEP")
        
endereco = brazilcep.get_address_from_cep('45715-154')
print(endereco)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())