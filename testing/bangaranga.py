from PIL import ImageFont
from PIL import Image, ImageDraw
import board
import busio
import adafruit_ssd1306
import time
import random

WIDTH = 128
HEIGHT = 64
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 20)


i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

draw.text((0, 0), "Bangaranga!", font=font, fill=255)

oled.image(image)
oled.show()
