from PIL import ImageFont
from PIL import Image, ImageDraw
import board
import busio
import adafruit_ssd1306
import time
import random

WIDTH = 128
HEIGHT = 64
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 6)


i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

ascii_art = """\
 ╱|、
(˚ˎ 。7
|、˜〵        
じしˍ,)ノ
   """

for line in ascii_art.split("\n"):
        draw.text((0, y), line, fill=255, font=font)
        y += 8


oled.image(image)
oled.show()
