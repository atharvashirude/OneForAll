from tkinter import *
import login


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
        #x = int(width / 2 - 600 / 2)
        #y = int(height / 2 - 400 / 2)
        #str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(("%dx%d+0+0" % (width_value, height_value)))

        #disable resize of the window
        self.win.resizable(width=False, height=False)

        #change the title of the window
        self.win.title("WELCOME | OnwForAll | ADMINISTRATOR")

    def add_frame(self):
        #create a inner frame
        self.frame = Frame(self.win, height=300, width=450,bg="Black")
        self.frame.place(x=80, y=50)

        x, y = 70, 0

        # place the photo in the frame
        # you can find the images from flaticon.com site
        self.img = PhotoImage(file='images/images.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+50, y=y+33)

        self.labeltitle = Label(self.frame, text="OneForAll",bg="black",fg='white')
        self.labeltitle.config(font=("Courier", 17, 'bold'))
        self.labeltitle.place(x=175, y=0)

        self.button = Button(self.frame, text="Continue", font=('helvetica', 20, 'underline italic')
                             , bg='dark green', fg='white', command=self.login)
        self.button.place(x=x+95, y=y+250)

        self.win.mainloop()

    #open a new window on button press
    def login(self):
        # destroy current window
        self.win.destroy()

        #open the new window
        log = login.LoginWindow()
        log.add_frame()


if __name__ == "__main__":
    x = WelcomeWindow()
    x.add_frame()
