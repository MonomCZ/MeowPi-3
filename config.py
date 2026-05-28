import os

input_mode='keyboard'
#keyboard or gpio

#bad usb
bad_usb_options = ['change_layout','change_script','start','stop']
bad_usb_scripts = os.listdir(os.path.expanduser('~/MeowPi-3/modes/bad_usb/bad_usb_scripts/'))
bad_usb_scripts.remove('__init__.py')
bad_usb_scripts = [f.replace('.py', '') for f in bad_usb_scripts]
print(bad_usb_scripts)
bad_usb_scripts_index = 0
used_script = ('notepad_message') #options : notepad_message , bee_movie_script
used_layout = 'cz' #cz or us

#evil twin
wifi_ssid = "Free wifi"

wifi_names = ["Free Wifi", "KFC Wifi", "McDonalds Wifi", "Starbucks Free"]
#                   0           1           2                   3

evil_twin_options = ['change ssid', 'start evil twin', 'stop evil twin']
