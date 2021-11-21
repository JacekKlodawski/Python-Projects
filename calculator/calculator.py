from tkinter import *

root = Tk()
root.title("Simple Calculator")

EntryBox = Entry(root, width=35, borderwidth=5).grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#EntryBox.insert(0,)

def press_1():
    pass

#Number Buttons

Button_1 = Button(root, text="1", padx=40, pady=20, command=press_1).grid(row=1, column=0)
Button_2 = Button(root, text="2", padx=40, pady=20, command=press_1).grid(row=1, column=1)
Button_3 = Button(root, text="3", padx=40, pady=20, command=press_1).grid(row=1, column=2)

Button_4 = Button(root, text="4", padx=40, pady=20, command=press_1).grid(row=2, column=0)
Button_5 = Button(root, text="5", padx=40, pady=20, command=press_1).grid(row=2, column=1)
Button_6 = Button(root, text="6", padx=40, pady=20, command=press_1).grid(row=2, column=2)

Button_7 = Button(root, text="7", padx=40, pady=20, command=press_1).grid(row=3, column=0)
Button_8 = Button(root, text="8", padx=40, pady=20, command=press_1).grid(row=3, column=1)
Button_9 = Button(root, text="9", padx=40, pady=20, command=press_1).grid(row=3, column=2)

Button_0 = Button(root, text="0", padx=40, pady=20, command=press_1).grid(row=4, column=0)

#Functional Buttons
Button_Clear = Button(root, text="C", padx=39, pady=20).grid(row=4, column=2)
Button_Equals = Button(root, text="=", padx=40, pady=20).grid(row=4, column=1)

Button_Add = Button(root, text="+", padx=40, pady=20).grid(row=1, column=4)
Button_Subtract = Button(root, text="-", padx=39, pady=20).grid(row=2, column=4)

Button_Multiply = Button(root, text="*", padx=40, pady=20).grid(row=3, column=4)
Button_Divide = Button(root, text="/", padx=40, pady=20).grid(row=4, column=4)


root.mainloop()