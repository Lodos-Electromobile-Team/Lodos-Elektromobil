
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys
import qimage2ndarray


class MainApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.video_size = QtCore.QSize(800, 480)
        self.setup_ui()
        self.setup_camera()

    def setup_ui(self):
        """Initialize widgets.
        """
        self.image_label = QtWidgets.QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.quit_button = QtWidgets.QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.quit_button)

        self.setLayout(self.main_layout)

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture('http://10.42.0.165')
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,
                         self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,
                         self.video_size.height())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        _, frame = self.capture.read()
        if frame is None:
            pass
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)
            image = qimage2ndarray.array2qimage(
                frame)  # SOLUTION FOR MEMORY LEAK
            self.image_label.setPixmap(QtGui.QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())
