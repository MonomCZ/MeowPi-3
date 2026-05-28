#from PIL import ImageFont
from PIL import Image, ImageDraw
import board
import busio
import adafruit_ssd1306


WIDTH = 128
HEIGHT = 64

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

def display_text(text,y):
    draw.text((0, y), text, fill=255, )
    oled.image(image)
    oled.show()

def clear():
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0) 
    oled.image(image)
    oled.show()