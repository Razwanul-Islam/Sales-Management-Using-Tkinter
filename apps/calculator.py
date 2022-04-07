#simple calculator with tkinter
from tkinter import *
def calculator():
    calculatorWindow = Tk()
    calculatorWindow.title("Sales management system: Calculator")


    #create text entry box
    text_entry = Entry(calculatorWindow, width=60, borderwidth=4)
    text_entry.grid(row=0, column=0, columnspan=4, padx=0, pady=10)


    #create buttons
    button_1 = Button(calculatorWindow, text="1", padx=40, pady=20)
    button_2 = Button(calculatorWindow, text="2", padx=40, pady=20)
    button_3 = Button(calculatorWindow, text="3", padx=40, pady=20)
    button_4 = Button(calculatorWindow, text="4", padx=40, pady=20)
    button_5 = Button(calculatorWindow, text="5", padx=40, pady=20)
    button_6 = Button(calculatorWindow, text="6", padx=40, pady=20)
    button_7 = Button(calculatorWindow, text="7", padx=40, pady=20)
    button_8 = Button(calculatorWindow, text="8", padx=40, pady=20)
    button_9 = Button(calculatorWindow, text="9", padx=40, pady=20)
    button_0 = Button(calculatorWindow, text="0", padx=40, pady=20)
    btn_add = Button(calculatorWindow, text="+", padx=39, pady=20)
    btn_substract = Button(calculatorWindow, text="-", padx=40, pady=20)
    btn_equal = Button(calculatorWindow, text="=", padx=40, pady=20)
    btn_clear = Button(calculatorWindow, text="Clear", padx=36, pady=20)
    btn_multiply = Button(calculatorWindow, text="*", padx=40, pady=20)
    btn_divide = Button(calculatorWindow, text="/", padx=40, pady=20)


    #put buttons on the screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_0.grid(row=4, column=0)
    btn_add.grid(row=1, column=3)
    btn_substract.grid(row=2, column=3)
    btn_equal.grid(row=4, column=2)
    btn_clear.grid(row=4, column=1)
    btn_multiply.grid(row=3, column=3)
    btn_divide.grid(row=4, column=3)

    #create a function for buttons
    def button_click(number):
        current = text_entry.get()
        current = "" if current == "Error" else current
        text_entry.delete(0, END)
        text_entry.insert(0, str(current) + str(number))


    def button_add():
        first_number = text_entry.get()
        first_number = "0" if first_number == "Error" else first_number
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        text_entry.delete(0, END)


    def button_equal():
        second_number = text_entry.get()
        global f_num
        if second_number == "Error":
            second_number = 0
        if f_num == "Error":
            f_num = 0
        text_entry.delete(0, END)

        if math == "addition":
            text_entry.insert(0, f_num + int(second_number))

        if math == "subtraction":
            text_entry.insert(0, f_num - int(second_number))

        if math == "multiplication":
            text_entry.insert(0, f_num * int(second_number))

        if math == "division":
            if int(second_number) == 0:
                text_entry.insert(0, "Error")
            else:
                text_entry.insert(0, f_num / int(second_number))


    def button_clear():
        text_entry.delete(0, END)


    def button_subtract():
        first_number = text_entry.get()
        first_number = "0" if first_number == "Error" else first_number
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        text_entry.delete(0, END)


    def button_multiply():
        first_number = text_entry.get()
        first_number = "0" if first_number == "Error" else first_number
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        text_entry.delete(0, END)


    def button_divide():
        first_number = text_entry.get()
        first_number = "0" if first_number == "Error" else first_number
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        text_entry.delete(0, END)


    #put buttons on the screen
    button_1.configure(command=lambda: button_click(1))
    button_2.configure(command=lambda: button_click(2))
    button_3.configure(command=lambda: button_click(3))
    button_4.configure(command=lambda: button_click(4))
    button_5.configure(command=lambda: button_click(5))
    button_6.configure(command=lambda: button_click(6))
    button_7.configure(command=lambda: button_click(7))
    button_8.configure(command=lambda: button_click(8))
    button_9.configure(command=lambda: button_click(9))
    button_0.configure(command=lambda: button_click(0))
    btn_add.configure(command=button_add)
    btn_equal.configure(command=button_equal)
    btn_clear.configure(command=button_clear)
    btn_substract.configure(command=button_subtract)
    btn_multiply.configure(command=button_multiply)
    btn_divide.configure(command=button_divide)


    calculatorWindow.mainloop()