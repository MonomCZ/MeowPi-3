#main.py
#libraries etc 
#       keyboard or gpio
mode = 'keyboard'
if mode == 'keyboard':
    from input.keyboard import get_input as get_input
#elif mode == 'gpio':
#    from input.gpio import  as 



#import modes.ssh.ssh as ssh
#import modes.evil_twin.evil_twin as evil_twin
#variables
running=True
modes = ['ssh','evil_twin']
selected_mode_index = 0
selected_mode = modes[0]
tabs = ['modes','options','overview']
current_tab = 'modes'
#code

while running:
    #input check
    action = get_input()
    if action == 'up':
        selected_mode_index = (selected_mode_index + 1) % len(modes)
        selected_mode = modes[selected_mode_index]
        #print(selected_mode) #debug

    elif action == 'down':
        selected_mode_index -= 1
        selected_mode_index = (selected_mode_index + 1) % len(modes)
        selected_mode = modes[selected_mode_index]
        #print(selected_mode) #debug

    elif action == 'mode':
        if current_tab == 'modes':
            current_tab = 'overview'
        elif current_tab == 'overview':
            current_tab = 'modes'
    
    

