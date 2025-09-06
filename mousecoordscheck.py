import pyautogui
import pynput.mouse as mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")

# Start listening for mouse events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()


'''
Mouse clicked at (245, 507)

Mouse clicked at (237, 421)

Mouse clicked at (239, 574)

70 apart
'''
