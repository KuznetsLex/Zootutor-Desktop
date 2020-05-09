from pydub import AudioSegment
from pydub.playback import play
import sys
from an_main import *
from chicken import *
from sheep import *
from cow import *
from dog import *
from horse import *
from pig import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)






class MyWin(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_handlers()
        self.ui.pushButton_6.clicked.connect(self.play_question)



    def init_handlers(self):
        self.ui.pushButton.clicked.connect(self.show_window_2)
        self.ui.pushButton_1.clicked.connect(self.show_window_3)
        self.ui.pushButton_2.clicked.connect(self.show_window_4)
        self.ui.pushButton_3.clicked.connect(self.show_window_5)
        self.ui.pushButton_4.clicked.connect(self.show_window_6)
        self.ui.pushButton_5.clicked.connect(self.show_window_7)



    def show_window_2(self):
        sound = AudioSegment.from_mp3('Sounds/Chicken_1.wav')
        play(sound)
        self.w2 = MyWin2()
        self.w2.show()

    def show_window_3(self):
        sound = AudioSegment.from_mp3('Sounds/Sheep_1.wav')
        play(sound)
        self.w3 = MyWin3()
        self.w3.show()

    def show_window_4(self):
        sound = AudioSegment.from_mp3('Sounds/Cow_1.wav')
        play(sound)
        self.w4 = MyWin4()
        self.w4.show()

    def show_window_5(self):
        sound = AudioSegment.from_mp3('Sounds/Horse_1.wav')
        play(sound)
        self.w5 = MyWin5()
        self.w5.show()

    def show_window_6(self):
        sound = AudioSegment.from_mp3('Sounds/Dog_1.wav')
        play(sound)
        self.w6 = MyWin6()
        self.w6.show()

    def show_window_7(self):
        sound = AudioSegment.from_mp3('Sounds/Pig_1.wav')
        play(sound)
        self.w7 = MyWin7()
        self.w7.show()

    def play_question(self):
        sound = AudioSegment.from_mp3('Sounds/main.wav')
        play(sound)





class MyWin2(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.play_sound)
        self.setFixedSize(1130,700)
        self.ui.pushButton_4.clicked.connect(self.play_question)
        self.ui.pushButton_1.clicked.connect(self.play_footprint)
        self.ui.pushButton_2.clicked.connect(self.play_food)

    def play_question(self):
        sound = AudioSegment.from_mp3('Sounds/main_2.wav')
        play(sound)

    def play_footprint(self):
        sound = AudioSegment.from_mp3('Sounds/Chicken_footprint.wav')
        play(sound)

    def play_food(self):
        sound = AudioSegment.from_mp3('Sounds/Chicken_food.wav')
        play(sound)


    def play_sound(self):
        sound = AudioSegment.from_mp3('Sounds/Chicken.wav')
        play(sound)

    def back(self):
        self.hide()


class MyWin3(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.play_sound)
        self.setFixedSize(1130,700)
        self.ui.pushButton_4.clicked.connect(self.play_question)
        self.ui.pushButton_1.clicked.connect(self.play_footprint)
        self.ui.pushButton_2.clicked.connect(self.play_food)

    def play_question(self):
        sound = AudioSegment.from_mp3('Sounds/main_2.wav')
        play(sound)

    def play_footprint(self):
        sound = AudioSegment.from_mp3('Sounds/Sheep_footprint.wav')
        play(sound)

    def play_food(self):
        sound = AudioSegment.from_mp3('Sounds/Sheep_food.wav')
        play(sound)


    def play_sound(self):
        sound = AudioSegment.from_mp3('Sounds/Sheep.wav')
        play(sound)

    def back(self):
        self.hide()



class MyWin4(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.play_sound)
        self.setFixedSize(1130,700)
        self.ui.pushButton_4.clicked.connect(self.play_question)
        self.ui.pushButton_1.clicked.connect(self.play_footprint)
        self.ui.pushButton_2.clicked.connect(self.play_food)

    def play_question(self):
        sound = AudioSegment.from_mp3('Sounds/main_2.wav')
        play(sound)

    def play_footprint(self):
        sound = AudioSegment.from_mp3('Sounds/Cow_footprint.wav')
        play(sound)

    def play_food(self):
        sound = AudioSegment.from_mp3('Sounds/Cow_food.wav')
        play(sound)


    def play_sound(self):
        sound = AudioSegment.from_mp3('Sounds/Cow.wav')
        play(sound)

    def back(self):
        self.hide()



class MyWin5(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.play_sound)
        self.setFixedSize(1130,700)
        self.ui.pushButton_4.clicked.connect(self.play_question)
        self.ui.pushButton_1.clicked.connect(self.play_footprint)
        self.ui.pushButton_2.clicked.connect(self.play_food)


    def play_question(self):
        sound = AudioSegment.from_mp3('Sounds/main_2.wav')
        play(sound)

    def play_footprint(self):
        sound = AudioSegment.from_mp3('Sounds/Horse_footprint.wav')
        play(sound)

    def play_food(self):
        sound = AudioSegment.from_mp3('Sounds/Horse_food.wav')
        play(sound)


    def play_sound(self):
        sound = AudioSegment.from_mp3('Sounds/Horse.wav')
        play(sound)

    def back(self):
        self.hide()



class MyWin6(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.play_sound)
        self.setFixedSize(1130,700)
        self.ui.pushButton_4.clicked.connect(self.play_question)
        self.ui.pushButton_1.clicked.connect(self.play_footprint)
        self.ui.pushButton_2.clicked.connect(self.play_food)

    def play_question(self):
        sound = AudioSegment.from_mp3('Sounds/main_2.wav')
        play(sound)

    def play_footprint(self):
        sound = AudioSegment.from_mp3('Sounds/Dog_footprint.wav')
        play(sound)

    def play_food(self):
        sound = AudioSegment.from_mp3('Sounds/Dog_food.wav')
        play(sound)


    def play_sound(self):
        sound = AudioSegment.from_mp3('Sounds/Dog.wav')
        play(sound)

    def back(self):
        self.hide()



class MyWin7(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.play_sound)
        self.setFixedSize(1130,700)
        self.ui.pushButton_4.clicked.connect(self.play_question)
        self.ui.pushButton_1.clicked.connect(self.play_footprint)
        self.ui.pushButton_2.clicked.connect(self.play_food)

    def play_question(self):
        sound = AudioSegment.from_mp3('Sounds/main_2.wav')
        play(sound)

    def play_footprint(self):
        sound = AudioSegment.from_mp3('Sounds/Pig_footprint.wav')
        play(sound)

    def play_food(self):
        sound = AudioSegment.from_mp3('Sounds/Pig_food.wav')
        play(sound)


    def play_sound(self):
        sound = AudioSegment.from_mp3('Sounds/Pig.wav')
        play(sound)

    def back(self):
        self.hide()




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.setFixedSize(1130,700)
    myapp.show()
    sys.exit(app.exec_())

