import subprocess 
import os       
import pathlib  

# HOSTAPD --------------------
def configure_hostapd(): 
    content = f"""interface=wlan0
driver=nl80211
ssid=FREEWIFI
hw_mode=g
channel=6
"""
    with open("/etc/hostapd/hostapd.conf", "w") as f:
        f.write(content)

# -----------------------------------

# DNSMASQ--------------
def configure_dnsmasq():
    content2 = f"""interface=wlan0
dhcp-range=192.168.4.10,192.168.4.100,12h
address=/#/192.168.4.1
"""

    with open("/etc/dnsmasq.conf", "w") as f:
        f.write(content2)
    
    
#--------------------------

#
def configure_interface():
    subprocess.run(["ip", "link", "set", "wlan0", "up"])
    subprocess.run(["ip", "addr", "flush", "dev", "wlan0"])   # flush
    subprocess.run(["ip", "addr", "add", "192.168.4.1/24", "dev", "wlan0" ])   # add IP

def start_services():
    sluzby = ["hostapd", "dnsmasq"]

    for sluzba in sluzby:
        subprocess.run(["systemctl", "start", sluzba])

app = Flask(__name__)

@app.route("/")
def index():
    return "Vítej na portalu!"

def run_portal():
    app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    configure_interface()
    configure_hostapd()
    configure_dnsmasq()
    start_services()
    run_portal()