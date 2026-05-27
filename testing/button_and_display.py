from PIL import ImageFont
from PIL import Image, ImageDraw
import board
import busio
import adafruit_ssd1306
import time
import random
import input.gpio_input as gpio_input

WIDTH = 128
HEIGHT = 64
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 15)

number=1

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()
number=1
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

draw.text((0, 0), 'press the button 11 times!', fill=255, )
oled.image(image)
oled.show()

while True:
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=0)
    if number > 11:
        draw.text((0, 15), 'Good Boyy~', fill=255, font=font)
        time.sleep(0.00001)
        number=0

    elif number==0:
        if gpio_input.button1():
            draw.text((0, 0), 'press the button 11 times!', fill=255,)
    else:
        if not number==11:
            draw.text((0, 15), str(number), fill=255, font=font)
        time.sleep(0.1)
        if gpio_input.button1():
            number+=1

    oled.image(image)
    oled.show()
