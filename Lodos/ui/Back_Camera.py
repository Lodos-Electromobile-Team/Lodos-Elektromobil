# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LodosUiProject/Back_Camera.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 480)
        Form.setStyleSheet("#Form{\n"
"    background-color: black;\n"
"}\n"
"\n"
"#lblError{\n"
"    color: white;\n"
"}")
        self.lblError = QtWidgets.QLabel(Form)
        self.lblError.setGeometry(QtCore.QRect(0, 0, 800, 480))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblError.setFont(font)
        self.lblError.setScaledContents(False)
        self.lblError.setAlignment(QtCore.Qt.AlignCenter)
        self.lblError.setObjectName("lblError")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.pushButton.setObjectName("pushButton")
        self.lblVideo = QtWidgets.QLabel(Form)
        self.lblVideo.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.lblVideo.setText("")
        self.lblVideo.setObjectName("lblVideo")
        self.widget = parkpilot(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 200, 480))
        self.widget.setObjectName("widget")
        self.lblError.raise_()
        self.lblVideo.raise_()
        self.pushButton.raise_()
        self.widget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblError.setText(_translate("Form", "Kameraya Bağlanamıyor!"))
        self.pushButton.setText(_translate("Form", "<--"))

from ui.parkpilotX import parkpilot

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

