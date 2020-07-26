from PyQt5 import QtWidgets  
from ui import res_rc, Battery_Status
import pyqtgraph as pg

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