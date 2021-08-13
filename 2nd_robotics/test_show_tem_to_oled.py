# 온도 습도 센서의 결과를 oled에 출력하기
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime

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

def draw_txt(loc, sub, result):
    draw.text((x, top + loc), f"{sub} : {result}", font=font, fill=255)

def time_now(per_sec = 1):
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        time.sleep(per_sec)
        return now

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    temperature = dhtDevice.temperature
    huminity = dhtDevice.humidity
    now = time_now()

    draw_txt(2, 'Temperature', temperature)
    draw_txt(12, 'Huminity', huminity)
    draw_txt(22, 'Now', now)

    # display image
    disp.image(image)
    disp.show()
    time.sleep(0.1)





print(temperature, huminity)

