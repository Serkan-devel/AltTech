#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import\
    QApplication,\
    QWidget,\
    QPlainTextEdit,\
    QGridLayout,\
    QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot
from mindsapi import mindsapi
import sys
import subprocess


def run(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return result.stdout.readline().decode('utf8')


class App(QWidget):
    def __init__(self):
        super().__init__()

        config = mindsapi.MindsAPI.get_config()
        self.api = mindsapi.MindsAPI(
            config['minds']['user'],
            config['minds']['password'])
        self.api.login()

        self.title = 'Post to Minds'
        self.setWindowTitle(self.title)

        self.textbox = QPlainTextEdit(self)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        self.shortcut.activated.connect(self.on_click)

        grid = QGridLayout()
        grid.setSpacing(0)
        grid.addWidget(self.textbox)
        self.setLayout(grid)

        self.setGeometry(100, 100, 300, 200)
        self.show()

    @pyqtSlot()
    def on_click(self):
        text = self.textbox.toPlainText()
        text = text.replace("'", "’")
        run("echo '" + text + "' | ./post_text2image.py")
        self.textbox.setPlainText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
