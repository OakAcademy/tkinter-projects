from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("Password Vault")
window.geometry("600x400")
window.resizable(0, 0)

conn = sqlite3.connect("passvault.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS manager ( 
                                                        app_name text,
                                                        url text,
                                                        email_id text,
                                                        password text
                                                        )
""")

conn.commit()
conn.close()

def submit():
    conn = sqlite3.connect("passvault.db")
    cursor = conn.cursor()

    if appName.get() != "" and url.get() !="" and emailId.get()!="" and password.get()!="":
        cursor.execute("INSERT INTO manager VALUES(:appName, :url, :emailId, :password)",
                       {
                           "appName": appName.get(),
                           "url" : url.get(),
                           "emailId" : emailId.get(),
                           "password" : password.get()
                       })
        conn.commit()
        conn.close()
        messagebox.showinfo("Info", "Record added database!")

        appName.delete(0, END)
        url.delete(0, END)
        emailId.delete(0, END)
        password.delete(0, END)

    else:
        messagebox.showinfo("Alert!", "Please fill all the field!")
        conn.close()

def query():

    queryButton.configure(text="Hide Records", command=hide)
    conn = sqlite3.connect("passvault.db")
    cursor = conn.cursor()

    cursor.execute("SELECT *, oid FROM manager")
    records = cursor.fetchall()
    print(records)

    p_records = ""
    for record in records:
        p_records += str(record[4]) + " " + str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3] + "\n")
        print(record)

    queryLabel["text"] = p_records
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("passvault.db")
    cursor= conn.cursor()

    t = deleteId.get()
    if t != "":
        cursor.execute("DELETE FROM manager WHERE oid = " + deleteId.get())
        deleteId.delete(0, END)
        messagebox.showinfo("Alert!"," Record %s Deleted!" %t)
    else:
        messagebox.showinfo("Alert!", "Please enter record id to delete!")

    conn.commit()
    conn.close()

def update():
    t = updateId.get()
    if t != "":
        global edit
        edit = Tk()
        edit.title("Update Record")
        edit.geometry("500x400")
        edit.resizable(0, 0)

        global appNameEdit, urlEdit, emailIdEdit, passwordEdit

        appNameEdit = Entry(edit, width=30)
        appNameEdit.grid(row=0, column=1, padx=20, pady=10)
        urlEdit = Entry(edit, width=30)
        urlEdit.grid(row=1, column=1, padx=20, pady=10)
        emailIdEdit = Entry(edit, width=30)
        emailIdEdit.grid(row=2, column=1, padx=20, pady=10)
        passwordEdit = Entry(edit, width=30)
        passwordEdit.grid(row=3, column=1, padx=20, pady=10)


        appNameLabel = Label(edit, text="Application Name: ")
        appNameLabel.grid(row=0, column=0)
        urlLabel = Label(edit, text="Url: ")
        urlLabel.grid(row=1, column=0)
        emailIdLabel = Label(edit, text=" Email Id: ")
        emailIdLabel.grid(row=2, column=0)
        passwordLabel = Label(edit, text="Password: ")
        passwordLabel.grid(row=3, column=0)

        submitButtonEdit = Button(edit, text="Save Record", command=change)
        submitButtonEdit.grid(row=4, column=0, columnspan=2, pady=5, padx=15, ipadx=135)

        conn =sqlite3.connect("passvault.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM manager WHERE oid= " + updateId.get())
        records = cursor.fetchall()

        for record in records:
            appNameEdit.insert(0, record[0])
            urlEdit.insert(0, record[1])
            emailIdEdit.insert(0, record[2])
            passwordEdit.insert(0, record[3])

        conn.commit()
        conn.close()

    else:
        messagebox.showinfo("Alert!", "Please enter record id to update!")


def change():
    conn = sqlite3.connect("passvault.db")
    cursor = conn.cursor()

    if appNameEdit.get() != "" and urlEdit.get() != "" and emailIdEdit.get() != "" and passwordEdit.get() != "":
        cursor.execute("""UPDATE manager SET
        appName = :appName,
        url = :url,
        emailId = :emailId,
        password = :password
        
        WHERE oid = :oid""",
                       {
                           'appName' : appNameEdit.get(),
                           'url' : urlEdit.get(),
                           'emailId' : emailIdEdit.get(),
                           'password' : passwordEdit.get(),
                           'oid' : updateId.get()
                       }
        )

        conn.commit()
        conn.close()
        messagebox.showinfo("Alert!", "Record Updated in Database!")

        updateId.delete(0, END)
        edit.destroy()

    else:
        messagebox.showinfo("Alert!", "Please enter all details!")
        conn.close()

def hide():

    queryLabel['text'] = ""
    queryButton.configure(text= "Show Records", command=query)

appName = Entry(window, width=30)
appName.grid(row = 0, column=1, padx=20)
url = Entry(window, width=30)
url.grid(row=1, column=1, padx=20)
emailId = Entry(window, width=30)
emailId.grid(row=2, column=1, padx=20)
password = Entry(window, width=30)
password.grid(row=3, column=1, padx=20)
deleteId = Entry(window, width=20)
deleteId.grid(row=6, column=1, padx=20)
updateId = Entry(window, width=20)
updateId.grid(row=7, column=1, padx=20)

appNameLabel = Label(window, text="Application Name: ")
appNameLabel.grid(row=0,column=0)
urlLabel = Label(window, text="Url: ")
urlLabel.grid(row=1, column=0)
emailIdLabel = Label(window, text=" Email Id: ")
emailIdLabel.grid(row=2, column=0)
passwordLabel = Label(window, text="Password: ")
passwordLabel.grid(row=3, column=0)

submitButton = Button(window, text="Add Record", command=submit)
submitButton.grid(row=5, column=0, pady=5, padx=15, ipadx=35)

deleteButton = Button(window, text="Delete Record", command=delete)
deleteButton.grid(row=6, column=0, pady=5, padx=15, ipadx=30)

updateButton = Button(window, text="Update Record", command=update)
updateButton.grid(row=7, column=0, pady=5, padx=15, ipadx=30)

frame = Frame(window, bg="black", bd=5)
frame.place(relx = 0.5, rely=0.5, relwidth=0.98, relheight=0.45, anchor=N)

global queryLabel
queryLabel = Label(frame, anchor=NW, justify=LEFT)
queryLabel.place(relwidth=1, relheight=1)

queryButton= Button(window, text="Show Records", command=query)
queryButton.grid(row=5, column=1, pady=5, padx=15, ipadx=30)

window.mainloop()