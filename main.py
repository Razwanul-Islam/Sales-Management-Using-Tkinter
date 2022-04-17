import sqlite3
from tkinter import *
from apps.calculator import calculator
from apps.notepad import notepad
from apps.salesinfo import SalesInfo
from apps.addsale import AddSale
def Main():
    mainWindow = Tk()
    mainWindow.title("Sales management system: Sales info")
    mainWindow.geometry("560x360")
    mainWindow.resizable(False,False)
    bg = PhotoImage(file="./images/whitishbg.png")
    bgLabel = Label(mainWindow,image=bg,width=560,height=360)
    bgLabel.place(x=0,y=0)
    # calculator button
    buttonCalculator = Button(mainWindow, text="Calculator",width="15", command=calculator,background="blue",foreground="white",font="times 12")
    buttonCalculator.grid(row=0, column=0,padx=(40,10),pady=(120,10))
    # notepad button
    buttonNotePad = Button(mainWindow, text="Notepad", width="15",command=notepad,background="green",foreground="white",font="times 12")
    buttonNotePad.grid(row=0, column=1,padx=10,pady=(120,10))
    # Due management
    buttonDue = Button(mainWindow, text="Due management", width="15",background="orange",foreground="white",font="times 12")
    buttonDue.grid(row=0,column=2,padx=10,pady=(120,10))
    # sales info button
    buttonSalesInfo = Button(mainWindow,text="Sales Info",width="15",command=lambda:SalesInfo(mainWindow),background="red",foreground="white",font="times 12")    
    buttonSalesInfo.grid(row=1,column=0,padx=(40,10),pady=20)
    # sales info button
    buttonReminder = Button(mainWindow,text="Reminder",width="15",background="grey",foreground="white",font="times 12")    
    buttonReminder.grid(row=1,column=1)
    # Add sell info
    buttonAddSale = Button(mainWindow,text="Add sale info",width="15",command=lambda:AddSale(mainWindow),background="purple",foreground="white",font="times 12")
    buttonAddSale.grid(row=1,column=2)
    mainWindow.mainloop()

Main()