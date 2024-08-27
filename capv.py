import time
from pynput import mouse, keyboard

running = False
start_pos = None

def on_press(key):
    global running
    global start_pos
    try:
        if key == keyboard.Key.insert:
            running = True
            if running:
                start_pos = mouse_controller.position
                start_automation()
    except AttributeError:
        pass

def start_automation():
    mouse_controller.press(mouse.Button.left)
    time.sleep(5)
    mouse_controller.release(mouse.Button.left)
    while running:
        for _ in range(4):
            if not running:
                return
            click_and_hold(100)
        if running:
            mouse_controller.position = start_pos

def click_and_hold(move_x):
    current_pos = mouse_controller.position
    mouse_controller.press(mouse.Button.left)
    time.sleep(4)
    mouse_controller.release(mouse.Button.left)
    mouse_controller.position = (current_pos[0] + move_x, current_pos[1])

mouse_controller = mouse.Controller()
keyboard_listener = keyboard.Listener(on_press=on_press)

keyboard_listener.start()
keyboard_listener.join()