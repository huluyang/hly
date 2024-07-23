import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

"""

这是一个表格的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTableWidget_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        table_widget = QTableWidget(self)
        table_widget.setRowCount(2)
        table_widget.setColumnCount(2)
        table_widget.setItem(0, 0, QTableWidgetItem('第一行的第一列'))
        table_widget.setItem(0, 1, QTableWidgetItem('第一行的第二列'))
        table_widget.setItem(1, 0, QTableWidgetItem('第二行的第一列'))
        table_widget.setItem(1, 1, QTableWidgetItem('第二行的第二列'))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
