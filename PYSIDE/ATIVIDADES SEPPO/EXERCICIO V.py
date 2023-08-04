from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Conversão de Metros para Centimetros")
        self.setGeometry(100, 100, 300, 150)


        self.label1 = QLabel("Metros:", self)
        self.label1.setGeometry(10, 10, 80, 30)


        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)


        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 40, 280, 30)


        self.button = QPushButton("Converter", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.converter)


    def converter(self):
        metros = int(self.input1.text())
        conversao = metros*100 
        self.result_label.setText(f"A Conversão de {metros}m é: {conversao}cm.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())