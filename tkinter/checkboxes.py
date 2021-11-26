from tkinter import *

root = Tk()
root.title('Title')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myLabel = Label(root, text=var.get()).pack()
myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()