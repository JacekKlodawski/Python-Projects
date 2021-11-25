from tkinter import *
from PIL import *

root = Tk()
root.title('Title')

def open():
    top = Toplevel()
    lbl = Label(top, text="New Window").pack()

btn = Button(root, text="Open Window", command=open).pack()



root.mainloop()