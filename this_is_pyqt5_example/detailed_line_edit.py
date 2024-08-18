import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit


"""

这是一个单行输入框的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        line_edit = QLineEdit(self)
        line_edit.resize(180, 30)
        # line_edit.setText("这是设置的默认输入的内容")
        # line_edit.setPlaceholderText("这是设置的默认提示的内容")  # 输入内容后会自动消失
        # line_edit.clear()  # 清空输入框中已输入的内容
        line_edit.textChanged.connect(self.change_fun)  # 这是当输入框里面的内容有所改变时会调用的函数
    def change_fun(self, e):
        # 这里的e参数输出的是每次输入框改变时的内容  可直接判断内容字符串是否符合或包含想要筛选的内容
        print(e)
        print("注意，输入框的内容改变了，当前改变后的内容为：", e)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
