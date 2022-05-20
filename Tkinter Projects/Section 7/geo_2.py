from tkinter import *
from tkinter import ttk

window = Tk()
window.title("New")

content = ttk.Frame(window, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)

nameLabel = ttk.Label(content, text="Name")
name = ttk.Entry(content)

firstVar = BooleanVar()
secondVar = BooleanVar()
thirdVar = BooleanVar()

first = ttk.Checkbutton(content, text="First", variable=firstVar, onvalue=True)
second = ttk.Checkbutton(content, text="Second", variable=secondVar, onvalue=True)
third = ttk.Checkbutton(content, text="Third", variable=thirdVar, onvalue=True)

okay = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N,S,E,W)),
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N,S,E,W))
nameLabel.grid(column=3, row=0, columnspan=2, sticky=NW, padx=5, pady=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), padx=5, pady=5)
first.grid(column=0, row=3)
second.grid(column=1, row=3)
third.grid(column=2, row=3)
okay.grid(column=3, row=3)
cancel.grid(column=4, row=3)




window.mainloop()