import time
from digitalio import DigitalInOut, Direction, Pull
import board

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

buttons = []

gps = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    board.GP27,
    board.GP28,
    ]

for pin in gps:
    switch = DigitalInOut(pin)
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    buttons.append(switch)



while True:
    
    pressed = False
    for but in buttons:
      if but.value != True:
        pressed = True
        break

    led.value = pressed

    
#    led.value = True
#    time.sleep(0.1)
#    led.value = False
#    time.sleep(0.1)