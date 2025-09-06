'''
while True:
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.left:
                while True:
                    location = pyautogui.locateOnScreen('interruptionsimg.png')
                    while True:
                        try:
                            pyautogui.moveTo(location)
                        except ImageNotFoundException:
                            continue

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
substring = "continue with interruptions"


while True:
   with keyboard.Events() as events:
       for event in events:
           if event.key == keyboard.Key.left:
               while True:
                   pyautogui.screenshot(region=(769,356,1128,594),r"C:\Users\divmi\OneDrive\Desktop\Coding Projects\SongsterrPopupBlock\test.png")
                   mainstring = pytesseract.image_to_string(Image.open('test.png'))
                   if substring in mainstring:
                       pyautogui.click(x=967, y=525)
                   else:
                       print("nope")
           else:
               print("waiting")


import pyautogui
from PIL import Image
import pytesseract
from pynput import keyboard

while True:
   with keyboard.Events() as events:
       for event in events:
           if event.key == keyboard.Key.left:
                while True:
                    location = pyautogui.locateOnScreen('interruptionsimg.png')
                    while True:
                        try:
                            pyautogui.moveTo(location)
                        except pyautogui.ImageNotFoundException:
                            continue




'''


