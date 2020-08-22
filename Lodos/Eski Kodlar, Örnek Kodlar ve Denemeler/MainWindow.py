
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

import app
from ui import res_rc, Main_Window

class MainWindow(QMainWindow, Main_Window.Ui_MainWindow, app.Application):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowTitle("Lodos Electromobile")
        self.timer = QTimer(self)

        self.lastSinyal = 0
        self.sinyal = False

        """
        self.btnBackCam.clicked.connect(self.backCamShow)
        self.btnBataryaDurum.clicked.connect(self.batteryStatisticShow)
        self.btnBtSettings.clicked.connect(self.BtSettingsShow)
        """
        
        self.btnSolSinyal.clicked.connect(lambda: serial.mesajGonder('1'))
        self.btnSolSinyal.clicked.connect(lambda: self.setSinyal(1))

        self.btnSagSinyal.clicked.connect(lambda: self.mesajGonder('2'))
        self.btnSagSinyal.clicked.connect(lambda: self.setSinyal(2))

        self.btnDortlu.clicked.connect(lambda: self.mesajGonder('3'))
        self.btnDortlu.clicked.connect(lambda: self.setSinyal(3))

        self.timer.timeout.connect(self.sinyalVer)

        self.show()


        # self.btnFar.mouseReleaseEvent = self.farClick
    """
    def backCamShow(self):
        bc.startStream()
        # bc.showFullScreen()
        bc.show()

    def batteryStatisticShow(self):
        # battery.showFullScreen()
        battery.show()

    def bluetoothSettingsShow(self):
        # bluetoothStn.showFullScreen()
        bluetoothStn.show()
    """
    def setSinyal(self, sinyal):
        if mySerial.serialPort.isOpen() or 1 == 1:
            self.sinyal = False
            self.sinyal = False
        
            self.btnSolSinyal.setStyleSheet("#btnSolSinyal{\n"
                                            "    background-image: url(:/res/solSinyal.png);\n"
                                            "    background-color:transparent;\n"
                                            "}\n"
                                            "#btnSolSinyal:hover{\n"
                                            "    background-image: url(:/res/solSinyalHovered.png);\n"
                                            "    background-color:transparent;\n"
                                            "}")
            self.btnSagSinyal.setStyleSheet("#btnSagSinyal{\n"
                                            "    background-image: url(:/res/sagSinyal.png);\n"
                                            "    background-color:transparent;\n"
                                            "}\n"
                                            "#btnSagSinyal:hover{\n"
                                            "    background-image: url(:/res/sagSinyalHovered.png);\n"
                                            "    background-color:transparent;\n"
                                            "}")
            if self.lastSinyal == 0:
                self.sinyalVer()
                self.timer.start(700)
            if self.lastSinyal == sinyal:
                self.timer.stop()
                self.lastSinyal = 0
                return
            else:
                self.lastSinyal = sinyal
        else:
            print("Seri Port Bağlı Değil.")

    def sinyalVer(self):
        if self.lastSinyal == 1:
            if not self.sinyal:
                self.btnSolSinyal.setStyleSheet("#btnSolSinyal{\n"
                                                "    background-image: url(:/res/solSinyalActivated.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
            elif self.sinyal:
                self.btnSolSinyal.setStyleSheet("#btnSolSinyal{\n"
                                                "    background-image: url(:/res/solSinyal.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
            self.sinyal = not self.sinyal
        elif self.lastSinyal == 2:
            if not self.sinyal:
                self.btnSagSinyal.setStyleSheet("#btnSagSinyal{\n"
                                                "    background-image: url(:/res/sagSinyalActivated.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
            elif self.sinyal:
                self.btnSagSinyal.setStyleSheet("#btnSagSinyal{\n"
                                                "    background-image: url(:/res/sagSinyal.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
            self.sinyal = not self.sinyal
        elif self.lastSinyal == 3:
            if not self.sinyal:
                self.btnSolSinyal.setStyleSheet("#btnSolSinyal{\n"
                                                "    background-image: url(:/res/solSinyalActivated.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
                self.btnSagSinyal.setStyleSheet("#btnSagSinyal{\n"
                                                "    background-image: url(:/res/sagSinyalActivated.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
            elif self.sinyal:
                self.btnSolSinyal.setStyleSheet("#btnSolSinyal{\n"
                                                "    background-image: url(:/res/solSinyal.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
                self.btnSagSinyal.setStyleSheet("#btnSagSinyal{\n"
                                                "    background-image: url(:/res/sagSinyal.png);\n"
                                                "    background-color:transparent;\n"
                                                "}")
            self.sinyal = not self.sinyal

    def updateUi(self, hiz):
        self.ledHizGosterge.display(hiz)
