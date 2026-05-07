#keyboard.py 
#for testing without rpi or gpio
def get_input():
    keypress=input('enter your action:')
    if keypress == 'w' or keypress == 'u':
        return 'up'
    elif keypress == 's' or keypress == 'd':
        return 'down'
    elif keypress == 'm':
        return 'mode'
    elif keypress == 'o':
        return 'options'
    elif keypress == 'c':
        return 'confirm'