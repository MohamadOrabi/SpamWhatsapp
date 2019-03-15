import numpy as np
from PIL import ImageGrab
# from directkeys import click, queryMousePosition
import pyautogui
import cv2
import time
import sys


x_send = 994*2;
y_send = 643*2;

x_type = 740*2;
y_type = 643*2;

while True:
	mouse_pos = pyautogui.position();

	if mouse_pos.x < 5:
		break;

pyautogui.keyDown('shift')

while (True):

	start_time = time.time()
	pyautogui.hotkey('command', 'v')
	pyautogui.press('enter')  					# press the Enter key

	print("Frame took () seconds",format(time.time()-start_time) )
	# pyautogui.keyDown('ctrl')
	# pyautogui.press('v')  # press the Enter key
	# pyautogui.keyUp('shift')
	# pyautogui.press('ctrl')  # press the Enter keyv