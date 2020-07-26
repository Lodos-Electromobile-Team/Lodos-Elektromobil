# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LodosUiProject/klavye.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_klavye(object):
    def setupUi(self, klavye):
        klavye.setObjectName("klavye")
        klavye.resize(800, 240)
        klavye.setStyleSheet("#bg{\n"
"    border-image: url(:/res/blur-bg.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.bg = QtWidgets.QLabel(klavye)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 240))
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.pushButton_4 = QtWidgets.QPushButton(klavye)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 30, 50, 50))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(klavye)
        self.pushButton.setGeometry(QtCore.QRect(170, 30, 50, 50))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(klavye)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 30, 50, 50))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(klavye)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 30, 50, 50))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(klavye)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 30, 50, 50))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(klavye)
        self.pushButton_6.setGeometry(QtCore.QRect(689, 30, 71, 121))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(klavye)
        QtCore.QMetaObject.connectSlotsByName(klavye)

    def retranslateUi(self, klavye):
        _translate = QtCore.QCoreApplication.translate
        klavye.setWindowTitle(_translate("klavye", "Form"))
        self.pushButton_4.setText(_translate("klavye", "L"))
        self.pushButton.setText(_translate("klavye", "A"))
        self.pushButton_3.setText(_translate("klavye", "M"))
        self.pushButton_2.setText(_translate("klavye", "S"))
        self.pushButton_5.setText(_translate("klavye", "E"))
        self.pushButton_6.setText(_translate("klavye", ":)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    klavye = QtWidgets.QWidget()
    ui = Ui_klavye()
    ui.setupUi(klavye)
    klavye.show()
    sys.exit(app.exec_())

