import board
import time 
import math
import adafruit_hcsr04
import simpleio
import neopixel
dot=neopixel.NeoPixel(board.NEOPIXEL,1)
Var = 0
blue = 0
green = 0
red = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
print("starting")
while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    if sonar.distance > 0 and sonar.distance < 5:
        dot.fill(simpleio.map_range(sonar.distance,0,5,255,0),0,simpleio.map_range(sonar.distance,0,5,0,255))
    if sonar.distance > 5 and sonar.distance < 20:
        dot.fill(0,simpleio.map_range(sonar.distance,0,5,0,255),simpleio.map_range(sonar.distance,0,5,255,0))
    if sonar.distance > 20:
        dot.fill(simpleio.map_range(sonar.distance,0,40,0,600))
