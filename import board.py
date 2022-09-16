import board
import time 
import math
import adafruit_hcsr04
import simpleio
import neopixel
dot=neopixel.NeoPixel(board.NEOPIXEL,1)
dot.brightness=.1
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
print("starting")
while True:
    try:
        if sonar.distance < 5:
            dot.fill((255,0,0))
        elif sonar.distance < 10 and sonar.distance > 5:
            dot.fill((simpleio.map_range(sonar.distance,5,10,255,0),0,simpleio.map_range(sonar.distance,5,10,0,255)))
        else:
            dot.fill((0,simpleio.map_range(sonar.distance,10,20,0,255),simpleio.map_range(sonar.distance,10,20,255,0)))
        print((sonar.distance))
        time.sleep(.001)
    except RuntimeError:
        print("Retrying!")