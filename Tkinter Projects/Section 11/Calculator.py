from tkinter import *

window = Tk()
window.geometry("270x430")
window.title("Calculator")
window.resizable(0, 0)

def addToText(n):
    entryCalc.insert(END, n)

def clear():
    entryCalc.delete(0, END)

def operations():
    result = eval(entryCalc.get())
    entryCalc.delete(0, END)
    entryCalc.insert(0, result)






entryCalc = Entry(window, font=("Calibri", 16))
entryCalc.pack(fill=X, padx=5, pady=5, ipady=5)

frameNumbers = Frame(window)
frameNumbers.pack(side=TOP, anchor=NW)

frameOperations = Frame(frameNumbers)
frameOperations.pack(side=RIGHT)

frame1 = Frame(frameNumbers)
frame1.pack()

button1 = Button(frame1, text="1", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("1"))
button1.pack(side=LEFT)
button2 = Button(frame1, text="2", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("2"))
button2.pack(side=LEFT)
button3 = Button(frame1, text="3", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("3"))
button3.pack(side=LEFT)

frame2 = Frame(frameNumbers)
frame2.pack()

button4 = Button(frame2, text="4", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("4"))
button4.pack(side=LEFT)
button5 = Button(frame2, text="5", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("5"))
button5.pack(side=LEFT)
button6 = Button(frame2, text="6", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("6"))
button6.pack(side=LEFT)

frame3 = Frame(frameNumbers)
frame3.pack()

button7 = Button(frame3, text="7", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("7"))
button7.pack(side=LEFT)
button8 = Button(frame3, text="8", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("8"))
button8.pack(side=LEFT)
button9 = Button(frame3, text="9", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("9"))
button9.pack(side=LEFT)

frame4 = Frame(frameNumbers)
frame4.pack()

buttonDot = Button(frame4, text=".", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("."))
buttonDot.pack(side=LEFT)
button0 = Button(frame4, text="0", fg="black", bg="gray", width=9, height=4, command=lambda: addToText("0"))
button0.pack(side=LEFT)
buttonEqual = Button(frame4, text="=", fg="black", bg="gray", width=9, height=4, command=lambda: operations())
buttonEqual.pack(side=LEFT)

buttonDivide = Button(frameOperations, text="/", fg="black", bg="gray", width=6, height=4, command=lambda: addToText("/"))
buttonDivide.pack()
buttonPlus = Button(frameOperations, text="+", fg="black",bg="gray", width=6, height=4, command=lambda: addToText("+"))
buttonPlus.pack()
buttonMinus = Button(frameOperations, text="-", fg="black", bg="gray", width=6, height=4, command=lambda: addToText("-"))
buttonMinus.pack()
buttonMultiply = Button(frameOperations, text="X", fg="black", bg="gray", width=6, height=4, command=lambda: addToText("*"))
buttonMultiply.pack()

frameClear = Frame(window)
frameClear.pack()

buttonClear = Button(frameClear, text="C", fg="black", bg="gray", width=40, height=6, command=clear)
buttonClear.pack()




















window.mainloop()