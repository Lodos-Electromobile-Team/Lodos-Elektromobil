
from collections import deque
from copy import deepcopy
from serial import Serial as _Serial
from struct import unpack
from time import sleep


from PyQt5.QtCore import  pyqtSignal


class Serial():
    updateUiSignal = pyqtSignal(float)
    updateWheelStatus = pyqtSignal(float)
    @classmethod
    def __init__(cls):
        # super(cls).__init()
        cls.rawData = bytearray(5 * 4)
        cls.data = []
        for i in range(5):
            cls.data.append(deque([0]))

        cls.serialPort = _Serial()
        cls.serialPort.baudrate = 9600
        cls.serialPort.port = "/dev/ttyUSB0"
        # mySerial.serialPort.port = "/dev/ttyACM0"  # Deneme
        
        # cls.updateUiSignal[float].connect(self.updateUi)
        
        cls.serialConnect()

    @classmethod
    def mesajGonder(cls, mesaj):
        if cls.serialPort.isOpen():
            cls.serialPort.write(mesaj.encode())
        else:
            print("Seri Port Bağlı Değil.")

    @classmethod
    def serialConnect(cls):
        try:
            cls.serialPort.open()
        except:
            # cls.message.append("Bağlantı Hatası!!")
            print("Baglanti Hatasi!!!")

    @classmethod
    def serialDisconnect(cls):
        if cls.serialPort.isOpen():
            cls.serialPort.close()
        else:
            cls.message.append("Seriport Zaten Kapalı.")

    @classmethod
    def getdata(cls):
        while True:
            sleep(0.2)
            if(cls.serialPort.isOpen()):
                cls.serialPort.reset_input_buffer()
                cls.serialPort.readinto(cls.rawData)
                privateData = deepcopy(cls.rawData[:])
                for i in range(5):
                    _data = privateData[(i*4): (4 + i*4)]
                    value, = unpack('f', _data)
                    cls.data[i].append(value)
                # print(cls.data[0][-1])
                cls.updateUiSignal.emit(cls.data[0][-1])
                cls.updateWheelStatus.emit(cls.data[1][-1])