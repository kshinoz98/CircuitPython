#[Lines 1-6] Importing neccesary libraries
import board            #Communcating to Arduino
import time             #So I can use sleep() function
import math             #So that logic works
import adafruit_hcsr04  #Communcating to Ultrasonic Sensor
import simpleio         #So I can use map() function
import neopixel         #Communicating to Neopixel
dot=neopixel.NeoPixel(board.NEOPIXEL,1)
dot.brightness=.1
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2) #Defining the pins for Ultrasonic Sensors
son = 0                                                                 #Variable to define averaging (ish)
print("Starting")
while True:
    try:
        if (son - sonar.distance) < 10 and (son - sonar.distance) > -10 :   #If the distance doesn't jump up or down 10
            if sonar.distance < 5:                                          #Defining bounds for shading in and out
                dot.fill((255,0,0))
            elif sonar.distance < 10 and sonar.distance > 5:                #Defining bounds for shading in and out
                dot.fill((simpleio.map_range(sonar.distance,5,10,255,0),0,simpleio.map_range(sonar.distance,5,10,0,255)))
            else:                                                           #Defining bounds for shading in and out
                dot.fill((0,simpleio.map_range(sonar.distance,10,20,0,255),simpleio.map_range(sonar.distance,10,20,255,0)))
        print((sonar.distance)) #For checking bugs
        son=sonar.distance      #To find if the distance jumps
        time.sleep(.001)        #Delay
    except RuntimeError:
        print("Retrying!")