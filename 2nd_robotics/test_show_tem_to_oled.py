# 온도 습도 센서의 결과를 oled에 출력하기
from PIL import Image, ImageDraw, ImageFont
import time

import board
import busio
import adafruit_ssd1306
import adafruit_dht

# 온습도 센서 객체 생성
dhtDevice = adafruit_dht.DHT22(board.D4)

i2c = busio.I2C(board.SCL, board.SDA)

# creat obj ss1396
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# clear display
disp.fill(0)
disp.show()

# create blank image
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# get drawing obj
draw = ImageDraw.Draw(image)

# draw clear image
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# first define some constant
padding = -1
top = padding
bottom = height - padding
x = 0

# load font
font = ImageFont.load_default()

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    temperature = dhtDevice.temperature
    huminity = dhtDevice.humidity

    draw.text((x, top + 2), f"Temperature : {temperature}C", font=font, fill=255)
    draw.text((x, top + 12), f"Huminity : {huminity}%", font=font, fill=255)

    # display image
    disp.image(image)
    disp.show()
    time.sleep(0.1)





print(temperature, huminity)

