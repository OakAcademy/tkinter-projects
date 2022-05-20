import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from time import sleep

class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)  # bind mouse events
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 18

            self.tip_window = tk.Toplevel(self.widget)
            self.tip_window.overrideredirect(True)
            self.tip_window.geometry("+%d+%d" % (x_left, y_top))

            label = tk.Label(self.tip_window, text=self.tip_text, justify=tk.LEFT,
                             background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                             font=("tahoma", "8", "normal"))
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()


window = tk.Tk()

window.title("Python GUI")

lab_fr_cont = ttk.LabelFrame(window, text="Label Frame Container")
lab_fr_cont.grid(column=0, row= 0, padx = 10, pady= 5)

label_1 = ttk.Label(lab_fr_cont, text="A Label")
label_1.grid(column=0, row=0)


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

chVarArr = tk.IntVar()
chVarRel = tk.IntVar()
chVarDec = tk.IntVar()

my_check = tk.Checkbutton(lab_fr_cont, text="Arrest him", variable = chVarArr, state='disabled')
my_check.grid(column=0, row=2, sticky=tk.W)

my_check_2 = tk.Checkbutton(lab_fr_cont, text = "Release him", variable = chVarRel)
my_check_2.grid(column=1, row=2, sticky=tk.W)

my_check_3 = tk.Checkbutton(lab_fr_cont, text = "Decide later", variable = chVarDec)
my_check_3.grid(column=2, row=2, sticky=tk.W)

my_check.deselect()
my_check_2.deselect()
my_check_3.select()

def spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

def spin_2():
    value = spin_2.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin = tk.Spinbox(lab_fr_cont, from_=0, to=10,values = [0,8,26,98,19], width=5, bd=10, command=spin)
spin.grid(column=2, row=0)

spin_2 = tk.Spinbox(lab_fr_cont, from_=0, to=10, values=[0,8,26,98,19], width=5, bd=10, command=spin_2, relief=tk.RIDGE)
spin_2.grid(column=3, row=0)

scrol_w = 30
scrol_h = 10
scr = scrolledtext.ScrolledText(lab_fr_cont, width=scrol_w, height=scrol_h, wrap=tk.WORD)
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
    curRad = tk.Radiobutton(lab_fr_cont, text=colors[col], variable=radVar,
                            value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

buttons_frame = ttk.LabelFrame(lab_fr_cont, text='Labels in a Frame')
buttons_frame.grid(column=0, row=7)


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label = "New")
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu_bar.add_cascade(label="File", menu=file_menu)

def msgbox():
    # msg.showinfo("Python Message Info Box", "I start to programming with Python")
    # msg.showwarning("Python Message Warning Box", " There might be a bug in this code!")
    # msg.showerror("Python Message Error Box", "Bug Alert!")
    answer = msg.askyesnocancel("Python Message Multi Choice Box","Are you sure to delete?")
    print(answer)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=msgbox)

ToolTip(spin,"This is a spin control")
ToolTip(scr, "This is a scrolledtext widget")

progress_bar = ttk.Progressbar(buttons_frame, orient="horizontal", length=286, mode="determinate")
progress_bar.grid(column=0, row=4, pady=2)

def run_progress_bar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i
        progress_bar.update()
    progress_bar["value"] = 0

def start_progress_bar():
    progress_bar.start()

def stop_progress_bar():
    progress_bar.stop()

def progress_bar_stop_after(wait_ms=1000):
    window.after(wait_ms, progress_bar.stop)

ttk.Button(buttons_frame, text="Run Progressbar   ", command=run_progress_bar).grid(column=0, row=0, sticky="W")
ttk.Button(buttons_frame, text="Start Progressbar   ", command=start_progress_bar).grid(column=0, row=1, sticky="W")
ttk.Button(buttons_frame, text="Stop immediately   ", command=stop_progress_bar).grid(column=0, row=2, sticky="W")
ttk.Button(buttons_frame, text="Stop after second   ", command=progress_bar_stop_after).grid(column=0, row=3, sticky="W")


for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

for child in lab_fr_cont.winfo_children():
    child.grid_configure(padx=8, pady=2)

tab_3 = ttk.Frame(tab_control)


window.mainloop()