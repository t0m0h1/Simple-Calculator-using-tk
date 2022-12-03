# a Tkinter GUI which can perform all basic calculations(not a sci calculator).

# import the whole tkinter module 

from tkinter import *

expression = " "

tk=Tk()
tk.configure(background="gray")
tk.title("Simple Calculator by @THH")
# i want it to be a small pop-up window instead of a full screen application.
tk.geometry('400x500')


# this function shows the expression in the text entry

def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    #some exeptions needed in order to negate the ZeroDivisionError
    try:
        global expression 
        #here str converts the result into a string
        total = str(eval(expression))

        equation.set(total)

        expression = " "

        #except block handles further problems
    except:

        equation.set("... error ...")
        expression = ""

#next function works like an all clear

def clear():
    global expression
    expression = " "
    equation.set("")
#using grid positioning
equation = StringVar()
expression_field = Entry(tk, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=105, pady=5)

#building the input buttons

button1 = Button(tk, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(tk, text= ' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(tk, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(tk, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0, pady=5)

button5 = Button(tk, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(tk, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(tk, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(tk, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(tk, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(tk, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0, pady=5)

bplus = Button(tk, text=' + ', fg='black', bg='red', command=lambda: press("+"), height=1, width=7)
bplus.grid(row=2, column=3)

bminus = Button(tk, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
bminus.grid(row=3, column=3)

bmultiply = Button(tk, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
bmultiply.grid(row=4, column=3)

bdivide = Button(tk, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
bdivide.grid(row=5, column=3)
 
bequals = Button(tk, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7)
bequals.grid(row=5, column=2)

bclear = Button(tk, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
bclear.grid(row=5, column='1')

bdecimal = Button(tk, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
bdecimal.grid(row=6, column=0)
 

#this calc can only do one operation per use, clear must be used 

tk.mainloop()