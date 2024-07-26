import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

"""

这是一个单选框的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QRadioButton_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.radio_button1 = QRadioButton('我是第一个单选框', self)
        # self.radio_button1.setAutoExclusive(False)  # 默认情况下，单选框是互斥的，即只能选择一个 这个设置为False 可以当做多选框使用
        self.radio_button1.setChecked(True)  # 设置第一个单选框为选中状态
        print(self.radio_button1.isChecked())  # 获取第一个单选框是否被选中
        self.radio_button1.toggled.connect(self.is_check)

        self.radio_button2 = QRadioButton('我是第二个单选框', self)

        self.radio_button2.move(0, 50)

    def is_check(self, checked):
        print("这是我的选中状态改变就会触发的函数")
        # 第一种判断方法
        if checked:
            print('我被选中了')
        else:
            print('我没被选中')
        # 第二种判断方法
        if self.radio_button1.isChecked():
            print('我被选中了')
        else:
            print('我没被选中')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
