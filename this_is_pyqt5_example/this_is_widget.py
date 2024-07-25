import sys
from PyQt5.QtWidgets import QApplication, QWidget

"""

这是一个窗口的例子

"""


class Window(QWidget):
    pass


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
