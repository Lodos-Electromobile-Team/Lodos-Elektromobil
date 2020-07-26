# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LodosUiProject/klavye.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsBlurEffect
from pynput.keyboard import Key, Controller

class Ui_klavye(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_klavye,self).__init__(parent)

        self.keyboard = Controller()

        self.setObjectName("klavye")
        self.resize(800, 240)
        self.setStyleSheet("#bg{\n"
"    border-image: url(:/res/blur-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.bg = QtWidgets.QLabel(self)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 231))
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(150) 
        self.bg.setGraphicsEffect(self.blur_effect)

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 30, 50, 50))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(170, 30, 50, 50))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 30, 50, 50))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 30, 50, 50))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 30, 50, 50))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(689, 30, 71, 121))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(lambda: self.press(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.press(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.press(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.press(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.press(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(self.enter)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_4.setText(_translate("klavye", "L"))
        self.pushButton.setText(_translate("klavye", "A"))
        self.pushButton_3.setText(_translate("klavye", "M"))
        self.pushButton_2.setText(_translate("klavye", "S"))
        self.pushButton_5.setText(_translate("klavye", "E"))
        self.pushButton_6.setText(_translate("klavye", ":)"))
        
    def press(self, key):
        self.keyboard.press(key)

    def enter(self):
        self.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    klavye = QtWidgets.QWidget()
    ui = Ui_klavye()
    ui.setupUi(klavye)
    klavye.show()
    sys.exit(app.exec_())

