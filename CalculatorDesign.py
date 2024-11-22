#Library
from tkinter import *

root = Tk()
root.title("Amadeus Calculator..")
root.configure(background="gray25")

e = Entry(root, width = 40, borderwidth = 5, bg="gray15", fg="chartreuse", font = "Arial")
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
amds = Label(root, text="Calculator", bg="gray25", fg="chartreuse", font=("System 30"))
amds.place(x=100, y=345)

#Functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    global f_num
    global operator
    operator = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def button_sub():
    first_num = e.get()
    global f_num
    global operator
    operator = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def button_mult():
    first_num = e.get()
    global f_num
    global operator
    operator = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def button_div():
    first_num = e.get()
    global f_num
    global operator
    operator = "division"
    f_num = float(first_num)
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)

    if operator == "addition":
        e.insert(0, f_num + int(second_num))

    if operator == "subtraction":
        e.insert(0, f_num - int(second_num))

    if operator == "multiplication":
        e.insert(0, f_num * int(second_num))

    if operator == "division":
        e.insert(0, f_num / float(second_num))

#Numbers
button_1 = Button(root, text = "1", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 60, pady = 20, relief=RAISED, bd=3, font = "Arial", bg="gray50", fg="ghost white", command = lambda: button_click(0))

#Artithmetic Operators
button_clear = Button(root, text = "Clear", padx = 117, pady = 20, relief=RAISED, bd=3, bg="gray50", fg="ghost white", font = "Arial", command = button_clear)
button_add = Button(root, text = "+", padx = 58, pady = 20, relief=RAISED, bd=3, bg="gray50", fg="ghost white", font = "Arial", command = button_add)
button_sub = Button(root, text = "-", padx = 60, pady = 20, relief=RAISED, bd=3, bg="gray50", fg="ghost white", font = "Arial", command = button_sub)
button_mult = Button(root, text = "*", padx = 60, pady = 20, relief=RAISED, bd=3, bg="gray50", fg="ghost white", font = "Arial", command = button_mult)
button_div = Button(root, text = "/", padx = 60, pady = 20, relief=RAISED, bd=3, bg="gray50", fg="ghost white", font = "Arial", command = button_div)
button_equal = Button(root, text = "=", padx = 58, pady = 20, relief=RAISED, bd=3, bg="gray50", fg="ghost white", font = "Arial", command = button_equal)

#GUI Grid Layout
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row=2, column=2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0)

button_add.grid(row = 3, column = 3)
button_sub.grid(row = 2, column = 3)
button_mult.grid(row = 1, column = 3)
button_div.grid(row = 4, column = 3)

button_clear.grid(row = 4, column = 1, columnspan = 2)
button_equal.grid(row = 5, column = 3, columnspan = 2)

root.mainloop()
