import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet import L, MapWidget


class MapWindow(QWidget):
    def __init__(self):
        # Setting up the widgets and layout
        super().__init__()
        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        # Working with the maps with pyqtlet
        self.map = L.map(self.mapWidget)
        self.map.setView([40.9038902,31.1783139], 15)
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(self.map)
        self.marker = L.marker([40.9038902,31.1783139])
        self.marker.bindPopup('Maps are a treasure.')
        self.map.addLayer(self.marker)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MapWindow()
    sys.exit(app.exec_())