
from PIL import Image, ImageDraw
import board
import busio
import adafruit_ssd1306
import time

WIDTH = 128
HEIGHT = 64

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

number=1
while True:
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)  # clear image
    draw.text((0, 0), str(number), fill=255)
    number+=1
    time.sleep(0.0001)

    oled.fill(0)
    oled.image(image)
    oled.show()
