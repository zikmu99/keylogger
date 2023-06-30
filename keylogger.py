from pynput import keyboard

def on_press(key):
    with open("keyboard_usage.txt", "a") as file:
        file.write(f"Key Pressed: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the 'Esc' key
        return False

# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
