#Waiting for a challenge to come
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