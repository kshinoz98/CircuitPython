import board                       #[1-16] Setup for Buttons                 
import time                        #And servo
import math
import pwmio 
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn2.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.pull = Pull.UP

pwm = pwmio.PWMOut(board.D5, duty_cycle=2 **15, frequency=50)
myServo = servo.Servo(pwm)

print("starting") 
while True:                 #[17-27]If a button is pressed
    print("re")             #Rotate to either 180 or 0
    if btn.value == True:
        myServo.angle = 180
        time.sleep(1)
        print("Right")
    elif btn2.value == True :
        myServo.angle = 0
        time.sleep(1)
        print("Left")