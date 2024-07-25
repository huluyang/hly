import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

"""

这是一个窗口的例子

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 继承父类
        self.setWindowTitle("这是窗口的标题")  # 设置窗口的标题
        self.setWindowIcon(QIcon("C:/img/img.png"))  # 设置窗口的图标(替换为自己本地图片路径即可)
        self.resize(700, 700)  # 设置窗口的大小

        # # 设置窗口的最大和最小高度和宽度 一般用于窗口可以自适应大小的情况下 限制其最大和最小的尺寸 避免导致窗口内一些布局或者组件不显示或不正常
        # self.setMaximumHeight(100)  # 设置窗口的最大高度
        # self.setMaximumWidth(200)  # 设置窗口的最大宽度
        # self.setMaximumSize(100, 200)  # 设置窗口的最大尺寸
        # self.setMinimumHeight(10)  # 设置窗口的最小高度
        # self.setMinimumWidth(20)  # 设置窗口的最小宽度
        # self.setMinimumSize(10, 20)  # 设置窗口的最小尺寸
        # self.setFixedSize(300, 300)  # 设置窗口的固定尺寸 这个是将上面的最大和最小尺寸同时设置为同一个值 也就是说窗口不能改变大小

        # setWindowFlag后面的布尔值默认为True 表示显示
        # self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)  # 禁止窗口最小化按钮  就是最小化的按钮不显示了
        # self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)  # 禁止窗口最大化按钮  就是最大化的按钮不显示了
        # self.setWindowFlag(Qt.WindowCloseButtonHint, False)  # 禁止窗口关闭按钮  就是关闭的按钮不显示了
        # self.setWindowFlag(Qt.WindowContextHelpButtonHint, True)  # 禁止窗口帮助按钮  这个在QWidget控件没有
        # self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)  # 禁止窗口最大化和最小化按钮
        # self.setWindowFlag(Qt.WindowSystemMenuHint, True)  # 禁止窗口系统菜单  这个在QWidget控件没有
        # self.setWindowFlag(Qt.FramelessWindowHint, True)  # 禁止窗口的边框 这个适用于自己自定义整体窗口 请添加控件查看效果
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 窗口置顶 就是始终在最上层显示在最前面
        # self.setWindowFlag(Qt.Tool, True)  # 设置窗口为工具窗口 这个设置使程序不会在任务栏显示
        # self.setWindowFlags(Qt.Tool | Qt.WindowCloseButtonHint)  # 这个是设置多个的窗口属性

        # 设置窗体透明控件不透明 一般和self.setWindowFlag(Qt.FramelessWindowHint, True)一起使用 可自行添加控件并添加控件的背景颜色方便查看效果
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # self.showNormal()  # 窗口正常显示  主要用于窗口最小化后恢复窗口
        # self.showMinimized()  # 窗口最小化
        # self.showMaximized()  # 窗口最大化
        # self.setWindowOpacity(0.5)  # 设置窗口的透明度


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
