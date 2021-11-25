from tkinter import *
from typing import Match

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "add":
        e.insert(0, f_num + int(second_number))
    elif math == "sub":
        e.insert(0, f_num - int(second_number))
    elif math == "mul":
        e.insert(0, f_num * int(second_number))
    elif math == "div":
        if int(second_number) !=0:
            e.insert(0, f_num / int(second_number))
        else:
            raise ZeroDivisionError("Do not divide by 0")

            
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0,END)

#Number Buttons

Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=1, column=0)
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=1, column=1)
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=1, column=2)

Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)

Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=3, column=0)
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=3, column=1)
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=3, column=2)

Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=4, column=0)

#Functional Buttons
Button_Clear = Button(root, text="C", padx=39, pady=20, command=button_clear).grid(row=4, column=2)
Button_Equal = Button(root, text="=", padx=40, pady=20, command=button_equal).grid(row=4, column=1)

Button_Add = Button(root, text="+", padx=40, pady=20, command=button_add).grid(row=1, column=4)
Button_Subtract = Button(root, text="-", padx=39, pady=20, command=button_subtract).grid(row=2, column=4)

Button_Multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply).grid(row=3, column=4)
Button_Divide = Button(root, text="/", padx=40, pady=20, command=button_divide).grid(row=4, column=4)


root.mainloop()