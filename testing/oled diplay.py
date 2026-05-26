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

number=1

default_eyes = """\
  (=ↀωↀ=) """
blink_left_eye = """
  (=~_ↀ=) """
blink_right_eye = """
  (=ↀ_~=) """
blink_both_eyes = """
  (=~_~=) """
faces=[blink_left_eye,blink_right_eye,blink_both_eyes]

ascii_art = default_eyes

while True:
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)  # clear image

    y = 0
    for line in ascii_art.split("\n"):
        draw.text((0, y), line, fill=255, font=font)
        y += 8

    if blinking:
        time.sleep(blink_timer)
        ascii_art = default_eyes
        blinking = False
        no_blinking_timer = random.randint(0.5, 3)

    if not blinking:
        time.sleep(no_blinking_timer)
        ascii_art = random.choice(faces)
        blinking=True
        blink_timer = random.randint(0.1, 1)


    oled.fill(0)
    oled.image(image)
    oled.show()
