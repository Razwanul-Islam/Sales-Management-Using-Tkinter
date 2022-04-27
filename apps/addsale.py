from cProfile import label
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
def AddSale(window):
    window.destroy()
    def mainWindow(window):
        from .main import Main
        Main(window)
    addSaleWindow = Tk()
    addSaleWindow.title("Sales management system: Add sale info")
    back = Menu(addSaleWindow)
    back.add_command(label="Back",command=lambda:mainWindow(addSaleWindow))
    addSaleWindow.config(bg="#301122",menu=back)
    image = PhotoImage(file="./images/whitishbg.png")
    labelBackground = Label(addSaleWindow,image=image)
    labelBackground.place(x=0,y=0)
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
        messagebox.showinfo(title="Success", message="Reminder added successfully")
        mainWindow(addSaleWindow)

    # Add save sale info
    labelSaleInfoSave = Label(addSaleWindow, text="Add sale info",font="times 14 bold",background="white")
    labelSaleInfoSave.grid(row=2, column=0,columnspan=5,pady=20)
    # Customer name entry
    customerNameLabel = Label(addSaleWindow, text="Customer Name:",background="white")
    customerNameLabel.grid(row=3, column=0,padx=10,pady=5)
    customerName = Entry(addSaleWindow,border=2)
    customerName.grid(row=4, column=0,padx=10,pady=(5,30))
    # Total amount entry
    totalAmountLabel = Label(addSaleWindow, text="Total Amount:",background="white") 
    totalAmountLabel.grid(row=3, column=1,padx=10,pady=5)
    totalAmount = Entry(addSaleWindow,border=2)
    totalAmount.grid(row=4, column=1,padx=10,pady=(5,30))
    # Paid amount entry
    paidAmountLabel = Label(addSaleWindow, text="Paid Amount:",background="white")
    paidAmountLabel.grid(row=3, column=2,padx=10,pady=5)
    paidAmount = Entry(addSaleWindow,border=2)
    paidAmount.grid(row=4, column=2,padx=10,pady=(5,30))
    # Due amount entry
    dueAmountLabel = Label(addSaleWindow, text="Due Amount:",background="white")
    dueAmountLabel.grid(row=3, column=3,padx=10,pady=5)
    dueAmount = Entry(addSaleWindow,border=2)
    dueAmount.grid(row=4, column=3,padx=10,pady=(5,30))
    # save button
    saveInfo = Button(addSaleWindow, text="Save", width=10, height=1,background="#4169e1",foreground="white",font="times 10 bold",command=lambda:saveSaleInfo(customerName.get(),totalAmount.get(),paidAmount.get(),dueAmount.get()))
    saveInfo.grid(row=4, column=4,pady=(5,30))
    addSaleWindow.mainloop()
