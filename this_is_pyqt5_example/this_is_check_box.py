import sys

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox

"""

这是一个多选框的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QCheckBox_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        QCheckBox('我是第一个多选框', self)

        self.check_box2 = QCheckBox('我是第二个多选框', self)

        self.check_box2.move(0, 50)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
