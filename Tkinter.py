import time
import os
import tkinter as tk

def mytkinter():
    root = tk.Tk()

    root.geometry("400x200")

    label = tk.Label(root,text="Please enter the path of the file", font=("", 15))
    label.pack(pady=20)

    textbox = tk.Text(root, height=3)
    textbox.pack()

    entry = tk.Entry(root, width=30)
    entry.pack()

    button = tk.Button(root, text="RUN")
    button.pack()

    root.mainloop()

