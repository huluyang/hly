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
        QRadioButton('我是第一个单选框', self)

        self.radio_button2 = QRadioButton('我是第二个单选框', self)

        self.radio_button2.move(0, 50)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
