# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
# window.title("New")
#
# content = ttk.Frame(window, padding=(3,3,12,12))
# frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
#
# nameLabel = ttk.Label(content, text="Name")
# name = ttk.Entry(content)
#
# firstVar = BooleanVar()
# secondVar = BooleanVar()
# thirdVar = BooleanVar()
#
# first = ttk.Checkbutton(content, text="First", variable=firstVar, onvalue=True)
# second = ttk.Checkbutton(content, text="Second", variable=secondVar, onvalue=True)
# third = ttk.Checkbutton(content, text="Third", variable=thirdVar, onvalue=True)
#
# okay = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")
#
# content.pack(side = LEFT, fill=BOTH)
# frame.pack(side=LEFT, fill=X)
# nameLabel.pack(side=RIGHT, fill=Y)
# name.pack(side=RIGHT, fill=BOTH)
# first.pack(side= BOTTOM, fill=BOTH)
# second.pack(side= BOTTOM,fill=X)
# third.pack(side=BOTTOM, fill=Y)
# okay.pack(side=TOP, fill=X)
# cancel.pack(side=TOP, fill= Y)
#
# window.mainloop()

from tkinter import *

window = Tk()

canvas = Canvas(window, height=450, width=750)
canvas.pack()

frameTop = Frame(window, bg = "blue")
frameTop.place(relx = 0.1, rely=0.1, relwidth=0.8, relheight=0.4)

frameBottomLeft = Frame(window, bg = "black")
frameBottomLeft.place(relx= 0.1, rely=0.5, relwidth=0.4, relheight=0.4)

frameBottomRight = Frame(window, bg="red")
frameBottomRight.place(relx =0.5, rely=0.5, relwidth=0.4, relheight=0.4)

window.mainloop()









