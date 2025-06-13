# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
        MainWindow.resize(852, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_board = QLabel(self.centralwidget)
        self.lbl_board.setObjectName(u"lbl_board")
        self.lbl_board.setGeometry(QRect(10, 10, 831, 551))
        self.lbl_board.setPixmap(QPixmap(u"../images/number_board.png"))
        self.lbl_board.setScaledContents(True)
        self.btn_return = QPushButton(self.centralwidget)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setGeometry(QRect(10, 570, 80, 25))
        self.lbl_player = QLabel(self.centralwidget)
        self.lbl_player.setObjectName(u"lbl_player")
        self.lbl_player.setGeometry(QRect(30, 500, 31, 51))
        self.lbl_player.setPixmap(QPixmap(u"../images/pieces_red.png"))
        self.lbl_player.setScaledContents(True)
        self.btn_dice = QPushButton(self.centralwidget)
        self.btn_dice.setObjectName(u"btn_dice")
        self.btn_dice.setGeometry(QRect(380, 570, 61, 61))
        self.lbl_dice_show = QLabel(self.centralwidget)
        self.lbl_dice_show.setObjectName(u"lbl_dice_show")
        self.lbl_dice_show.setGeometry(QRect(480, 570, 61, 51))
        font = QFont()
        font.setPointSize(15)
        self.lbl_dice_show.setFont(font)
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(704, 570, 91, 41))
        self.lbl_snake = QLabel(self.centralwidget)
        self.lbl_snake.setObjectName(u"lbl_snake")
        self.lbl_snake.setGeometry(QRect(340, 170, 261, 231))
        self.lbl_snake.setStyleSheet(u"background: transparent;")
        self.lbl_snake.setPixmap(QPixmap(u"C:/Users/potat/Downloads/snake-removebg-preview.png"))
        self.lbl_snake.setScaledContents(True)
        self.lbl_ladder = QLabel(self.centralwidget)
        self.lbl_ladder.setObjectName(u"lbl_ladder")
        self.lbl_ladder.setGeometry(QRect(120, 160, 191, 381))
        self.lbl_ladder.setStyleSheet(u"background: transparent;")
        self.lbl_ladder.setPixmap(QPixmap(u"C:/Users/potat/Downloads/ladder-removebg-preview.png"))
        self.lbl_ladder.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.lbl_board.raise_()
        self.btn_return.raise_()
        self.btn_dice.raise_()
        self.lbl_dice_show.raise_()
        self.btn_reset.raise_()
        self.lbl_player.raise_()
        self.lbl_snake.raise_()
        self.lbl_ladder.raise_()

        self.retranslateUi(MainWindow)
        self.btn_return.clicked.connect(MainWindow.btn_return_a)
        self.btn_dice.clicked.connect(MainWindow.btn_dice_a)
        self.btn_reset.clicked.connect(MainWindow.btn_reset_a)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Snakes & Ladders", None))
        self.lbl_board.setText("")
        self.btn_return.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.lbl_player.setText("")
        self.btn_dice.setText("")
        self.lbl_dice_show.setText("")
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.lbl_snake.setText("")
        self.lbl_ladder.setText("")
    # retranslateUi

