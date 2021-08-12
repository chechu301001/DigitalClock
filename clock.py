from tkinter import *
from time import strftime

root =Tk()
root.title("DigiClock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="light green")
label.pack(anchor='center')

time()

mainloop()