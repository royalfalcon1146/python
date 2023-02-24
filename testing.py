#!/usr/bin/env python3
#! THERE IS NO TOMORROW!!!
#! DON'T WAIT FOR A CHANCE!!!

# for FILE in * ; do sudo python3 ~/Documents/testing/testing.py $FILE ; done

from PIL import Image
import subprocess
import os
import sys
# /opt/icons
# /home/student-04-46d2e4258652/images

my_filename = sys.argv[1]

my_image = Image.open(my_filename)
new_image = my_image.resize((128,128))
new_image = new_image.rotate(270)
new_image.save(fr"/opt/icons{my_filename}.jpeg")

