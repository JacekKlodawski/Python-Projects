from tkinter import *

root = Tk()

# Tworzenie elementów
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is").grid(row=0, column=1)
# Wyświetlanie na ekranie
myLabel1.grid(row=0, column=0)


root.mainloop()