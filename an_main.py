# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'an_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from random import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 704)
        MainWindow.setMinimumSize(QtCore.QSize(150, 150))
        MainWindow.setIconSize(QtCore.QSize(100, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 1141, 961))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fon.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 100, 931, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(240, 190))
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        a=randint(0,3)
        if a==0:
            icon.addPixmap(QtGui.QPixmap("images/Animals/Pig.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a==1:
            icon.addPixmap(QtGui.QPixmap("images/Animals/Pig_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a==2:
            icon.addPixmap(QtGui.QPixmap("images/Animals/Pig_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a==3:
            icon.addPixmap(QtGui.QPixmap("images/Animals/Pig_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(285, 400))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(240, 190))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        a2=randint(0,3)
        if a2==0:
            icon1.addPixmap(QtGui.QPixmap("images/Animals/Dog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a2==1:
            icon1.addPixmap(QtGui.QPixmap("images/Animals/Dog_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a2==2:
            icon1.addPixmap(QtGui.QPixmap("images/Animals/Dog_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a2==3:
            icon1.addPixmap(QtGui.QPixmap("images/Animals/Dog_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(330, 320))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(240, 190))
        self.pushButton_3.setMaximumSize(QtCore.QSize(240, 150))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        a3=randint(0,3)
        if a3==0:
            icon2.addPixmap(QtGui.QPixmap("images/Animals/Horse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a3==1:
            icon2.addPixmap(QtGui.QPixmap("images/Animals/Horse_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a3==2:
            icon2.addPixmap(QtGui.QPixmap("images/Animals/Horse_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a3==3:
            icon2.addPixmap(QtGui.QPixmap("images/Animals/Horse_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(320, 300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(240, 190))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        a4=randint(0,3)
        if a4==0:
            icon3.addPixmap(QtGui.QPixmap("images/Animals/Cow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a4==1:
            icon3.addPixmap(QtGui.QPixmap("images/Animals/Cow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a4==2:
            icon3.addPixmap(QtGui.QPixmap("images/Animals/Cow_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a4==3:
            icon3.addPixmap(QtGui.QPixmap("images/Animals/Cow_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(290, 190))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(240, 190))
        self.pushButton.setMaximumSize(QtCore.QSize(240, 150))
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        a5=randint(0,3)
        if a5==0:
            icon4.addPixmap(QtGui.QPixmap("images/Animals/Chicken.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a5==1:
            icon4.addPixmap(QtGui.QPixmap("images/Animals/Chicken_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a5==2:
            icon4.addPixmap(QtGui.QPixmap("images/Animals/Chicken_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a5==3:
            icon4.addPixmap(QtGui.QPixmap("images/Animals/Chicken_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(260, 190))
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(240, 190))
        self.pushButton_1.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton_1.setText("")
        icon5 = QtGui.QIcon()
        a6=randint(0,3)
        if a6==0:
            icon5.addPixmap(QtGui.QPixmap("images/Animals/Sheep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a6==1:
            icon5.addPixmap(QtGui.QPixmap("images/Animals/Sheep_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a6==2:
            icon5.addPixmap(QtGui.QPixmap("images/Animals/Sheep_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elif a6==3:
            icon5.addPixmap(QtGui.QPixmap("images/Animals/Sheep_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon5)
        self.pushButton_1.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 172, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
"        background: rgba(255,255,255,0)\n"
"}")
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/Krest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(90, 90))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
"        background: rgba(255,255,255,0)\n"
"}")
        self.pushButton_6.setText("")
        icon7 = QtGui.QIcon()

        icon7.addPixmap(QtGui.QPixmap("images/Question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QtCore.QSize(70, 100))
        self.pushButton_6.setAutoRepeat(False)
        self.pushButton_6.setAutoExclusive(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
