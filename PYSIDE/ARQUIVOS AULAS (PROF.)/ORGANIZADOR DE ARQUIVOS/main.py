import shutil  # Importa a biblioteca shutil para operações de arquivo.
import sys     # Importa a biblioteca sys para manipulação de argumentos de linha de comando.
import os      # Importa a biblioteca os para operações do sistema operacional.
from PySide6.QtWidgets import *  # Importa as classes da biblioteca PySide6 para criar a GUI.
from PySide6.QtGui import QIcon  # Importa a classe QIcon da biblioteca PySide6 para ícones.
from tela import Ui_MainWindow  # Importa a classe Ui_MainWindow do arquivo ui_main.py.


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Organizador de Arquivos")
        appIcon = QIcon("folder.png")
        self.setWindowIcon(appIcon)
        
        self.btn_abrir.clicked.connect(self.open_path)
        self.btn_organizar.clicked.connect(self.organize)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str('pasta com arquivos'), '/home', QFileDialog.ShowDirsOnly | 
                                                    QFileDialog.DontResolveSymlinks)
        self.txt_path.setText(self.path)
        self.path = str(self.path)

        
    def organize(self):
        path = self.path  # Obtém o diretório selecionado.
        files = os.listdir(path)  # Lista todos os arquivos no diretório.

        for file in files:
            filename, extension = os.path.splitext(file)  # Divide o nome do arquivo e sua extensão.
            extension = extension[1:]  # Remove o ponto da extensão.
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            else:
                os.makedirs(path + '/' + extension)  # Cria um diretório para a extensão, se não existir.
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

        msg = QMessageBox()  # Cria um diálogo de mensagem.
        msg.setIcon(QMessageBox.Information)
        msg.setText('Arquivos Organizados')
        msg.exec()  # Exibe o diálogo de mensagem.
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    windown = MainWindow()
    windown.show()
    app.exec()