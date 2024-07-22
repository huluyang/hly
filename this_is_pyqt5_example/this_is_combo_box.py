import sys

from PyQt5.QtWidgets import QApplication, QWidget, QComboBox

"""

这是一个下拉框的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QComboBox_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        combo_box = QComboBox(self)
        combo_box.addItem('第一个')
        combo_box.addItem('第二个')
        combo_box.addItems(['第三个', '第四个', '第五个', '第六个', '第七个'])
        combo_box.show()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
