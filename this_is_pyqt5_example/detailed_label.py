import sys

from PyQt5.QtCore import Qt
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
        self.label = QLabel('我是显示的文本', self)
        # self.label.setText("这是更改后的文本")  # 设置文本内容

        # self.label.setText('<a href="http://www.baidu.com">Link</a>')  # 设置文本内容为超链接
        # self.label.setOpenExternalLinks(True)  # 设置打开超链接


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
