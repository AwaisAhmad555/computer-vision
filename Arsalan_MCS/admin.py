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


        # Background Image

        self.background = ImageTk.PhotoImage(file="background_0.jpg")
        background = Label(self.root,image=self.background).place(x=250,y=0,relwidth=1,relheight=1)



        # Left image

        self.left_image = Image.open("hand.jpg")
        self.new_left_image = self.left_image.resize((400, 665))
        self.left_image = ImageTk.PhotoImage(self.new_left_image)
        background = Label(self.root, image=self.left_image).place(x=80, y=20, width=400, height=665)


        self.return_value = 0
        # back navigation image

        #self.back_image = ImageTk.PhotoImage(file="back.png")
        self.back_image = Image.open("back.png")
        self.new_back_image = self.back_image.resize((30,30))
        self.back_image = ImageTk.PhotoImage(self.new_back_image)

        back_btn = Button(self.root,image=self.back_image,bd=0,cursor="hand2", command= self.back_function).place(x=20, y=20, width=30, height=30)


        # Registration frame

        registration_frame = Frame(self.root,bg="white")

        registration_frame.place(x=480,y=20,width=700,height=665)

        # Title

        title = Label(registration_frame,text="REGISTER NEW CAR INFORMATION !", font=("Comic Sans MS", 20, "bold"), bg="white", fg="green").place(x=50,y=20)


        # Registration_No

        registration_no = Label(registration_frame, text="registration_no", font=("Comic Sans MS", 15, "bold"), bg="white",
                      fg="black").place(x=50, y=80)

        self.registration_no_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.registration_no_txt.place(x=50,y=120,width=250)

        # Engine_Number

        engine_number = Label(registration_frame, text="engine_number", font=("Comic Sans MS", 15, "bold"), bg="white",
                           fg="black").place(x=370, y=80)

        self.engine_number_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.engine_number_txt.place(x=370,y=120,width=250)

        #Model

        model = Label(registration_frame, text="model", font=("Comic Sans MS", 15, "bold"), bg="white",
                           fg="black").place(x=50, y=160)

        self.model_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.model_txt.place(x=50, y=200, width=250)

        # Registration_Date

        registration_date = Label(registration_frame, text="registration_date", font=("Comic Sans MS", 15, "bold"),
                               bg="white",
                               fg="black").place(x=370, y=160)

        self.registration_date_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.registration_date_txt.place(x=370, y=200, width=250)


        # Security Question

       # security_question = Label(registration_frame, text="Security Question", font=("Comic Sans MS", 15, "bold"),
                     # bg="white",
                     # fg="black").place(x=50, y=250)


       # self.security_question_txt = ttk.Combobox(registration_frame,font=("Comic Sans MS", 12),state="readonly", justify=CENTER)
        #self.security_question_txt["values"] = ("Select", "Your favorite food","Your Birth Place","Your High School Name")
        #self.security_question_txt.current(0)
       # self.security_question_txt.place(
            #x=50, y=290, width=250)

        # Security Answer

        chassis_number = Label(registration_frame, text="chassis_number", font=("Comic Sans MS", 15, "bold"),bg="white",fg="black").place(x=370, y=580)

        self.chassis_number_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.chassis_number_txt.place(x=370, y=620, width=250)

        #Token_Paid

        token_paid = Label(registration_frame, text="token_paid", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=50, y=240)

        self.token_paid_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.token_paid_txt.place(x=50, y=280, width=250)



        # Owner_Name

        owner_name = Label(registration_frame, text="owner_name", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=370, y=240)

        self.owner_name_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.owner_name_txt.place(x=370, y=280, width=250)

        #####
        #Color

        color = Label(registration_frame, text="color", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=370, y=320)

        self.color_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.color_txt.place(x=370, y=360, width=250)

        ########
        # Company

        company = Label(registration_frame, text="company", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=50, y=320)

        self.company_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.company_txt.place(x=50, y=360, width=250)

        ########
        # Fuel_Type

        fuel_type = Label(registration_frame, text="fuel_type", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=370, y=400)

        self.fuel_type_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.fuel_type_txt.place(x=370, y=440, width=250)

        ###############

        #Engine_Capacity

        engine_capacity = Label(registration_frame, text="engine_capacity", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=50, y=400)

        self.engine_capacity_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.engine_capacity_txt.place(x=50, y=440, width=250)

        ##################
        # Vehicle_price

        vehicle_price = Label(registration_frame, text="vehicle_price", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=370, y=490)

        self.vehicle_price_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.vehicle_price_txt.place(x=370, y=530, width=250)
        ####################

        # Latest_payment_details

        latest_payment_details = Label(registration_frame, text="latest_payment_details", font=("Comic Sans MS", 15, "bold"),
                         bg="white",
                         fg="black").place(x=50, y=490)

        self.latest_payment_details_txt = Entry(registration_frame, font=("Comic Sans MS", 12), bg="lightgray")
        self.latest_payment_details_txt.place(x=50, y=530, width=250)




        # terms and conditions


       # self.check_variable = IntVar()

        #self.checkbox = Checkbutton(registration_frame,text="I Agreed the terms and Conditions !", variable= self.check_variable, onvalue = 1, offvalue = 0,  bg="white", font=("Comic Sans MS", 12))
        #self.checkbox.place(x=50,y=405)



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

        register_btn = Button(registration_frame,image=self.button_image,bd=0,cursor="hand2",command=self.main_function).place(x=50,y=590,width=150,height=50)





        pass


    def main_function(self):


        registration_no = self.registration_no_txt.get()
        chassis_number = self.chassis_number_txt.get()
        engine_number = self.engine_number_txt.get()
        model =  self.model_txt.get()
        registration_date = self.registration_date_txt.get()
        token_paid =  self.token_paid_txt.get()
        owner_name = self.owner_name_txt.get()
        #confirm_password = self.confirm_password_txt.get()
        color = self.color_txt.get()
        company = self.company_txt.get()
        fuel_type = self.fuel_type_txt.get()
        engine_capacity = self.engine_capacity_txt.get()
        vehicle_price = self.vehicle_price_txt.get()
        latest_payment_details = self.latest_payment_details_txt.get()


        if(latest_payment_details == "" or vehicle_price == "" or engine_capacity == "" or fuel_type == "" or  company == "Select" or color == "" or owner_name == ""  or token_paid == "" or registration_date == ""or model == ""or engine_number == ""or chassis_number == ""or registration_no == ""):


            messagebox.showerror(title="Alert", message="Please Enter All required Information !")



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

                    # checking if user already exists in database

                    cursor.execute(query="SELECT * from car_detail where Registration_No =%s",
                                   args=self.registration_no_txt.get())

                    row = cursor.fetchone()

                    if row != None:

                        messagebox.showerror(title="Alert", message="License number already existed ! Please try another one")

                        pass

                    else:

                        insert_query = "INSERT INTO car_detail(registration_no, chassis_number, engine_number, model, registration_date, token_paid, owner_name, color, company,fuel_type, engine_capacity, vehicle_price, latest_payment_details) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (
                    registration_no, chassis_number, engine_number, model, registration_date, token_paid, owner_name,
                    color, company, fuel_type, engine_capacity, vehicle_price, latest_payment_details)

                    cursor.execute(insert_query, values)

                    connection.commit()
                    connection.close()

                    # print("1 record inserted, ID:", cursor.lastrowid)

                    messagebox.showinfo(title="Success", message="Registration Successful !")

                    # clearing text fields
                    self.registration_no_txt.delete(0, END)
                    self.chassis_number_txt.delete(0, END)
                    self.engine_number_txt.delete(0, END)
                    self.model_txt.delete(0, END)
                    self.registration_date_txt.delete(0, END)
                    self.owner_name_txt.delete(0, END)
                    self.color_txt.delete(0, END)
                    self.company_txt.delete(0, END)
                    self.fuel_type_txt.delete(0, END)
                    self.engine_capacity_txt.delete(0, END)
                    self.vehicle_price_txt.delete(0, END)
                    self.latest_payment_details_txt.delete(0, END)
                    self.token_paid_txt.delete(0, END)

                    pass

                    # print("connection successful")

                    # pass

                except Exception as exp:

                    messagebox.showerror("", f"Error : {str(exp)}", parent=self.root)

                    pass

                pass


            pass



        pass

    def back_function(self):


        self.root.destroy()

        self.return_value = 1



        pass

    pass


def main_function():

    root = Tk()

    register_object = Register(root=root)
    root.mainloop()

    number = register_object.return_value

    if number == 1:

        from Arsalan_MCS.dashboard import main_program

        main_program()


        pass



    pass


