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

draw.text((0, 0), "Hello World!", fill=255)
draw.text((0, 16), "This is a test.", fill=255)
draw.text((0, 32), "Another line.", fill=255)
draw.text((0, 48), "Last line.", fill=255)



oled.image(image)
oled.show()