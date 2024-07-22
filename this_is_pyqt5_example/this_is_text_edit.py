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
        text_edit = QTextEdit(self)
        text_edit.move(10, 10)
        text_edit.show()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
