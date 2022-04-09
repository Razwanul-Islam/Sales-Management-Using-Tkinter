from tkinter import *
from apps.calculator import calculator
from apps.notepad import notepad
def Main():
    mainWindow = Tk()
    mainWindow.title("Sales management system")
    mainWindow.geometry("800x500")
    menuBar = Menu(mainWindow)
    menuBar.add_command(label="Notepad", command=notepad)
    menuBar.add_command(label="Calculator", command=calculator)
    menuBar.add_command(label="Total sale")
    menuBar.add_command(label="Remainning Due")
    menuBar.add_command(label="Payment Reminder")
    menuBar.add_command(label="Cash in hand")
    menuBar.config(bg="light blue")
    mainWindow.config(menu=menuBar)
    mainWindow.mainloop()