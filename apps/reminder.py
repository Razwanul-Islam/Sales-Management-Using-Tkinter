from asyncio.windows_events import NULL
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
from tkcalendar import Calendar, DateEntry

def Reminder(window=NULL):
    if window is not NULL:window.destroy()
    # importing main window
    def mainWindow(window):
        from .main import Main
        Main(window)
    
    def AddReminder(window2):
        window2.destroy()
        top = tk.Tk()
        top.title("Add reminder")
        top.geometry("500x360")
        bg = tk.PhotoImage(file="./images/whitishbg.png")
        bgLabel = tk.Label(top,image=bg,width=560,height=360).place(x=0,y=0)
        # Menubar
        menubar = tk.Menu(top)
        menubar.add_command(label="Back",command=lambda:Reminder(top))
        def submit(date,title,description):
            db = sqlite3.connect('1.db')
            c = db.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS reminder(date TEXT,title TEXT,description TEXT)")
            c.execute("INSERT INTO reminder VALUES(?,?,?)",(date,title,description))
            db.commit()
            db.close()
            messagebox.showinfo(title="Success", message="Reminder added successfully")
            top.destroy()
            Reminder()
        tk.Label(top, text='Choose date').pack(padx=10, pady=10)
        cal = DateEntry(top, width=12, background='darkblue',
                        foreground='white', borderwidth=2)
        cal.pack(padx=10, pady=10)
        titleLabel = tk.Label(top, text='Title')
        titleLabel.pack(padx=10, pady=10)
        titleReminder = tk.Entry(top, width=100, bg='white')
        titleReminder.pack(padx=10, pady=10)
        descriptionLabel = tk.Label(top, text='Description')
        descriptionLabel.pack(padx=10, pady=10)
        descriptionReminder = tk.Entry(top, width=100, bg='white')
        descriptionReminder.pack(padx=10, pady=10,ipady=40)
        submitButton = tk.Button(top, text='Submit',foreground="white",background="green", command=lambda: submit(cal.get_date(),titleReminder.get(),descriptionReminder.get()))
        submitButton.pack(padx=10, pady=10)
        top.config(menu=menubar)
        top.mainloop()

    def getThisMonthReminders(date,window2):
        window2.destroy()
        month,date,year = date.split("/")
        month = month if len(month) == 2 else "0"+month
        year = year if len(year) == 4 else "20"+year
        db = sqlite3.connect('1.db')
        c = db.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS reminder(date TEXT,title TEXT,description TEXT)")
        c.execute("SELECT * FROM reminder WHERE date LIKE ?",(year+"-"+month+"%",))
        reminders = c.fetchall()
        db.close()
        mReminderWindow = tk.Tk()
        mReminderWindow.title("Reminders of the month")
        mReminderWindow.geometry("500x300")
        bg = tk.PhotoImage(file="./images/whitishbg.png")
        bgLabel = tk.Label(mReminderWindow,image=bg,width=560,height=360).place(x=0,y=0)
        # Menubar
        menubar = tk.Menu(mReminderWindow)
        menubar.add_command(label="Back",command=lambda:Reminder(mReminderWindow))
        # Show all reminder in a list
        tk.Label(mReminderWindow, text="Date",background="white",font="times 13 bold").grid(row=0, column=0,padx=(30,10),pady=(30,0))
        tk.Label(mReminderWindow, text="Title",background="white",font="times 13 bold").grid(row=0, column=1,pady=(30,0))
        tk.Label(mReminderWindow, text="Description",background="white",font="times 13 bold").grid(row=0, column=2,padx=(10,30),pady=(30,0))
        for row in range(len(reminders)):
            tk.Label(mReminderWindow, text=reminders[row][0]).grid(row=row+1, column=0)
            tk.Label(mReminderWindow, text=reminders[row][1]).grid(row=row+1, column=1)
            tk.Label(mReminderWindow, text=reminders[row][2]).grid(row=row+1, column=2)
        mReminderWindow.config(menu=menubar)
        mReminderWindow.mainloop()

    root = tk.Tk()
    root.title('Reminder')
    back = Menu(root)
    back.add_command(label="Back",command=lambda:mainWindow(root))
    bg = tk.PhotoImage(file="./images/whitishbg.png")
    bgLabel = tk.Label(root,image=bg,width=560,height=360).place(x=0,y=0)
    tk.Button(root, text='Add Reminder',background="blue",foreground="white", command=lambda:AddReminder(root)).pack(padx=10, pady=10)
    cal = Calendar(root, font="Arial 14", selectmode='day', locale='en_US',
                    cursor="hand1")
    tk.Button(root, text='This Months Reminder',background="green",foreground="white", command=lambda:getThisMonthReminders(cal.get_date(),root)).pack(padx=10, pady=10)
    # Get all events from database

    db = sqlite3.connect('1.db')
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS reminder(date TEXT,title TEXT,description TEXT)")
    c.execute("SELECT * FROM reminder")
    data = c.fetchall()
    # Place events on calendar
    cal.tag_config('reminder', background='red', foreground='yellow')
    for row in data:
        cal.calevent_create(datetime.strptime(row[0], '%Y-%m-%d'), row[1], row[2])
    cal.pack(fill="both", expand=True)
    root.config(menu=back)
    root.mainloop()