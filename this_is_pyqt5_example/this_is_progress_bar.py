import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton

"""

这是一个进度条的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QProgressBar_Example')
        self.resize(250, 150)
        self.progress_bar = QProgressBar(self)
        self.init_ui()

    def init_ui(self):

        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.show()

        start_btn = QPushButton('进度条开始变化', self)
        start_btn.move(50, 50)
        start_btn.clicked.connect(self.start_progress)

    def start_progress(self):
        for i in range(101):
            time.sleep(0.1)
            self.progress_bar.setValue(i)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
