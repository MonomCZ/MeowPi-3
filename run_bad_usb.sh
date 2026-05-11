# first run:
#chmod +x run_bad_usb.sh
#then start with
#./run_bad_usb.sh

#!/bin/bash
cd ~/MeowPi-3
sudo PYTHONPATH=. python3 modes/bad_usb/bad_usb.py
