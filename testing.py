#!/usr/bin/env python3
#! THERE IS NO TOMORROW!!!
#! DON'T WAIT FOR A CHANCE!!!

from tkinter import * #? Importing the module

mywindow = Tk() #? Setting the variable as our popup message
mywindow.title("Title of pop here")
mywindow.geometry("400x300") #? Size of the popup window
text = Label(mywindow, text= "Text you want to display")
text.pack()

mywindow.mainloop()