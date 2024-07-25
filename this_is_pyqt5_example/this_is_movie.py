import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie

"""

这是一个动图展示的的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMovie_Example')
        self.resize(1800, 1000)
        self.init_ui()

    def init_ui(self):
        label = QLabel(self)
        label.setGeometry(30, 30, 837, 647)  # 大小可根据图片大小调整
        gif = QMovie(r"C:\img\gif.gif")  # 替换为自己本地的图片路径即可
        label.setMovie(gif)
        gif.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
