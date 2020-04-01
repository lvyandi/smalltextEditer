# -*- coding:utf-8 -*-

# Copyright(C), 2019-2019, QiTech. Co.,Ltd.
# FileName : textedit.py
# Author : lvyandi
# Version : 0.10
# Date : 2020/3/30
# Description :
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit


class MyTextEdit(QTextEdit):
    def __init__(self, e):
        super().__init__(e)



    def keyPressEvent(self, e):
        # 获取输入框事件
        print(e.key())
        print(e.__dict__)
        if e.key() == Qt.Key_Up:
            pass



