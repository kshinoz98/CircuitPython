import board
import neopixel
import time 
import math

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.25 
x = 0

print("Make it red!")

red = 254
green = 1
blue = 127
red_direction = -1
green_direction = 1
blue_direction = -1
while True:
    red = red + red_direction
    green = green + green_direction
    blue = blue + blue_direction
 
    if (red >= 255 or red <= 0):
        red_direction = red_direction * -1
    if (green >= 255 or green <= 0):
        green_direction = green_direction * -1
    if (blue >= 255 or blue <= 0):
        blue_direction = blue_direction * -1
    time.sleep(.01)
    dot.fill((red,green,blue))