from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0, "Enter Something")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Enter Something", command=myClick)
myButton.pack()

root.mainloop()