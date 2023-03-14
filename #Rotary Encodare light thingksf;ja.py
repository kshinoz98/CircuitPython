#Rotary Encodare light thingksf;ja
import time
import rotaryio
import board
from digitalio import DigitalInOut, Direction, Pull

encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)
last_position = 0
btn = DigitalInOut(board.D1)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0

while True:
    position = encoder.position
    if position != last_position:
        print(position)
        if position > last_position:
            ("Up")
        elif position < last_position:
            ("Down")
    last_position = position
    if btn.value == 0:
        print("buttion")
        time.sleep(.005)

    
