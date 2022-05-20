import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from time import sleep

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


def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i  # increment progressbar
        progress_bar.update()  # have to call update() in loop
    progress_bar["value"] = 0  # reset/clear progressbar


def start_progressbar():
    progress_bar.start()


def stop_progressbar():
    progress_bar.stop()


def progressbar_stop_after(wait_ms=1000):
    window.after(wait_ms, progress_bar.stop)

buttons_frame = ttk.LabelFrame(lab_fr_cont_2, text=' ProgressBar ')
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

progress_bar = ttk.Progressbar(buttons_frame, orient="horizontal", length=286, mode="determinate")
progress_bar.grid(column=0, row=4, pady=2)

ttk.Button(buttons_frame, text=" Run Progressbar   ", command=run_progressbar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_progressbar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_progressbar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text=" Stop after second ", command=progressbar_stop_after).grid(column=0, row=3, sticky='W')

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

for child in lab_fr_cont_2.winfo_children():
    child.grid_configure(padx=8, pady=2)

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

tab_3 = ttk.Frame(tab_control)
tab_control.add(tab_3, text='Tab 3')

tab_3_frame = tk.Frame(tab_3, bg="blue")
tab_3_frame.pack()

for orange_color in range(2):
    canvas = tk.Canvas(tab_3_frame, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)









window.mainloop()