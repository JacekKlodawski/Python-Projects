from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Title')

#Left Upper Window Icon
root.iconbitmap('path')

#Exit Button
button_quit = Button(root, text="Exit", command=root.quit).pack()

#Images
my_img = ImageTk.PhotoImage(Image.open("path"))


root.mainloop()