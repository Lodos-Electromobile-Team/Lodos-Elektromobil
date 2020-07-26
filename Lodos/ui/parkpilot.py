# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LodosUiProject/parkpilot.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Park_Pilot(object):
    def setupUi(self, Park_Pilot):
        Park_Pilot.setObjectName("Park_Pilot")
        Park_Pilot.resize(200, 480)
        Park_Pilot.setStyleSheet("#bg{\n"
"    border: 2px solid white;\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"#car{\n"
"    border-image: url(:/res/parkpilot/aracUsttenMavi.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sol1{\n"
"    border-image: url(:/res/parkpilot/sol1.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sol2{\n"
"    border-image: url(:/res/parkpilot/sol2.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sol3{\n"
"    border-image: url(:/res/parkpilot/sol3.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sol4{\n"
"    border-image: url(:/res/parkpilot/sol4.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sol5{\n"
"    border-image: url(:/res/parkpilot/sol5.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"\n"
"#sag1{\n"
"    border-image: url(:/res/parkpilot/sag1.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sag2{\n"
"    border-image: url(:/res/parkpilot/sag2.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sag3{\n"
"    border-image: url(:/res/parkpilot/sag3.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sag4{\n"
"    border-image: url(:/res/parkpilot/sag4.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"#sag5{\n"
"    border-image: url(:/res/parkpilot/sag5.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"")
        self.sol1 = QtWidgets.QLabel(Park_Pilot)
        self.sol1.setGeometry(QtCore.QRect(30, 360, 70, 20))
        self.sol1.setText("")
        self.sol1.setObjectName("sol1")
        self.sol2 = QtWidgets.QLabel(Park_Pilot)
        self.sol2.setGeometry(QtCore.QRect(25, 370, 75, 20))
        self.sol2.setText("")
        self.sol2.setObjectName("sol2")
        self.sol3 = QtWidgets.QLabel(Park_Pilot)
        self.sol3.setGeometry(QtCore.QRect(20, 380, 80, 20))
        self.sol3.setText("")
        self.sol3.setObjectName("sol3")
        self.sol4 = QtWidgets.QLabel(Park_Pilot)
        self.sol4.setGeometry(QtCore.QRect(15, 390, 85, 20))
        self.sol4.setText("")
        self.sol4.setObjectName("sol4")
        self.sol5 = QtWidgets.QLabel(Park_Pilot)
        self.sol5.setGeometry(QtCore.QRect(10, 400, 90, 20))
        self.sol5.setText("")
        self.sol5.setObjectName("sol5")
        self.sag1 = QtWidgets.QLabel(Park_Pilot)
        self.sag1.setGeometry(QtCore.QRect(100, 360, 70, 20))
        self.sag1.setText("")
        self.sag1.setObjectName("sag1")
        self.sag2 = QtWidgets.QLabel(Park_Pilot)
        self.sag2.setGeometry(QtCore.QRect(100, 370, 75, 20))
        self.sag2.setText("")
        self.sag2.setObjectName("sag2")
        self.sag3 = QtWidgets.QLabel(Park_Pilot)
        self.sag3.setGeometry(QtCore.QRect(100, 380, 80, 20))
        self.sag3.setText("")
        self.sag3.setObjectName("sag3")
        self.sag4 = QtWidgets.QLabel(Park_Pilot)
        self.sag4.setGeometry(QtCore.QRect(100, 390, 85, 20))
        self.sag4.setText("")
        self.sag4.setObjectName("sag4")
        self.sag5 = QtWidgets.QLabel(Park_Pilot)
        self.sag5.setGeometry(QtCore.QRect(100, 400, 90, 20))
        self.sag5.setText("")
        self.sag5.setObjectName("sag5")
        self.car = QtWidgets.QLabel(Park_Pilot)
        self.car.setGeometry(QtCore.QRect(20, 30, 160, 350))
        self.car.setText("")
        self.car.setObjectName("car")
        self.bg = QtWidgets.QLabel(Park_Pilot)
        self.bg.setGeometry(QtCore.QRect(0, 0, 200, 480))
        self.bg.setText("")
        self.bg.setObjectName("bg")

        self.retranslateUi(Park_Pilot)
        QtCore.QMetaObject.connectSlotsByName(Park_Pilot)

    def retranslateUi(self, Park_Pilot):
        _translate = QtCore.QCoreApplication.translate
        Park_Pilot.setWindowTitle(_translate("Park_Pilot", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Park_Pilot = QtWidgets.QWidget()
    ui = Ui_Park_Pilot()
    ui.setupUi(Park_Pilot)
    Park_Pilot.show()
    sys.exit(app.exec_())

