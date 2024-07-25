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
        QLineEdit(self)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
