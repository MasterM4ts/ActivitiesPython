from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Total do seu Salário no Referido Mês")
        self.setGeometry(100, 100, 350, 150)


        self.label1 = QLabel("Ganho por Hora:", self)
        self.label1.setGeometry(10, 10, 80, 30)


        self.input1 = QLineEdit(self)
        self.input1.setGeometry(105, 10, 80, 30)


        self.label2 = QLabel("Horas de Trabalho:", self)
        self.label2.setGeometry(10, 50, 100, 30)


        self.input2 = QLineEdit(self)
        self.input2.setGeometry(105, 50, 80, 30)


        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 90, 280, 30)


        self.button = QPushButton("Calcular", self)
        self.button.setGeometry(210, 10, 100, 70)
        self.button.clicked.connect(self.calcular_salario)


    def calcular_salario(self):
        gan_hora = float(self.input1.text())
        trab_hora = float(self.input2.text())
        calculo = gan_hora * trab_hora
        self.result_label.setText(f"O Total do Seu Salário é: R${calculo}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())