import tkinter as tk
import math

window = tk.Tk()
window.title("BMI")

weight_value = tk.IntVar()
height_value = tk.IntVar()

Weight=tk.Label(window, text = "Please enter your weight in kg: ", foreground="black", font="bold")
Weight.grid(row=0, column=0)

Height = tk.Label(window, text = "Please enter your height in cm: ", foreground="black", font="bold")
Height.grid(row=1, column=0)

weight_entered = tk.Entry(window, textvariable=weight_value)
weight_entered.grid(column=1, row=0)

height_entered = tk.Entry(window, textvariable=height_value)
height_entered.grid(column=1, row=1)


def calculate():
    Result_Calculation = int(weight_value.get()) / int((height_value.get()/100)**2)
    result.configure(text=float(Result_Calculation))


calculate_button = tk.Button(window, text="Calculate", width = 30, height=3, command=calculate)
calculate_button.grid(column=0, row=2)

result = tk.Label(window,text="BMI",foreground='red', font="bold")
result.grid(column=1, row=2)

window.mainloop()