from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Title')

def popup():
    response = messagebox.askyesno("This is my popup","Hello World!")
    Label(root, text=response). pack()

    if response == 1:
        Label(root, text="Yes"). pack()
    else:
        Label(root, text="No"). pack()

# showinfo, whowwarning, showerror, askquestion, askokcancel, askyesno

Button(root, text="popup", command=popup).pack()

root.mainloop()