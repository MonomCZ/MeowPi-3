#Imports
import os 
import pathlib
import time 
import sys
import subprocess
from wifi_options import wifi_ssid

#For comands like stop procesess  -- "systemctl", "stop", "NetworkManager  
def cmd(comand, ignore_error = False): # ignore_error so the script dont fail if we are trying to turn off a function that isnt even on
    result = subprocess.run(comand, capture_output=True, text=True)
    if result.returncode !=0 and not ignore_error:
          print(f"ERROR: {result.stderr.strip()}")
          sys.exit(1)
    return result     

    
#Configruration
IFACE = "wlan0"
PORTAL_IP = "192.168.4.1"
WIFI_SSID = wifi_ssid


#Step 1 stop all services
def stoping_services():
    print("Stoping all services...")
    cmd(["systemctl", "stop", "wpa_supplicant"], ignore_error=True)
    cmd(["systemctl", "disable", "wpa_supplicant"], ignore_error=True) # to turn off wpa_suplicatnt
    cmd(["systemctl", "stop", "NetworkManager"], ignore_error=True)
    cmd(["systemctl", "stop", "hostapd"], ignore_error=True)
    cmd(["systemctl", "stop", "dnsmasq"], ignore_error=True)
    print("Step 1 DONE... all services where stoped")


<<<<<<< HEAD
# Step 2 configureting intarfeces
def configureting_intarfeces():
     print("Configureting intarfeces")
     cmd (["ip", "link", "set", IFACE, "up"], ignore_error=True) # Turn on InterFace
     cmd (["ip", "addr", "flush", "dev", IFACE], ignore_error=True) # Flush InterFace
     cmd(["ip", "addr", "add", f"{PORTAL_IP}/24", "dev", IFACE], ignore_error=True) # to add IP to InterFace
     print("Step 2 DONE ... Configureting intarfeces was successful")
=======
# ── Krok 1: Zastav konfliktní služby ─────────────────────────sudo python3 wifi_portal.py────────────────
def stop_conflicting_services():
    print("\n[1/4] Zastavuji konfliktní služby...")
    cmd(["systemctl", "stop", "wpa_supplicant"],    ignoruj_chybu=True)
    cmd(["systemctl", "stop", "NetworkManager"],    ignoruj_chybu=True)
    cmd(["systemctl", "stop", "hostapd"],           ignoruj_chybu=True)
    cmd(["systemctl", "stop", "dnsmasq"],           ignoruj_chybu=True)
    cmd(["systemctl", "disable", "wpa_supplicant"], ignoruj_chybu=True)
    time.sleep(1)
    print("  ✓ Hotovo")
>>>>>>> f03167260a5a631d51eafedacb069906621fe15e


#Step 3 Rewriting config files (Configuring HOSTAPD and DNSMASQ)
def configurating_hostap():
     os.makedirs("/etc/hostapd", exist_ok=True)
     with open("/etc/hostapd/hostapd.conf", "w") as f:
          f.write(f"""interface={IFACE}
            driver=nl80211
            ssid={WIFI_SSID}
            hw_mode=g
            channel=6
            wmm_enabled=0
            auth_algs=1
            ignore_broadcast_ssid=0
            """)

def configurating_dnsmasq():
     os.makedirs("/etc/dnsmasq", exist_ok=True)
     with open("/etc/dnsmasq.conf", "w") as f:
          f.write(f"""interface={IFACE} 
            bind-interfaces
            dhcp-range=192.168.4.10,192.168.4.100,255.255.255.0,12h
            dhcp-option=3,192.168.4.1
            dhcp-option=6,192.168.4.1
            address=/#/192.168.4.1
            no-resolv  
            """)

def starting_services():
     #Useing definicions to configure.
     configurating_hostap()
     configurating_dnsmasq()
     time.sleep(1)
     #Starting the servecises
     cmd(["systemctl", "unmask", "hostapd"], ignore_error=True) 
     cmd(["systemclt", "start", "hostapd"])
     time.sleep(2)
     cmd(["systemctl", "start", "dnsmasq"])

     print("All services are running DNSMASQ ... ON HOSTAPD... ON")

def main():
    #Use ALL functions
    stoping_services()
    configureting_intarfeces()
    starting_services()

if __name__ == "__main__":
     main()








