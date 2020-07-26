# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LodosUiProject/Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("#ledHizGosterge{\n"
"    background-color:None;\n"
"}\n"
"#ledHizGosterge:hover{\n"
"    border: 2px solid red;\n"
"  border-radius: 25px;\n"
"    background-color:gray;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-image: url(:/res/bg.png);\n"
"    background-repeat: no-repeat;\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#btnSagSinyal{\n"
"    background-image: url(:/res/sagSinyal.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnSagSinyal:hover{\n"
"    background-image: url(:/res/sagSinyalHovered.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnSolSinyal{\n"
"    background-image: url(:/res/solSinyal.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnSolSinyal:hover{\n"
"    background-image: url(:/res/solSinyalHovered.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"\n"
"#btnDortlu{\n"
"    background-image: url(:/res/dortlu.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnDortlu:hover{\n"
"    background-image: url(:/res/dortluHovered.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnBackCam{\n"
"    background-image: url(:/res/btnGeri.png);\n"
"    background-color:transparent;\n"
"}\n"
"#btnBackCam:hover{\n"
"    background-image: url(:/res/btnGeriSelected.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnBataryaDurum{\n"
"    background-image: url(:/res/btnBatteryStatistic.png);\n"
"    background-color:transparent;\n"
"}\n"
"#btnBataryaDurum:hover{\n"
"    background-image: url(:/res/btnBatteryStatisticSelected.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnFar{\n"
"    background-image: url(:/res/btnFar.png);\n"
"    background-color:transparent;\n"
"}\n"
"#btnFar:hover{\n"
"    background-image: url(:/res/btnFarSelected.png);\n"
"    background-color:transparent;\n"
"}\n"
"#checkBox{\n"
"    background-image: url(:/res/btnFarSelected.png);\n"
"}\n"
"\n"
"#btnBluetoothSettings{\n"
"    background-image: url(:/res/btnBluetooth.png);\n"
"    background-color:transparent;\n"
"}\n"
"#btnBluetoothSettings:hover{\n"
"    background-image: url(:/res/btnBluetoothSelected.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btn{\n"
"    background-image: url(:/res/button.png);\n"
"    background-color:transparent;\n"
"}\n"
"#btn:hover{\n"
"    background-image: url(:/res/button-clicked.png);\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"#btnSettings{\n"
"    background-image: url(:/res/btnAyarlar.png);\n"
"    background-color:transparent;\n"
"}\n"
"#btnSettings:hover{\n"
"    background-image: url(:/res/btnAyarlarSelected.png);\n"
"    background-color:transparent;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBackCam = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackCam.setGeometry(QtCore.QRect(590, 30, 95, 95))
        self.btnBackCam.setText("")
        self.btnBackCam.setObjectName("btnBackCam")
        self.ledHizGosterge = QtWidgets.QLCDNumber(self.centralwidget)
        self.ledHizGosterge.setGeometry(QtCore.QRect(300, 190, 211, 91))
        self.ledHizGosterge.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ledHizGosterge.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ledHizGosterge.setDigitCount(3)
        self.ledHizGosterge.setObjectName("ledHizGosterge")
        self.sarj = QtWidgets.QLabel(self.centralwidget)
        self.sarj.setGeometry(QtCore.QRect(0, 390, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.sarj.setFont(font)
        self.sarj.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sarj.setStyleSheet("color:white")
        self.sarj.setAlignment(QtCore.Qt.AlignCenter)
        self.sarj.setObjectName("sarj")
        self.btnFar = QtWidgets.QPushButton(self.centralwidget)
        self.btnFar.setGeometry(QtCore.QRect(660, 170, 95, 91))
        self.btnFar.setText("")
        self.btnFar.setObjectName("btnFar")
        self.btnSagSinyal = QtWidgets.QPushButton(self.centralwidget)
        self.btnSagSinyal.setGeometry(QtCore.QRect(190, 380, 75, 75))
        self.btnSagSinyal.setText("")
        self.btnSagSinyal.setObjectName("btnSagSinyal")
        self.btnDortlu = QtWidgets.QPushButton(self.centralwidget)
        self.btnDortlu.setGeometry(QtCore.QRect(90, 360, 100, 100))
        self.btnDortlu.setText("")
        self.btnDortlu.setObjectName("btnDortlu")
        self.btnSolSinyal = QtWidgets.QPushButton(self.centralwidget)
        self.btnSolSinyal.setGeometry(QtCore.QRect(10, 380, 75, 75))
        self.btnSolSinyal.setText("")
        self.btnSolSinyal.setObjectName("btnSolSinyal")
        self.btnBataryaDurum = QtWidgets.QPushButton(self.centralwidget)
        self.btnBataryaDurum.setGeometry(QtCore.QRect(110, 30, 95, 95))
        self.btnBataryaDurum.setText("")
        self.btnBataryaDurum.setObjectName("btnBataryaDurum")
        self.btnBluetoothSettings = QtWidgets.QPushButton(self.centralwidget)
        self.btnBluetoothSettings.setGeometry(QtCore.QRect(50, 170, 95, 95))
        self.btnBluetoothSettings.setText("")
        self.btnBluetoothSettings.setObjectName("btnBluetoothSettings")
        self.btnSettings = QtWidgets.QPushButton(self.centralwidget)
        self.btnSettings.setGeometry(QtCore.QRect(700, 380, 95, 91))
        self.btnSettings.setText("")
        self.btnSettings.setObjectName("btnSettings")
        self.widget = Ui_klavye(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 240, 800, 240))
        self.widget.setObjectName("widget")
        self.lineEdit = ClickableLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 30, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sarj.setText(_translate("MainWindow", "97%"))

from ClickableLineEdit import ClickableLineEdit
from ui.klavyeX import Ui_klavye

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

