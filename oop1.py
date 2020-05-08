from pydub import AudioSegment
from pydub.playback import play
import sys
from main import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication,QPushButton, QGridLayout)
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication,QPushButton, QGridLayout,QInputDialog)
from PyQt5.QtGui import QFont
from random import *





#class Window1(QMainWindow):
#    def __init__(self):
 #       super().__init__()
  #      self.setMinimumWidth(450)
   #     self.setMinimumHeight(250)
    #    self.button = QPushButton(self)
     #   self.button.setText("Теория")
      #  self.button.setFont(QFont("Segoe Print",10))
       # self.button.move(30,80)
#
#
 #       self.init_handlers()
  #      self.setGeometry(300, 300, 280, 170)
#
 #       self.show()
#     def init_handlers(self):  # обработка нажатия для октрытия 2 окна
#       self.button.clicked.connect(self.show_window_2)
#
#
 #    def show_window_2(self):  # открытие 2  окна
   #      self.w2 = MyWin()
     #    self.w2.show()


class MyWin(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_handlers()


    def init_handlers(self):
        self.ui.pushButton.clicked.connect(self.show_window_2)


    def show_window_2(self):
        self.w2 = MyWin2()
        self.w2.show()




    def slice(self):
        text, ok = QInputDialog.getInt(self, 'Input Dialog',
            'Введите продолжительность трека (отрицательное число, если необходимо считать с конца):')
        if ok:

            sound = AudioSegment.from_wav('myfile.wav')
            if text>=0:
                duration = sound[:text*1000]
            if text<=0:
                duration = sound[text*1000:]
            return(duration.export('myfile.wav', format='wav'))



class MyWin2(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.slice)



    def slice(self):
        self.hide()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

