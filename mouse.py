import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import random
import time

class MouseMover:
    def __init__(self, master):
        self.master = master
        self.master.title("Mouse Mover")
        self.master.geometry("300x200")
        
        self.running = False

        # Create UI elements
        self.label = tk.Label(master, text="Seleziona la durata (ore):")
        self.label.pack(pady=10)
        
        self.duration_var = tk.StringVar(value="1")
        self.duration_menu = ttk.Combobox(master, textvariable=self.duration_var, values=["1", "2", "3"])
        self.duration_menu.pack(pady=5)

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def start(self):
        try:
            self.duration = int(self.duration_var.get()) * 3600
        except ValueError:
            self.duration = 3600  # Default to 1 hour if invalid input
        
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        # Start the mouse moving in a separate thread
        self.thread = threading.Thread(target=self.move_mouse)
        self.thread.start()

    def stop(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def move_mouse(self):
        start_time = time.time()
        while self.running and (time.time() - start_time < self.duration):
            x = random.randint(0, pyautogui.size().width)
            y = random.randint(0, pyautogui.size().height)
            pyautogui.moveTo(x, y, duration=0.5)
            time.sleep(5)
        
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMover(root)
    root.mainloop()