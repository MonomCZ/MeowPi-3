import os

input_mode='keyboard'
#keyboard or gpio

#bad usb
bad_usb_options = ['change_layout','change_script','start','stop']
#bad_usb_scripts = os.listdir(os.path.expanduser('~/MeowPi-3/modes/bad_usb/bad_usb_scripts/'))
bad_usb_scripts = os.listdir(os.path.join(os.path.dirname(__file__), 'modes/bad_usb/bad_usb_scripts/'))


bad_usb_scripts.remove('__init__.py')
bad_usb_scripts.remove('__pycache__')
bad_usb_scripts = [f.replace('.py', '') for f in bad_usb_scripts]
print(bad_usb_scripts)
bad_usb_scripts_index = 0
used_script = ('notepad_message') #options : notepad_message , bee_movie_script
used_layout = 'cz' #cz or us

#evil twin
WIFI_PRESETS = {

    "PRESET: FREE WIFI": { "ssid": "Free Wifi", "portal": "free_wifi.html" },
    "PRESET: STARBUCKS WIFI": { "ssid": "Starbucks WiFi", "portal": "starbucks_wifi.html" },
    #TODO: add more presets
}
ACTIVE_PRESET = "PRESET: FREE WIFI"