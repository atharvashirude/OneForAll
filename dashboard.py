from tkinter import *
from tkinter import messagebox
import db.db
from tkinter import ttk
from mysql.connector import Error
from mysql.connector import errorcode
import mysql.connector
import crypto
from PIL import ImageTk
import re
import login

fontm = ('courier', 14, 'bold')

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="test"
)

cursor = con.cursor()

#*****Variables*****


#val = (adname, adwebsite, adusername, adwebsite, adpassword)

class DashboardWindow(Tk):
    def __init__(self):
        #Tk.__init__(self)
        self.root = Tk()
        # reset the window and background color
        self.canvas = Canvas(self.root, width=600, height=500, bg='Black')
        self.canvas.pack(expand=YES, fill=BOTH)
        #img2 = ImageTk.PhotoImage(file='images/wall.jpg')
        #label13 = Label(self.root, image=img2)
        #label13.place(x=0, y=0)
        # show window in center of the screen
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        #x = int(width / 2 - 600 / 2)
        #y = int(height / 2 - 500 / 2)
        #str1 = "600x500+" + str(x) + "+" + str(y)
        self.root.geometry("%dx%d+0+0" % (width, height))

        # disable resize of the window
        self.root.resizable(width=False, height=False)

        # change the title of the window
        self.root.title("WELCOME | OneForAll Window | ADMINISTRATOR")
        self.addmainframe()
        self.root.mainloop()
        #self.root.configure(background="black")
        #self.root.title("WELCOME | OneForAll | ADMINISTRATOR")
    '''
    def database(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toor",
            database="test"
        )

        self.cursor = self.con.cursor()
    '''
    def addmainframe(self):
        self.frame = Frame(self.root, height=600, width=1200)
        self.frame.place(x=80, y=50)

        self.img2 = ImageTk.PhotoImage(file='images/wall.jpg')
        self.label13 = Label(self.frame, image=self.img2)
        self.label13.place(x=0, y=0)

        self.img1 = PhotoImage(file='images/icon1.png')
        self.label12 = Label(self.frame, image=self.img1)
        self.label12.place(x = 100, y =  100)

        self.img4 = PhotoImage(file='images/logout.png')
        self.img = PhotoImage(file='images/Add.gif')
        self.image = PhotoImage(file='images/Search.gif')

        self.label = Label(self.frame, text="Dashboard", font='ubuntu 35 bold underline',fg="yellow green",bg="black")
        self.label.place(x=500, y=33)

        self.label2 = Label(self.frame, text="Add", font='Courier 15 bold',fg="yellow green",bg="black")
        self.label2.place(x=495, y= 430)

        self.label1 = Label(self.frame, text="Show", font='Courier 15 bold',fg="yellow green",bg="black")
        self.label1.place(x=690, y=430)

        self.labellog = Label(self.frame, text="Logout", font='Courier 15 bold', fg="yellow green", bg="black")
        self.labellog.place(x=982, y=150)

        self.button = Button(self.frame, text="Logout", font='Courier 15 bold', command=self.logout,image=self.img4,fg="yellow green",bg="black")
        self.button.place(x=1000, y=100)

        self.button = Button(self.frame, text="Add", font='Courier 15 bold', command=self.add, image=self.img,width=120,height=120,bg="grey")
        self.button.place(x=450, y=290)

        self.button = Button(self.frame, text="Show", font='Courier 15 bold', command=self.show, image=self.image ,width=120,height=120,bg="grey")
        self.button.place(x=650, y=290)
        #self.win.mainloop()

    def logout(self):
        self.root.destroy()
        log = login.LoginWindow()
        log.add_frame()

    def add(self):
        self.session()

    def session(self):
        screen2 = Toplevel()
        screen2.title("Add")
        screen2.configure(background="black")
        self.screen2 = screen2
        # show window in center of the screen
        width = screen2.winfo_screenwidth()
        height = screen2.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        screen2.geometry(str1)

        linfo = Label(screen2, text="Enter your information", font=('courier', 17, 'bold'),fg="yellow green",bg="black")
        linfo.place(x=100, y=40)

        lname = Label(screen2, text="Name*", font=fontm,fg="yellow green",bg="black")
        lname.place(x=70, y=100)

        lname = Label(screen2, text="Type*", font=fontm,fg="yellow green",bg="black")
        lname.place(x=70, y=150)

        lusername = Label(screen2, text="Username", font=fontm,fg="yellow green",bg="black")
        lusername.place(x=70, y=200)

        lemail = Label(screen2, text="Email*", font=fontm,fg="yellow green",bg="black")
        lemail.place(x=70, y=250)

        lpassword = Label(screen2, text="Password*", font=fontm,fg="yellow green",bg="black")
        lpassword.place(x=70, y=300)

        lurl = Label(screen2, text="URL", font=fontm,fg="yellow green",bg="black")
        lurl.place(x=70, y=350)

        lbl = Label(screen2, text="* Marked Fields are Mandatory", font=('courier', 9, 'bold'),fg="yellow green",bg="black")
        lbl.place(x=200, y=470)

        #****Entrys****



        self.name_text = Entry(screen2, font=fontm,fg="yellow green",bg="black")
        self.name_text.place(x=220, y=100)

        self.var = StringVar(screen2)
        self.var.set("Select Option")
       # print(adname.get()+"      ds")
        self.website_text = OptionMenu(screen2, self.var, "Bank", "Social Media", "App", "Other")
        self.website_text.config(font=fontm,fg="yellow green",bg="black")
        self.website_text.place(x=220, y=150)

        self.username_text = Entry(screen2, font=fontm,fg="yellow green",bg="black")
        self.username_text.place(x=220, y=200)

        self.email_text = Entry(screen2, font=fontm,fg="yellow green",bg="black")
        self.email_text.place(x=220, y=250)

        self.password_text = Entry(screen2, font=fontm,fg="yellow green",bg="black",show='*')
        self.password_text.place(x=220, y=300)

        self.url_text = Entry(screen2, font=fontm,fg="yellow green",bg="black")
        self.url_text.place(x=220, y=350)

        self.add_button = Button(screen2, text="Save", font='Courier 15 bold', command=self.validating_name,fg="yellow green",bg="black")
        self.add_button.place(x=250, y=400)

    def validating_name(self):

        # RegexObject = re.compile( Regular expression, flag )
        # Compiles a regular expression pattern into a regular expression object
        regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
                                re.IGNORECASE)
        match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', self.email_text.get(), re.I)

        p = re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')
        m = p.match(self.url_text.get())
        # RegexObject is matched with the desired
        # string using search function
        # In case a match is found, search() returns
        # MatchObject Instance
        # If match is not found, it return None

        res = regex_name.search(self.name_text.get())

        # If match is found, the string is valid
        if res and match and m:
            self.save()

        # If match is not found, string is invalid
        else:
            messagebox.showerror("Invalid","Invalid Name or email address")

    def save(self):
        #db.db.addata()
        self.encrypt = crypto.Encode("allforone",self.password_text.get())
        en = crypto.Encode("allforone",self.encrypt)
        print("encrypted: "+en)
        self.decrypt = crypto.Decode("allforone",en)
        print("decrypted: "+self.decrypt)
        if self.name_text.get() == "" or self.var.get() == "Select Option" or self.password_text.get() == "" or self.email_text.get() == "":
        #if self.name_text.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        #elif (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", self.email_text.get())!= None):
            #messagebox.showerror("Error", "Invalid Email !")


        else:

            #print(cred)

            val = (self.name_text.get(), self.var.get(), self.username_text.get(), self.email_text.get(), self.encrypt, self.url_text.get())
            print(val)
            res = db.db.addata(val)
            if res == False:
                messagebox.showerror("Error", "Not Saved")
            else:
                messagebox.showinfo("Successful Save!","Successful Save!")
            self.screen2.destroy()



    def session2(self):
        screen3 = Toplevel()
        screen3.title("Show")
        screen3.configure(background="Black")
        self.screen3 = screen3
        # show window in center of the screen
        width = screen3.winfo_screenwidth()
        height = screen3.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        #screen3.geometry(str1)
        screen3.geometry("%dx%d+0+0" % (width, height))
        #img2 = ImageTk.PhotoImage(file='images/wall.jpg')
        #label13 = Label(screen3, image=img2)
        #label13.place(x=0, y=0)

        cool = self.showdata()
        #print(self.data[3])


        self.showcase = ttk.Treeview(screen3, columns=(1,2,3,4,5,6,7), show="headings",height="25")
        self.showcase.place(x=50, y=140)
        #showcase.clipboard_get(column="Password")
        self.showcase.heading(1, text="ID")
        self.showcase.heading(2, text="Name")
        self.showcase.heading(3, text="Type")
        self.showcase.heading(4, text="Username")
        self.showcase.heading(5, text="Email")
        self.showcase.heading(6, text="Password")
        self.showcase.heading(7, text="URL")

        self.showcase.column(1, minwidth=0, width=30, stretch=NO)
        self.showcase.column(5, stretch=YES)

        self.showcase.bind('<Double-1>', self.session3)

        #self.showcase.delete(*self.showcase.get_children())
        for i in self.data:
            self.showcase.insert('','end',values=i)

        scrollbar = ttk.Scrollbar(screen3,orient="vertical", command=self.showcase.yview)
        #scrollbar.pack(side=RIGHT, fill="y")
        scrollbar.place(x=1282,y=140,height=518)
        self.showcase.configure(yscrollcommand=scrollbar.set)

        lurl = Label(screen3, text="Search", font=fontm,fg="yellow green",bg="black")
        lurl.place(x=420, y=18)

        self.search_text = Entry(screen3, font=fontm,width=34,fg="yellow green",bg="black")
        self.search_text.place(x=500, y=18)

        self.search_button = Button(screen3, text="Search", font='Courier 15 bold', command=self.search,fg="yellow green",bg="black")
        self.search_button.place(x=900, y=16)
        self.refimg = PhotoImage(file='images/captcha.png')
        self.refresh_button = Button(screen3, text="Refresh", font='Courier 15 bold', command=self.search,fg="yellow green",bg="black")
        self.refresh_button.place(x=1100, y=48)

        self.id = StringVar()
        self.id_text = Entry(screen3, font=fontm, width=9,fg="yellow green",bg="black")
        self.id_text.place(x=480, y=82)
        #self.id = self.id_text.get()
        self.decrypt_label = Label(screen3, text="Enter the ID to decrypt the password", font=fontm,fg="yellow green",bg="black")
        self.decrypt_label.place(x=70, y=85)
        self.dec = StringVar()

        self.decrypt_button = Button(screen3, text="Decrypt", font='Courier 15 bold', command=self.security,fg="yellow green",bg="black")
        self.decrypt_button.place(x=600, y=77)

        self.decrypt_text = Entry(screen3, font=fontm, width=23, textvariable = self.dec,fg="yellow green",bg="black")
        self.decrypt_text.place(x=730, y=82)
        #self.decrypt_text.delete(0, END)
        #self.decrypt_text.insert(0, self.decrypted)






    def show(self):
        print()
        self.session2()

    def security(self):
        if self.id_text.get() == "":
            messagebox.showerror("Error","Enter ID")
        else:
            self.add_frame()

    def decryptt(self):
        try:
            #hell =self.id
            print('input: ' + self.id_text.get())
            idd=self.id_text.get()
            #print(self.decrypt_text.get())
            '''
            connect = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="toor",
                database="test"
            )
            cursorr = connect.cursor()
            '''
            hell = ['qwert','rada','cvvv']
            print(hell[0])
            print("Hello")

            #sql = "SELECT `pasword` FROM datapass WHERE `id` =%s"
            print("qwery" + idd)
            #sql = "SELECT `pasword` FROM datapass WHERE `id` = '%"+self.id_text.get()+"%'"
            #cursor.execute("SELECT pasword FROM datapass WHERE id= %s",hell)
            cursor.execute("select pasword from data where id = "+idd)
            data = cursor.fetchall()
            print(data)
            print(data[0][0])
            #    self.getrow(event)
            total = cursor.rowcount
            #str1 = "[('wqnDkcOYw5LDnsKywqDCoMKY',)]"
            #print("str[1:5] = "+ str(data[3:-4]))


            print(str(data[0]))
            print("Total " + str(total))
            self.decrypted = crypto.Decode("allforone",data[0][0])
            con.commit()
            print(self.decrypted)
            self.dec.set(self.decrypted)

            #self.getrow(event)
            #total = cursor.rowcount

            #print("Total " + str(total))
            
        except mysql.connector.Error as error:
            print("Failed to show " + str(error))
            messagebox.showerror("Enter ID")
            return False

    def session3(self, event):
        screen4 = Toplevel()
        screen4.title("Update | Delete")
        self.screen4 = screen4
        #self.screen2 = screen2
        # show window in center of the screen
        width = screen4.winfo_screenwidth()
        height = screen4.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        screen4.geometry(str1)
        screen4.configure(background="Black")
        linfo = Label(screen4, text="Enter your information", font=('courier', 17, 'bold'),fg="yellow green",bg="black")
        linfo.place(x=100, y=20)

        lid = Label(screen4, text="ID", font=fontm,fg="yellow green",bg="black")
        lid.place(x=70, y=65)

        lname = Label(screen4, text="Name*", font=fontm,fg="yellow green",bg="black")
        lname.place(x=70, y=100)

        lname = Label(screen4, text="Type*", font=fontm,fg="yellow green",bg="black")
        lname.place(x=70, y=150)

        lusername = Label(screen4, text="Username", font=fontm,fg="yellow green",bg="black")
        lusername.place(x=70, y=200)

        lemail = Label(screen4, text="Email*", font=fontm,fg="yellow green",bg="black")
        lemail.place(x=70, y=250)

        lpassword = Label(screen4, text="Password*", font=fontm,fg="yellow green",bg="black")
        lpassword.place(x=70, y=300)

        lurl = Label(screen4, text="URL", font=fontm,fg="yellow green",bg="black")
        lurl.place(x=70, y=350)

        lbl = Label(screen4, text="* Marked Fields are Mandatory", font=('courier', 9, 'bold'), fg="yellow green",
                    bg="black")
        lbl.place(x=200, y=470)

        self.t0 = StringVar()
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        self.t4 = StringVar()
        self.t5 = StringVar()

        # ****Entrys****

        self.id = Entry(screen4, font=fontm, textvariable=self.t1, width=3, state='disabled',fg="yellow green",bg="black")
        self.id.place(x=220, y=65)


        self.name_text1 = Entry(screen4, font=fontm, textvariable=self.t0,fg="yellow green",bg="black")
        self.name_text1.place(x=220, y=100)

        self.var1 = StringVar(screen4)
        self.var1.set("Select Option")
        # print(adname.get()+"      ds")
        self.website_text1 = OptionMenu(screen4, self.var1, "Bank", "Social Media", "App", "Other")
        self.website_text1.config(font=fontm,fg="yellow green",bg="black")
        self.website_text1.place(x=220, y=150)

        self.username_text1 = Entry(screen4, font=fontm, textvariable=self.t2,fg="yellow green",bg="black")
        self.username_text1.place(x=220, y=200)

        self.email_text1 = Entry(screen4, font=fontm, textvariable=self.t3,fg="yellow green",bg="black")
        self.email_text1.place(x=220, y=250)

        self.password_text1 = Entry(screen4, font=fontm, textvariable=self.t4,fg="yellow green",bg="black",show='*')
        self.password_text1.place(x=220, y=300)

        self.url_text1 = Entry(screen4, font=fontm, textvariable=self.t5,fg="yellow green",bg="black")
        self.url_text1.place(x=220, y=350)

        rowid = self.showcase.identify_row(event.y)
        item = self.showcase.item(self.showcase.focus())

        self.t1.set(item['values'][0])
        self.t0.set(item['values'][1])
        self.var1.set(item['values'][2])
        self.t2.set(item['values'][3])
        self.t3.set(item['values'][4])
        self.t4.set(item['values'][5])
        self.t5.set(item['values'][6])

        self.update_button = Button(screen4, text="Update", font='Courier 15 bold', command=self.validating_name1,fg="yellow green",bg="black")
        self.update_button.place(x=150, y=400)

        self.delete_button = Button(screen4, text="Delete", font='Courier 15 bold', command=self.delete_check,fg="yellow green",bg="black")
        self.delete_button.place(x=320, y=400)

    def delete_check(self):
        delete = messagebox.askyesno("Delete", "Are you sure you want to delete?")
        print(delete)
        if delete == True:
            self.delete()
        else:
            print("not deleted")
    def validating_name1(self):

        # RegexObject = re.compile( Regular expression, flag )
        # Compiles a regular expression pattern into a regular expression object
        regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',
                                re.IGNORECASE)
        match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', self.email_text1.get(), re.I)

        p = re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')
        m = p.match(self.url_text1.get())
        # RegexObject is matched with the desired
        # string using search function
        # In case a match is found, search() returns
        # MatchObject Instance
        # If match is not found, it return None

        res = regex_name.search(self.name_text1.get())

        # If match is found, the string is valid
        if res and match and m:
            self.updatee()

        # If match is not found, string is invalid
        else:
            messagebox.showerror("Invalid","Invalid Name or email address")

    def updatee(self):
        # db.db.addata()
        self.encrypt1 = crypto.Encode("allforone", self.password_text1.get())
        en = crypto.Encode("allforone", self.encrypt1)
        print("encrypted: " + en)
        self.decrypt1 = crypto.Decode("allforone", en)
        print("qwertdecrypted: " + self.decrypt1)
        if self.name_text1.get() == "" or self.var1.get() == "Select Option" or self.password_text1.get() == "" or self.email_text1.get() == "":
        # if self.name_text.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            val = (self.name_text1.get(), self.var1.get(), self.username_text1.get(), self.email_text1.get(), self.encrypt1, self.url_text1.get(), self.id.get())
            print(val)
            res = db.db.update(val)
            if res == False:
                messagebox.showerror("Error", "Not Updated")
            else:
                messagebox.showinfo("Successful Update!","Successful Update!")
                self.screen4.destroy()

    def delete(self):

        if self.id.get() == "":
        # if self.name_text.get() == "":
            messagebox.showerror("Error", "Name is required!")
        else:
            val = (self.id.get())
            print(val)
            res = db.db.delete(val)
            if res == False:
                messagebox.showerror("Error", "Not Deleted")
            else:
                messagebox.showinfo("Successful Delete!","Successful Delete!")
                self.screen4.destroy()


    def showdata(self):
        try:
            connectt = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="toor",
                database="test"
            )

            cursorr= connectt.cursor()
            sql = "SELECT id, naame, website, username, email, pasword, url FROM data"
            cursorr.execute(sql)
            self.data = cursorr.fetchall()
            #self.getrow(event)
            total = cursorr.rowcount
            print(self.data)
            print("Total " + str(total))

            # hello = DashboardWindow()
            # hello.show(data)

        except mysql.connector.Error as error:
            print("Failed to show " + str(error))
            messagebox.showerror("Failed to show")
            return False


    def search(self):
        try:
            connectt = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="toor",
                database="test"
            )

            cursorr = connectt.cursor()
            search_data = self.search_text.get()
            query = "SELECT id, naame, website, username, email, pasword, url FROM data WHERE id LIKE '%"+search_data+"%' OR naame LIKE '%"+search_data+"%' OR username LIKE '%"+search_data+"%' OR website LIKE '%"+search_data+"%' OR pasword LIKE '%"+search_data+"%' OR url LIKE '%"+search_data+"%' "
            cursorr.execute(query)
            self.data = cursorr.fetchall()
            self.showcase.delete(*self.showcase.get_children())
            for i in self.data:
                self.showcase.insert('','end',values=i)
        except mysql.connector.Error as error:
            print("Failed to search " + str(error))
            messagebox.showerror("Failed to Search")
            return False

    def add_frame(self):
        frame5 = Toplevel()
        frame5.title("Security Check")
        self.frame5 = frame5
        # self.screen2 = screen2
        # show window in center of the screen
        width = frame5.winfo_screenwidth()
        height = frame5.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "450x400+" + str(x) + "+" + str(y)
        frame5.geometry(str1)
        frame5.configure(background="Black")
        x, y = 70, 20

        self.img = PhotoImage(file='images/login.png')
        self.label = Label(self.frame5, image=self.img,bg="black")
        self.label.place(x = x + 80, y = y + 0)

        #now create a login form
        self.label = Label(self.frame5, text="Login to Decrypt",fg="yellow green",bg="black")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=100, y = y + 150)

        self.emlabel = Label(self.frame5, text="Username",fg="yellow green",bg="black")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y= y + 230)

        self.email = Entry(self.frame5, font='Courier 12',fg="yellow green",bg="black")
        self.email.place(x=200, y= y + 230)

        self.pslabel = Label(self.frame5, text="Password",fg="yellow green",bg="black")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=y+260)

        self.password = Entry(self.frame5,show='*', font='Courier 12',fg="yellow green",bg="black")
        self.password.place(x=200, y=y+260)

        self.button = Button(self.frame5, text="Login", font='Courier 15 bold',
                             command=self.login,fg="yellow green",bg="black")
        self.button.place(x=170, y=y+305)



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
                messagebox.showinfo("Message", "Successful")
                self.frame5.destroy()

                x = self.decryptt()
            else:
                messagebox.showerror("ALert!", "Wrong username/password")