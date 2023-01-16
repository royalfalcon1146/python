# There is no tomorrow!!!
#! Waiting for a challenge!
import os
import datetime

timestamp = os.path.getmtime(r"C:\Users\ALBARAA.DESKTOP-87EJ24R\Programming\Tests Folder\myTxtFile.txt")
t = str(datetime.datetime.fromtimestamp(timestamp))

print(t[:11])

