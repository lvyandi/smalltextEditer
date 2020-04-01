# -*- coding:utf-8 -*-

# Copyright(C), 2019-2019, QiTech. Co.,Ltd.
# FileName : testMain.py
# Author : lvyandi
# Version : 0.10
# Date : 2020/3/30
# Description :


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.my_UI()

    def my_UI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('事件处理')
        self.show()

    def keyPressEvent(self, e):  # 重写keyPressEvent()事件处理函数
        # 如果我们点击了Esc按钮，应用将会被终止。
        print(e)
        print(e.key())
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
