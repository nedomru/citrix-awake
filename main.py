import pystray
from PIL import Image
import ctypes
import threading
import time
import sys


# Create a simple white icon (16x16)
def create_icon():
    image = Image.new('RGB', (16, 16), color='white')
    return image


# Function to prevent screen lock without input simulation
def prevent_screen_lock():
    while True:
        # Set thread execution state to keep system awake
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)  # ES_SYSTEM_REQUIRED | ES_CONTINUOUS
        time.sleep(60)  # Check every minute


# Setup tray icon and menu
def setup_tray():
    icon = pystray.Icon("ScreenStay")
    icon.icon = create_icon()
    icon.menu = pystray.Menu(
        pystray.MenuItem('Выйти', lambda: (icon.stop(), sys.exit(0)))
    )

    # Start screen lock prevention in a separate thread
    thread = threading.Thread(target=prevent_screen_lock, daemon=True)
    thread.start()

    icon.run()


if __name__ == "__main__":
    setup_tray()