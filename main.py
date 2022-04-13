from cProfile import label
import sqlite3
from tkinter import *

from django import db
from apps.calculator import calculator
from apps.notepad import notepad
def Main():
    mainWindow = Tk()
    mainWindow.title("Sales management system")
    # Create menubar
    # menuBar = Menu(mainWindow)
    # menuBar.add_command(label="Notepad", command=notepad)
    # menuBar.add_command(label="Calculator", command=calculator)
    # menuBar.add_command(label="Payment Reminder")
    # menuBar.config(bg="light blue")

    buttonCalculator = Button(mainWindow, text="Calculator", command=calculator,background="blue",foreground="white")
    buttonCalculator.grid(row=0, column=0)
    buttonNotePad = Button(mainWindow, text="Notepad", command=notepad,background="green",foreground="white")
    buttonNotePad.grid(row=0, column=1)

    # Add save sale info to database
    def saveSaleInfo(Name,total_Amount,paid_Amount,due_Amount):
        db = sqlite3.connect("1.db")
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS sales(id INTEGER PRIMARY KEY,customerName text,totalAmount REAL,paidAmount REAL,dueAmount REAL,saleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute("INSERT INTO sales(customerName,totalAmount,paidAmount,dueAmount) VALUES(?,?,?,?)",(Name,total_Amount,paid_Amount,due_Amount))
        db.commit()
        db.close()
        customerName.delete(0,END)
        totalAmount.delete(0,END)
        paidAmount.delete(0,END)
        dueAmount.delete(0,END)
        refreshGetData()

    # get total sale info from database
    def getGetTotalSale():
        db = sqlite3.connect("1.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sales")
        data = cursor.fetchall()
        total = 0
        for row in data:
            total += row[2]
        return total

    # get cash in hand info from database
    def getCashInHand():
        db = sqlite3.connect("1.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sales")
        data = cursor.fetchall()
        total = 0
        for row in data:
            total += row[3]
        return total

    # get remainning due info from database
    def getRemainningDue():
        db = sqlite3.connect("1.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM sales")
        data = cursor.fetchall()
        total = 0
        for row in data:
            total += row[4]
        return total

    def refreshGetData():
        totalSale.config(text=str(getGetTotalSale()))
        cashInHand.config(text=str(getCashInHand()))
        remainningDue.config(text=str(getRemainningDue()))

    mainWindow.config(background="white")

    # Add save sale info
    labelSaleInfoSave = Label(mainWindow, text="Add sale info",font="times 14 bold",background="white")
    labelSaleInfoSave.grid(row=2, column=0,columnspan=5)
    # Customer name entry
    customerNameLabel = Label(mainWindow, text="Customer Name:",background="white")
    customerNameLabel.grid(row=3, column=0,padx=10,pady=5)
    customerName = Entry(mainWindow,border=2)
    customerName.grid(row=4, column=0,padx=10,pady=5)
    # Total amount entry
    totalAmountLabel = Label(mainWindow, text="Total Amount:",background="white") 
    totalAmountLabel.grid(row=3, column=1,padx=10,pady=5)
    totalAmount = Entry(mainWindow,border=2)
    totalAmount.grid(row=4, column=1,padx=10,pady=5)
    # Paid amount entry
    paidAmountLabel = Label(mainWindow, text="Paid Amount:",background="white")
    paidAmountLabel.grid(row=3, column=2,padx=10,pady=5)
    paidAmount = Entry(mainWindow,border=2)
    paidAmount.grid(row=4, column=2,padx=10,pady=5)
    # Due amount entry
    dueAmountLabel = Label(mainWindow, text="Due Amount:",background="white")
    dueAmountLabel.grid(row=3, column=3,padx=10,pady=5)
    dueAmount = Entry(mainWindow,border=2)
    dueAmount.grid(row=4, column=3,padx=10,pady=5)
    # save button
    saveInfo = Button(mainWindow, text="Save", width=10, height=1,background="#4169e1",foreground="white",font="times 10 bold",command=lambda:saveSaleInfo(customerName.get(),totalAmount.get(),paidAmount.get(),dueAmount.get()))
    saveInfo.grid(row=4, column=4)

    # Sales Info
    # Add total sale info
    labelTotalSale = Label(mainWindow, text="Total Sale",background="white",font="times 13 bold")
    labelTotalSale.grid(row=5, column=0,pady=5)
    totalSale = Label(mainWindow, text=getGetTotalSale(),background="blue",foreground="white",width=10,height=5,font="times 14 bold")
    totalSale.grid(row=6, column=0)
    # Add cash in hand info
    labelCashInHand = Label(mainWindow, text="Cash in hand",background="white",font="times 13 bold")
    labelCashInHand.grid(row=5, column=2)
    cashInHand = Label(mainWindow, text=getCashInHand(),background="green",foreground="white",width=10,height=5,font="times 14 bold")
    cashInHand.grid(row=6, column=2)
    # Add remainning due info
    labelRemainningDue = Label(mainWindow, text="Remainning Due",background="white",font="times 13 bold")
    labelRemainningDue.grid(row=5, column=4)
    remainningDue = Label(mainWindow, text=getRemainningDue(),background="red",foreground="white",width=10,height=5,font="times 14 bold")
    remainningDue.grid(row=6, column=4,padx=10,pady=5)
    
    
    mainWindow.mainloop()
