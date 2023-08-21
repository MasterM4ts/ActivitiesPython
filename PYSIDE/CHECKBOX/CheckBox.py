import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCheckBox, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Check Box")
        self.label = QLabel("Só Aceita!!!")
        self.ck = QCheckBox("Aceito")
        self.label2 = QLabel()
        
        
        #self.ck.setTristate(True) 
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.ck)
        layout.addWidget(self.label2)
        
        
        container = QWidget()
        container.setLayout(layout)
        
        
        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)        
    
    
    def state(self, m):
        if m == 2:
            self.label2.setText("NÃO ACEITO!!!")
        
        
        else:
            self.label2.setText("NÃO ACEITO!!!")           


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()        