import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 8)

def led_color(r, g, b):
    pixels[0] = (r, g, b)
    pixels[1] = (r, g, b)
    pixels[2] = (r, g, b)
    pixels[3] = (r, g, b)
    pixels[4] = (r, g, b)
    pixels[5] = (r, g, b)
    pixels[6] = (r, g, b)
    pixels[7] = (r, g, b)

while True:
    led_color(255, 0, 0)
    pixels.show
