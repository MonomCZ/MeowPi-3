import ui.ui as ui
import time
import subprocess
ui.clear()



ui.display_text('Welcome to bad usb', 0)
ui.display_text('meow pi thingy!!!', 20)
time.sleep(3)

ui.clear()
ui.display_text("hold the button to start ^the attack", 20)

ui.display_text("and press it to switch the ^current mode", 40)
output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode().strip()
ui.display_text(output, 0)

