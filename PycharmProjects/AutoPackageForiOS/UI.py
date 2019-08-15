#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QLabel, QApplication, QLabel, QAction, QMessageBox, QFrame, QLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit)

from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt
import PyQt5.QtCore

from Source import *


class AutoPackage(QWidget):

    def __init__(self):
        super().__init__()
        self.archive = AutoArchive(self)
        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.tipLabel = QLabel(self)
        self.tipLabel.setAlignment(Qt.AlignCenter)
        self.tipLabel.setFrameShape(QFrame.Panel)
        self.tipLabel.setText('请耐心填好下面配置')

        # 创建一个PushButton并为他设置一个tooltip
        self.uploadButton = QPushButton('一键打包', self)
        self.uploadButton.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.sizeHint()显示默认尺寸
        self.uploadButton.resize(self.uploadButton.sizeHint())
        # self._thread = MyThread(self)
        # self._thread.updated.connect(self.showLog)
        # self.uploadButton.clicked.connect(self._thread.start)
        self.archive.updated.connect(self.showLog)
        self.uploadButton.clicked.connect(self.archive.start)

        # 日志框
        self.logEdit = QTextEdit()
        # logEdit.setPlainText()
        self.logEdit.setReadOnly(True)

        grid = QGridLayout()
        grid.addWidget(self.tipLabel)
        grid.addWidget(self.uploadButton)
        grid.addWidget(self.logEdit)

        grid.setSpacing(20)
        self.setLayout(grid)


        self.setGeometry(300, 300, 375, 667)
        self.setWindowTitle('iOS自动打包小助手 Author:linlufeng')
        self.show()

    def upload(self):
        self.archive.startArchive()

    def showLog(self, str):
        self.logEdit.append(str)
        self.logEdit.moveCursor(QTextCursor.Down)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '感谢使用',
                                     "感谢使用,是否退出?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AutoPackage()
    sys.exit(app.exec_())