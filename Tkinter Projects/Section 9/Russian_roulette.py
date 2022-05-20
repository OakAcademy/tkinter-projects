import tkinter as tk
from random import shuffle

gun = [False,True,False,False,False,False]

window = tk.Tk()
window.title("Russian Roulette")
window.geometry("300x250")

label = tk.Label(window, text="Fire", font=("Tahoma", 30), pady=20)
label.pack()

def shuffle_gun():
    shuffle(gun)
    button_1.config(state="normal")
    button_2.config(state="normal")
    label.config(text="Fire")
    print(gun)


def shoot():
    if gun[0]:
        label.config(text="You are dead")
        button_1.config(state="disabled")
        button_2.config(state="disabled")
    else:
        label.config(text="You are alive")
        button_2.config(state="disabled")
    print(gun[0])

button_1 = tk.Button(window, text="Shuffle", command=shuffle_gun, font=("Tahoma",20))
button_1.pack()

button_2 = tk.Button(window, text="  Fire  ",command=shoot, font=("Tahoma",20))
button_2.pack()


window.mainloop()