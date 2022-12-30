#This code opens a window to select a file to read every line of.
#If the user doesnt select a file, an error will happen, just put a try and except method :)
import tkinter as tk
from tkinter import filedialog

# Create a GUI window
root = tk.Tk()
root.withdraw()

# Open a file dialog and get the selected file's path
file_path = filedialog.askopenfilename()

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read and process the file contents
  for line in file:
    # Do something with each line
    pass