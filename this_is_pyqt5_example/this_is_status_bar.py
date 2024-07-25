import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar

"""

这是一个在窗口底部显示状态信息控件的例子

"""


class Window(QMainWindow):  # 注意继承QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QStatusBar_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('你好呀', 5000)  # 消息会显示在状态栏上，5秒后自动消失


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
