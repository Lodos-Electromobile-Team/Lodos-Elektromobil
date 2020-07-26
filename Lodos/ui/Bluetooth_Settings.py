# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LodosUiProject/Bluetooth_Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-image: url(:/res/boss.png);\n"
"}\n"
"\n"
"#listDevices{\n"
"    font-size:25px;\n"
"    font-weight: bold;\n"
"    background-color: darkgray;\n"
"    border: 2px solid red;\n"
"    border-radius:10px;\n"
"    padding: 5px 0;\n"
"    color:white;\n"
"}\n"
"#listDevices::item::selected{\n"
"    background-color: darkred;\n"
"}\n"
"\n"
"#lblBluetoothStatus{\n"
"    color:white;\n"
"    font-size:30px;\n"
"    font-weight: bold;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBackMain = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackMain.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.btnBackMain.setObjectName("btnBackMain")
        self.lblBluetoothStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblBluetoothStatus.setGeometry(QtCore.QRect(180, 30, 441, 31))
        self.lblBluetoothStatus.setText("")
        self.lblBluetoothStatus.setObjectName("lblBluetoothStatus")
        self.btnBluetoothSwitch = CustomSwitch(self.centralwidget)
        self.btnBluetoothSwitch.setGeometry(QtCore.QRect(70, 10, 111, 61))
        self.btnBluetoothSwitch.setObjectName("btnBluetoothSwitch")
        self.listDevices = QtWidgets.QListWidget(self.centralwidget)
        self.listDevices.setGeometry(QtCore.QRect(30, 90, 531, 361))
        self.listDevices.setObjectName("listDevices")
        self.btnTara = QtWidgets.QPushButton(self.centralwidget)
        self.btnTara.setGeometry(QtCore.QRect(640, 20, 121, 51))
        self.btnTara.setObjectName("btnTara")
        self.btnBaglan = QtWidgets.QPushButton(self.centralwidget)
        self.btnBaglan.setGeometry(QtCore.QRect(640, 80, 121, 51))
        self.btnBaglan.setObjectName("btnBaglan")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBackMain.setText(_translate("MainWindow", "<--"))
        self.btnTara.setText(_translate("MainWindow", "Tara"))
        self.btnBaglan.setText(_translate("MainWindow", "Bağlan"))

from ui.customswitch import CustomSwitch

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

