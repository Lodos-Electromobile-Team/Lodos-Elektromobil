from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                             QMainWindow, QPushButton, QSplashScreen)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QColor
import sys
import time


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("A simple App")
        self.central_widget = FormWidget(self)
        self.setCentralWidget(self.central_widget)
        self.resize(200, 50)


class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        btn_quit = QPushButton("QUIT")
        layout.addWidget(btn_quit, 0)
        btn_quit.clicked.connect(self.parent().close)


def main():
    """time.sleep simulata i tempi di caricamento dell'applicazione"""
    app = QApplication(sys.argv)
    pixmap = QPixmap("splash.jpg")
    splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
    splash.show()
    message = "\n INFO: Loading players..."
    splash.showMessage(message, Qt.AlignLeft, QColor("Red"))
    splash.repaint()
    time.sleep(2)
    message += "\n INFO: Loading evaluations..."
    splash.showMessage(message)
    splash.repaint()
    time.sleep(2)
    window = MainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
