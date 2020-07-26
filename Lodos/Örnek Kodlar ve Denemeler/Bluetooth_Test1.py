import re
import time
import pexpect
import subprocess
# import bluetooth


class BluetoothctlError(Exception):
    """This exception is raised, when bluetoothctl fails to start."""
    pass


class Application():
    def __init__(self):
        subprocess.check_output("rfkill unblock bluetooth", shell=True)
        self.child = pexpect.spawn("bluetoothctl", echo=False)
        self.start_scan()
        self.devices = self.get_connectable_devices()
        '''
        self.devices = self.get_connectable_devices()
        print(self.trust(self.devices[0]['mac_address']))
        print(self.connect(self.devices[0]['mac_address']))
        print(self.get_paired_devices())
        '''
        print(self.remove(self.devices[0]['mac_address']))
        # print(self.remove(self.devices[0]['mac_address']))
        # print(self.is_connected())

    def get_output(self, command, pause=0):
        """Run a command in bluetoothctl prompt, return output as a list of lines."""
        self.child.send(command + "\n")
        time.sleep(pause)

        start_failed = self.child.expect(["bluetooth", pexpect.EOF])

        if start_failed:
            raise BluetoothctlError(
                "Bluetoothctl failed after running " + command)
        return self.child.before.decode().split("\r\n")

    def bluetooth_on(self):
        """Open bluetooth module."""
        try:
            out = self.get_output("power on")
            return out
        except BluetoothctlError as e:
            print(e)
            return None

    def bluetooth_off(self):
        """Close bluetooth module."""
        try:
            out = self.get_output("power off")
            return out
        except BluetoothctlError as e:
            print(e)
            return None

    def start_scan(self):
        """Start bluetooth scanning process."""
        try:
            out = self.get_output("scan on")
            return out
        except BluetoothctlError as e:
            print(e)
            return None

    def stop_scan(self):
        """Stop bluetooth scanning process."""
        try:
            out = self.get_output("scan off")
            return out
        except BluetoothctlError as e:
            print(e)
            return None

    def make_discoverable(self):
        """Make device discoverable."""
        try:
            out = self.get_output("discoverable on")
            return out
        except BluetoothctlError as e:
            print(e)
            return None

    def get_connectable_devices(self):
        """Get a  list of connectable devices.
        Must install 'sudo apt-get install bluez blueztools' to use this"""
        try:
            res = []
            # Requires 'apt-get install bluez'
            out = subprocess.check_output(["hcitool", "scan"])
            out = out.decode().split("\n")
            device_name_re = re.compile("^\t([0-9,:,A-F]{17})\t(.*)$")
            for line in out:
                device_name = device_name_re.match(line)
                if device_name is not None:
                    res.append({
                        "mac_address": device_name.group(1),
                        "name": device_name.group(2)
                    })
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            return res

    def get_paired_devices(self):
        """Return a list of tuples of paired devices."""
        try:
            out = self.get_output("paired-devices")
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            paired_devices = []
            for line in out:
                device = self.parse_device_info(line)
                if device:
                    paired_devices.append(device)

    def parse_device_info(self, info_string):
        """Parse a string corresponding to a device."""
        device = {}
        block_list = ["[\x1b[0;", "removed"]
        string_valid = not any(
            keyword in info_string for keyword in block_list)

        if string_valid:
            try:
                device_position = info_string.index("Device")
            except ValueError:
                pass
            else:
                if device_position > -1:
                    attribute_list = info_string[device_position:].split(
                        " ", 2)
                    device = {
                        "mac_address": attribute_list[1],
                        "name": attribute_list[2]
                    }

        return device

    def is_connected(self):
        """Returns True if there is a current connection to any device, otherwise returns False"""
        try:
            res = False
            # Requires 'apt-get install bluez'
            out = subprocess.check_output(["hcitool", "con"])
            out = out.decode().split("\n")
            mac_addr_re = re.compile("^.*([0-9,:,A-F]{17}).*$")
            for line in out:
                mac_addr = mac_addr_re.match(line)
                if mac_addr != None:
                    res = True
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            return res

    def pair(self, mac_address):
        """Try to pair with a device by mac address."""
        try:
            out = self.get_output("pair " + mac_address, 4)
            return out
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            res = self.child.expect(
                ["Failed to pair", "Pairing successful", pexpect.EOF])
            print(res)
            success = True if res == 1 else False
            return success

    def remove(self, mac_address):
        """Remove paired device by mac address, return success of the operation."""
        try:
            out = self.get_output("remove " + mac_address, 3)
            return out
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            res = self.child.expect(
                ["not available", "Device has been removed", pexpect.EOF])
            success = True if res == 1 else False
            return success

    def connect(self, mac_address):
        """Try to connect to a device by mac address."""
        try:
            out = self.get_output("connect " + mac_address, 2)
            return out
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            res = self.child.expect(
                ["Failed to connect", "Connection successful", pexpect.EOF])
            success = True if res == 1 else False
            return success

    def disconnect(self, mac_address):
        """Try to disconnect to a device by mac address."""
        try:
            out = self.get_output("disconnect " + mac_address, 2)
            return out
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            res = self.child.expect(
                ["Failed to disconnect", "Successful disconnected", pexpect.EOF])
            success = True if res == 1 else False
            return success

    def trust(self, mac_address):
        """Trust the device with the given MAC address"""
        try:
            out = self.get_output("trust " + mac_address, 4)
            return out
        except BluetoothctlError as e:
            print(e)
            return None
        else:
            res = self.child.expect(
                ["not available", "trust succeeded", pexpect.EOF])
            success = True if res == 1 else False
            return success

    def start_agent(self):
        """Start agent"""
        try:
            out = self.get_output("agent on")
            return out
        except BluetoothctlError as e:
            print(e)
            return None

    def default_agent(self):
        """Start default agent"""
        try:
            out = self.get_output("default-agent")
            return out
        except BluetoothctlError as e:
            print(e)
            return None


if __name__ == "__main__":
    app = Application()
