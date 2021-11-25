from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import sys
from PyQt5 import uic
from random import randint

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "круг"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.geometry()

        self.pushButton.clicked.connect(self.run)
        self.to_do = False

    def run(self):
        self.to_do = True
        self.update()

    def paintEvent(self, event):
        if self.to_do:
            qpp = QPainter()

            qpp.begin(self)
            self.draw_circle(qpp)
            qpp.end()

    def draw_circle(self, qp):
        pen = QPen(2)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        pen.setColor(color)
        qp.setPen(pen)
        qp.setBrush(color)
        qp.drawEllipse(randint(100, 350), randint(100, 350), randint(50, 80), randint(50, 80))

        self.to_do = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())