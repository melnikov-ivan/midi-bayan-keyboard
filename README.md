# midi-bayan-keyboard
USB midi-keyboard with bayan layout

Idea is to implement bayan layout midi-keyboard using high level language like python. That is the first step to implement fully functional midi-bayan.

Today only circuitpython has midi-usb library to send commands. So we cannot use MicroPython.

Raspberry Pi Pico has 26 digital inputs, so we can implement 26 keys without shift registers or matrixes.