# midi-bayan-keyboard
USB midi-keyboard with bayan layout

Idea is to implement bayan layout midi-keyboard using high level language like python. That is the first step to implement fully functional midi-bayan.

Today only circuitpython has midi-usb library to send commands. So we cannot use MicroPython.

Raspberry Pi Pico has 26 digital inputs, so we can implement 26 keys without shift registers or matrixes.

# Steps

## 1. install CircuitPython to raspberry pi pico

Here is the instruction https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython

Press button and plug board to usb. Now it appears as a remote disk. Then copy `adafruit_circuitpython_etc.uf2`. That's it.

## 2. install code

Reboot board.

Install editor 
- [mu-editor](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/installing-mu-editor)
- [thonny](https://thonny.org/)

Copy all the files to your board except `sch` folder. That's all. Your midi-keyboard is ready.
