# usb-prober

[![Build Status](https://travis-ci.org/Heimdall-Framework/usb-prober.svg?branch=master)](https://travis-ci.org/Heimdall-Framework/usb-prober)

A lightweight script that lists all connected USB devices.

---

## Installation
Simply execute the `install.sh` file. The only python dependency is `libusb1`.

## Usage
After running the script in order to install your dependencies, all you need to do is to type `uprobe` on the command line. It will print all connected USB devices and their most important properties.

## Listed properties
* Port number
* Device product ID
* Device vendor ID
* Device class
* Device bus number
* Device bus address
