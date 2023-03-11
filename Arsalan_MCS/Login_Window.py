from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox, dialog
from tkinter import font
import pymysql
from numpy.distutils.log import Log



class Login:

    def __init__(self,root):

        self.root = root
        self.root.title = "Login Form"
        self.root.geometry("1350x700+0+0")

        self.return_value = 0

        # Background Image

        self.background_image = Image.open("background_0.jpg")
        self.background_image = self.background_image.resize((1350, 700))

        self.background = ImageTk.PhotoImage(self.background_image)
        background = Label(self.root,image=self.background).place(x=0,y=0,relwidth=1,relheight=1)


        # back navigation image

        #self.back_image = ImageTk.PhotoImage(file="back.png")
        self.back_image = Image.open("back.png")
        self.new_back_image = self.back_image.resize((30,30))
        self.back_image = ImageTk.PhotoImage(self.new_back_image)

        back_btn = Button(self.root,image=self.back_image,bd=0,cursor="hand2",command = self.back_function).place(x=20, y=20, width=30, height=30)


        # Registration frame

        registration_frame = Frame(self.root,bg="white")

        registration_frame.place(x=475,y=135,width=400,height=450)

        # Title

        title = Label(registration_frame,text="Log In", font=("Comic Sans MS", 20, "bold"), bg="white", fg="green").place(x=162,y=40)


        # First name

        Email = Label(registration_frame, text="User Email", font=("Comic Sans MS", 15, "bold"), bg="white",
                      fg="black").place(x=75, y=120)

        self.email_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.email_txt.place(x=75,y=160,width=250)




        # Password

        password = Label(registration_frame, text="Password", font=("Comic Sans MS", 15, "bold"),
                                bg="white",
                                fg="black").place(x=75, y=230)

        self.password_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.password_txt.place(x=75, y=270, width=250)






        # terms and conditions


        #self.forget_password_label = Label(registration_frame, text="Forget Password !",  bg="white", font=("Comic Sans MS", 12))
        #self.forget_password_label.place(x=127,y=410)


        self.button_image = ImageTk.PhotoImage(file="resized.png")

        #register_btn = Button(registration_frame,image=self.button_image,bd=0,cursor="hand2",command=self.main_function).place(x=50,y=440,width=150,height=50)

        #image=self.button_image

        register_btn = Button(registration_frame, text="Login", font=("Comic Sans MS", 14), bg="#4CAF50", bd=0, command=self.login_function, cursor="hand2",
                              ).place(x=120, y=340, width=150, height=50)

        pass

    def login_function(self):

        email = self.email_txt.get()
        password = self.password_txt.get()

        try:

            connection = pymysql.connect(host="localhost",
                                         user="root",
                                         password="",
                                         database="test",
                                         port=3306
                                         )

            cursor = connection.cursor()

            # checking if user already exists in database

            cursor.execute(query="SELECT * FROM registration WHERE email = %s AND password = %s", args=(self.email_txt.get(),self.password_txt.get()))

            row = cursor.fetchone()

            connection.close()

            if row != None:

                response = messagebox.askokcancel(title="Success", message="Login Successful !")

                if response == 1:

                    #main_program()

                    self.root.destroy()

                    self.return_value = 1


                    pass

                pass

            else:

                messagebox.showerror(title="Alert", message="Login failed ! please enter valid email or password")


                # print("1 record inserted, ID:", cursor.lastrowid)


                pass

            # print("connection successful")

            pass

        except Exception as exp:

            messagebox.showerror("", f"Error : {str(exp)}", parent=self.root)

            pass




        pass

    def back_function(self):

        self.root.destroy()

        self.return_value = 2


        pass

    def return_function(self):


        return self.return_value
        pass

    pass


def Login_main():


    root = Tk()

    Login_object = Login(root=root)

    root = mainloop()

    if Login_object.return_value == 1:

        from Arsalan_MCS.dashboard import main_program
        main_program()

        pass
    elif Login_object.return_value == 2:

        from Arsalan_MCS.first_form import first_form_main
        first_form_main()

        pass




    pass




