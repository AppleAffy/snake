# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_3.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(852, 639)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_return = QPushButton(self.centralwidget)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setGeometry(QRect(770, 10, 80, 25))
        self.chk_dark = QCheckBox(self.centralwidget)
        self.chk_dark.setObjectName(u"chk_dark")
        self.chk_dark.setGeometry(QRect(60, 130, 82, 23))
        self.lbl_misc = QLabel(self.centralwidget)
        self.lbl_misc.setObjectName(u"lbl_misc")
        self.lbl_misc.setGeometry(QRect(60, 330, 131, 41))
        font = QFont()
        font.setPointSize(16)
        self.lbl_misc.setFont(font)
        self.btn_red = QPushButton(self.centralwidget)
        self.btn_red.setObjectName(u"btn_red")
        self.btn_red.setGeometry(QRect(60, 420, 61, 51))
        self.btn_red.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.btn_yellow = QPushButton(self.centralwidget)
        self.btn_yellow.setObjectName(u"btn_yellow")
        self.btn_yellow.setGeometry(QRect(140, 420, 61, 51))
        self.btn_yellow.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.btn_pink = QPushButton(self.centralwidget)
        self.btn_pink.setObjectName(u"btn_pink")
        self.btn_pink.setGeometry(QRect(220, 420, 61, 51))
        self.btn_pink.setStyleSheet(u"background-color: rgb(255, 85, 255);")
        self.btn_green = QPushButton(self.centralwidget)
        self.btn_green.setObjectName(u"btn_green")
        self.btn_green.setGeometry(QRect(300, 420, 61, 51))
        self.btn_green.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.btn_black = QPushButton(self.centralwidget)
        self.btn_black.setObjectName(u"btn_black")
        self.btn_black.setGeometry(QRect(380, 420, 61, 51))
        self.btn_black.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 180, 80, 25))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_return.clicked.connect(MainWindow.btn_return_a)
        self.btn_red.clicked.connect(MainWindow.btn_color)
        self.btn_yellow.clicked.connect(MainWindow.btn_color)
        self.btn_pink.clicked.connect(MainWindow.btn_color)
        self.btn_green.clicked.connect(MainWindow.btn_color)
        self.btn_black.clicked.connect(MainWindow.btn_color)
        self.pushButton.clicked.connect(MainWindow.debug)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_return.setText(QCoreApplication.translate("MainWindow", u"Rerurn", None))
        self.chk_dark.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.lbl_misc.setText(QCoreApplication.translate("MainWindow", u"PLAYER:", None))
        self.btn_red.setText("")
        self.btn_yellow.setText("")
        self.btn_pink.setText("")
        self.btn_green.setText("")
        self.btn_black.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"DEBUG", None))
    # retranslateUi

