# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:37:04 2020

@author: OHyic
"""

import os

from pynput import keyboard
from pynput import mouse



def on_press(key):
    try:
        print('[INFO] alphanumeric key %s pressed'%(key.char))
    except AttributeError:
        print('[INFO] special key %s pressed'%(key))
        if str(key) == "Key.space":
            text +=" "
        elif str(key) == "Key.backspace":
            text = text[:-1]
        elif str(key) in ["Key.tab","Key.enter"]:
            print("write into file")
        
        print(text)
def on_click(x, y, button, pressed):
    if pressed:
        print('[INFO] mouse click at (%d,%d)'%(x, y))
        print(text)

text = ""
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
text = ""
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
