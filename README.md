## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code

In this assignment, we started doing code with circuit python. We just needed to make the onboard neopixel red.

```python
import board
import neopixel
import time 
import math

Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)
Kaz.brightness = 0.1 
print("Make it red!")
while True:
    Kaz.fill((255,0,0))
```


### Evidence

![Spinning](https://github.com/kshinoz98/CircuitPython/blob/master/Untitled_%20Sep%2027,%202022%203_18%20PM.gif?raw=true)

### Reflection
Connecting to the Arduino actually took an incredible amount of time. I learned a lot about what it takes to actually connect a board up, and even just getting that little light to turn red was a big victory. Also, in this time, I realized that circuitpython is a lot similar to C++ but with more adaptability for libraries. If I did this assignment again I would cheat off other people a lot earlier, because I spent a while just flondering while the people next to me actually knew what to do.

## CircuitPython_Servo

### Description & Code

Using circuitpython, connect to a servo and rotate it 180 degrees and back using buttons

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

### Evidence

![,,](https://github.com/kshinoz98/CircuitPython/blob/master/Untitled_%20Sep%2029,%202022%203_40%20PM.gif?raw=true)

### Wiring

![.](https://github.com/kshinoz98/CircuitPython/blob/master/Screen%20of%20servo%20wiring.png?raw=true)

### Reflection

Using PWMio I connected an object to the 3 pin. What that means, I have no clue, but thats how it works. From there, it's fairly simple to just use the adafruit motor library. Using .Servo() I moved it back and forth. If I could do this assignment again, I probably would have just googled it a lot earlier and then I wouldn't have spent so much time trying to figure out the code.

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

### Evidence

![gif](https://github.com/kshinoz98/CircuitPython/blob/master/ezgif-2.gif?raw=true)

### Wiring

![gif](https://raw.githubusercontent.com/kshinoz98/CircuitPython/b45fed4ddee888d03481fca24c670a8d5ac0b01c/Screenshot%202022-09-27%20144318.png)

### Reflection

Using some libraries, I connected the LCD screen and the buttons (Which was much harder than I expected). For the first button I had to "debounce" the counting button, and then the second button was a single if statement to tell it to count up or down. I feel like I had a pretty good grasp of this asssignment, as I had done one that was just like it in engineering 2, however I did get stuck on something for 30 mins when I only had to add .value. If I had to do this assignment again, I would have actually read the directions so I wouldn't have to redo the code because it did the wrong thing.

## RGB Led with Ultrasonic Sensor

### Description & Code

```python
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

```

### Evidence

![gif](https://github.com/kshinoz98/CircuitPython/blob/master/ezgifgif.gif?raw=true) 

### Wiring

![png](https://raw.githubusercontent.com/kshinoz98/CircuitPython/f4be6df7eb8828500e94754d2ccb5b5c8cd2b276/Screenshot%202022-09-19%20154243.png)

### Reflection

Using a few different libraries I connected to the ultrasonic sensor, and managed to get a running distance. However, that was only the easiest part. Finding the right bounds and ways to shade from red to blue and blue to green took quite a while, as there are a lot of way which have varying levels of workingness. However, the way that I finally went with seemed to have work the best. By defining ranges, I made the light shade correctly. If I did this assignment again, I would takes Graham's advice and learn how to use elif and else
