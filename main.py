#keyboard or gpio
mode = 'keyboard'
if mode == 'keyboard':
    from input.keyboard import KeyboardInput as InputHandler
elif mode == 'gpio':
    from input.gpio import GpioInput as InputHandler


import modes.ssh.ssh as ssh
import modes.evil_twin.evil_twin as evil_twin
#variables
running=True
modes = ['ssh','evil_twin']
selected_mode = modes[0]

while running:
    #input check
    


    #if select pressed
    if selected_mode == 'ssh':
        print('running ssh')
        #run ssh mode tba
    elif selected_mode == 'evil_twin':
        print('running evil twin')
        #run evil twin mode tba
