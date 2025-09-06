import pyautogui
from pynput import keyboard
while True:
   with keyboard.Events() as events:
       for event in events:
           if event.key == keyboard.Key.left:
               while True:
                   if pyautogui.pixelMatchesColor(979,568, (0,122,255),tolerance=1):
                      print("yeP")
                      pyautogui.click(x=970, y=568)
                   else:
                       print("nope")
           else:
               print("waiting")
