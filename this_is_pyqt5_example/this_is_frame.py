import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFrame

"""

这是一个frame容器(主要用来容纳按钮等小组件分隔界面的框架)的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFrame_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.frame = QFrame(self)
        self.frame.setStyleSheet('QFrame {background-color: red; border: 1px solid black;}')  # css样式
        self.frame.resize(100, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
