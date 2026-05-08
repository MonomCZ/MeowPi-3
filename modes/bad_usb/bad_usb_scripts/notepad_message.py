from modes.bad_usb.bad_usb import type_string, press_key, setup_gadget
import time

def run():
    press_key(0x08, 0x15)
    time.sleep(0.5)
    type_string("notepad")
    press_key(0x00, 0x28)
    time.sleep(1.5)
    type_string("Hello from MeowPi BadUSB mode! :3 (just install arch bro)")