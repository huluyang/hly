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
        self.check_box1 = QCheckBox('我是第一个多选框', self)
        self.check_box1.setChecked(True)  # 设置默认选中
        print(self.check_box1.isChecked())  # 获取状态 True为选中 False为未选中
        self.check_box1.toggled.connect(self.is_check)

    def is_check(self, checked):
        print("这是我的选中状态改变就会触发的函数")
        # # 第一种判断方法
        # if checked:
        #     print("我被选中了")
        # else:
        #     print("我被取消了")

        # 第二种判断方法
        # if self.check_box1.isChecked():
        #     print("我被选中了")
        # else:
        #     print("我被取消了")



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
