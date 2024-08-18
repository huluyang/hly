import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit

"""

这是一个多行输入框的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit_Example')
        self.resize(500, 300)
        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit(self)
        self.text_edit.setText("这是预先设置的默认内容")
        # text_edit.setPlaceholderText("这是预先设置的默认提示内容，输入内容后会自动消失")
        self.text_edit.textChanged.connect(self.change_fun)

    def change_fun(self):
        print("注意了, 输入框里面的内容改变了, 当前的内容为：", self.text_edit.toPlainText())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
