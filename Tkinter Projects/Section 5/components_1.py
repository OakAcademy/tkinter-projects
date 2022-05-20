import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text= "Hello Python", foreground="red", background="blue", font='bold')
label.grid(column=0, row=0)

# label2 = tk.Label(window, text="Hello Tkinter", foreground="white", background="black",font="italic")
# label2.grid(column=0, row=1)

name = tk.StringVar()

def change_me():
    button_1.configure(text="Hello " + name.get())
    label.configure(foreground="black", text="I've changed")

button_1 = tk.Button(window, text= "Click Me",command= change_me)
button_1.grid(column=1,row=1)


text_widget = tk.Entry(window, width=20, textvariable=name)
text_widget.grid(column=0, row=1)



window.mainloop()
