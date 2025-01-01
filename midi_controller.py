import time
import random
import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.control_change import ControlChange
from adafruit_midi.program_change import ProgramChange

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

print("Midi test")

print("Default output MIDI channel:", midi.out_channel + 1)


midi.send(ControlChange(3, 44))


while True:
    midi.send(NoteOn("A4", 120))  # 44 G sharp 2nd octave
    time.sleep(0.25)
    a_pitch_bend = PitchBend(random.randint(0, 16383))
#    midi.send(a_pitch_bend)
    time.sleep(0.25)
    midi.send(NoteOff("A4", 120)) # 


    midi.send(ProgramChange(22), channel = 0)
    time.sleep(0.5)
