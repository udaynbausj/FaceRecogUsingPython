import time
import re
from .recog import *
file = open("testfile.txt","w")
file.write("NAME")
file.write(",")
file.write("REGD.NO")
file.write(",")
file.write("DATE,TIME")
file.write("\n")
for t in range(0, 1):
    file.write(user)
    file.write(",")
    file.write(str(folder))
    file.write(",")
    file.write(time.strftime("%d/%m/%y"))
    file.write(",")
    file.write(time.strftime("%I:%M:%S"))



