from digitalio import DigitalInOut, Direction, Pull
import board

from midi_event import Event, EventType


gps = [
    {'pin': board.GP0, 'note': 69},
    {'pin': board.GP1, 'note': 72},
    {'pin': board.GP2, 'note': 66},
    {'pin': board.GP3, 'note': 63},
    {'pin': board.GP4, 'note': 60},
    {'pin': board.GP5, 'note': 57},
    {'pin': board.GP6, 'note': 54},
    {'pin': board.GP7, 'note': 51}, # d#
    {'pin': board.GP8, 'note': 48}, # с
    {'pin': board.GP9, 'note': 70},
    {'pin': board.GP10, 'note': 67},
    {'pin': board.GP11, 'note': 64},
    {'pin': board.GP12, 'note': 61},
    {'pin': board.GP13, 'note': 58},
    {'pin': board.GP14, 'note': 55},
    {'pin': board.GP15, 'note': 52}, # e
    {'pin': board.GP16, 'note': 49}, # c#
    {'pin': board.GP17, 'note': 71},
    {'pin': board.GP18, 'note': 68},
    {'pin': board.GP19, 'note': 65},
    {'pin': board.GP20, 'note': 62},
    {'pin': board.GP21, 'note': 59},
    {'pin': board.GP22, 'note': 56},
    {'pin': board.GP26, 'note': 53},
    {'pin': board.GP27, 'note': 50}, # d
    {'pin': board.GP28, 'note': 47}
    ]

class Keyboard:

    def __init__(self, queue):
        self.queue = queue
        self.buttons = []
        self.pressed = []
        self.layout = []
        
        for pin in gps:
            switch = DigitalInOut(pin['pin'])
            switch.direction = Direction.INPUT
            switch.pull = Pull.UP

            self.buttons.append(switch)
            self.pressed.append(False)
            self.layout.append(pin['note'])


    def read_buttons(self):
        current = [but.value != True for but in self.buttons] # check 0 digital input

        for i in range(len(current)):
            cur = current[i]
            prev = self.pressed[i]
            if cur == prev:
                continue

            note = self.layout[i]
            # print(str(i) + " " + str(note))
            if cur == True: 
                self.queue.append(Event(type = EventType.NOTE_ON, value = note))
            if cur == False:
                self.queue.append(Event(type = EventType.NOTE_OFF, value = note))

            
        self.pressed = current
