from tkinter import *

window = Tk()

window.geometry("450x450")
window.title("Pomodoro")

bell = True


def clock(m, s):
    mstr = str(m)
    sstr = str(s)
    if m < 10:
        mstr = "0" + mstr
    if s < 10:
        sstr = "0" + sstr
    return mstr + ":" + sstr


def study_time():
    global counting
    global bell

    start["state"] = "disabled"

    if bell:
        window.bell()
        bell = False

    status.config(text="Study time")
    curr = countdown["text"]
    m, s = curr.split(":")
    mint, sint = int(m), int(s)
    if sint > 0:
        sint -= 1
        countdown.config(text=clock(mint, sint))
    if sint == 0:
        if mint > 0:
            sint = 59
            mint -= 1
            countdown.config(text=clock(mint, sint))
        else:
            countdown.config(text=clock(5, 0))
            bell = True
            break_time()
            return
    counting = window.after(1000, study_time)


def break_time():
    global counting
    global bell

    if bell:
        window.bell()
        bell = False

    status.config(text="Break time")
    curr = countdown["text"]
    m, s = curr.split(":")
    mint, sint = int(m), int(s)
    if sint > 0:
        sint -= 1
        countdown.config(text=clock(mint, sint))
    if sint == 0:
        if mint > 0:
            sint = 59
            mint -= 1
            countdown.config(text=clock(mint, sint))
        else:
            countdown.config(text=clock(25, 0))
            bell = True
            study_time()
            return
    counting = window.after(1000, break_time)


def stop():
    start["state"] = "active"
    try:
        window.after_cancel(counting)
        status.config(text="Stopped")
    except NameError:
        return


def reset():
    stop()
    countdown.config(text="25:00")
    status.config(text="Not started")


status = Label(window, text="Not started", font=("Tahoma", 15))
status.pack(pady=10)

countdown = Label(window, text="25:00", font=("Tahoma", 40))
countdown.pack(pady=10)

start = Button(window, text="Start", font=("Tahoma", 15), command=study_time)
start.pack(pady=25)

pause = Button(window, text="Pause", font=("Tahoma", 15), command=stop)
pause.pack(pady=25)

reset = Button(window, text="Reset", font=("Tahoma", 15), command=reset)
reset.pack(pady=10)

window.mainloop()
