# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(852, 639)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_play = QPushButton(self.centralwidget)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setGeometry(QRect(290, 330, 221, 81))
        font = QFont()
        font.setPointSize(29)
        self.btn_play.setFont(font)
        self.btn_quit = QPushButton(self.centralwidget)
        self.btn_quit.setObjectName(u"btn_quit")
        self.btn_quit.setGeometry(QRect(290, 540, 221, 81))
        self.btn_quit.setFont(font)
        self.lbl_logo = QLabel(self.centralwidget)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(150, 90, 581, 191))
        self.lbl_logo.setScaledContents(True)
        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(290, 440, 221, 81))
        self.btn_settings.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_play.clicked.connect(MainWindow.btn_play_a)
        self.btn_quit.clicked.connect(MainWindow.btn_quit_a)
        self.btn_settings.clicked.connect(MainWindow.btn_settings_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Snakes & Ladders", None))
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
        self.lbl_logo.setText("")
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
    # retranslateUi

