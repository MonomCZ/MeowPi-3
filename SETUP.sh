#!/bin/bash

#RUN THIS WITH:
#bash setup.sh
cat << 'EOF'
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠟⣛⣽⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠤⢤⡴⠛⠁⠀⣴⠋⠱⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⠶⠶⠶⣤⣤⡶⠶⠾⠋⠀⠀⠈⠀⠀⠀⢰⣧⣀⣰⣟⠙⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟⠳⣄⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣿⣛⡀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣏⣠⡟⠁⠀⠀⢀⣴⡀⠀⡀⠀⣤⣄⠀⢤⣀⠀⠈⠁⠈⠳⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⡟⣼⣷⣴⣶⣿⠁⢹⡄⠻⣶⣿⣯⣀⡀⣿⣷⠀⠀⠀⢀⡈⢿⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⡿⠋⢻⠻⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣼⠹⣦⣧⣿⣆⠙⠛⣯⡻⠿⣆⠈⠁⠀⠀⠈⠙⣮⡿⣦⣀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣥⣴⣭⣿⣷⣤⣼⢴⣒⡮⣽⡻⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⣼⣿⣿⠉⢿⣇⠙⠋⢹⣯⣄⠀⣘⣿⣦⣼⣷⣤⠀⠀⣀⠀⠈⢿⡦⢿⣷⡦⠀⠀
⠀⠀⠀⠀⣾⢹⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣾⡿⡟⠻⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠟⣿⣿⣇⣀⣼⣿⣦⡀⠀⣿⣿⣿⣿⡏⠁⠀⠀⠙⢷⠀⠙⡆⠀⠘⣷⠀⠀⠀⠀⠀
⠀⣀⣤⠤⠿⠸⣿⣿⣿⣿⡿⠁⣿⣿⣿⣿⣿⣿⡇⣿⠃⠰⠀⠉⡛⠳⠶⣤⣀⣀⠀⠀⠀⢰⣿⣿⠿⠛⣿⣿⠻⢿⣶⡿⠋⢿⣿⡧⠀⠀⠀⢀⡾⠀⠀⢻⢦⣄⣻⣧⠀⠀⠀⠀
⣼⣿⣿⣿⣿⣦⡈⠙⠛⠉⠀⠀⠘⣿⣿⣿⣿⡿⣵⣃⡀⠀⠀⠀⠀⠀⠀⠒⠿⣿⣿⣶⣤⣼⡏⢻⣄⠀⢻⣿⠀⢀⡿⠳⣄⣈⣛⣃⣀⣤⠶⢿⡄⠀⠀⢸⣼⣯⠛⠛⠛⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⣠⣴⣶⣶⣶⣦⡀⠉⠉⠁⣈⣭⣍⣙⢷⣶⠶⢶⣦⣤⣄⣀⣀⠀⠉⠙⠛⠿⢿⣿⣷⣶⣗⢺⣏⣰⣦⣤⣽⠟⠉⠉⠀⠀⣸⢿⣶⣄⣸⡏⠛⠓⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣾⣿⣿⣿⣿⣷⣼⣇⠀⠀⠀⠀⠈⠉⠉⠛⠛⠷⠶⠶⠤⣭⣝⣿⣿⣿⣷⣯⣉⣹⡇⠀⣀⣠⡾⢻⣿⣿⡍⠛⠷⠀⠀⠀⠀⠀⠀⠀
⠙⠿⣿⣿⣯⠄⡏⣿⣿⣿⣿⣿⣿⣿⣿⠘⣿⣿⣿⣿⣿⣿⣇⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠉⣩⡿⠛⢿⣿⣿⣶⣟⣩⣿⠗⠈⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣇⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⣿⣿⣿⣿⡿⢏⣾⠓⠀⢀⣀⣀⣀⣠⣤⣤⣤⣴⣶⣶⣷⡶⠶⠾⠛⠀⠀⠀⠹⡏⠻⢿⣯⣾⣯⣀⠀⠀⣿⠀⣠⡶⠶⠾⣷⣦⡀⠀
⠀⠀⠀⠀⠈⢻⣮⡿⣿⣿⣿⣿⣿⠟⢁⣾⣙⣿⣿⣶⣾⣟⣛⣿⣭⠭⠿⠶⠾⠛⠛⠛⠉⠉⠁⢸⡁⣀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⠻⣿⡟⠷⣰⣿⠀⠻⠷⢤⣤⣀⠙⣧⡀
⠀⠀⠀⠀⠀⠀⠙⠻⣮⣍⣉⣩⣥⡶⠿⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣽⣗⡀⠀⠀⠀⢀⣾⡇⠀⠀⠀⠀⠈⠃⣰⢿⡇⠀⠀⠀⠀⠈⠻⣇⠘⣧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⢤⡶⣶⣿⣿⣷⣶⣤⡤⠶⠶⠞⠋⣾⠀⠀⠀⠀⠀⠀⠀⢻⠀⢻⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠏⣧⣀⣀⣀⣀⡀⠀⠀⠀⠠⣿⡀⠀⠀⠀⠀⠀⠀⣼⠀⣸⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣿⣭⡉⠉⠙⠛⣃⣠⣤⣶⣿⣧⡀⠀⠀⠀⣠⡼⠃⢠⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠿⠛⠛⠛⠻⠿⣿⡿⠲⣿⣿⣝⣛⠚⠋⠉⣀⣴⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠁⠀⠸⢻⣿⡛⠛⠛⠋⠉⠀⠀⠀
EOF


echo 'Setting up MeowPi!!! :3'
#downloading and installing dependencies
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-flask python3-pip python3-venv hostapd dnsmasq iptables python3-pil i2c-tools fonts-dejavu
cd ~/MeowPi-3

echo 'PYTHONPATH=/home/avsie/MeowPi-3' | sudo tee -a /etc/environment
source /etc/environment

pip3 install --break-system-packages adafruit-blinka adafruit-circuitpython-ssd1306

#some linux ssh fix
grep -qxF 'export TERM=xterm-256color' ~/.bashrc || echo 'export TERM=xterm-256color' >> ~/.bashrc
#gadget mode (bad_usb) enable
read -p "Do you want to enable gadget mode (this is required for badusb but any external USB devices like a keyboard won't work)? (y/n): " answer
if [[ "$answer" == "y" ]]; then 
    echo "enabling gadget mode!"
    echo 'external keyboards will NOT work'
    sleep 2
    echo "dtoverlay=dwc2,dr_mode=peripheral" | sudo tee -a /boot/firmware/config.txt
    sudo sed -i 's/rootwait/rootwait modules-load=dwc2,g_hid/' /boot/firmware/cmdline.txt
 else
    echo "bad usb mode will NOT work"
    echo "bad usb mode will NOT work"
    echo "bad usb mode will NOT work"
    echo "bad usb mode will NOT work"
    echo "bad usb mode will NOT work"
    sleep 2
fi

sudo raspi-config nonint do_i2c 0
#giving perms for run files
chmod +x ~/MeowPi-3/run_bad_usb.sh ~/MeowPi-3/run_evil_twin.sh

cat << 'EOF'
                           ╱|、
                          (˚ˎ 。7
                          |、˜〵        
                          じしˍ,)ノ
EOF
echo 'MeowPi setup complete!'
echo 'PLEASE REBOOT!'