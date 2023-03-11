from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox, dialog
from tkinter import font
import pymysql
#from numpy.distutils.log import Log



class Login:

    def __init__(self,root):

        self.root = root
        self.root.title = "Registration Form"
        self.root.geometry("1350x700+0+0")

        self.return_value = 0

        # Background Image

        self.background_image = Image.open("background_0.jpg")
        self.background_image = self.background_image.resize((1350, 700))

        self.background = ImageTk.PhotoImage(self.background_image)
        background = Label(self.root,image=self.background).place(x=0,y=0,relwidth=1,relheight=1)


        # title

        title = Label(self.root, text="Wellcome To HandWritten Digits Classification System",
                      font=("Comic Sans MS", 18, "bold"), bd=10, bg="silver",
                      fg="MediumSeaGreen").place(x=30, y=30)



        # Registration frame

        registration_frame = Frame(self.root,bg="white")

        registration_frame.place(x=230,y=95,width=900,height=590)

        # Title

        title = Label(registration_frame,text="SELECT OPTION", font=("Comic Sans MS", 20, "bold"), bg="white", fg="MediumSeaGreen").place(x=320,y=40)



        self.Login_image = Image.open("assets\\user_icon.jpg")
        self.new_Login_image = self.Login_image.resize((120, 120))
        self.Login_image = ImageTk.PhotoImage(self.new_Login_image)

        login_btn = Button(registration_frame,image=self.Login_image, text="Login", font=("Comic Sans MS", 14), bg="#4CAF50",bd=0,cursor="hand2",command=self.login_function).place(x=500,y=200,width=200,height=200)

        login_text = Label(registration_frame,text="Login", font=("Comic Sans MS", 16, "bold"),bg="white", fg="black").place(x=570,y=420)

        self.Register_image = Image.open("assets\\edit_list_image.png")
        self.new_Register_image = self.Register_image.resize((120, 120))
        self.Register_image = ImageTk.PhotoImage(self.new_Register_image)

        register_btn = Button(registration_frame, image= self.Register_image, text="Register", font=("Comic Sans MS", 14), bg="#008CBA", bd=0, cursor="hand2",
                              command=self.register_function).place(x=200, y=200, width=200, height=200)

        register_text = Label(registration_frame, text="Registration", font=("Comic Sans MS", 16, "bold"), bg="white",
                           fg="black").place(x=235, y=420)

        pass

    def login_function(self):

        self.return_value = 1

        self.root.destroy()

        pass

    def register_function(self):


        self.return_value = 2

        self.root.destroy()


        pass

    def return_function(self):


        #print(self.return_value)


        return self.return_value
        pass

    pass


def first_form_main():

    root = Tk()

    Login_object = Login(root=root)

    root = mainloop()

    number = Login_object.return_function()

    # print(number)

    if number == 2:

        from Arsalan_MCS.Registration_Window import registration_function

        registration_function()

        pass

    elif number == 1:


        from Arsalan_MCS.Login_Window import Login_main

        Login_main()

        pass


    pass

"""if Login_object.return_value == 1:

    #main_program()


    pass"""




first_form_main()
