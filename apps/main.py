import sqlite3
from tkinter import *


def Main(window = None):
    def Calculator():
        from .calculator import calculator
        return calculator()
    def Notepad():
        from .notepad import notepad
        return notepad()
    def Salesinfo0(window):
        from .salesinfo import SalesInfo
        return SalesInfo(window)
    def Addsale0(window):
        from .addsale import AddSale
        return AddSale(window)
    def Reminder0(window):
        from .reminder import Reminder
        return Reminder(window)
    def Duereminder0(window):
        from .duereminder import DueReminder
        return DueReminder(window)
    if window is not None:window.destroy()
    mainWindow = Tk()
    mainWindow.title("Sales management system: Sales info")
    mainWindow.geometry("560x360")
    bg = PhotoImage(file="./images/whitishbg.png")
    bgLabel = Label(mainWindow,image=bg,width=560,height=360)
    bgLabel.place(x=0,y=0)
    # calculator button
    buttonCalculator = Button(mainWindow, text="Calculator",width="15", command=Calculator,background="blue",foreground="white",font="times 12")
    buttonCalculator.grid(row=0, column=0,padx=(40,10),pady=(120,10))
    # notepad button
    buttonNotePad = Button(mainWindow, text="Notepad", width="15",command=Notepad,background="green",foreground="white",font="times 12")
    buttonNotePad.grid(row=0, column=1,padx=10,pady=(120,10))
    # Due management
    buttonDue = Button(mainWindow, text="Due Reminder", width="15",command=lambda:Duereminder0(mainWindow),background="orange",foreground="white",font="times 12")
    buttonDue.grid(row=0,column=2,padx=10,pady=(120,10))
    # sales info button
    buttonSalesInfo = Button(mainWindow,text="Sales Info",width="15",command=lambda:Salesinfo0(mainWindow),background="red",foreground="white",font="times 12")    
    buttonSalesInfo.grid(row=1,column=0,padx=(40,10),pady=20)
    # sales info button
    buttonReminder = Button(mainWindow,text="Reminder",width="15",command=lambda:Reminder0(mainWindow),background="grey",foreground="white",font="times 12")    
    buttonReminder.grid(row=1,column=1)
    # Add sell info
    buttonAddSale = Button(mainWindow,text="Add sale info",width="15",command=lambda:Addsale0(mainWindow),background="purple",foreground="white",font="times 12")
    buttonAddSale.grid(row=1,column=2)
    mainWindow.mainloop()