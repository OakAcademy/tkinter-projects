import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()

window.title("Python GUI")

a_label = ttk.Label(window, text="A Label")
a_label.grid(column=0, row=0)


def show_name():
    action.configure(text='Hello ' + name.get() + ' ' + chosen_name.get())

ttk.Label(window, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(window, text="Hello!", command=show_name)
action.grid(column=2, row=1)

ttk.Label(window, text="Choose a name:").grid(column=1, row=0)
names = tk.StringVar()
chosen_name = ttk.Combobox(window, width=12, textvariable=names, state='readonly')
chosen_name['values'] = ("Joe", "William", "Jack", "Averell")
chosen_name.grid(column=1, row=1)
chosen_name.current(0)

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

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(window, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, sticky='WE', columnspan=3)

colors = ["Blue", "Black", "Red"]

def radCall():
    radSel = radVar.get()
    if radSel == 0:
        window.configure(background=colors[0])
    elif radSel == 1:
        window.configure(background=colors[1])
    elif radSel == 2:
        window.configure(background=colors[2])


radVar = tk.IntVar()

for col in range(3):
    curRad = tk.Radiobutton(window, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

buttons_frame = ttk.LabelFrame(window, text='Labels in a Frame')
buttons_frame.grid(column=0, row=7)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

window.mainloop()