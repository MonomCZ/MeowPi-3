import ui.ui as ui
import time
import config as config

ui.clear()



ui.display_text('Welcome to bad usb', 0)
ui.display_text('meow pi thingy!!!', 20)
time.sleep(3)

ui.clear()
ui.display_text("hold button to start", 20)

ui.display_text("press to switch the mode", 40)

ui.display_temperature()

ui.display_text(config.used_script, 0)