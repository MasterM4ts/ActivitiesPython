from Telas import TelaPrincipal
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec_())