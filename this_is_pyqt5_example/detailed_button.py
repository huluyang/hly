import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

"""

这是一个按钮的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QPushButton_Example')
        self.resize(250, 150)

        self.init_ui()

    def init_ui(self):
        btn = QPushButton('我是按钮', self)

        # btn.setText('我是按钮啊') # 单独设置按钮的文本

        # btn.setStyleSheet('background-color:red;color:white;')  # 设置按钮的背景颜色样式 第一种写法

        # btn.setStyleSheet('QPushButton{background-color:red;color:white;}')  # 第二种写法

        # btn.setStyleSheet('QPushButton{background-color: rgb(255, 100, 255)}')  # 也可以使用rgb颜色

        # 第三种写法（这个一般用在控件较多界面较复杂 使用以上两种失效或出现混乱或需要独立设置变化时）
        # btn.setObjectName("btn")
        # btn.setStyleSheet(
        #     '#btn{background-color:red}'
        #     '#btn{color:white}'
        # )

        # 当鼠标在按钮上时，按钮的背景颜色变成红色
        # btn.setStyleSheet(
        #     ':hover{background-color:red}'
        # )

        # 按钮增加背景图片(将c:/images/1.png替换为自己本地图片路径即可) 一般用于制作自定义按钮border-image是自适用图片 常用！！
        # background-image不会自适应图片 可自行测试看下效果
        # btn.setStyleSheet(
        #     'QPushButton{border-image:url(c:/images/1.png)}'
        # )

        btn.clicked.connect(self.show_message)

    def show_message(self):
        print('按钮被点击了')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
