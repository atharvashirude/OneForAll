from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class Loginn:
    def __init__(self, root):

        self.root = root
        self.root.title("One For All")

        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value)) #Full Screen
        self.root.configure(background='grey')

        #---Variables---
        self.username = StringVar()
        self.password = StringVar()

        #---Images---
        self.background_image = ImageTk.PhotoImage(file="wall.jpg")
        self.LockImage = ImageTk.PhotoImage(file="paslock.jpeg")

        background_label = Label(self.root, image=self.background_image).pack()

        ITitle = Label(self.root, bd=1, relief=GROOVE, font=('Courier', 50, 'bold'), bg="Black", fg="White", text=' OneForAll ')
        ITitle.place(x=500, y=40)

        Frame1 = Frame(self.root, bg="grey")
        Frame1.place(x=100, y=210)
        Lock_Label = Label(Frame1, image=self.LockImage).grid(row=0, column=0, pady=0)

        username_label = Label(self.root, text="Username", font=('Courier', 15, 'bold'), bg="Black", fg="White")
        username_label.place(x=650, y=260)

        username_text = Entry(self.root, textvariable=self.username, font=('Courier', 15, 'bold italic'), bg="Black", fg="White")
        username_text.place(x=800, y=260)

        Password_Label = Label(self.root, text="Password", font=('Courier', 15, 'bold'), bg="Black", fg="White")
        Password_Label.place(x=650, y=400)

        password_text = Entry(self.root, textvariable=self.password, font=('Courier', 15, 'bold'), bg="Black", fg="White")
        password_text.place(x=800, y=400)
        password_text.config(show="*")

        login_button = Button(self.root, text="Login", command=self.Login, font=('Courier', 15, 'bold'), bg="Black", fg="White")
        login_button.place(x=780, y=500)

    def Login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Lol", "All fields are required!")
        elif self.username.get() == "Bond" and self.password.get() == "007":
            messagebox.showinfo("Successful Login!", "Welcome !")

        else:
            messagebox.showerror("Ohh noooo!!", "Invalid Username or Password!")

    def session(self):
        screen2 = Toplevel(root)
        screen2.title("OneForAll")
        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        screen2.geometry("%dx%d+0+0" % (width_value, height_value))

    def login_success(self):
        session()

root = Tk()
obj = Loginn(root)
root.mainloop()
