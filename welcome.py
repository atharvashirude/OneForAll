from tkinter import *
import login
import dashboard
import db.db
import crypto
from tkinter import messagebox
import re
fontm = ('courier', 14, 'bold')

class WelcomeWindow:

    #create a constructor
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        #reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=400, bg='Black')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width_value = self.win.winfo_screenwidth()
        height_value = self.win.winfo_screenheight()
        x = int(width_value / 2 - 600 / 2)
        y = int(height_value / 2 - 400 / 2)
        str1 = "600x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        #disable resize of the window
        self.win.resizable(width=False, height=False)

        #change the title of the window
        self.win.title("WELCOME | OneForAll | ADMINISTRATOR")

    def add_frame(self):
        #create a inner frame
        self.frame = Frame(self.win, height=300, width=450,bg="Black")
        self.frame.place(x=80, y=50)

        x, y = 70, 0

        # place the photo in the frame

        self.img = PhotoImage(file='images/icon12.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+55, y=y+33)

        self.labeltitle = Label(self.frame, text="OneForAll",bg="black",fg='yellow green')
        self.labeltitle.config(font=("Ubuntu", 18, 'bold'))
        self.labeltitle.place(x=170, y=0)

        self.button = Button(self.frame, text=" Login ", font=('ubuntu', 17, ' bold')
                             , bg="yellow green", fg='Black', command=self.login)
        self.button.place(x=x+200, y=y+250)
        self.button.bind('<Return>',self.enter)

        self.button = Button(self.frame, text="Register", font=('helvetica', 17, ' bold')
                             , bg="yellow green", fg='Black', command=self.registerr)
        self.button.place(x=x + 25, y=y + 250)
        #self.button.bind('<Return>', self.registerr)

        self.win.mainloop()

    def enter(self, event=None):
        self.login()

    def registerr(self):
        self.addregister()

    def addregister(self):
        screen2 = Toplevel()
        screen2.title("Register")

        self.screen2 = screen2
        # show window in center of the screen
        width = screen2.winfo_screenwidth()
        height = screen2.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        screen2.geometry(str1)
        screen2.configure(background="Black")
        linfo = Label(screen2, text="Enter your information to register !", font=('courier', 16, 'bold'),fg="yellow green",bg="black")
        linfo.place(x=70, y=40)

        lname = Label(screen2, text="Name", font=fontm,fg="yellow green",bg="black")
        lname.place(x=70, y=100)


        lusername = Label(screen2, text="Username", font=fontm,fg="yellow green",bg="black")
        lusername.place(x=70, y=150)

        lemail = Label(screen2, text="Email", font=fontm,fg="yellow green",bg="black")
        lemail.place(x=70, y=200)

        lpassword = Label(screen2, text="Password", font=fontm,fg="yellow green",bg="black")
        lpassword.place(x=70, y=250)



        #****Entrys****



        self.name_text = Entry(screen2, font=fontm,fg="yellow green",bg="black")
        self.name_text.place(x=220, y=100)

        self.username_text = Entry(screen2, font=fontm,fg="yellow green",bg="black")
        self.username_text.place(x=220, y=150)

        self.email_text = Entry(screen2, font=fontm,fg="yellow green",bg="black")
        self.email_text.place(x=220, y=200)

        self.password_text = Entry(screen2, font=fontm,fg="yellow green",bg="black",show='*')
        self.password_text.place(x=220, y=250)




        self.register_button = Button(screen2, text="Register", font='Courier 15 bold', command=self.validating_name,fg="yellow green",bg="black")
        self.register_button.place(x=250, y=350)

    def validating_name(self):

        # RegexObject = re.compile( Regular expression, flag )
        # Compiles a regular expression pattern into a regular expression object
        regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
                                re.IGNORECASE)
        match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', self.email_text.get(), re.I)

        # RegexObject is matched with the desired
        # string using search function
        # In case a match is found, search() returns
        # MatchObject Instance
        # If match is not found, it return None

        res = regex_name.search(self.name_text.get())

        # If match is found, the string is valid
        if res and match:
            self.register()

        # If match is not found, string is invalid
        else:
            messagebox.showerror("Invalid","Invalid Name or email address")


    def register(self):
        #db.db.addata()
        self.encrypt = crypto.Encode("allforone",self.password_text.get())
        en = crypto.Encode("allforone",self.encrypt)
        print("encrypted: "+en)
        self.decrypt = crypto.Decode("allforone",en)
        print("decrypted: "+self.decrypt)
        if self.name_text.get() == "" or self.password_text.get() == "" or self.email_text.get() == "" or self.password_text.get() == "":
        #if self.name_text.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            val = (self.name_text.get(), self.username_text.get(), self.email_text.get(), self.password_text.get())
            print(val)
            res = db.db.logindata(val)
            if res == False:
                messagebox.showerror("Error", "Not Saved")
            else:
                messagebox.showinfo("Successful Save!","Successful Save!")
                self.screen2.destroy()

    #open a new window on button press
    def login(self):
        # destroy current window
        self.win.destroy()

        #open the new window
        #res = db.db.logindata()
        log = login.LoginWindow()
        log.add_frame()
        #ds = dashboard.DashboardWindow()
        #ds.addmainframe()


if __name__ == "__main__":
    x = WelcomeWindow()
    x.add_frame()
