from tkinter import *
import sqlite3

def SalesInfo(window):
    window.destroy()
    def mainWindow(window):
        from .main import Main
        Main(window)
    salesInfoWindow = Tk()
    salesInfoWindow.title("Sales management system: Sales Info.")
    salesInfoWindow.config(bg="white")
    image1 = PhotoImage(file="./images/whitishbg.png")
    labelBackground1 = Label(salesInfoWindow,image=image1)
    labelBackground1.place(x=0,y=0)
    # Add save sale info to database
    

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

    
    # Sales Info
    back = Menu(salesInfoWindow)
    back.add_command(label="Back",command=lambda:mainWindow(salesInfoWindow))
    # Add total sale info
    labelTotalSale = Label(salesInfoWindow, text="Total Sale",background="white",font="times 13 bold")
    labelTotalSale.grid(row=5, column=0,pady=(30,0))
    totalSale = Label(salesInfoWindow, text=getGetTotalSale(),background="blue",foreground="white",width=10,height=5,font="times 14 bold")
    totalSale.grid(row=6, column=0,padx=40,pady=(10,50))
    # Add cash in hand info
    labelCashInHand = Label(salesInfoWindow, text="Cash in hand",background="white",font="times 13 bold")
    labelCashInHand.grid(row=5, column=2,pady=(30,0))
    cashInHand = Label(salesInfoWindow, text=getCashInHand(),background="green",foreground="white",width=10,height=5,font="times 14 bold")
    cashInHand.grid(row=6, column=2,padx=40,pady=(10,50))
    # Add remainning due info
    labelRemainningDue = Label(salesInfoWindow, text="Remainning Due",background="white",font="times 13 bold")
    labelRemainningDue.grid(row=5, column=4,pady=(30,0))
    remainningDue = Label(salesInfoWindow, text=getRemainningDue(),background="red",foreground="white",width=10,height=5,font="times 14 bold")
    remainningDue.grid(row=6, column=4,padx=40,pady=(10,50))

    salesInfoWindow.config(menu=back)
    salesInfoWindow.mainloop()