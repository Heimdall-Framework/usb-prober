#!/usr/bin/env python3
import usb1 as usb

class Prober():
    def probe(self):
        with usb.USBContext() as context:
            
            # gets a list of all connected devices
            usb_devices_list = context.getDeviceList()

            # prints a separator
            print('-'*80)

            # lists information for each connected device
            for device in usb_devices_list:
                device_class = None
                for device_configuration in device.iterConfigurations():
                    device_class = next(device_configuration.__getitem__(0).__iter__()).getClass()
                    break

                print('Port number: {}'.format(device.getPortNumber()))
                print('Device product ID: {}'.format(device.getProductID()))
                print('Device vendor ID: {}'.format(device.getVendorID()))
                print('Device class: {}'.format(device_class))
                print('Device bus number: {}'.format(device.getBusNumber()))
                print('Device bus address: {}'.format(device.getDeviceAddress()))

                print('-'*80)

def main():
    Prober().probe()