import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu

"""

这是一个在系统托盘处显示图标的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSystemTrayIcon_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.sys_tray_icon = QSystemTrayIcon(self)
        self.sys_tray_icon.setIcon(QIcon(r'C:/img/img.png'))  # 将C:/img/img.png替换为自己本机的图片路径即可
        self.sys_tray_icon.show()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
