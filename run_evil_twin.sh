#!/bin/bash
#start with: 
#./run_evil_twin.sh


cd /home/$SUDO_USER/MeowPi-3
sudo env PYTHONPATH=. ~/MeowPi-3/venv/bin/python3 modes/evil_twin/evil_twin.py