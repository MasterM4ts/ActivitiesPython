# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import imagen_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 802)
        MainWindow.setStyleSheet(u"background-color: rgb(19, 199, 16);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(14, 126, 138);")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_principal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_txt_titulo = QFrame(self.frame_principal)
        self.frame_txt_titulo.setObjectName(u"frame_txt_titulo")
        self.frame_txt_titulo.setFrameShape(QFrame.StyledPanel)
        self.frame_txt_titulo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_txt_titulo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_txt_titulo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_txt_titulo)

        self.label_img = QLabel(self.frame_principal)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setPixmap(QPixmap(u":/Icon/kisspng-portable-network-graphics-clip-art-computer-icons-folder-clipart-ourclipart-5bf17747181536.1339426515425513670987-removebg-preview.png"))
        self.label_img.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_img)

        self.frame_input = QFrame(self.frame_principal)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_input)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.led_input = QLineEdit(self.frame_input)
        self.led_input.setObjectName(u"led_input")
        self.led_input.setMaximumSize(QSize(400, 25))
        self.led_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.led_input)

        self.btn_abrir = QPushButton(self.frame_input)
        self.btn_abrir.setObjectName(u"btn_abrir")
        self.btn_abrir.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        self.btn_abrir.setFont(font1)
        self.btn_abrir.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.horizontalLayout.addWidget(self.btn_abrir)


        self.verticalLayout_3.addWidget(self.frame_input)

        self.frame_btn = QFrame(self.frame_principal)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_organizar = QPushButton(self.frame_btn)
        self.btn_organizar.setObjectName(u"btn_organizar")
        self.btn_organizar.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(11)
        self.btn_organizar.setFont(font2)
        self.btn_organizar.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.horizontalLayout_2.addWidget(self.btn_organizar)


        self.verticalLayout_3.addWidget(self.frame_btn)


        self.verticalLayout_4.addWidget(self.frame_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ORGANIZADOR DE ARQUIVOS", None))
        self.label_img.setText("")
        self.btn_abrir.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.btn_organizar.setText(QCoreApplication.translate("MainWindow", u"ORGANIZAR", None))
    # retranslateUi