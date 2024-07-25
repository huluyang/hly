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
        QTextEdit(self)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
