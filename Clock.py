from tkinter import Tk
from tkinter import Label
import time
from time import strftime

root = Tk()
root.title("DIGITAL CLOCK")

def time():
    display_time = strftime('%I:%M:%S %p')
    clock.config(text=display_time)
    clock.after(200,time)
clock = Label(root,font=("arial",150),bg="black",fg="blue")

clock.pack()

time()

root.mainloop()

