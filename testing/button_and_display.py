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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 20)

number=1

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()
number=1
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)


while True:
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=0)
    draw.text((0, 0), str(number), fill=255, font=font)
    if gpio_input.button1():
        print("Button 1 pressed")
        number+=1

    oled.image(image)
    oled.show()
