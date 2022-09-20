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
Redo = True                     #[16-17] Variables to 
Redo2 = True                    # "debounce" button
lcd.print("Starting")
while True:                                     #[19-35] Code to add and subtract
    if btn.value == True and Redo == True:      #from variable and "debounce" the 
        num = num + 1                           #buttons.
        lcd.clear()
        lcd.print(str(num))
        Redo = False
        time.sleep(.1)
    elif btn.value == False and Redo == False:
        Redo = True
    if btn2.value == True and Redo2 == True:
        num = num - 1
        lcd.clear()
        lcd.print(str(num))
        Redo2 = False
        time.sleep(.1)
    elif btn2.value == False and Redo2 == False:
        Redo2 = True