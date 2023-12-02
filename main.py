import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint
from mainm import Ui_Form


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def drawCircle(self, qp):
        for _ in range(randint(10, 20)):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(10, 50)
            x, y = randint(0, 300 - r), randint(0, 250 - r)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
