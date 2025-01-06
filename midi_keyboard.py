from digitalio import DigitalInOut, Direction, Pull
import board

from midi_event import Event, EventType


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

class Keyboard:

    def __init__(self, queue):
        self.queue = queue
        self.buttons = []
        self.pressed = []
        
        for pin in gps:
            switch = DigitalInOut(pin)
            switch.direction = Direction.INPUT
            switch.pull = Pull.UP

            self.buttons.append(switch)
            self.pressed.append(False)



    def read_buttons(self):
        current = [but.value != True for but in self.buttons] # check 0 digital input
        i = 0
        for i in range(0, len(current) - 1):
            cur = current[i]
            prev = self.pressed[i]
            if cur == prev:
                continue
            
            if cur == True: 
                value = i + 40
                self.queue.append(Event(type = EventType.NOTE_ON, value = value))
            if cur == False:
                value = i + 40
                self.queue.append(Event(type = EventType.NOTE_OFF, value = value))

#            self.pressed[i] = cur
            i = i + 1
            
        self.pressed = current
