import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from random import randint


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
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
        qp.setBrush(QColor("yellow"))
        for _ in range(randint(10, 20)):
            r = randint(10, 50)
            x, y = randint(0, 300 - r), randint(0, 250 - r)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
