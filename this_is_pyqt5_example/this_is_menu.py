import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu

"""

这是一个添加右键菜单的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMenu_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.label = QLabel('在我身上右键查看菜单功能', self)
        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.customContextMenuRequested.connect(self.menu_ui)

    def menu_ui(self):
        self.menu = QMenu()  # 这里注意  如果menu前面不加self则不生效
        self.menu.popup(QCursor.pos())
        self.menu.addAction(u'第一个选项')

        self.menu2 = QMenu(u'第二个选项')
        self.menu2.addAction(u'二级菜单的第一个选项')
        self.menu.addMenu(self.menu2)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
