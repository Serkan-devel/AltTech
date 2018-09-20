import sys
from PyQt5.QtWidgets import QTextEdit, QWidget, QApplication, QShortcut, QGridLayout
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import pyqtSlot
from mindsapi import mindsapi
import os
import sys
import subprocess

def run(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return result.stdout.readline().decode('utf8')

class App(QWidget):

    def __init__(self):
        super().__init__()

        username = os.environ['MINDS_USER']
        password = os.environ['MINDS_PW']
        self.api = mindsapi.MindsAPI(username, password)
        self.api.login()

        self.title = 'Post to Minds'
        self.setWindowTitle(self.title)

        self.textbox = QTextEdit(self)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Return"), self)
        self.shortcut.activated.connect(self.on_click)

        grid = QGridLayout()
        grid.setSpacing(0)
        grid.addWidget(self.textbox)
        self.setLayout(grid)

        self.setGeometry(100, 100, 400, 300)
        self.show()

    @pyqtSlot()
    def on_click(self):
        text = self.textbox.toPlainText()
        #self.api.post_custom(message=text)
        run("echo '"+ text +"' | ./render_text.py ")
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
