from tkinter import *
import sqlite3
from main import Main

#create an object to create a window
window = Tk()

#Actions on Pressing Login Button
def login(window):
    def login_database():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
        row=cur.fetchall()
        conn.close()
        if row!=[]:
            user_name=row[0][1]
            login_window.destroy()
            Main()
        else:
            l3.config(text="user not found")

    window.destroy()  #closes the previous window
    login_window = Tk() #creates a new window for loging in
    login_window.title("LogIn")  #set title to the window
    login_window.geometry("400x250")  #set dimensions to the window
    #add 2 Labels to the window
    l1 = Label(login_window,text="email: ",font="times 14")
    l1.grid(row=1,column=0)

    l2 = Label(login_window,text="Password: ",font="times 14")
    l2.grid(row=2,column=0)

    l3 = Label(login_window,font="times 14")
    l3.grid(row=5,column=1)

    #creating 2 adjacent text entries
    email_text = StringVar() #stores string
    e1 = Entry(login_window,textvariable=email_text)
    e1.grid(row=1,column=1)

    password_text = StringVar()
    e2 = Entry(login_window,textvariable=password_text,show='*')
    e2.grid(row=2,column=1)

    #create 1 button to login
    b = Button(login_window,text="login",width=20,command=login_database)
    b.grid(row=4,column=1)

    l0 = Label(login_window,text="Don't have an account? ",font="times 14")
    l0.grid(row=6,column=0)
    signup_btn = Button(login_window,text="Signup",width=20,command=lambda:signup(login_window))
    signup_btn.grid(row=6,column=1)
    login_window.mainloop()

#Actions on Pressing Signup button
def signup(window):
    #Database action on pressing signup button
    def signup_database():
        conn = sqlite3.connect("1.db") #create an object to call sqlite3 module & connect to a database 1.db
        #once you have a connection, you can create a cursor object and call its execute() method to perform SQL commands
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text,password text)")
        cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
        
        #execute message after account successfully created
        l4 = Label(signup_window,text="account created",font="times 15")
        
        l4.grid(row=6,column=0,columnspan=2)
        
        conn.commit()  #save the changes 
        conn.close() #close the connection
        login(signup_window) #call login function

    window.destroy()  #closes the previous window
    signup_window = Tk() #creates a new window for signup process
    signup_window.geometry("400x250") #dimensions for new window
    signup_window.title("Sign Up") #title for the window
    #create 3 Labels
    l1 = Label(signup_window,text="User Name: ",font="times 14")
    l1.grid(row=1,column=0)

    l2 = Label(signup_window,text="User email: ",font="times 14")
    l2.grid(row=2,column=0)

    l3 = Label(signup_window,text="Password: ",font="times 14")
    l3.grid(row=3,column=0)

    #create 3 adjacent text entries
    name_text = StringVar() #declaring string variable for storing name and password
    e1 = Entry(signup_window,textvariable=name_text)
    e1.grid(row=1,column=1)

    email_text = StringVar()
    e2 = Entry(signup_window,textvariable=email_text)
    e2.grid(row=2,column=1)

    password_text = StringVar()
    e3 = Entry(signup_window,textvariable=password_text,show='*')
    e3.grid(row=3,column=1)

    #create 1 button to signup
    b1 = Button(signup_window,text="signup",width=20,command=signup_database)
    b1.grid(row=4,column=1)

    l0 = Label(signup_window,text="Already have an account? ",font="times 14")
    l0.grid(row=6,column=0,pady=20)
    signup_btn = Button(signup_window,text="Login",width=20,command=lambda:login(signup_window))
    signup_btn.grid(row=6,column=1)
    signup_window.mainloop()

#main window code and driver code
#give dimensions to the window
# window.geometry("800x400")
#add title to the window
window.title("Sales management system")
window.config(background="white")
#adding the label "Register Here"
label1 = Label(window, text="Login or Register Here!",font="times 20",background="white")
label1.grid(row=1,column=0,columnspan=6,padx=50)
#adding two buttons - login and signup
button1 = Button(window,text="Login",width=30,height=1,command=lambda:login(window))
button1.config(background="#4169e1",foreground="white",font="times 14")
button1.grid(row=2,column=2,pady=50,padx=50)

button2 = Button(window,text="Signup",width=30,height=1,command=lambda:signup(window))
button2.config(background="#4BB543",foreground="white",font="times 14")
button2.grid(row=2,column=3,pady=50,padx=50)


#calling mainloop method which is used when your application is ready to run and it tells the code to keep displaying
window.mainloop()