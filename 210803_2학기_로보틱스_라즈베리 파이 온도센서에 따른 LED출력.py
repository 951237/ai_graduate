# 라이브러리 가져오기
import board
import adafruit_dht
import neopixel

# 온습도계 센서 객체 생성
dhtDevice = adafruit_dht.DHT22(board.D4)

# led 센서 객체 생성
pixels = neopixel.NeoPixel(board.D18, 8)

def led_color(r, g, b):
    pixels[0] = (int(r), int(g), int(b))
    pixels[1] = (int(r), int(g), int(b))
    pixels[2] = (int(r), int(g), int(b))
    pixels[3] = (int(r), int(g), int(b))
    pixels[4] = (int(r), int(g), int(b))
    pixels[5] = (int(r), int(g), int(b))
    pixels[6] = (int(r), int(g), int(b))
    pixels[7] = (int(r), int(g), int(b))

while True:
    temperature_c = dhtDevice.temperature
    if float(temperature_c) <= 25:   # 25도 이하면 파랑색
        led_color(0, 0, 255)
        pixels.show
    elif float(temperature_c) <= 27:    # 25도 초과 27도 이하면 노랑색
        led_color(255, 255, 0)
        pixels.show
    elif float(temperature_c) > 27: # 27도 이상이면 빨강색
        led_color(255, 0, 0)
        pixels.show
