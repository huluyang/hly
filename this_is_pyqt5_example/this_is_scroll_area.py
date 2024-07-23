import sys

from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QTableWidgetItem, QFrame, QLabel, QVBoxLayout

"""

这是一个滚动窗口的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QScrollArea_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        frame = QFrame()
        frame_layout = QVBoxLayout(frame)  # 垂直布局（就是按照垂直的顺序从上向下排列的布局）
        for i in range(20):
            label = QLabel("第{}个".format(i))
            label.move(0, i * 20)
            frame_layout.addWidget(label)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(frame)





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
