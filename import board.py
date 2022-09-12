import board
import neopixel
import time 
import math

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 
x = 0

print("Make it red!")
dot.fill((255,0,0))