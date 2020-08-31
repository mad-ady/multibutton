#!/usr/bin/python3
from evdev import uinput, ecodes as e
import sys

#validate that the arguments sent are valid strings defined in linux/input.h
if len(sys.argv) == 1 :
    print("""Usage: """+sys.argv[0]+""" KEY_A KEY_LEFTSHIFT

Inject an arbitrary key combination via uinput kernel module.
Key syntax is defined in linux/input.h
    """)
    exit()
else:
    for key in sys.argv[1:]:
        if key not in e.ecodes:
            sys.stderr.write("Error: "+key+" is not a valid key defined in linux/input.h\n")
            exit(1)

with uinput.UInput() as ui:
    for key in sys.argv[1:]:
        ui.write(e.EV_KEY, e.ecodes[key], 1)
    ui.syn()
    