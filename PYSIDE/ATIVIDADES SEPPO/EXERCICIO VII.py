from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Dobro da Área do Quadrado")
        self.setGeometry(100, 100, 300, 150)


        self.label1 = QLabel("Área do Quadrado:", self)
        self.label1.setGeometry(10, 10, 80, 30)


        self.input1 = QLineEdit(self)
        self.input1.setGeometry(100, 10, 80, 30)


        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)


        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(190, 10, 100, 70)
        self.button.clicked.connect(self.calculo_area)


    def calculo_area(self):
        area = float(self.input1.text())
        calculo = area * 2
        self.result_label.setText(f"O Dobro da Área do Quadrado é: {calculo}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())