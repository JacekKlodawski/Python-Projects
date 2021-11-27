from tkinter import *

root = Tk()
root.title('Title')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, *options).pack()

myButton = Button(root, text="Show", command=show).pack()

root.mainloop()