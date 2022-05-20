import tkinter as tk
from tkinter import ttk

window = tk.Tk()

names=tk.StringVar()

chosen_name = ttk.Combobox(window, width=20, textvariable=names, values=["John","William","Jack","Averell"],state='readonly')
chosen_name.current(2)
chosen_name.grid(column=1, row=0)

label_1 = ttk.Label(window,text="Choose a name: ", font=("Arial", 10,"italic","bold")).grid(column=0,row=0)

def show_name():
    chosen_show.configure(text="Hello, " + names.get())


chosen_show= ttk.Button(window, text="Hello", command=show_name)
chosen_show.grid(column=1, row=1)

chVarArr = tk.IntVar()
chVarRel = tk.IntVar()
chVarDec = tk.IntVar()

my_check = tk.Checkbutton(window, text="Arrest him", variable = chVarArr, state='disabled')
my_check.grid(column=0, row=2, sticky=tk.W)

my_check_2 = tk.Checkbutton(window, text = "Release him", variable = chVarRel)
my_check_2.grid(column=1, row=2, sticky=tk.W)

my_check_3 = tk.Checkbutton(window, text = "Decide later", variable = chVarDec)
my_check_3.grid(column=2, row=2, sticky=tk.W)

my_check.deselect()
my_check_2.deselect()
my_check_3.select()


color_1 = "blue"
color_2 = "black"
color_3 = "red"

def radio_change_color():
    radioSelect= radVar.get()
    if radioSelect == 1:
        window.configure(background=color_1)
    elif radioSelect == 2:
        window.configure(background=color_2)
    elif radioSelect == 3:
        window.configure(background=color_3)

radVar = tk.IntVar()

radio_1 = tk.Radiobutton(window, text=color_1, variable=radVar, value=1, command=radio_change_color)
radio_1.grid(column=0, row=3, sticky=tk.W)

radio_2 = tk.Radiobutton(window, text=color_2,variable=radVar, value=2, command=radio_change_color)
radio_2.grid(column=1, row=3, sticky=tk.W)

radio_3 = tk.Radiobutton(window, text=color_3, variable=radVar, value=3, command=radio_change_color)
radio_3.grid(column=2, row=3, sticky=tk.W)
















window.mainloop()