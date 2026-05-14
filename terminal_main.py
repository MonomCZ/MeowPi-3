import os
import config
import subprocess
current_index = 0
print("Pick a mode!")
base = os.path.dirname(__file__)
mode_options = os.listdir(os.path.join(base, "modes"))
mode_options.remove("__init__.py")

for i in mode_options:
        
        if i == "__pycache__":
              mode_options.remove(i)
        elif i == "__init__.py":
                  mode_options.remove(i)
        current_index +=1
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
               file_path = 'nastaveni.py'
               with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()


               new_content = content.replace('layout = "us"', 'layout = "cz"')

               with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

        elif current_option == "start":
                print("Starting bad usb attack...")
                subprocess.Popen(["bash", "run_bad_usb.sh"])