from pynput import keyboard

def keyboard_start():
    with keyboard.Listener(on_press=action_function) as lstn:
        lstn.join()
        
def action_function(key):
    print(f"Pressed: {key}")