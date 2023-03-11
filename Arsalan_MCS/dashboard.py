from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import cv2 as opencv
import pymysql

class Dashboard:

   def __init__ (self,root):
       self.root = root
       self.root.title("Take a photo or select an image")
       self.root.geometry("1350x700+0+0")

       self.flag = 0

       #self BG image
       self.bg = ImageTk.PhotoImage(file = "assets\\pic3.jpg")
       bg = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       title = Label(self.root, text="Welcome To HandWritten Digits Classification System", font=("Comic Sans MS", 18, "bold"),bd=10, bg="silver",
                     fg="MediumSeaGreen").place(x=80, y=10)
       #ReGiSTER FRAME
       frame1 = Frame(self.root,bg="Aliceblue")
       frame1.place(x=120,y=80,width=1100,height=610)
       title = Label(frame1,text="Select from Following !",font=("Comic Sans MS",18,"bold"),bd=10,bg="Lavender",fg="#F96167").place(x=400,y=30)



       #

       self.return_value = 0
       # back navigation image

       # self.back_image = ImageTk.PhotoImage(file="back.png")
       self.back_image = Image.open("back.png")
       self.new_back_image = self.back_image.resize((30, 30))
       self.back_image = ImageTk.PhotoImage(self.new_back_image)

       back_btn = Button(self.root, image=self.back_image, bd=0, cursor="hand2", command=self.back_function).place(x=20,
                                                                                                                   y=20,
                                                                                                                   width=30,
                                                                                                                   height=30)

       #


       background_image = opencv.imread("assets\\camera2.jpg")

       background_image = opencv.resize(background_image,(225,100))

       #opencv.imwrite("assets\\btn_bgd.jpg",img=background_image)

       #self.btn_cam =ImageTk.PhotoImage(file="assets\\btn_bgd.jpg")

       image = Image.open('assets\\upload.jpg')
       # The (450, 350) is (height, width)
       image = image.resize((35,35), Image.ANTIALIAS)

       self.button_bg =ImageTk.PhotoImage(image)

       background_image = opencv.imread("assets\\upload.jpg")
       #self.btn_cam = image.resize((350, 350), Image.ANTIALIAS)

       photo = PhotoImage(file="assets\\ocr (1).png")

       #btn= Button(self.root,image=self.btn_cam, bd=0, cursor="hand2").place(x=870, y=240)


       Label(self.root, text="Hand Digit recognition",
                     font=("Comic Sans MS", 16, "bold"), bd=10, bg="Aliceblue",
                     fg="black").place(x=330, y=387)


       Label(self.root, text="license plate detection",
             font=("Comic Sans MS", 16, "bold"), bd=10, bg="Aliceblue",
             fg="black").place(x=730, y=387)

       Label(self.root, text="Vehicle Information Registration",
             font=("Comic Sans MS", 16, "bold"), bd=10, bg="Aliceblue",
             fg="black").place(x=273, y=632)

       Label(self.root, text="Edit Vehicle Information",
             font=("Comic Sans MS", 16, "bold"), bd=10, bg="Aliceblue",
             fg="black").place(x=710, y=632)



       self.recognition_image = Image.open("assets\\digit_recognition.png")
       self.new_recognition_image = self.recognition_image.resize((120, 120))
       self.recognition_image = ImageTk.PhotoImage(self.new_recognition_image)

       btn_HD_recognition = Button(self.root, image = self.recognition_image, text="Hand Digit recognition", font=("Comic Sans MS", 15),bg="#4CAF50", bd=0, cursor="hand2", command = self.flag_1).place(x=350,y=190, height = 200, width = 200)



       self.license_plate_image = Image.open("assets\\license-plate.png")
       self.new_license_plate_image = self.license_plate_image.resize((120, 120))
       self.license_plate_image = ImageTk.PhotoImage(self.new_license_plate_image)


       btn_license_plate_detection = Button(self.root, image = self.license_plate_image, text="license plate detection", font=("Comic Sans MS", 15), bg="#008CBA", bd=0, command = self.flag_2,
                                   cursor="hand2").place(x=750, y=190, height = 200, width = 200)


       self.registration_image = Image.open("assets\\register.png")


       self.new_registration_image = self.registration_image.resize((120, 120))
       self.registration_image = ImageTk.PhotoImage(self.new_registration_image)


       btn_car_registration = Button(self.root, image = self.registration_image, text="Vehicle Information \nRegistration", font=("Comic Sans MS", 15), bg="#f44336", bd=0,
                                   cursor="hand2", command = self.flag_3).place(x=350, y=440, height = 200, width = 200)


       #

       self.edit_information_image = Image.open("assets\\register.png")

       R,G,B, a = self.edit_information_image.split()

       self.edit_information_image = Image.merge("RGBA",(R,B,B,a))

       self.new_edit_information_image = self.edit_information_image.resize((120, 120))

       self.edit_information_image = ImageTk.PhotoImage(self.new_edit_information_image)


       btn_car_registration = Button(self.root, image=self.edit_information_image,
                                     text="Edit Vehicle Information", font=("Comic Sans MS", 15),
                                     bg="#ffeb66", bd=0,
                                     cursor="hand2", command = self.flag_4).place(x=750, y=440, height=200, width=200)

       #btn_login = Button(self.root, text="Open Files", font=("times new roman", 15), bd=0, cursor="hand2").place(x=900,y=500,width=200)
       #btn_img = Button(self.root, image = self.button_bg, bd=0, cursor="hand2").place(x=870,y=500)

       pass

   def flag_1(self):

       response = messagebox.askokcancel("Information", "Loading CNN model takes time! \nNeed to wait until model gets loaded \nPress "
                                             "Ok to continue")

       if response == 1:

           self.flag = 1
           self.terminate()

           pass


       pass

   def flag_2(self):

       self.flag = 2
       self.terminate()

       pass

   def flag_3(self):

       self.flag = 3
       self.terminate()

       pass

   def flag_4(self):

       self.flag = 4
       self.terminate()

       pass




   def terminate(self):


       self.root.destroy()

       pass


   def flag_return(self):


       return self.flag
       pass


   def back_function(self):

       self.flag = 5
       self.terminate()


       pass


   pass


"""if __name__ == '__main__':
    
    pass"""

def main_program():

    root = Tk()
    dashboard_object = Dashboard(root)
    root = mainloop()

    number = dashboard_object.flag_return()

    if number == 2:

        from Arsalan_MCS.license_plate_file import license_plate_main_program

        license_plate_main_program()

        pass

    elif number == 1:

        from Arsalan_MCS.digit_recognition_file import digit_recognition_main_program



        digit_recognition_main_program()



        pass

    elif number == 3:

        from Arsalan_MCS.admin import main_function

        main_function()



        pass

    elif number == 4:

        from Arsalan_MCS.edit_information import edit_information_main_function

        edit_information_main_function()



        pass


    elif number == 5:

        from Arsalan_MCS.first_form import first_form_main

        first_form_main()



        pass




    pass

#main_program()


