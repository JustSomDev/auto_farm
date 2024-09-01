from time import sleep
import os
os.system("pip install pyautogui")
os.system("pip install keyboard")
from keyboard import *
from pyautogui import *
state = False
b = False
while True:
	if is_pressed("f4"):
		state=not state
		print("switched")
	if state:
		mouseDown(button='left')
		b=True
		sleep(0.1)
	if b and not state:
		mouseUp(button='left')
		b=False
	sleep(0.05)