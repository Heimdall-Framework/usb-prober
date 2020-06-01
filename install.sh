#!/bin/bash

function install_dependencies(){
    apt-get update
    pip3 libusb1
    
    echo ">> All dependencies were installed successfully."
}

function config_use_command (){
    cp prober.py /usr/bin/uprobe
    chmod +x /usr/bin/uprobe 
    echo ">> Command was configurated successfully."
}

function setup (){
    echo ">>> Prober installation is starting."

    echo ">> Installing dependencies."    
    install_dependencies
    echo ">> Configurating command."
    config_use_command

    echo ">>> The prober was installed. You can now use it as a command by typing 'uprobe'."
}

setup