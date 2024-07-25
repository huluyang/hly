import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGraphicsOpacityEffect

"""

这是一个介绍大部分控件通用函数的例子  这里只是拿QLabel举例说明 可以随意替换为其他控件 比如 按钮

"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Genera_Example')
        self.resize(250, 150)
        self.init_ui()

    def init_ui(self):
        label = QLabel('我是显示的文本', self)
        label.setStyleSheet('background-color:rgb(255,0,0)')  # 这里设置控件的背景颜色 以方便查看我们重新设置的控件的大小

        label.resize(180, 27)  # 设置控件的大小 180为宽度（也就是大白话中的长度） 27为高度（也就是大白话中的宽度）  可以简单的理解为XY轴

        label.move(77, 78)  # 设置控件的位置 这里表示的是以整个窗口的左上角为原点 77为x轴的偏移量 78为y轴的偏移量

        label_size = label.size()  # 读取控件的大小
        print("整体大小为：", label_size, "宽度为：", label_size.height(), "长度为：", label_size.width())

        label.setGeometry(77, 78, 180, 27)  # 设置控件的位置和大小 这里的77为x轴的偏移量 78为y轴的偏移量 180为宽度 27为高度

        label.hide()  # 设置控件为隐藏不显示  一般在比较复杂的需求中 根据需求进行隐藏和显示

        label.show()  # 设置控件为显示  大部分控件一般默认的都是显示的

        label.setText('我是新的文本')  # 设置控件的文本内容 比如 按钮、单选框、多选框等控件上面显示的文字

        label.setAlignment(Qt.AlignCenter)  # 设置控件的文本居中

        label.setToolTip("这是鼠标长时间放在这里的提示信息")  # 设置控件的提示信息

        label.isVisible()  # 判断控件是否可见 主要用于大型项目的判断 如果隐藏就显示 如果显示就隐藏 一类的需求

        label.showNormal()  # 设置控件为正常显示 一般用于窗口被用户最大化之后恢复窗口初始化时的的大小

        label.setEnabled(True)  # 设置控件是否可用 一般用于在满足一些条件的情况下比如输入框输入了正确的内容之后 某些按钮控件才可以被点击

        # 设置控件的透明度
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.1)
        label.setGraphicsEffect(op)

        print(label.text())  # 获取控件的文本内容

        label.mousePressEvent = self.mouse_press  # 设置控件的鼠标点击事件(就是点击鼠标的时候触发的函数)

        label.mouseReleaseEvent = self.mouse_release  # 设置控件的鼠标释放事件（就是松开鼠标的时候触发的函数）

        label.mouseMoveEvent = self.mouse_move  # 设置控件的鼠标移动事件（就是移动鼠标的时候触发的函数）

        label.leaveEvent = self.leave_event  # 设置控件的鼠标离开事件（就是鼠标离开控件的时候触发的函数）

        label.enterEvent = self.enter_event  # 设置控件的鼠标进入事件（就是鼠标进入控件的时候触发的函数）

        # 注意 这里的键盘事件是针对整个窗口的 并不是所有的控件都可以使用这个事件的窗口
        self.keyPressEvent = self.key_press  # 设置控件的键盘按下事件（就是按下键盘的时候触发的函数）

        self.keyReleaseEvent = self.key_release  # 设置控件的键盘释放事件（就是松开键盘的时候触发的函数）

        # 以下为设置控件的样式案例
        label.setStyleSheet('background-color:rgb(255,0,0)')  # 设置控件的背景颜色
        label.setStyleSheet('color:rgb(0,0,0)')  # 设置控件的文本颜色
        '''文本字体
                font
                font-size
                font-style:normal(标准字体)  italic(斜体)  oblique()
                font-weight:normal(标准字体==400)  bold(加粗字体==700)  bolder(更粗字体)  lighter(更细字体)  100-900
                color
        '''

        label.setStyleSheet('font-size:20px')  # 设置控件的字体大小
        label.setStyleSheet('font-family:微软雅黑')  # 设置控件的字体
        label.setStyleSheet('font-weight:bold')  # 设置控件的字体加粗
        label.setStyleSheet('font-style:italic')  # 设置控件的字体倾斜
        label.setStyleSheet('background-image:url(c:/image/1.jpg)')  # 设置控件的背景图片
        # border 表示边框
        label.setStyleSheet('border-image:url(c:/image/1.jpg)')  # 设置控件的背景图片  建议使用
        label.setStyleSheet(':hover{background-color:rgb(0,0,0)}')  # 设置控件的鼠标悬停时候的背景颜色
        label.setStyleSheet('border:1px solid rgb(0,0,0)')  # 设置控件的边框 solid 表示实线
        label.setStyleSheet(  # 注意多个样式的时候需要在每一个样式后面添加一个分号 否则不会生效
            'border: 7px;'
            'border-style: solid;'
            'border-radius: 5px;'
        )  # border-radius为设置边框的圆角

        label.setStyleSheet('QLabel{background-color:red;color:white;}')  # 第二种写法

        # 第三种写法（这个一般用在控件较多界面较复杂 使用以上两种失效或出现混乱或需要独立设置变化时）
        label.setObjectName("btn")
        label.setStyleSheet(
            '#btn{background-color:red}'
            '#btn{color:white}'
        )

    def mouse_press(self, event):
        print("鼠标点击我了，想自定义干点儿啥请自由发挥")
        print(event.button())  # 获取鼠标点击的按钮 0为左键 4为中键 2为右键 也可以使用下面的方式进行判断
        if event.button() == Qt.LeftButton:
            print("你点击了左键")
        elif event.button() == Qt.RightButton:
            print("你点击了右键")

    def mouse_release(self, event):  # 同上方mouse_press中的使用方法获取event
        print("鼠标释放我了，想自定义干点儿啥请自由发挥")

    def mouse_move(self, event):
        print("鼠标在移动了，想自定义干点儿啥请自由发挥")
        print("鼠标目前的坐标为：", event.pos(), "鼠标目前的坐标x轴的值为：", event.pos().x(), "鼠标目前的坐标y轴的值为：",
              event.pos().y())

    def enter_event(self, event):
        print("鼠标进入我了，想自定义干点儿啥请自由发挥")
        print("鼠标目前的坐标为：", event.pos(), "鼠标目前的坐标x轴的值为：", event.pos().x(), "鼠标目前的坐标y轴的值为：",
              event.pos().y())

    def leave_event(self, event):  # 这里离开了就不能通过event.pos()获取鼠标的坐标了会报错 因为离开了 不在监控范围了
        print("鼠标离开我了，想自定义干点儿啥请自由发挥")

    def key_press(self, event):
        print("有键盘按键按下了，想自定义干点儿啥请自由发挥")
        print("按下的键为：", event.key())
        if event.key() == Qt.Key_A:
            print("你按下了A键")
        elif event.key() == Qt.Key_B:
            print("你按下了B键")
        elif event.key() == Qt.Key_C:
            print("你按下了C键")
        elif event.key() == Qt.Key_D:
            print("你按下了D键")

    def key_release(self, event):
        print("有键盘按键被释放了，想自定义干点儿啥请自由发挥")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
