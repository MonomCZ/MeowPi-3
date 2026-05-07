#main.py
#libraries etc 
from config import input_mode as input_mode
import main_functions.funtions as functions
if input_mode == 'keyboard':
    from input.keyboard import get_input as get_input
#elif input_mode == 'gpio':
#    from input.gpio import  as 
from modes.evil_twin.wifi_options import options as evil_twin_options
#import modes.ssh.ssh as ssh
#import modes.evil_twin.evil_twin as evil_twin
#variables
running=True

tabs = ['modes','options','overview']
current_tab = 'modes'
#modes
modes = ['ssh','evil_twin']
current_mode = None
selected_mode_index = 0
selected_mode = modes[0]
#options
modes_options = [evil_twin_options]
modes_options_index = 0
selected_option = 0
options = []
#code

while running:
    #input check
    action = get_input()
    if action == 'up':
        selected_mode_index = functions.scrolling_list(current_tab, modes, options, selected_mode_index, 1)
        selected_mode = modes[selected_mode_index]
        #print(selected_mode) #debug

    elif action == 'down':
        selected_mode_index = functions.scrolling_list(current_tab, modes, options, selected_mode_index, -1)
        selected_mode = modes[selected_mode_index]
        #print(selected_mode) #debug

    elif action == 'mode':
        if current_tab == 'modes':
            current_tab = 'overview'
        else:
            current_tab = 'modes'
    elif action == 'option':
        if current_tab == 'options':
            current_tab = 'overview'
        else:
            current_tab = 'options'
    elif action == 'confirm':
        if current_tab == 'modes':
            current_mode = selected_mode
            #print(selected_mode) #debug


    action = None
    

