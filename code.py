from digitalio import DigitalInOut, Direction, Pull
from board import LED

from midi_keyboard import Keyboard
from midi_controller import Controller

led = DigitalInOut(LED)
led.direction = Direction.OUTPUT


queue = list()
keyboard = Keyboard(queue)
controller = Controller(queue)

import time
time.sleep(1)

i = 0
while True:
    keyboard.read_buttons()
    controller.process()
    queue.clear()
    
    i = i + 1
    if i % 1000 == 0:
        i = 0
        led.value = True
        led.value = False
