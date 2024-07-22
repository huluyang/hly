import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

"""

这是一个显示文本的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        label = QLabel(self, '我是显示的文本')
        label.show()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
