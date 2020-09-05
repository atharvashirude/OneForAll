
from tkinter import *
from tkinter import ttk
from PIL import Jpeg2KImagePlugin
from tkinter import messagebox
import Add
import hashlib
import os
import encode
import List
import Search


LARGE_FONT = ("Courier", 15,"bold")
BUTTON_FONT = ("Courier", 10, "bold")


class Login(Tk):
    """docstring for Login"""

    def __init__(self, *args):
        Tk.__init__(self, *args)

        if os.name == 'nt':
            Tk.iconbitmap(self, default='icon.ico')
        Tk.wm_title(self, "Password Manager")
        self.state = {
            "text": "Login to access password database.", "val": False
        }

        if encode.password:
            self.addLoginFrame()
        else:
            self.addRegisterFrame()

        # Adding frames

    def addLoginFrame(self, *kwargs):
        login = Frame(self, padx=30, pady=50, bd=40)
        login.place(x=370,y=200)

        loginLabel = Label(login, text=self.state['text'], bd=10, font=LARGE_FONT, width=40)
        loginLabel.grid(row=0, columnspan=3)

        entry = ttk.Entry(login, show="*")
        entry.grid(row=2, column=1, pady=3)
        # _ marks an unused variable; used for lambda compatibility
        # Bind event for when enter is pressed in the Entry
        entry.bind('<Return>', lambda _: self.checkPwd(
            login, label=loginLabel, entry=entry, btn=submitBtn))
        entry.focus_set()

        s = ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT)
        submitBtn = ttk.Button(login, text="Submit", style="Submit.TButton",
                               command=lambda: self.checkPwd(
                                   login, label=loginLabel, entry=entry,
                                   btn=submitBtn))

        submitBtn.place(x=200,y=100)

    """Kwargs = loginLabel, password entry, and submit button"""
    def checkPwd(self, frame, **kwargs):
        chk = kwargs['entry'].get()
        # if passwords match
        if encode.password == encode.password:
            self.addConfigBtn(frame)

            self.state['text'] = "Welcome! !"
            self.state['val'] = True
            # Using .config() to modift the args
            kwargs['label'].config(text=self.state['text'])
            kwargs['entry'].config(state=DISABLED)
            kwargs['btn'].config(state=DISABLED)

            # adding buttons


        # If passwords don't match
        else:
            messagebox.showerror("Ohh noooo!!", "Try again!")

    def addConfigBtn(self, login):
        # configured buttons
        # btnList = (addBtn, listBtn, getBtn)
        register = Frame(self, padx=2, pady=2, bd=2)
        register.pack()
        # Creating temp references to images using temp1,2,3 so as to disallow
        # garbage collection problems
        btnList = ["Add", "List", "Search"]
        btnCmdList = [lambda: Add.AddWindow(self),
                      lambda: List.ListWindow(self),
                      lambda: Search.SearchWindow(self)]
        f = []  # Frames array
        img = []  # image array
        self.temp = []  # temp array

        for i in range(3):
            f.append(Frame(login, padx=2, width=50, height=50))
            f[i].grid(row=3, column=i)
            img.append(PhotoImage(
                file=btnList[i] + ".gif", width=48, height=48))
            self.temp.append(img[i])
            ttk.Button(f[i], image=img[i], text=btnList[i], compound="top",
                       style="Submit.TButton",
                       command=btnCmdList[i]).grid(sticky="NWSE")

    def addRegisterFrame(self, *arg):
        register = Frame(self, padx=2, pady=2, bd=2)
        register.pack()

        info = "Register with a password\nTo start using the manager"
        registerLabel = Label(register, text=info,
                              bd=10, font=LARGE_FONT, width=30)
        registerLabel.grid(row=0, columnspan=3)

        entry = ttk.Entry(register, show="*")
        entry.grid(row=1, column=1, pady=3)
        entry.focus_set()

        entryChk = ttk.Entry(register, show="*")
        entryChk.grid(row=2, column=1, pady=3)
        entryChk.bind('<Return>', lambda _: self.register(register,
                                                          entry, entryChk))

        s = ttk.Style()
        s.configure("Submit.TButton", font=BUTTON_FONT)
        submitBtn = ttk.Button(register, text="Register",
                               style="Submit.TButton",
                               command=lambda: self.register(register,
                                                             entry, entryChk))
        submitBtn.grid(row=3, column=1, pady=3)

    def register(self, frame, *pwd):
        # pwd is a list containing password inputs
        if pwd[0].get() == pwd[1].get():
            #encode('utf-8')
            encode.password = "1234"
            # Saving password for future use.
            open(".pwd", "w").write(encode.password)

            frame.destroy()
            self.addLoginFrame()
        else:
            error = "Passwords dont match!!\nTry again."
            errorLabel = Label(frame, text=error,
                               bd=10, font=("Verdana", 11), fg="red")
            errorLabel.grid(row=4, column=1, pady=3)

            # Removing previosly entered Passwords
            for wid in pwd:
                wid.delete(0, 'end')

if __name__ == '__main__':
    new = Login()

    new.title("One For All")
    ITitle = Label(new, bd=1, relief=GROOVE, font=('ubuntu', 50, 'bold'), bg="Black", fg="White",
                   text=' OneForAll ')
    ITitle.place(x=475, y=40)
    width_value = new.winfo_screenwidth()
    height_value = new.winfo_screenheight()
    new.geometry("%dx%d+0+0" % (width_value, height_value))  # Full Screen
    new.configure(background='Grey')
    new.mainloop()
