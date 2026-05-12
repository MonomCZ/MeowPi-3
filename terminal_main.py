import os
import config
import subprocess

print("Pick a mode!")
base = os.path.dirname(__file__)
mode_options = os.listdir(os.path.join(base, "modes"))
mode_options.remove("__init__.py")
mode_options.remove("__pycache__")
current_index = 0
for i in mode_options:
    
        
        print(f"{current_index}. {i}")
        current_index += 1
current_index = 0

user_input = int(input("Come on! Pick one!: "))
current_mode = mode_options[user_input]
print(f"You picked {current_mode}!")
print("pick an option!")
options = getattr(config, f"{current_mode}_options")
for i in options:
    print(f"{current_index}. {i}")
    current_index += 1
current_index = 0

user_input = int(input("Come on! Pick one!: "))
current_option = options[user_input]
print(f"You picked {current_option}!")
if current_mode == "bad_usb":
        if current_option == "change_layout":
                print("Changing layout...")
                new_layout = input("Pick a layout (cz or us): ")
                config.used_layout = new_layout
                print(f"Layout changed to {new_layout}!")
        elif current_option == "start":
                print("Starting bad usb attack...")
                subprocess.Popen(["bash", "run_bad_usb.sh"])