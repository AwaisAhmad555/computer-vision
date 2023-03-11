from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox, dialog
from tkinter import font
import pymysql


class Register:

    def __init__(self,root):

        self.root = root
        self.root.title = "Registration Form"
        self.root.geometry("1350x700+0+0")

        self.flag = 0

        # Background Image

        self.background = ImageTk.PhotoImage(file="background_0.jpg")
        background = Label(self.root,image=self.background).place(x=250,y=0,relwidth=1,relheight=1)

        # Left image

        self.left_image = ImageTk.PhotoImage(file="hand.jpg")
        background = Label(self.root, image=self.left_image).place(x=80, y=100, width=400, height=500)

        # back navigation image

        #self.back_image = ImageTk.PhotoImage(file="back.png")
        self.back_image = Image.open("back.png")
        self.new_back_image = self.back_image.resize((30,30))
        self.back_image = ImageTk.PhotoImage(self.new_back_image)

        back_btn = Button(self.root,image=self.back_image,bd=0,cursor="hand2",command=self.back_navigation_function).place(x=20, y=20, width=30, height=30)


        # Registration frame

        registration_frame = Frame(self.root,bg="white")

        registration_frame.place(x=480,y=100,width=700,height=500)

        # Title

        title = Label(registration_frame,text="REGISTER NOW", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50,y=20)


        # First name

        first_name = Label(registration_frame, text="First Name", font=("Comic Sans MS", 15, "bold"), bg="white",
                      fg="black").place(x=50, y=70)

        self.first_name_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.first_name_txt.place(x=50,y=110,width=250)

        # Last name

        last_name = Label(registration_frame, text="Last Name", font=("Comic Sans MS", 15, "bold"), bg="white",
                           fg="black").place(x=370, y=70)

        self.last_name_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.last_name_txt.place(x=370,y=110,width=250)

        # Contact Number

        contact_number = Label(registration_frame, text="Contact Number", font=("Comic Sans MS", 15, "bold"), bg="white",
                           fg="black").place(x=50, y=160)

        self.contact_number_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.contact_number_txt.place(x=50, y=200, width=250)

        # Email

        email = Label(registration_frame, text="Email", font=("Comic Sans MS", 15, "bold"),
                               bg="white",
                               fg="black").place(x=370, y=160)

        self.email_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.email_txt.place(x=370, y=200, width=250)


        # Security Question

        security_question = Label(registration_frame, text="Security Question", font=("Comic Sans MS", 15, "bold"),
                      bg="white",
                      fg="black").place(x=50, y=250)


        self.security_question_txt = ttk.Combobox(registration_frame,font=("Comic Sans MS", 12),state="readonly", justify=CENTER)
        self.security_question_txt["values"] = ("Select", "Your favorite food","Your Birth Place","Your High School Name")
        self.security_question_txt.current(0)
        self.security_question_txt.place(
            x=50, y=290, width=250)

        # Security Answer

        security_answer = Label(registration_frame, text="Security Answer", font=("Comic Sans MS", 15, "bold"),
                                  bg="white",
                                  fg="black").place(x=370, y=250)

        self.security_answer_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.security_answer_txt.place(x=370, y=290, width=250)




        # Password

        password = Label(registration_frame, text="Password", font=("Comic Sans MS", 15, "bold"),
                                bg="white",
                                fg="black").place(x=50, y=340)

        self.password_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.password_txt.place(x=50, y=380, width=250)



        # confirm Password

        confirm_password = Label(registration_frame, text="Confirm Password", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=370, y=340)

        self.confirm_password_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.confirm_password_txt.place(x=370, y=380, width=250)




        # terms and conditions


        self.check_variable = IntVar()

        self.checkbox = Checkbutton(registration_frame,text="I Agreed the terms and Conditions !", variable= self.check_variable, onvalue = 1, offvalue = 0,  bg="white", font=("Comic Sans MS", 12))
        self.checkbox.place(x=50,y=405)



        # button

        # Create style Object
        """style = Style()

        style.configure('TButton', font=
        ('calibri', 20, 'bold'),
                        borderwidth='4')

        # Changes will be reflected
        # by the movement of mouse.
        style.map('TButton', foreground=[('active', '!disabled', 'green')],
                  background=[('active', 'black')])"""


        self.button_image = ImageTk.PhotoImage(file="resized.png")

        register_btn = Button(registration_frame,image=self.button_image,bd=0,cursor="hand2",command=self.main_function).place(x=50,y=440,width=150,height=50)





        pass


    def main_function(self):


        first_name = self.first_name_txt.get()
        last_name = self.last_name_txt.get()
        email = self.email_txt.get()
        contact =  self.contact_number_txt.get()
        security_question = self.security_question_txt.get()
        security_answer =  self.security_answer_txt.get()
        password = self.password_txt.get()
        confirm_password = self.confirm_password_txt.get()


        if(first_name == "" or last_name == "" or email == "" or contact == "" or security_question == "Select" or security_answer == "" or password == "" or confirm_password == ""):


            messagebox.showerror(title="Alert", message="Please Enter All required Information !")




            pass
        elif (password !=  confirm_password):

            messagebox.showerror(title="Alert", message="Password and Confirm password must be matched !")

            pass

        elif(self.check_variable.get() == 0):

            messagebox.showerror(title="Alert", message="Please confirm our terms and conditions !")

            pass

        else:

            answer = messagebox.askyesnocancel("Confirmation", "Continue To register Using entered information?")

            if answer == TRUE:


                try:

                    connection = pymysql.connect(host="localhost",
                                                 user="root",
                                                 password="",
                                                 database="test",
                                                 port=3306
                                                 )

                    cursor = connection.cursor()

                    #checking if user already exists in database

                    cursor.execute(query="SELECT * from registration where email =%s",args=self.email_txt.get())

                    row = cursor.fetchone()

                    if row != None:

                        messagebox.showerror(title="Alert",message="User already existed ! Please try another email")

                        pass

                    else:

                        insert_query = "INSERT INTO registration(f_name,l_name,contact,email,question,answer,password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                        values = (first_name, last_name, contact, email, security_question, security_answer, password)

                        cursor.execute(insert_query, values)

                        connection.commit()
                        connection.close()

                        # print("1 record inserted, ID:", cursor.lastrowid)

                        messagebox.showinfo(title="Success", message="Registration Successful !")

                        #clearing text fields
                        self.first_name_txt.delete(0, END)
                        self.last_name_txt.delete(0, END)
                        self.email_txt.delete(0, END)
                        self.contact_number_txt.delete(0, END)
                        self.security_question_txt.current(0)
                        self.security_answer_txt.delete(0, END)
                        self.password_txt.delete(0, END)
                        self.confirm_password_txt.delete(0, END)



                        pass


                    #print("connection successful")



                    pass

                except Exception as exp:


                    messagebox.showerror("", f"Error : {str(exp)}",parent=self.root)


                    pass


                pass



            pass



        pass


    def back_navigation_function(self):


        self.root.destroy()
        self.flag = 1


        pass

    def return_function(self):


        return self.flag
        pass

    pass

"""root = Tk()

register_object = Register(root=root)
root.mainloop()"""

def registration_function():

    root = Tk()

    register_object = Register(root=root)
    root.mainloop()

    number = register_object.return_function()

    if number == 1:

        from Arsalan_MCS.first_form import first_form_main

        first_form_main()

        pass


    pass
