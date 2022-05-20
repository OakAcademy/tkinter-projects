import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu


window = tk.Tk()
window.title("OAK")

tab_control = ttk.Notebook(window)
tab_1 = ttk.Frame(tab_control)
tab_control.add(tab_1, text="Tab 1")
tab_control.pack(expand=1, fill="both")

tab_2 = ttk.Frame(tab_control)
tab_control.add(tab_2, text="Tab 2")

lab_fr_cont = ttk.LabelFrame(tab_1, text="Label Frame Controller")
lab_fr_cont.grid(column=0, row=0, padx=10, pady=5)

label_1 = ttk.Label(lab_fr_cont, text="Enter a name: ")
label_1.grid(column=0, row = 0, sticky= tk.W)

ttk.Label(lab_fr_cont, text="Choose a name").grid(column= 1, row=0)

def show_name():
    action.configure(text='Hello ' + name.get() + ' ' + chosen_name.get())

ttk.Label(lab_fr_cont, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(lab_fr_cont, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(lab_fr_cont, text="Hello!", command=show_name)
action.grid(column=2, row=1)

ttk.Label(lab_fr_cont, text="Choose a name:").grid(column=1, row=0)
names = tk.StringVar()
chosen_name = ttk.Combobox(lab_fr_cont, width=12, textvariable=names, state='readonly')
chosen_name['values'] = ("Joe", "William", "Jack", "Averell")
chosen_name.grid(column=1, row=1)
chosen_name.current(0)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(lab_fr_cont, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=2, sticky='WE', columnspan=3)

for child in lab_fr_cont.winfo_children():
    child.grid_configure(padx=10)

lab_fr_cont_2 = ttk.LabelFrame(tab_2, text="Label Frame Controller 2")
lab_fr_cont_2.grid(column=0, row=0, padx=10, pady=10)

chVarArr = tk.IntVar()
chVarRel = tk.IntVar()
chVarDec = tk.IntVar()

my_check = tk.Checkbutton(lab_fr_cont_2, text="Arrest him", variable = chVarArr, state='disabled')
my_check.grid(column=0,  sticky=tk.W)

my_check_2 = tk.Checkbutton(lab_fr_cont_2, text = "Release him", variable = chVarRel)
my_check_2.grid(column=0,  sticky=tk.W)

my_check_3 = tk.Checkbutton(lab_fr_cont_2, text = "Decide later", variable = chVarDec)
my_check_3.grid(column=0, sticky=tk.W)

my_check.deselect()
my_check_2.deselect()
my_check_3.select()

colors = ["Blue", "Black", "Red"]

def radCall():
    radSel = radVar.get()
    if radSel == 0:
        lab_fr_cont_2.configure(text=colors[0])
    elif radSel == 1:
        lab_fr_cont_2.configure(text=colors[1])
    elif radSel == 2:
        lab_fr_cont_2.configure(text=colors[2])


radVar = tk.IntVar()

for col in range(3):
    curRad = tk.Radiobutton(lab_fr_cont_2, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

for col in range(3):
    curRad = tk.Radiobutton(lab_fr_cont, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row = 3, sticky=tk.W)


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label = "New")
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu_bar.add_cascade(label="File", menu=file_menu)


help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")



window.mainloop()