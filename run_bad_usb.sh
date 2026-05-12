#!/bin/bash

#start with:
#./run_bad_usb.sh


cd /home/$SUDO_USER/MeowPi-3
sudo PYTHONPATH=. python3 modes/bad_usb/bad_usb.py
