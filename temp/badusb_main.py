import ui.ui as ui
import input.gpio_input as gpio_input
import time
import config as config



ui.clear()



ui.display_text('Welcome to bad usb', 0)
ui.display_text('meow pi thingy!!!', 20)
ui.show()
time.sleep(3)

while True:
    ui.show()
    ui.clear()
    ui.display_text("hold 1s to start", 20)

    ui.display_text("press to switch the mode", 40)

    ui.display_temperature()

    if len(config.used_script) > 20:
        displayed_used_script = config.used_script[:20]
        mode_cut=True
    else:
        mode_cut=False
        displayed_used_script = config.used_script

    
    if mode_cut:
        displayed_used_script+="..."

    press=False
    
    ui.display_text(displayed_used_script, 0)
    if hold:
        hold=False
        sleep(0.2)
    elif gpio_input.button1():
        time.sleep(0.2)
        press=True
        print("pressed")
        time.sleep(1)
        if gpio_input.button1():
            press=False
            hold=True
            print("held")
            time.sleep(0.5)
    
    if press:
        print("pressed registered")
        config.bad_usb_scripts_index =(config.bad_usb_scripts_index+1) %len(config.bad_usb_scripts)
        config.used_script = config.bad_usb_scripts[config.bad_usb_scripts_index]

        

