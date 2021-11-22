from PyQt5.QtWidgets import QPushButton, QMainWindow,QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys
from PyQt5 import uic
from random import randint

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):
    def __init__(self):

        super().__init__()
        uic.loadUi('ui_file.ui', self)
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
        pen = QPen(Qt.yellow, 2)
        qp.setPen(pen)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(randint(100, 350), randint(100,350), randint(50,80), randint(50,80))

        self.to_do = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())