import time
import random
import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange
from adafruit_midi.program_change import ProgramChange

from midi_event import EventType

class Controller:
    
    def __init__(self, queue):
        self.queue = queue
        self.midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

        print("Default output MIDI channel:", self.midi.out_channel + 1)


    
    def process(self):
        for event in self.queue:
            if event.type == EventType.NOTE_ON:
                command = NoteOn(note = event.value, velocity = 127, channel = 0)
            elif event.type == EventType.NOTE_OFF:
                command = NoteOff(note = event.value, velocity = 127, channel = 0)
            else:
                raise Exception('Unsupported event type: ' + event.type)

            self.midi.send(command)
            
            # midi.send(NoteOff("A4", 120)) # 44 G sharp 2nd octave
            # midi.send(ControlChange(3, 44))
            # midi.send(ProgramChange(22), channel = 0)
            # midi.send(PitchBend(random.randint(0, 16383)))

        self.queue.clear()
