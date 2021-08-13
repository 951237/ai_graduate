import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
x = 0

sequence = [
    [(24, 5, 50, 50), (78, 5, 104, 50)],
    [(24, 5, 50, 50), (78, 10, 104, 45)],
    [(24, 5, 50, 50), (78, 20, 104, 35)],
    [(24, 5, 50, 50), (78, 30, 104, 30)],
    [(24, 5, 50, 50), (78, 20, 104, 35)],
    [(24, 5, 50, 50), (78, 10, 104, 45)],
    [(24, 5, 50, 50), (78, 5, 104, 50)],

    [(24, 5, 50, 50), (78, 5, 104, 50)],
    [(24, 10, 50, 45), (78, 5, 104, 50)],
    [(24, 20, 50, 35), (78, 5, 104, 50)],
    [(24, 30, 50, 30), (78, 5, 104, 50)],
    [(24, 20, 50, 35), (78, 5, 104, 50)],
    [(24, 10, 50, 45), (78, 5, 104, 50)],
    [(24, 5, 50, 50), (78, 5, 104, 50)],

    [(24, 5, 50, 50), (78, 5, 104, 50)],
    [(24, 20, 50, 35), (78, 20, 104, 35)],
    [(24, 5, 50, 50), (78, 5, 104, 50)],
    [(24, 20, 50, 35), (78, 20, 104, 35)],
    [(24, 5, 50, 50), (78, 5, 104, 50)],
    [(24, 20, 50, 35), (78, 20, 104, 35)],
    [(24, 5, 50, 50), (78, 5, 104, 50)],
    [(24, 20, 50, 35), (78, 20, 104, 35)],
]

# Load default font.
font = ImageFont.load_default()
def eye(fir, sec):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #draw eye
    draw.rectangle(fir, outline=1, fill=255)
    draw.rectangle(sec, outline=1, fill=255)
    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(0.1)

for sec in sequence:
    eye(sec[0], sec[1])


