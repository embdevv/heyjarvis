# main.py
# SECURITY: No network code here. Starts UI + wake loop.

import threading
from modules.visualizer import run_visualizer
from modules.wake_word  import listen_for_wake_word

if __name__ == "__main__":
    # Start the visualizer in a separate thread
    ui_thread =   threading.Thread(target=run_visualizer, daemon=True)
    wake_thread = threading.Thread(target=listen_for_wake_word, daemon=False)

    ui_thread.start()
    wake_thread.start()
    
    ui_thread.join()  # Wait for the UI thread to finish
    wake_thread.join()  # Wait for the wake word thread to finish