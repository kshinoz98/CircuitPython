## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
---

## Hello_CircuitPython

### Description & Code

In this assignment, we just started doing code with circuit python, and our assignment was to make the onboard neopixel red. The main focus of the assignment was to learn how to connect a board and getting familiar with the syntax of CircuitPython.

```python
import board
import neopixel
import time 
import math

Dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
Dot.brightness = 0.1 
print("Make it red!")
while True:
    Dot.fill((255,0,0))
```


### Evidence

![Spinning](https://github.com/kshinoz98/CircuitPython/blob/master/Untitled_%20Sep%2027,%202022%203_18%20PM.gif?raw=true)

### Reflection
Connecting to the Arduino actually took an incredible amount of time. Because the libraries were not built in, getting them in or replacing the libraries was very complicated. I learned a lot about what it takes to actually connect a board up, and even just getting that little light to turn red was a big victory. Also, in this time, I realized that circuitpython is a lot similar to C++ but with more adaptability for libraries. If I did this assignment again I would cheat off other people a lot earlier, because I spent a while just flondering while the people next to me actually knew what to do.

## CircuitPython_Servo

### Description & Code

Using circuitpython,connect to a servo and rotate it 180 degrees and back using buttons. The focus of this assignment is to learn how to use servos, and just generally learn how to use electronic parts with the metro.

```python
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
```

Evidence              | Wiring
:-------------------------:|:-------------------------:
<img src="https://github.com/kshinoz98/CircuitPython/blob/master/Untitled_%20Sep%2029,%202022%203_40%20PM.gif?raw=true" alt="The Base" height="300">  |  <img src="https://github.com/kshinoz98/CircuitPython/blob/master/Screen%20of%20servo%20wiring.png?raw=true" alt="The Base" height="300">

### Reflection

Using PWMio I connected an object to the 3 pin. What that means, I have no clue, but thats how it works. Thanks to [**This Site**](https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo) for that information.
 From there, it's fairly simple to just use the adafruit motor library function .Servo(). If I could do this assignment again, I probably would have just googled it a lot earlier and then I wouldn't have spent so much time trying to figure out the code myself.

## CircuitPython_LCD

### Description & Code

```python
import board
import math
import time
from lcd.lcd import LCD                                     #[4-14] code to connect 
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface   #input pins to board
from digitalio import DigitalInOut, Direction, Pull
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn2.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.pull = Pull.UP
num = 0                         #Display Variable
Redo = True                     #[16-17] Variable to "debounce" button

lcd.print("Starting")
while True:                                 #[19-30] Code to add and subtract 
    if btn.value == True and Redo == True:  #from variable and 
        if btn2.value == True:              #"debounce" the  #buttons.         
            num = num - 1
        else:
            num = num + 1                                   
        lcd.clear()
        lcd.print(str(num))
        Redo = False
        time.sleep(.1)
    elif btn.value == False and Redo == False:
        Redo = True

```
Evidence              | Wiring
:-------------------------:|:-------------------------:
<img src="https://github.com/kshinoz98/CircuitPython/blob/master/ezgif-2.gif?raw=true" alt="The Base" height="400">  |  <img src="https://user-images.githubusercontent.com/113209502/199816756-320b356f-50dc-4665-8adc-c88c1b4b7e8a.png" alt="The Base" height="400">

### Reflection

Using some libraries, I connected the LCD screen and the buttons (Which was much harder than I expected). For the first button I had to "debounce" the counting button, and then the second button was a single if statement to tell it to count up or down. I feel like I had a pretty good grasp of this asssignment, as I had done one that was just like it in engineering 2, however I did get stuck on something for 30 mins when I only had to add .value. If I had to do this assignment again, I would have actually read the directions so I wouldn't have to redo the entire code because I did the wrong thing.

## Motor Control

### Description & Code

Using a transistor and an external battery pack, control a DC motor. The learning target of this assignment was to learn how to use a transitor as well as relearning how to create analog outputs in the neww coding language.

```python
import board               #[lines 1-4] Importing neccesary libraries
import time
from analogio import AnalogOut, AnalogIn
import simpleio

motor = AnalogOut(board.A1) #[lines 5 & 6] Definining the motor and potentiometer
pot = AnalogIn(board.A0)

while True:
    print(simpleio.map_range(pot.value, 96, 65520, 0, 65535)) #Print mapped potentiometer value to motor inputs
    motor.value = int(simpleio.map_range(pot.value, 96, 65520, 0, 65535)) #Write the mapped value to motor
    time.sleep(.1)                                                      #So that the serial monitor works

```
Evidence              | Wiring
:-------------------------:|:-------------------------:
<img src="https://github.com/kshinoz98/CircuitPython/blob/d20d813b4dadc8ccec0c083e8bce710b5941454e/Untitled_%20Nov%202,%202022%2012_49%20PM.gif?raw=true" alt="The Base" height="400">  |  <img src="https://user-images.githubusercontent.com/113209502/199816609-97197a27-0c43-4816-a0a1-7d8257e2447a.pnG" alt="The Base" height="400">

### Reflection

Using a few different libraries I connected to the ultrasonic sensor, and managed to get a running distance. However, that was only the easiest part. Finding the right bounds and ways to shade from red to blue and blue to green took quite a while, as there are a lot of way which have varying levels of workingness. However, the way that I finally went with seemed to have work the best. By defining ranges, I made the light shade correctly. If I did this assignment again, I would takes Graham's advice and learn how to use elif and else


