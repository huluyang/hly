import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSlider

"""

这是一个滑动条的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSlider_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.slider = QSlider(self)
        self.slider.setRange(0, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
