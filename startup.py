import os, sys
from tkinter import *

root = Tk()
var = StringVar()

label = Label( root, textvariable=var, relief=RAISED )

var.set("Swaminarayan")
label.pack()
root.mainloop()
