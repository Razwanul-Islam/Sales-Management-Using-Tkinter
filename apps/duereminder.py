from tkinter import *
from sqlite3 import *
from datetime import datetime


def DueReminder(window=None):
    # If has parent window , close / destroy the parent window
    if window is not None:window.destroy()
    def mainWindow(window):
        from .main import Main
        Main(window)
    # Initialize variable and lists
    row_num = 0
    types= (
        "Delay less than 3 days",
        "Delay more than 3 days",
        "Delay more than 7 days",
        "Delay more than 15 days",
        "Delay more than 1 month"
    )
    categorize =[[],[],[],[],[]]
    # Funcitions

    # due clear
    def clearDue(id):
        print(f"Due cleared of {id}") 

    # Fetch sales info from database
    db = connect("1.db")
    cur = db.cursor()
    cur.execute("SELECT * from sales WHERE dueAmount>0")
    data = cur.fetchall()

    # Categorize according to delay
    currentDate = datetime.now()
    for row in data:
        date = datetime.strptime(row[5],"%Y-%m-%d %H:%M:%S")
        dif = currentDate - date
        if dif.days>30:
            categorize[4].append(row)
        elif dif.days>15:
            categorize[3].append(row)
        elif dif.days>7:
            categorize[2].append(row)
        elif dif.days>3:
            categorize[1].append(row)
        else:
            categorize[0].append(row)

    # Create window
    dueReminderWindow = Tk()
    dueReminderWindow.title("Due Reminder")
    dueReminderWindow.geometry("700x400")

    # Back button
    back = Menu(dueReminderWindow)
    back.add_command(label="Back",command=lambda:mainWindow(dueReminderWindow))

    # Bg image
    bg=PhotoImage(file="./images/whitishbg.png")
    Label(dueReminderWindow,image=bg).place(x=0,y=0)

    # Show all data in window
    for i in range(len(types)):
        Label(dueReminderWindow,text=types[i],font="arial 12 bold").grid(row=row_num,column=0)
        row_num+=1
        # table header
        Label(dueReminderWindow,text="Customer name",font="arial 10 bold").grid(row=row_num,column=0,padx=5,pady=5)
        Label(dueReminderWindow,text="Sale amount",font="arial 10 bold").grid(row=row_num,column=1,padx=5,pady=5)
        Label(dueReminderWindow,text="Paid amount",font="arial 10 bold").grid(row=row_num,column=2,padx=5,pady=5)
        Label(dueReminderWindow,text="Due amount",font="arial 10 bold").grid(row=row_num,column=3,padx=5,pady=5)
        Label(dueReminderWindow,text="Sales date",font="arial 10 bold").grid(row=row_num,column=4,padx=5,pady=5)
        row_num+=1
        for index,row in enumerate(categorize[i]):
            Label(dueReminderWindow,text=row[1],font="arial 10").grid(row=row_num,column=0,padx=5,pady=5)
            Label(dueReminderWindow,text=row[2],font="arial 10").grid(row=row_num,column=1,padx=5,pady=5)
            Label(dueReminderWindow,text=row[3],font="arial 10").grid(row=row_num,column=2,padx=5,pady=5)
            Label(dueReminderWindow,text=row[4],font="arial 10").grid(row=row_num,column=3,padx=5,pady=5)
            Label(dueReminderWindow,text=row[5],font="arial 10").grid(row=row_num,column=4,padx=5,pady=5)
            row_num+=1
    # Window mainloop
    dueReminderWindow.config(menu=back)
    dueReminderWindow.mainloop()