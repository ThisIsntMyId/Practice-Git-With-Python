# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

#creating tk object
top = Tk()

#creating a canvas
C = Canvas(top, bg = "blue", height = 250, width = 300)

coord = 10, 10, 240, 210

#creating arc
arc = C.create_arc(coord, start = -90, extent = 350, fill = "red")
C.pack()
top.mainloop()
#my comment at the end
