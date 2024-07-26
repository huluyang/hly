import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton

"""

这是一个提示消息弹窗的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMessageBox_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        self.btn = QPushButton('点击显示弹窗', self)
        self.btn.clicked.connect(self.show_message)

    def show_message(self):
        # 提示弹窗
        QMessageBox.information(self, '这是弹窗的标题', '这是弹窗的详细内容')

        # 警告弹窗
        QMessageBox.warning(self, '这是弹窗的标题', '这是弹窗的详细内容')

        # 提问弹窗
        QMessageBox.question(self, '这是弹窗的标题', '这是弹窗的详细内容')

        # 错误弹窗
        QMessageBox.critical(self, '这是弹窗的标题', '这是弹窗的详细内容')

        # 关于弹窗
        QMessageBox.about(self, '这是弹窗的标题', '这是弹窗的详细内容')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
