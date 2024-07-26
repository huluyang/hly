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
        self.btn = QPushButton('点击选择文件夹或文件', self)
        self.btn.clicked.connect(self.show_message)

    def show_message(self):
        # 选择文件夹
        select_dir = QFileDialog.getExistingDirectory(self, '这是选取文件夹弹窗的标题', 'C:/')
        print("您选择的文件夹路径为：", select_dir)

        # 选择单个文件
        # select_file = QFileDialog.getOpenFileName(self, '这是选取文件的弹窗的标题', 'C:/', 'All Files (*);')
        # print("您选择的文件路径为：", select_file[0])

        # 选择多个文件 按住Ctrl键进行多选文件
        # select_file = QFileDialog.getOpenFileNames(self, '这是选取多个文件的弹窗的标题', 'C:/', 'All Files (*);')
        # print("您选择的多个文件路径列表为：", select_file[0])

        # 保存文件 可自定义获取用户输入的数据进行文件写入并保存
        # select_file = QFileDialog.getSaveFileName(self, '这是保存文件的弹窗的标题', 'C:/', 'All Files (*);')
        # print("您选择的保存文件路径为：", select_file[0])


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
