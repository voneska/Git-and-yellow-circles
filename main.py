import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.draw_btn.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = randint(1, min([self.width(), self.height()]))
        x = randint(0, self.width() - diameter - 1)
        y = randint(0, self.height() - diameter - 1)
        color = [randint(0, 255) for i in range(3)]
        self.circles += [(color, (x, y, diameter, diameter))]
        self.update()

    def draw_circles(self, qp):
        qp.setBrush(QColor(0, 0, 0, 0))
        for color, data in self.circles:
            pen = QPen(QColor(*color), 5)
            qp.setPen(pen)
            qp.drawEllipse(*data)

    def paintEvent(self, *args, **kwargs):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
