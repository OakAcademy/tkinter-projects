import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Tk Components")

scroll_w = 20
scroll_h = 5

scrText = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=scroll_w, height= scroll_h)
scrText.grid(column=1, row=0, columnspan=3)

label1 = tk.Label(window, text="Label 1").grid(column=0, row=0)
label2 = tk.Label(window, text="Label 2").grid(column=0, row=1)
label3 = tk.Label(window, text="Label 3").grid(column=0, row=2)

colors = ["Blue","Black","Red"]

def radio_change_color():
    radioSelect= radVar.get()
    if radioSelect == 0:
        window.configure(background=colors[0])
    elif radioSelect == 1:
        window.configure(background=colors[1])
    elif radioSelect == 2:
        window.configure(background=colors[2])

radVar = tk.IntVar()

for col in range(3):
    cuRad = tk.Radiobutton(window, text=colors[col], variable=radVar, value=col, command=radio_change_color)
    cuRad.grid(column=col, row=3, sticky=tk.W)


window.mainloop()

