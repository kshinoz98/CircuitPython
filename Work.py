import board
import neopixel
import time 
import math

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 
x = 0

print("Make it red!")

while True:
    dot.fill((x, 0, 0))
    time.sleep(0.000005)
    x=x+1