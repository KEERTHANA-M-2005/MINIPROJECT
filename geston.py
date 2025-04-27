import tkinter as tk
from tkinter import ttk
import subprocess
import os
import warnings

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

def open_file1():
    subprocess.Popen(["python", r"./cursor.py"])

def open_file2():
    subprocess.Popen(["python", r"./vbcontrol.py"])

# Create main window
window = tk.Tk()
window.title("Geston")
window.geometry("300x300")

# Set background color
window.configure(bg="#f0f0f0")  # Light gray background

# Create a ttk style for buttons
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 12),
                padding=10,
                relief="flat",
                background="#4CAF50",  # Green button color
                foreground="black",  # **Set text color to black**
                borderwidth=0,  # Remove border
                )
style.map("TButton",
          background=[('active', '#45a049')],  # Darker green on active
          foreground=[('active', 'black')],  # **Ensure active state text is also black**
          )

# Add title label
title_label = tk.Label(window, text="Geston", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#444444")  # Dark gray title
title_label.pack(pady=15)

# Add description label
description_label = tk.Label(window, text="Control your environment with simple gestures.\nChoose an action below to begin.", font=("Helvetica", 10), bg="#f0f0f0", fg="#666666", justify="center") # DarkerDescription
description_label.pack(pady=5)

# Create buttons with styled ttk.Button
button1 = ttk.Button(window, text="Start Cursor Control", command=open_file1)
button1.pack(pady=15)

button2 = ttk.Button(window, text="Start VB Control", command=open_file2)
button2.pack(pady=15)

# Run the Tkinter event loop
window.mainloop()
