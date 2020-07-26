from PyQt5 import QtWidgets  
from ui import res_rc, Bluetooth_Settings
from ui.customswitch import CustomSwitch
import subprocess

class BtSettings(QtWidgets.QMainWindow, Bluetooth_Settings.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        subprocess.check_output("rfkill unblock bluetooth", shell=True)
        
        
        self.nearby_devices = []


        self.btnBackMain.clicked.connect(self.backToMain)
        self.btnBluetoothSwitch.clicked.connect(self.bltSwitch)
        self.btnBaglan.clicked.connect(self.connect2Device)
        self.btnTara.clicked.connect(self.scanForDevice)

    def backToMain(self):
        self.hide()

    def show(self):
        self.isBltOpen()
        super().show()

    def isBltOpen(self):
        p1 = subprocess.run(
            ['hciconfig -a | grep Name'], capture_output=True, shell=True, text=True)
        p1 = p1.stdout
        # print(p1)
        if p1 != "":
            name = p1.split("'")[1]
            self.lblBluetoothStatus.setStyleSheet('color: lightgray')
            self.lblBluetoothStatus.setText("Açık   "+name)
            self.btnBluetoothSwitch.setChecked(True)
        else:
            self.lblBluetoothStatus.setStyleSheet('color: lightgray')
            self.lblBluetoothStatus.setText("Kapalı")
            self.btnBluetoothSwitch.setChecked(False)

    def bltSwitch(self):
        self.listDevices.clear()
        if self.btnBluetoothSwitch.isChecked():
            p1 = subprocess.run(['sudo bluetoothctl power on'],
                                capture_output=True, shell=True)
            if p1.returncode != 0:
                print(p1.stderr)
                self.lblBluetoothStatus.setStyleSheet('color: red')
                self.lblBluetoothStatus.setText("Hata!")
            else:
                self.isBltOpen()
                self.scanForDevice()

        else:
            p1 = subprocess.run(['sudo bluetoothctl power off'],
                                capture_output=True, shell=True)
            if p1.returncode != 0:
                print(p1.stderr)
                self.lblBluetoothStatus.setStyleSheet('color: red')
                self.lblBluetoothStatus.setText("Hata!")
            else:
                self.isBltOpen()
                self.listDevices.addItem("Bluetooth Kapalı")

    def scanForDevice(self):
        self.listDevices.clear()

        self.listDevices.addItem("scanning...")


        p1 = subprocess.check_output(
            ['hcitool scan'], shell=True, text=True)
        p1 = p1.split("\t")[1:]
        if len(p1) == 0:
            self.listDevices.clear()
            self.listDevices.addItem("Cihaz bulunamadı")
        else:
            self.listDevices.clear()
            self.nearby_devices = []
            # self.nearby_devices = {'mac_address': p1[i], 'name': p1[i+1] for i in range(0, len(p1), 2)}
            for i in range(0, len(p1), 2):
                self.nearby_devices.append(
                    {'mac_address': p1[i], 'name': p1[i+1][:-1]})
            del(p1)
            for device in self.nearby_devices:
                self.listDevices.addItem(device['name'])

    def connect2Device(self):
        selectedItem = self.listDevices.currentItem()
        if selectedItem is not None:

            p1 = subprocess.run(['sudo bluetoothctl discoverable on'], capture_output=False, shell=True, text=True)
            p1 = subprocess.run(['sudo bluetoothctl pairable on'], capture_output=False, shell=True, text=True)
            # p1 = subprocess.run(['sudo bluetoothctl agent NoInputNoOutput'], capture_output=False, shell=True, text=True)
            # p1 = subprocess.run(['sudo bluetoothctl default-agent'], capture_output=False, shell=True, text=True)

            for i in self.nearby_devices:
                if i['name'] == selectedItem.text():
                    print(i['mac_address'] + ", cihaza bağlanılıyor")
                    p1 = subprocess.run(['sudo bluetoothctl pair ' + i['mac_address']], capture_output=True, shell=True)
                    if p1.returncode != 0:
                        print(1)
                        print(p1)
                    else:
                        p1 = subprocess.run(['sudo bluetoothctl trust ' + i['mac_address']], capture_output=True, shell=True)
                        if p1.returncode != 0:
                            print(2)
                            print(p1)
                        else:
                            p1 = subprocess.run(['sudo bluetoothctl connect ' + i['mac_address']], capture_output=True, shell=True)
                            if p1.returncode != 0:
                                print(3)
                                print(p1)
                            else:
                                print("cihazın bağlanmış olması gerek :)")
                                