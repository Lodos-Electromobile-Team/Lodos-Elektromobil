import time

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThreadPool, QTimer

import Thread
import Serial
import MainWindow

class Application(Thread.Worker):
    main = None 
    def __init__(self):
        app = QApplication([])
        serial= Serial.Serial()
        print(Application.main)
        if Application.main == None:
            Application.main = MainWindow.MainWindow()
            Application.main.show()

        app.exec_()

if __name__ == "__main__":
    Application()