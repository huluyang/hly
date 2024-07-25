import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton

"""

这是一个选取文件夹弹窗的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFileDialog_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.btn = QPushButton('点击选择文件夹', self)
        self.btn.clicked.connect(self.show_message)

    def show_message(self):
        select_dir = QFileDialog.getExistingDirectory(self, '这是选取文件夹弹窗的标题', 'C:/')
        print("您选择的文件夹路径为：", select_dir)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
