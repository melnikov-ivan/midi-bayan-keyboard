from digitalio import DigitalInOut, Direction, Pull
from board import LED
import time

from midi_keyboard import Keyboard
from midi_controller import Controller

led = DigitalInOut(LED)
led.direction = Direction.OUTPUT


queue = list()
keyboard = Keyboard(queue)
controller = Controller(queue)

import gc

i = 0
while True:
    keyboard.read_buttons()
    controller.process()
    
    i = i + 1
    if i % 1000 == 0:
        i = 0
        print(gc.mem_alloc())
        #print(gc.mem_free())
        led.value = True
#        time.sleep(0.5)
        led.value = False
#       time.sleep(0.5)
