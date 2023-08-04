from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.inicio()
        
    def inicio(self):  
        self.setWindowTitle("Pokedex")
        
        
        self.button_pikachu = QPushButton("Pikachu")
        self.button_charmander = QPushButton("Charmander")
        
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(600, 400)
        self.image_frame.setLayout(QVBoxLayout())
        
        
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.image_label)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.button_pikachu)
        layout.addWidget(self.button_charmander)
        layout.addWidget(self.image_frame)
        
        
        self.button_pikachu.clicked.connect(self.display_pikachu)
        self.button_charmander.clicked.connect(self.display_charmander)
        
        
        self.setLayout(layout)
        
        
    def display_pikachu(self):
        pixmap = QPixmap("PYSIDE/QPIXMAP/POKEMON/pokemon1.png")
        self.image(pixmap)
    
    
    def display_charmander(self):
        pixmap = QPixmap("PYSIDE/QPIXMAP/POKEMON/pokemon2.png")
        self.image(pixmap)
    
    
    def image(self, pixmap):
        scale_pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scale_pixmap)
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()