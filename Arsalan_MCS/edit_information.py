from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox, dialog
from tkinter import font
import pymysql
import tkinter

class Register:

    def __init__(self,root):

        rows = self.license_plate_names()

        rows = list(rows)

        rows.insert(0,["Select"])



        for i in range(len(rows)):

            rows[i] = rows[i][0]

            pass


        #print(rows)


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

        title = Label(registration_frame,text="EDIT CAR INFORMATION !", font=("Comic Sans MS", 20, "bold"), bg="white", fg="green").place(x=50,y=20)


        # Registration_No

        registration_no = Label(registration_frame, text="registration_no", font=("Comic Sans MS", 15, "bold"), bg="white",
                      fg="black").place(x=50, y=80)


        self.registration_no_txt = ttk.Combobox(registration_frame, font=("Comic Sans MS", 12), state="readonly",
                                             justify=CENTER)

        self.registration_no_txt["values"] = rows
        self.registration_no_txt.current(0)
        self.registration_no_txt.place(
            x=50, y=120, width=250)


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



                                             # SEARCH BUTTON

        btn_search = Button(registration_frame, text="Search", font=("Comic Sans MS", 15), bg="#008CBA",
                                             bd=0,command=self.search,
                                             cursor="hand2").place(x=50, y=590)


                                             # UPDATE BUTTON
        btn_update = Button(registration_frame, text="Update", font=("Comic Sans MS", 15), bg="#4CAF50", bd=0,
                           command = self.main_function,cursor="hand2").place(x=138, y=590)


                                             # DELETE BUTTON
        btn_delete = Button(registration_frame, text="Delete", font=("Comic Sans MS", 15), bg="#f44336", bd=0,
                            command=self.delete_information,cursor="hand2")

        btn_delete.place(x=225, y=590)




        pass


                                # LOADING LICENSE PLATE NUMBERS FUNCTION

    def license_plate_names(self):

        rows = []

        try:
            connection = pymysql.connect(host="localhost",
                                         user="root",
                                         password="",
                                         database="test",
                                         port=3306
                                         )

            cursor = connection.cursor()

            cursor.execute(query="SELECT Registration_No FROM car_detail")

            rows = cursor.fetchall()

            #print(rows)

            # self.tree.insert("", tkinter.END, values=rows)

            connection.close()

            pass

        except Exception as exp:

            #messagebox.showerror("Alert", str(exp))

            pass


        return rows
        pass



                           # SEARCHING INFORMATION FUNCTION

    def search(self):


        try:
            connection = pymysql.connect(host="localhost",
                                         user="root",
                                         password="",
                                         database="test",
                                         port=3306
                                         )

            cursor = connection.cursor()

            license_plate_number = self.registration_no_txt.get()

            cursor.execute(query="SELECT * FROM car_detail where Registration_No = %s",args=license_plate_number)

            rows = cursor.fetchone()

            rows = rows[1:]


            # INSERTING rows VALUES IN VARIABLES

            chassis_number = rows[1]
            engine_number = rows[2]
            model = rows[3]
            registration_date = rows[4]
            token_paid = rows[5]
            owner_name = rows[6]
            color = rows[7]
            company = rows[8]
            fuel_type = rows[9]
            engine_capacity = rows[10]
            vehicle_price = rows[11]
            latest_payment_details = rows[12]


            # INSERTING VALUES IN TEXT FIELDS


            self.chassis_number_txt.delete(0, END)
            self.chassis_number_txt.insert(0, chassis_number)


            self.engine_number_txt.delete(0, END)
            self.engine_number_txt.insert(0, engine_number)


            self.model_txt.delete(0, END)
            self.model_txt.insert(0, model)


            self.registration_date_txt.delete(0, END)
            self.registration_date_txt.insert(0, registration_date)


            self.owner_name_txt.delete(0, END)
            self.owner_name_txt.insert(0, owner_name)


            self.color_txt.delete(0, END)
            self.color_txt.insert(0, color)


            self.company_txt.delete(0, END)
            self.company_txt.insert(0, company)


            self.fuel_type_txt.delete(0, END)
            self.fuel_type_txt.insert(0, fuel_type)


            self.engine_capacity_txt.delete(0, END)
            self.engine_capacity_txt.insert(0, engine_capacity)


            self.vehicle_price_txt.delete(0, END)
            self.vehicle_price_txt.insert(0, vehicle_price)


            self.latest_payment_details_txt.delete(0, END)
            self.latest_payment_details_txt.insert(0, latest_payment_details)


            self.token_paid_txt.delete(0, END)
            self.token_paid_txt.insert(0, token_paid)



            # self.tree.insert("", tkinter.END, values=rows)

            connection.close()

            pass

        except Exception as exp:

            messagebox.showerror("Alert", str(exp))

            pass


        pass



                                        # UPDATE RECORD FUNCTION

    def main_function(self):


        registration_no = self.registration_no_txt.get()
        chassis_number = self.chassis_number_txt.get()
        engine_number = self.engine_number_txt.get()
        model =  self.model_txt.get()
        registration_date = self.registration_date_txt.get()
        token_paid =  self.token_paid_txt.get()
        owner_name = self.owner_name_txt.get()
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

            answer = messagebox.askyesnocancel("Confirmation", "Continue To UPDATE Using Given information?")

            if answer == TRUE:

                try:

                    connection = pymysql.connect(host="localhost",
                                                 user="root",
                                                 password="",
                                                 database="test",
                                                 port=3306
                                                 )

                    cursor = connection.cursor()


                    insert_query = "UPDATE car_detail SET  chassis_number = %s, engine_number = %s, model = %s, registration_date = %s, token_paid = %s, owner_name = %s, color = %s, company = %s ,fuel_type = %s, engine_capacity = %s, vehicle_price = %s, latest_payment_details = %s WHERE registration_no = %s"

                    values = (chassis_number, engine_number, model, registration_date, token_paid, owner_name,
                    color, company, fuel_type, engine_capacity, vehicle_price, latest_payment_details,registration_no)

                    cursor.execute(insert_query, values)

                    connection.commit()
                    connection.close()

                    # print("1 record inserted, ID:", cursor.lastrowid)

                    messagebox.showinfo(title="Success", message="Record Updated Successfully !")

                    # clearing text fields
                    """self.registration_no_txt.delete(0, END)
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
                    self.token_paid_txt.delete(0, END)"""

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

                            # SEARCHING INFORMATION FUNCTION

    def delete_information(self):

        answer = messagebox.askyesnocancel("Confirmation", "DELETE the Given information?")

        if answer == TRUE:

            try:
                connection = pymysql.connect(host="localhost",
                                             user="root",
                                             password="",
                                             database="test",
                                             port=3306
                                             )

                cursor = connection.cursor()

                license_plate_number = self.registration_no_txt.get()

                cursor.execute(query="DELETE FROM car_detail where Registration_No = %s", args=license_plate_number)


                connection.commit()
                connection.close()

                messagebox.showinfo("Message","Record Deleted !")


                # REMOVING DELETED LICENSE PLATE FROM DROP DOWN MENU


                rows = self.license_plate_names()

                rows = list(rows)

                rows.insert(0, ["Select"])

                for i in range(len(rows)):

                    rows[i] = rows[i][0]

                    pass

                self.registration_no_txt.delete(0,END)

                self.registration_no_txt["values"] = rows

                self.registration_no_txt.current(0)

                pass

            except Exception as ex:

                messagebox.showerror("Alert !",str (ex))

                pass


            pass





        pass

                       # Main class ended here

    pass



############################ Main program ##############################


def edit_information_main_function():

    root = Tk()

    register_object = Register(root=root)
    root.mainloop()

    number = register_object.return_value

    if number == 1:

        from Arsalan_MCS.dashboard import main_program

        main_program()


        pass



    pass


#edit_information_main_function()
