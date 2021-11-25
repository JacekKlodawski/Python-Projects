from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Title')

root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("all files","*.*")))


root.mainloop()