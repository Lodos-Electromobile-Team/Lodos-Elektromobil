from PyQt5 import QtCore

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

