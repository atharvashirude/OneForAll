from tkinter import *
from tkinter import messagebox
import db.db
import dashboard
from dashboard import DashboardWindow
import mysql.connector


class LoginWindow:

    def __init__(self):
        self.win = Tk()
        # reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=500, bg='black')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("WELCOME | Login Window | ADMINISTRATOR")
        self.win.configure(background="black")

    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=80, y=50)
        self.frame.configure(background="black")
        x, y = 70, 20

        self.img = PhotoImage(file='images/login.png')
        self.label = Label(self.frame, image=self.img,bg="black")
        self.label.place(x = x + 80, y = y + 0)

        #now create a login form
        self.label = Label(self.frame, text="User Login",fg="yellow green",bg="black")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y = y + 150)

        self.emlabel = Label(self.frame, text="Username",fg="yellow green",bg="black")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y= y + 230)

        self.email = Entry(self.frame, font='Courier 12',fg="yellow green",bg="black")
        self.email.place(x=200, y= y + 230)

        self.pslabel = Label(self.frame, text="Password",fg="yellow green",bg="black")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=y+260)

        self.password = Entry(self.frame,show='*', font='Courier 12',fg="yellow green",bg="black")
        self.password.place(x=200, y=y+260)

        self.button = Button(self.frame, text="Login", font='Courier 15 bold',
                             command=self.login,fg="yellow green",bg="black")
        self.button.place(x=170, y=y+290)

        self.win.mainloop()

    def login(self):
        #get the data and store it into tuple (data)
        data = (
            self.email.get(),
            self.password.get()
        )
        #y = dashboard.DashboardWindow.save(data)
        #print(data)
        # validations
        if self.email.get() == "":
            messagebox.showwarning("Alert!","Enter Email First")
        elif self.password.get() == "":
            messagebox.showwarning("Alert!", "Enter Password first")
        else:
            res = db.db.user_login(data)
            if res:
                messagebox.showinfo("Message", "Login Successful")
                self.win.destroy()
                '''
                connect = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="toor",
                    database="test"
                )
                cursorr = connect.cursor()
                '''
                #tup = self.email.get()
                #val = self.password.get()
                '''val = (
                self.email.get(),
                self.password.get())
                print("hello")
                #qwery="select loginid from login where username=%s,password=%s"
                cursorr.execute("select loginid from login where username=%s,password=%s",val)
                print("executed")
                cred = cursorr.fetchone()
                print(cred)
                y = dashboard.DashboardWindow.save(cred)
                '''
                #y = dashboard.DashboardWindow.save(data)
                x = dashboard.DashboardWindow()
            else:
                messagebox.showerror("ALert!", "Wrong username/password")


    '''
    def security_add_frame(self):
        self.frame1 = Frame(self.win, height=400, width=450)
        self.frame1.place(x=80, y=50)
        self.frame1.configure(background="black")
        x, y = 70, 20

        #self.img1 = PhotoImage(file='images/login.png')
        #self.label11 = Label(self.frame1, image=self.img1,bg="black")
        #self.label11.place(x = x + 80, y = y + 0)

        #now create a login form
        self.label1 = Label(self.frame1, text="User Login",fg="yellow green",bg="black")
        self.label1.config(font=("Courier", 20, 'bold'))
        self.label1.place(x=140, y = y + 150)

        self.emlabel1 = Label(self.frame1, text="Username",fg="yellow green",bg="black")
        self.emlabel1.config(font=("Courier", 12, 'bold'))
        self.emlabel1.place(x=50, y= y + 230)

        self.email1 = Entry(self.frame1, font='Courier 12',fg="yellow green",bg="black")
        self.email1.place(x=200, y= y + 230)

        self.pslabel1 = Label(self.frame1, text="Password",fg="yellow green",bg="black")
        self.pslabel1.config(font=("Courier", 12, 'bold'))
        self.pslabel1.place(x=50, y=y+260)

        self.password1 = Entry(self.frame1,show='*', font='Courier 12',fg="yellow green",bg="black")
        self.password1.place(x=200, y=y+260)

        self.button1 = Button(self.frame1, text="Login", font='Courier 15 bold',
                             command=self.security_login,fg="yellow green",bg="black")
        self.button1.place(x=170, y=y+290)

        self.win.mainloop()

    def security_login(self):
        #get the data and store it into tuple (data)
        data = (
            self.email1.get(),
            self.password1.get()
        )
        #y = dashboard.DashboardWindow.save(data)
        #print(data)
        # validations
        if self.email1.get() == "":
            messagebox.showwarning("Alert!","Enter Email First")
        elif self.password1.get() == "":
            messagebox.showwarning("Alert!", "Enter Password first")
        else:
            res = db.db.user_login(data)
            if res:
                messagebox.showinfo("Message", " Successful")
                self.win.destroy()
    
                connect = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="toor",
                    database="test"
                )
                cursorr = connect.cursor()
                
                #tup = self.email.get()
                #val = self.password.get()
                val = (
                self.email.get(),
                self.password.get())
                print("hello")
                #qwery="select loginid from login where username=%s,password=%s"
                cursorr.execute("select loginid from login where username=%s,password=%s",val)
                print("executed")
                cred = cursorr.fetchone()
                print(cred)
                y = dashboard.DashboardWindow.save(cred)
                
                #y = dashboard.DashboardWindow.save(data)
                x = DashboardWindow.decryptt(self)


            else:
                messagebox.showerror("ALert!", "Wrong username/password")

    '''
