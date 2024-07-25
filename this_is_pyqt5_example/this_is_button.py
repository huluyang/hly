import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


"""

这是一个按钮的例子

"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QPushButton_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        QPushButton('我是按钮', self)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())