import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QListView

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
        self.combo_box = QComboBox(self)
        self.combo_box.addItem('第一个')
        self.combo_box.addItem('第二个')
        self.combo_box.addItems(['第三个', '第四个', '第五个', '第六个', '第七个'])  # 一次性添加多个
        self.combo_box.setCurrentText('第二个')  # 设置默认选中
        self.combo_box.setCurrentIndex(0)  # 设置默认选中的索引

        # 设置下拉框的样式
        list_view = QListView()
        self.combo_box.setView(list_view)
        self.combo_box.setStyleSheet(
            "QComboBox QAbstractItemView::item{height:30px}"  # 每个项的间距
            "QComboBox QAbstractItemView{font-size:15px}"  # 字体的大小
        )

        self.combo_box.currentTextChanged.connect(self.is_check)

    def is_check(self, text):
        print("你选择了:", text)  # 获取选中的文本


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
