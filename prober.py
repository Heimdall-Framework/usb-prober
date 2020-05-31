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
                print('Port number: {}'.format(device.getPortNumber()))
                print('Device product ID: {}'.format(device.getProductID()))
                print('Device vendor ID: {}'.format(device.getVendorID()))
                print('Device class: {}'.format(device.getDeviceClass()))
                print('Device bus number: {}'.format(device.getBusNumber()))
                print('Device bus address: {}'.format(device.getDeviceAddress()))

                print('-'*80)

if __name__ == '__main__':
    Prober().probe()