# -*- coding: utf-8 -*-
# QPropertyAnimation
# import os
# import serial.tools.list_ports
from ui import res_rc, Main_Window
import BackCamera, BatteryStatus, BluetoothSettings,MainWindow, Thread
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtCore import Qt # , pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QSplashScreen, QProgressBar


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

    mySerial = Thread.ThreadClass()
    battery = BatteryStatus.BatteryStatus()
    bluetoothStn = BluetoothSettings.BluetoothSettings()
    bc = BackCamera.BackCamera()
    main = MainWindow.MainWindow(mySerial)

    splash.finish(main)

    sys.exit(app.exec_())
