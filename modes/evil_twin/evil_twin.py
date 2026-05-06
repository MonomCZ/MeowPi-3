#!/usr/bin/env python3
"""
WiFi Hotspot – Raspberry Pi Zero 2 W
Spuštění: sudo python3 wifi_portal.py
"""

import os
import sys
import subprocess
import time
from modes.evil_twin.wifi_options import wifi_ssid

# ── Musíš být root ────────────────────────────────────────────────────────────
if os.geteuid() != 0:
    print("CHYBA: Spusť jako root →  sudo python3 wifi_portal.py")
    sys.exit(1)

# ── Konfigurace ───────────────────────────────────────────────────────────────
IFACE     = "wlan0"
PORTAL_IP = "192.168.4.1"
WIFI_SSID = wifi_ssid


# ── Pomocná funkce pro spouštění příkazů ─────────────────────────────────────
def cmd(prikaz: list, ignoruj_chybu: bool = False):
    print(f"  → {' '.join(prikaz)}")
    result = subprocess.run(prikaz, capture_output=True, text=True)
    if result.returncode != 0 and not ignoruj_chybu:
        print(f"CHYBA: {result.stderr.strip()}")
        sys.exit(1)
    return result


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


# ── Krok 2: Nastav IP adresu na wlan0 ────────────────────────────────────────
def configure_interface():
    print(f"\n[2/4] Nastavuji rozhraní {IFACE} → {PORTAL_IP}...")
    cmd(["ip", "link", "set", IFACE, "up"])
    cmd(["ip", "addr", "flush", "dev", IFACE], ignoruj_chybu=True)
    cmd(["ip", "addr", "add", f"{PORTAL_IP}/24", "dev", IFACE])
    print("  ✓ Hotovo")


# ── Krok 3: Zapiš config soubory ─────────────────────────────────────────────
def configure_hostapd():
    print("\n[3/4] Konfiguruji hostapd a dnsmasq...")

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

    with open("/etc/default/hostapd", "w") as f:
        f.write('DAEMON_CONF="/etc/hostapd/hostapd.conf"\n')

    with open("/etc/dnsmasq.conf", "w") as f:
        f.write(f"""interface={IFACE}
bind-interfaces
dhcp-range=192.168.4.10,192.168.4.100,255.255.255.0,12h
dhcp-option=3,{PORTAL_IP}
dhcp-option=6,{PORTAL_IP}
address=/#/{PORTAL_IP}
no-resolv
""")

    print("  ✓ Hotovo")


# ── Krok 4: Spusť hostapd a dnsmasq ──────────────────────────────────────────
def start_services():
    print("\n[4/4] Spouštím služby...")

    cmd(["systemctl", "unmask", "hostapd"], ignoruj_chybu=True)
    cmd(["systemctl", "start", "hostapd"])
    time.sleep(2)

    cmd(["systemctl", "start", "dnsmasq"])
    time.sleep(1)

    for sluzba in ["hostapd", "dnsmasq"]:
        result = cmd(["systemctl", "is-active", sluzba], ignoruj_chybu=True)
        if result.stdout.strip() == "active":
            print(f"  ✓ {sluzba} běží")
        else:
            print(f"  ✗ {sluzba} NEBĚŽÍ → journalctl -u {sluzba}")


# ── Spuštění ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("═══ WiFi Hotspot – start ═══")
    stop_conflicting_services()
    configure_interface()
    configure_hostapd()
    start_services()
    print(f"\n✓ Hotspot '{WIFI_SSID}' běží!")
