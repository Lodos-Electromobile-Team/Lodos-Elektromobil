from PyQt5 import QtCore, QtGui, QtWidgets  
from ui import res_rc, Back_Camera
import numpy as np
import cv2
import qimage2ndarray

class BackCamera(QtWidgets.QWidget, Back_Camera.Ui_Form):
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
        self.capture = cv2.VideoCapture('http://192.168.1.44')
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,
                         self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,
                         self.video_size.height())

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