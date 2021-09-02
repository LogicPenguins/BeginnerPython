import pyautogui
import os
from pathlib import Path


os.chdir(f"{Path.home()}\\small-projects-python\\pyautogui")

pyautogui.click(800, 400)
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

# Finished Automate The Boring Stuff - 8/31/2021