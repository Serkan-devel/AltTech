# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 484)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 3, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 662, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHello = QtWidgets.QMenu(self.menuBar)
        self.menuHello.setObjectName("menuHello")
        self.menuYou = QtWidgets.QMenu(self.menuBar)
        self.menuYou.setObjectName("menuYou")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDo_things = QtWidgets.QAction(MainWindow)
        self.actionDo_things.setObjectName("actionDo_things")
        self.actionPink_Floyd = QtWidgets.QAction(MainWindow)
        self.actionPink_Floyd.setObjectName("actionPink_Floyd")
        self.menuHello.addAction(self.actionDo_things)
        self.menuYou.addAction(self.actionPink_Floyd)
        self.menuBar.addAction(self.menuHello.menuAction())
        self.menuBar.addAction(self.menuYou.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuHello.setTitle(_translate("MainWindow", "Hello"))
        self.menuYou.setTitle(_translate("MainWindow", "You"))
        self.actionDo_things.setText(_translate("MainWindow", "Do things!"))
        self.actionPink_Floyd.setText(_translate("MainWindow", "Pink Floyd"))
