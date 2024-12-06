import sys
import random
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        self.circle_radius = 0
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.pushButton.hide()
        self.circle_radius = random.randint(10, 500)
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setBrush(QColor(255, 255, 0))

        center_x = (self.width() - self.circle_radius) // 2
        center_y = (self.height() - self.circle_radius) // 2
        qp.drawEllipse(center_x, center_y, self.circle_radius, self.circle_radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
