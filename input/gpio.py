import RPi.GPIO as GPIO
import time

btn = 22

while True:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    if GPIO.input(btn) == 1:
        print("Button is pressed")
        time.sleep(0.2)