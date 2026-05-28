import ui.ui as ui
import input.gpio_input as gpio_input
import time
import config as config


ui.clear()



ui.display_text('Welcome to bad usb', 0)
ui.display_text('meow pi thingy!!!', 20)
time.sleep(3)

while True:
    ui.clear()
    ui.display_text("hold 1s to start", 20)

    ui.display_text("press to switch the mode", 40)

    ui.display_temperature()

    if not len(config.used_script) < 20:
        displayed_used_script = config.used_script[:20]
        mode_cut=True
    else:
        mode_cut=False
        displayed_used_script = config.used_script[:20]

    displayed_used_script = config.used_script[:20]
    if mode_cut:
        displayed_used_script+="..."


    ui.display_text(displayed_used_script, 0)
    if gpio_input.button1():
        sleep(0.2)
        press=True
        sleep(0.8)
        if gpio_input.button1():
        

        

