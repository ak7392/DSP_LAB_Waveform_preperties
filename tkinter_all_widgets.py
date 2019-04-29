# Simple Calculator
# The calculator works in two different modes : Entry and Slider Mode
# For Entry mode, select entry mode radio button then you have to enter 2 values in entry fields to perform operations
# For Slider mode, select slider mode radio button then  you have to set sliders to desired values and perform operations
# By default slider mode is enabled

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


def Add_fun():
    a, b = getvals()
    string1 = 'Result: ' + str(a) + ' + ' + str(b) + ' =  ' + str(a + b)
    L1.config(text=string1)


def Sub_fun():
    a, b = getvals()
    string1 = 'Result: ' + str(a) + ' - ' + str(b) + ' =  ' + str(a - b)
    L1.config(text=string1)


def Mul_fun():
    a, b = getvals()
    string1 = 'Result: ' + str(a) + ' X ' + str(b) + ' =  ' + str(a * b)
    L1.config(text=string1)


def Div_fun():
    a, b = getvals()
    if b != 0:
        string1 = 'Result: ' + str(a) + ' / ' + str(b) + ' =  ' + str(a / b)
        L1.config(text=string1)
    else:
        L1.config(text='Division by zero is not possible')


def getvals():
    if var.get() == 1:
        E1.delete(0, 'end')
        E2.delete(0, 'end')
        return x.get(), y.get()
    elif var.get() == 2:
        try:
            S1.set(0)
            S2.set(0)
            return float(E1.get()), float(E2.get())
        except ValueError:
            L1.config(text='Please enter two valid values in entry fields')


def changeMode():
    if var.get() == 1:
        E1.config(state=Tk.DISABLED)
        E2.config(state=Tk.DISABLED)
        S1.config(state=Tk.NORMAL)
        S2.config(state=Tk.NORMAL)

        EVal1.config(state=Tk.DISABLED)
        EVal2.config(state=Tk.DISABLED)
        SVal1.config(state=Tk.NORMAL)
        SVal2.config(state=Tk.NORMAL)
    else:
        S1.config(state=Tk.DISABLED)
        S2.config(state=Tk.DISABLED)
        E1.config(state=Tk.NORMAL)
        E2.config(state=Tk.NORMAL)

        SVal1.config(state=Tk.DISABLED)
        SVal2.config(state=Tk.DISABLED)
        EVal1.config(state=Tk.NORMAL)
        EVal2.config(state=Tk.NORMAL)


top = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()
y = Tk.DoubleVar()
var = Tk.IntVar()
zeroval = Tk.StringVar().set('0')

# Define widgets

# Radio Buttons to select mode
R1 = Tk.Radiobutton(top, text="Slider Mode", variable=var, value=1, padx=10, pady=10, command=changeMode)
R2 = Tk.Radiobutton(top, text="Entry Mode", variable=var, value=2, padx=10, pady=10, command=changeMode)
R1.grid(row=1, column=1, columnspan=2)
R2.grid(row=1, column=3, columnspan=2)
R1.select()  # Select  a default mode for calculator

# Scales / Sliders to select values for calculations
S1 = Tk.Scale(top, variable=x)
S1.grid(row=3, column=1, padx=10, pady=10)
S2 = Tk.Scale(top, variable=y)
S2.grid(row=3, column=2, padx=10, pady=10)

# Entry widgets to get user input from keyboard
E1 = Tk.Entry(top)
E1.grid(row=3, column=3)
E2 = Tk.Entry(top)
E2.grid(row=3, column=4)

# Buttons to perform operations on values
Add = Tk.Button(top, text='Addition', command=Add_fun, fg='blue', padx=10, pady=10).grid(row=4, column=1)
Sub = Tk.Button(top, text='Subtraction', command=Sub_fun, fg='green', padx=10, pady=10).grid(row=4, column=2)
Mul = Tk.Button(top, text='Multiply', command=Mul_fun, fg='black', padx=10, pady=10).grid(row=4, column=3)
Div = Tk.Button(top, text='Division', command=Div_fun, fg='yellow', padx=10, pady=10).grid(row=4, column=4)


L1 = Tk.Label(top, text='Click above buttons to performs operations and see results')
L1.grid(row=5, column=1, columnspan=4)

SVal1 = Tk.Label(top, text='Value 1: ')
SVal1.grid(row=2, column=1)
SVal2 = Tk.Label(top, text='Value 2: ')
SVal2.grid(row=2, column=2)
EVal1 = Tk.Label(top, text='Value 1: ')
EVal1.grid(row=2, column=3)
EVal2 = Tk.Label(top, text='Value 2: ')
EVal2.grid(row=2, column=4)
changeMode()
top.mainloop()
