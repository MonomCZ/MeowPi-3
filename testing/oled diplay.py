from PIL import ImageFont
from PIL import Image, ImageDraw
import board
import busio
import adafruit_ssd1306
import time

WIDTH = 128
HEIGHT = 64
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 8)


i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

number=1

ascii_art = """\
  (=ↀωↀ=) """

while True:
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)  # clear image

    y = 0
    for line in ascii_art.split("\n"):
        draw.text((0, y), line, fill=255, font=font)
        y += 8

    oled.fill(0)
    oled.image(image)
    oled.show()
