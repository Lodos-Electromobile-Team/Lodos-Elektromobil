# -*- coding: utf-8 -*-
# QPropertyAnimation
from ui import res_rc, Main_Window, Back_Camera, Battery_Status, Bluetooth_Settings, parkpilot_rc
from ClickableLineEdit import ClickableLineEdit
import pyqtgraph as pg
import numpy as np
import cv2
import qimage2ndarray
import subprocess
# import os
import sys
import serial
import time
import copy
import struct
import collections
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets  # , QtBluetooth as QtBt
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QEvent, QTimer, Qt
from PyQt5.QtGui import QPixmap, QSplashScreen, QProgressBar
# from PyQt5.QtBluetooth import QBluetoothLocalDevice, QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo


class MainWindow(QtWidgets.QMainWindow, Main_Window.Ui_MainWindow):
    def __init__(self, mySerial, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.showFullScreen()
        self.show()
        self.setWindowTitle("Lodos Electromobile")
        self.mySerial = mySerial
        self.timer = QTimer(self)

        self.lastSinyal = 0
        self.sinyal = False

        self.serialConnect()
        mySerial.start()  # thread işlemi başlatıldı.

        self.widget.hide()

        self.btnBackCam.clicked.connect(self.backCamShow)
        self.btnBataryaDurum.clicked.connect(self.batteryStatisticShow)
        self.btnBluetoothSettings.clicked.connect(self.bluetoothSettingsShow)

        self.btnSolSinyal.clicked.connect(lambda: self.mesajGonder('1'))
        self.btnSolSinyal.clicked.connect(lambda: self.setSinyal(1))

        self.btnSagSinyal.clicked.connect(lambda: self.mesajGonder('2'))
        self.btnSagSinyal.clicked.connect(lambda: self.setSinyal(2))

        self.btnDortlu.clicked.connect(lambda: self.mesajGonder('3'))
        self.btnDortlu.clicked.connect(lambda: self.setSinyal(3))

        self.timer.timeout.connect(self.sinyalVer)

        mySerial.updateUiSignal[float].connect(self.updateUi)

        self.lineEdit.clicked.connect(self.showKeyboard)

        
        # self.btnFar.mouseReleaseEvent = self.farClick

    def showKeyboard(self):
        self.widget.show()

    

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

    def click(self, event):
        print("clicked")
        # self.lblFar.setText("Far Açık")

    def mesajGonder(self, mesaj):
        if mySerial.serialPort.isOpen():
            mySerial.serialPort.write(mesaj.encode())
        else:

            print("Seri Port Bağlı Değil.")

    def serialConnect(self):
        self.mySerial.serialPort.baudrate = 9600
        self.mySerial.serialPort.port = "/dev/ttyUSB0"
        # self.mySerial.serialPort.port = "/dev/ttyACM0"  # Deneme
        try:
            # seri porta bağlanma komutu verildi.
            mySerial.serialPort.open()
        except:
            # self.message.append("Bağlantı Hatası!!")
            print("Baglanti Hatasi!!!")

    def serialDisconnect(self):
        if mySerial.serialPort.isOpen():
            mySerial.serialPort.close()
        else:
            self.message.append("Seriport Zaten Kapalı.")


class BackCamWindow(QtWidgets.QWidget, Back_Camera.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.video_size = QtCore.QSize(800, 480)
        self.setupUi(self)
        self.setWindowTitle("Lodos Electromobile")
        self.setupCamera()
        self.timer = QtCore.QTimer()
        self.angle = 0

        self.pushButton.clicked.connect(self.backToMain)
        mySerial.updateWheelStatus[float].connect(self.updateAngle)

    def updateAngle(self, angle):
        self.angle = angle

    def backToMain(self):
        self.timer.stop()
        # main.showFullScreen()
        self.hide()
        cv2.destroyAllWindows()

    def startStream(self):
        self.timer.timeout.connect(self.displayVideoStream)
        self.timer.start(60)

    def setupCamera(self):
        # self.capture = cv2.VideoCapture('http://192.168.1.44')
        self.capture = cv2.VideoCapture(0)
        '''
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,
                         self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,
                         self.video_size.height())
        '''
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
    def displayVideoStream(self):
        _, frame = self.capture.read()
        if frame is None:
            pass
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # frame = cv2.flip(frame, 1)
            pts = np.array([[125, 500], [225, 300], [575, 300], [225, 300],
                            [275, 200], [525, 200], [675, 500]], np.integer)
            cv2.polylines(frame, [pts], False, (0, 0, 150), 4)

            pts = np.array([[125 + (self.angle * 0.2), 500],

                            [225 + (self.angle * 0.5), 300 -
                             (self.angle * 0.1)],
                            [575 + (self.angle * 0.5), 300 +
                             (self.angle * 0.1)],
                            [225 + (self.angle * 0.5), 300 -
                             (self.angle * 0.1)],

                            [275 + (self.angle * 0.9), 200 -
                             (self.angle * 0.2)],
                            [525 + (self.angle * 0.9), 200 +
                             (self.angle * 0.2)],

                            [575 + (self.angle * 0.5), 300 +
                             (self.angle * 0.1)],

                            [675 + (self.angle * 0.2), 500]], np.integer)

            cv2.polylines(frame, [pts], False, (200, 200, 100), 4)

            image = qimage2ndarray.array2qimage(
                frame)  # SOLUTION FOR MEMORY LEAK

            self.lblVideo.setPixmap(QtGui.QPixmap.fromImage(image))
        # time.sleep(0.01)


class BatteryStatus(QtWidgets.QMainWindow, Battery_Status.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Lodos Electromobile")

        pg.setConfigOptions(antialias=True)
        self.graphWidget.setBackground('k')

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [20, 21, 24, 25, 27, 26, 25, 28, 27, 28]
        pen = pg.mkPen(color=(255, 0, 0), width=2)

        self.graphWidget.plot(hour, temperature, pen=pen)
        self.btnBackMain.clicked.connect(self.backToMain)

    def backToMain(self):
        # main.showFullScreen()
        self.hide()


class BluetoothSettings(QtWidgets.QMainWindow, Bluetooth_Settings.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        subprocess.check_output("rfkill unblock bluetooth", shell=True)
        
        
        self.nearby_devices = []


        self.btnBackMain.clicked.connect(self.backToMain)
        self.btnBluetoothSwitch.clicked.connect(self.bltSwitch)
        self.btnBaglan.clicked.connect(self.connect2Device)
        self.btnTara.clicked.connect(self.scanForDevice)

    def backToMain(self):
        self.hide()

    def show(self):
        self.isBltOpen()
        super().show()

    def isBltOpen(self):
        p1 = subprocess.run(
            ['hciconfig -a | grep Name'], capture_output=True, shell=True, text=True)
        p1 = p1.stdout
        # print(p1)
        if p1 != "":
            name = p1.split("'")[1]
            self.lblBluetoothStatus.setStyleSheet('color: lightgray')
            self.lblBluetoothStatus.setText("Açık   "+name)
            self.btnBluetoothSwitch.setChecked(True)
        else:
            self.lblBluetoothStatus.setStyleSheet('color: lightgray')
            self.lblBluetoothStatus.setText("Kapalı")
            self.btnBluetoothSwitch.setChecked(False)

    def bltSwitch(self):
        self.listDevices.clear()
        if self.btnBluetoothSwitch.isChecked():
            p1 = subprocess.run(['sudo bluetoothctl power on'],
                                capture_output=True, shell=True)
            if p1.returncode != 0:
                print(p1.stderr)
                self.lblBluetoothStatus.setStyleSheet('color: red')
                self.lblBluetoothStatus.setText("Hata!")
            else:
                self.isBltOpen()
                self.scanForDevice()

        else:
            p1 = subprocess.run(['sudo bluetoothctl power off'],
                                capture_output=True, shell=True)
            if p1.returncode != 0:
                print(p1.stderr)
                self.lblBluetoothStatus.setStyleSheet('color: red')
                self.lblBluetoothStatus.setText("Hata!")
            else:
                self.isBltOpen()
                self.listDevices.addItem("Bluetooth Kapalı")

    def scanForDevice(self):
        self.listDevices.clear()

        self.listDevices.addItem("scanning...")


        p1 = subprocess.check_output(
            ['hcitool scan'], shell=True, text=True)
        p1 = p1.split("\t")[1:]
        if len(p1) == 0:
            self.listDevices.clear()
            self.listDevices.addItem("Cihaz bulunamadı")
        else:
            self.listDevices.clear()
            self.nearby_devices = []
            # self.nearby_devices = {'mac_address': p1[i], 'name': p1[i+1] for i in range(0, len(p1), 2)}
            for i in range(0, len(p1), 2):
                self.nearby_devices.append(
                    {'mac_address': p1[i], 'name': p1[i+1][:-1]})
            del(p1)
            for device in self.nearby_devices:
                self.listDevices.addItem(device['name'])

    def connect2Device(self):
        selectedItem = self.listDevices.currentItem()
        if selectedItem is not None:

            p1 = subprocess.run(['sudo bluetoothctl discoverable on'], capture_output=False, shell=True, text=True)
            p1 = subprocess.run(['sudo bluetoothctl pairable on'], capture_output=False, shell=True, text=True)
            # p1 = subprocess.run(['sudo bluetoothctl agent NoInputNoOutput'], capture_output=False, shell=True, text=True)
            # p1 = subprocess.run(['sudo bluetoothctl default-agent'], capture_output=False, shell=True, text=True)

            for i in self.nearby_devices:
                if i['name'] == selectedItem.text():
                    print(i['mac_address'] + ", cihaza bağlanılıyor")
                    p1 = subprocess.run(['sudo bluetoothctl pair ' + i['mac_address']], capture_output=True, shell=True)
                    if p1.returncode != 0:
                        print(1)
                        print(p1)
                    else:
                        p1 = subprocess.run(['sudo bluetoothctl trust ' + i['mac_address']], capture_output=True, shell=True)
                        if p1.returncode != 0:
                            print(2)
                            print(p1)
                        else:
                            p1 = subprocess.run(['sudo bluetoothctl connect ' + i['mac_address']], capture_output=True, shell=True)
                            if p1.returncode != 0:
                                print(3)
                                print(p1)
                            else:
                                print("cihazın bağlanmış olması gerek :)")
                                


class ThreadClass(QtCore.QThread):
    updateUiSignal = QtCore.pyqtSignal(float)
    updateWheelStatus = QtCore.pyqtSignal(float)

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__()
        self.serialPort = serial.Serial()
        self.rawData = bytearray(5 * 4)
        self.data = []
        for i in range(5):
            self.data.append(collections.deque([0]))

    def run(self):
        self.running = True
        while self.running:
            time.sleep(0.2)
            if(self.serialPort.isOpen()):
                self.serialPort.reset_input_buffer()
                self.serialPort.readinto(self.rawData)
                privateData = copy.deepcopy(self.rawData[:])
                for i in range(5):
                    data = privateData[(i*4): (4 + i*4)]
                    value, = struct.unpack('f', data)
                    self.data[i].append(value)
                # print(self.data[0][-1])
                self.updateUiSignal.emit(self.data[0][-1])
                self.updateWheelStatus.emit(self.data[1][-1])



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("ui/icon.png"))
    # Create and display the splash screen
    splash_pix = QPixmap('ui/splash.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)

    splash.setStyleSheet("background-color:black;")

    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(20, splash_pix.height() -
                            50, splash_pix.width()-40, 30)

    splash.setMask(splash_pix.mask())

    # splash.showFullScreen()
    splash.show()

    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    mySerial = ThreadClass()
    battery = BatteryStatus()
    bluetoothStn = BluetoothSettings()
    bc = BackCamWindow()
    main = MainWindow(mySerial)

    splash.finish(main)

    sys.exit(app.exec_())
