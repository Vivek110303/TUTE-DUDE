from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Simple Calculator")

# Entry widget
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Row 1
b = Button(window, text="1", width=12, command=lambda: click(1))
b.place(x=10, y=60)

b = Button(window, text="2", width=12, command=lambda: click(2))
b.place(x=130, y=60)

b = Button(window, text="3", width=12, command=lambda: click(3))
b.place(x=250, y=60)

# Row 2
b = Button(window, text="4", width=12, command=lambda: click(4))
b.place(x=10, y=120)

b = Button(window, text="5", width=12, command=lambda: click(5))
b.place(x=130, y=120)

b = Button(window, text="6", width=12, command=lambda: click(6))
b.place(x=250, y=120)

# Row 3
b = Button(window, text="7", width=12, command=lambda: click(7))
b.place(x=10, y=180)

b = Button(window, text="8", width=12, command=lambda: click(8))
b.place(x=130, y=180)

b = Button(window, text="9", width=12, command=lambda: click(9))
b.place(x=250, y=180)

# Row 4 (Operators)
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="+", width=12, command=add)
b.place(x=10, y=240)

def sub():
    n1 = e.get()
    global i
    global math
    math = "subtraction"
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="-", width=12, command=sub)
b.place(x=130, y=300)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="*", width=12, command=mult)
b.place(x=250, y=240)

# Row 5 (0 centered under 8)
b = Button(window, text="0", width=12, command=lambda: click(0))
b.place(x=130, y=240)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="/", width=12, command=div)
b.place(x=10, y=300)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        try:
            e.insert(0, i / int(n2))
        except ZeroDivisionError:
            e.insert(0, "Error")

b = Button(window, text="=", width=12, command=equal)
b.place(x=250, y=300)

def clear():
    e.delete(0, END)

# Row 6 (Clear button centered)
b = Button(window, text="Clear", width=12, command=clear)
b.place(x=130, y=360)

window.mainloop()
