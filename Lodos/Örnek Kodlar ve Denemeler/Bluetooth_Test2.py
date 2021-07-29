#!/usr/bin/env python

import sys
import os

from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtBluetooth import QBluetoothLocalDevice, QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo, QBluetoothAddress


class Application(QCoreApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dev = QBluetoothDeviceInfo()
        self.dlist = []
        self.counter = 0

        self.localDevice = QBluetoothLocalDevice()
        print("localDevice: " + self.localDevice.name())

        # self.scan_for_devices()
        self.agent = QBluetoothDeviceDiscoveryAgent(self)

        timer = QTimer(self.agent)
        timer.start(500)
        timer.timeout.connect(self.scan_for_devices)
        # self.exec()

    def display_status(self):
        print(self.agent.isActive(), self.agent.discoveredDevices())

    def fin(self, *args, **kwargs):
        # self.agent.stop()
        self.dlist = self.agent.discoveredDevices()
        while self.counter < len(self.dlist):
            print(str(self.counter) + ". " + self.dlist[self.counter].name() +
                  self.dlist[self.counter].isActive())
            self.counter += 1
        os.environ['QT_EVENT_DISPATCHER_CORE_FOUNDATION'] = '0'
        sys.exit(0)

    def err(self, *args, **kwargs):
        print("Error.")

    def scan_for_devices(self):
        self.agent.deviceDiscovered.connect(self.fin)
        self.agent.finished.connect(self.fin)
        self.agent.error.connect(self.err)
        self.agent.setLowEnergyDiscoveryTimeout(1000)
        # self.agent.discoveredDevices()
        self.agent.start()


if __name__ == '__main__':

    os.environ['QT_EVENT_DISPATCHER_CORE_FOUNDATION'] = '1'

    app = Application(sys.argv)

    sys.exit(app.exec_())

"""
 
class BluetoothSettings(QtWidgets.QMainWindow, Bluetooth_Settings.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnBackMain.clicked.connect(self.backToMain)
        self.btn_1.clicked.connect(self.scan_for_devices)
        self.btn_2.clicked.connect(self.scan_for_real)

    def backToMain(self):
        self.hide()

    def scan_for_real(self):
        print("scanning...")
        nearby_devices = discover_devices(lookup_names=True)
        print("found " + str(len(nearby_devices)) + " devices")
        for name, addr in nearby_devices:
            print(addr + " " + name)

    def fin(self, *args, **kwargs):
        self.counter = 0
        self.agent.stop()
        self.dlist = self.agent.discoveredDevices()
        while self.counter < len(self.dlist):
            print(str(self.counter) + ". " + self.dlist[self.counter].name())
            self.counter += 1
        self.timer.stop()
        # os.environ['QT_EVENT_DISPATCHER_CORE_FOUNDATION'] = '0'

    def foo(self, *args, **kwargs):
        print('foo', args, kwargs)

    def display_status(self):
        print(self.agent.isActive(), self.agent.discoveredDevices())

    def scan_for_devices(self):
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent(self)
        self.agent.deviceDiscovered.connect(self.foo)
        self.agent.finished.connect(self.fin)
        self.agent.error.connect(self.foo)
        self.agent.setLowEnergyDiscoveryTimeout(1000)
        self.agent.start()

        self.timer = QtCore.QTimer(self.agent)
        self.timer.start(500)
        self.timer.timeout.connect(self.display_status)



"""
