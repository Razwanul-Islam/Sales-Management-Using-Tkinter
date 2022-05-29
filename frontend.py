from tkinter import *
import sqlite3
from apps.main import Main
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
    bg = PhotoImage(file="./images/wt1.png")
    entryImage = PhotoImage(file="./images/img_textBox1.png")
    label1 = Label( login_window, image = bg)
    label1.place(x=0,y=0)
    login_window.title("LogIn")  #set title to the window
    login_window.geometry("420x400")  #set dimensions to the window
    login_window.resizable(False,False)
    #add 2 Labels to the window
    Label(text="Login",font="Garamond 20 bold",bg="white",fg="grey").place(x=180,y=30)
    l1 = Label(login_window,text="Email: ",font="times 10 bold",bg="white",fg="grey")
    l1.grid(row=1,column=0,pady=(100,0),padx=(60,0))

    l2 = Label(login_window,text="Password: ",font="times 10 bold",bg="white",fg="grey")
    l2.grid(row=3,column=0,pady=(10,0),padx=(60,0))

    l3 = Label(login_window,font="times 8",bg="white",fg="grey")
    l3.grid(row=6,column=0,pady=(10,0),padx=(60,0))

    #creating 2 adjacent text entries
    Label(login_window,image=entryImage).place(x=115,y=125)
    email_text = StringVar() #stores string
    e1 = Entry(login_window,textvariable=email_text,bd = 0,bg = "#c4c4c4",highlightthickness = 0)
    e1.image = entryImage
    e1.grid(row=2,column=0,pady=(10,0),padx=(120,0))

    Label(login_window,image=entryImage).place(x=115,y=183)
    password_text = StringVar()
    e2 = Entry(login_window,textvariable=password_text,show='*',bd = 0,bg = "#c4c4c4",highlightthickness = 0)
    e2.image = entryImage
    e2.grid(row=4,column=0,pady=(10,0),padx=(120,0))

    #create 1 button to login
    loginImage = PhotoImage(file="./images/loginbtn.png")
    b = Button(login_window,image=loginImage,command=login_database,bg="white",borderwidth = 0,highlightthickness = 0)
    b.grid(row=5,column=0,pady=(10,0),padx=(80,0))

    l0 = Label(login_window,text="Don't have an account? ",font="times 10 bold",bg="white",fg="grey")
    l0.grid(row=7,column=0)
    signupImage = PhotoImage(file="./images/signupbtn.png")
    signup_btn = Button(login_window,image=signupImage,command=lambda:signup(login_window),bg="white",borderwidth = 0,highlightthickness = 0)
    signup_btn.grid(row=7,column=1)
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
        l4 = Label(signup_window,text="account created",font="times 10",bg="grey",fg="white")
        
        l4.grid(row=8,column=0,columnspan=2)
        
        conn.commit()  #save the changes 
        conn.close() #close the connection
        login(signup_window) #call login function

    window.destroy()  #closes the previous window
    signup_window = Tk() #creates a new window for signup process
    bg = PhotoImage(file="./images/wt1.png")
    label1 = Label( signup_window, image = bg)
    label1.place(x=0,y=0)
    signup_window.geometry("420x400") #dimensions for new window
    signup_window.title("Sign Up") #title for the window
    signup_window.resizable(False,False)
    Label(text="Signup",font="Garamond 20 bold",bg="white",fg="grey").place(x=180,y=30)
    #create 3 Labels
    l1 = Label(signup_window,text="User Name: ",font="times 10 bold",bg="white",fg="grey")
    l1.grid(row=1,column=0,pady=(100,0),padx=(60,0))

    l2 = Label(signup_window,text="User email: ",font="times 10 bold",bg="white",fg="grey")
    l2.grid(row=3,column=0,pady=(10,0),padx=(60,0))

    l3 = Label(signup_window,text="Password: ",font="times 10 bold",bg="white",fg="grey")
    l3.grid(row=5,column=0,pady=(10,0),padx=(60,0))

    #create 3 adjacent text entries
    entryImage = PhotoImage(file="./images/img_textBox1.png")
    Label(signup_window,image=entryImage).place(x=115,y=125)
    name_text = StringVar() #declaring string variable for storing name and password
    e1 = Entry(signup_window,textvariable=name_text,bd = 0,bg = "#c4c4c4",highlightthickness = 0)
    e1.grid(row=2,column=0,pady=(10,0),padx=(120,0))

    Label(signup_window,image=entryImage).place(x=115,y=183)
    email_text = StringVar()
    e2 = Entry(signup_window,textvariable=email_text,bd = 0,bg = "#c4c4c4",highlightthickness = 0)
    e2.grid(row=4,column=0,pady=(10,0),padx=(120,0))

    Label(signup_window,image=entryImage).place(x=115,y=241)
    password_text = StringVar()
    e3 = Entry(signup_window,textvariable=password_text,show='*',bd = 0,bg = "#c4c4c4",highlightthickness = 0)
    e3.grid(row=6,column=0,pady=(10,0),padx=(120,0))

    #create 1 button to signup
    signupImage = PhotoImage(file="./images/signupbtn.png")
    b1 = Button(signup_window,image=signupImage,command=signup_database,bg="white",bd=0,highlightthickness = 0)
    b1.grid(row=7,column=0,pady=(10,0),padx=(80,0))
    
    l0 = Label(signup_window,text="Already have an account? ",font="times 10 bold",bg="white",fg="grey")    
    l0.grid(row=9,column=0,pady=15)
    loginImage = PhotoImage(file="./images/loginbtn.png")
    b2 = Button(signup_window,image=loginImage,command=lambda:login(signup_window),bg="white",bd=0,highlightthickness = 0)
    b2.grid(row=9,column=1)
    signup_window.mainloop()

#main window code and driver code
#give dimensions to the window
# window.geometry("800x400")
#add title to the window
window.title("Sales management system")
window.config(background="white")
window.geometry("800x400")
window.resizable(False,False)
# Background
bg = PhotoImage(file="./images/wt1.png")
Label( window, image = bg).place(x=0,y=0)
#adding the label "Register Here"
label1 = Label(window, text="Login or Register Here!",font="Garamond 20 bold",background="white")
label1.grid(row=1,column=0,columnspan=6,padx=(250),pady=(100,0))
loginImage = PhotoImage(file="./images/loginbtn.png")
signupImage = PhotoImage(file="./images/signupbtn.png")
#adding two buttons - login and signup
button1 = Button(window,image=loginImage,command=lambda:login(window),bg="white",bd=0,highlightthickness = 0)
button1.grid(row=2,column=2,pady=50,padx=(50,0))

button2 = Button(window,image=signupImage,command=lambda:signup(window),bg="white",bd=0,highlightthickness = 0)
button2.grid(row=2,column=3,pady=50,padx=50)

#calling mainloop method which is used when your application is ready to run and it tells the code to keep displaying
window.mainloop()