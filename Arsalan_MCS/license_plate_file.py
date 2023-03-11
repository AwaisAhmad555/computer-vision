from tkinter import *
from tkinter import ttk,messagebox, filedialog
from PIL import Image,ImageTk
import cv2 as opencv
import pymysql
import tkinter
import cv2
from Arsalan_MCS.license_plate_detection import main_function


class Register:
   def __init__ (self,root):


       self.root = root
       self.root.title("Take a photo or select an image")
       self.root.geometry("1350x700+0+0")


       #self BG image
       self.bg = ImageTk.PhotoImage(file = "assets\\pic3.jpg")
       bg = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       title = Label(self.root, text="Welcome To HandWritten Digits Classification System", font=("Comic Sans MS", 18, "bold"),bd=10, bg="silver",
                     fg="MediumSeaGreen").place(x=90, y=30)

       #MAIN FRAME
       frame1 = Frame(self.root,bg="Aliceblue")
       frame1.place(x=100,y=120,width=1150,height=500)
       title = Label(frame1,text="Please Select Image !",font=("Comic Sans MS",18,"bold"),bd=10,bg="Lavender",fg="#F96167").place(x=30,y=30)



       background_image = opencv.imread("assets\\camera2.jpg")

       background_image = opencv.resize(background_image,(225,100))

       opencv.imwrite("assets\\btn_bgd.jpg",img=background_image)

       self.btn_cam =ImageTk.PhotoImage(file="assets\\btn_bgd.jpg")

       image = Image.open('assets\\upload.jpg')
       # The (450, 350) is (height, width)
       image = image.resize((35,35), Image.ANTIALIAS)

       self.button_bg =ImageTk.PhotoImage(image)

       background_image = opencv.imread("assets\\upload.jpg")
       #self.btn_cam = image.resize((350, 350), Image.ANTIALIAS)

       photo = PhotoImage(file="assets\\ocr (1).png")

       self.image_shape = 0

       #btn= Button(self.root,image=self.btn_cam, bd=0, cursor="hand2").place(x=870, y=240)


       btn_license_plate_detection = Button(frame1, text="Select Image", font=("Comic Sans MS", 15), bg="#008CBA", bd=0, command=self.loadImage,
                                   cursor="hand2").place(x=30, y=440)


       btn_clear = Button(frame1, text="Clear", font=("Comic Sans MS", 15), bg="#4CAF50", bd=0,
                                            command=self.clear_canvas,
                                            cursor="hand2").place(x=270, y=440)

       btn_ocr = Button(frame1, text="Detect", font=("Comic Sans MS", 15), bg="#f44336", bd=0,
                          command=self.detect_number,
                          cursor="hand2")

       #btn_ocr.pack()

       btn_ocr.place(x=180, y=440)



       self.return_value = 0
       # back navigation image

       # self.back_image = ImageTk.PhotoImage(file="back.png")
       self.back_image = Image.open("back.png")
       self.new_back_image = self.back_image.resize((30, 30))
       self.back_image = ImageTk.PhotoImage(self.new_back_image)

       back_btn = Button(self.root, image=self.back_image, bd=0, cursor="hand2", command=self.back_function).place(
           x=20, y=20, width=30, height=30)





       # Canvas

       self.canvas1 = tkinter.Canvas(frame1)
       self.canvas1.configure(width=300, height=300, bg='#FCE77D')
       #self.canvas1.create_rectangle(0, 0, 120, 70, fill='green')
       self.canvas1.grid(column=1, row=0)
       self.canvas1.grid(padx=20, pady=20)
       self.canvas1.place(x=30, y=110)



       # Canvas 2 (small)

       self.canvas2 = tkinter.Canvas(frame1)
       self.canvas2.configure(width=270, height=70, bg='#FCE77D')
       # self.canvas1.create_rectangle(0, 0, 120, 70, fill='green')
       self.canvas2.grid(column=1, row=0)
       self.canvas2.grid(padx=20, pady=20)
       self.canvas2.place(x=345, y=420)



       self.text_field = Entry(frame1, font=("Comic Sans MS", 12), bg="lightgray")
       self.text_field.place(x=635, y=455, width=250)

       btn_get_record = Button(frame1, text="Fetch Record", font=("Comic Sans MS", 15), bg="#317773", bd=0,
                        command=self.get_record,
                        cursor="hand2").place(x=910, y=440)





       #btn_login = Button(self.root, text="Open Files", font=("times new roman", 15), bd=0, cursor="hand2").place(x=900,y=500,width=200)
       #btn_img = Button(self.root, image = self.button_bg, bd=0, cursor="hand2").place(x=870,y=500)

       columns_list = []

       for k in range(10):

           columns_list.append("c"+str(k))

           pass

       columns_names = ("Registration_No", "Chassis_Number", "Engine_Number", "Model", "Registration_Date", "Token_Paid", "Owner_Name", "Color", "Company",
       "Fuel_Type", "Engine_Capacity", "Vehicle_price", "Latest_payment_details")


       self.tree = ttk.Treeview(frame1, column=(columns_names), show='headings', selectmode='browse')

       #tree.grid(row=10,column=10,columnspan=4,padx=20,pady=20)




       for a in range(13):


           self.tree.column("#"+str(a), anchor=tkinter.CENTER, minwidth=0, width=100, stretch=NO)
           #tree.heading("#" + str(a), text="ID" + str(a))
           self.tree.heading(columns_names[a], text=columns_names[a])


           pass

       # adding scrollbar to treeView

       self.scrollbar = ttk.Scrollbar(self.tree)

       self.scrollbar.configure(command=self.tree.xview)
       self.scrollbar.configure(orient="horizontal")

       self.tree.configure(xscrollcommand=self.scrollbar.set)

       self.scrollbar.pack(side= BOTTOM, fill = BOTH)

       self.tree.pack()

       """for column_name in columns_names:
           
           tree.heading("#" + str(a), text="ID" + str(a))
           
           
           pass"""





       self.tree.pack()

       self.tree.place(x=380, y=112, width=700,height=280)


       # main Program selection menu

       main_program = Label(frame1, text="Select Detection method : ", font=("Comic Sans MS", 15, "bold"),
                                 bg="Aliceblue",
                                 fg="black").place(x=540, y=50)


       self.main_program_txt = ttk.Combobox(frame1, font=("Comic Sans MS", 12), state="readonly",
                                                 justify=CENTER)


       self.main_program_txt["values"] = (
       "Select", "HAAR Cascade", "Contour boundaries based segmentation")
       self.main_program_txt.current(0)
       self.main_program_txt.place(
           x=830, y=50, width=250)

       #self.tree.insert("",tkinter.END,values=columns_names)

       # Event Call Back

       pass



   def back_function(self):

       self.root.destroy()

       self.return_value = 1

       pass


   def return_function(self):

       return self.return_value
       pass

   pass




   def clear_canvas(self):

       self.image_shape = 0
       self.canvas1.delete("all")
       self.canvas2.delete("all")
       self.text_field.delete(0, END)

       try:

           self.tree.delete(0, END)

           pass

       except:


           pass

       #self.text_field.insert(0, text)


       pass

   def loadImage(self):

       self.filename = filedialog.askopenfilename()

       #print(self.filename)

       self.image_bgr = cv2.imread(self.filename)

       try:

           self.orignal_image = self.image_bgr.copy()

           self.image_shape = self.orignal_image.shape[0]

           self.height, self.width = self.image_bgr.shape[:2]
           #print(self.height, self.width)

           if self.width > self.height:

               self.new_size = (300, 300)
           else:
               self.new_size = (300, 300)

           self.image_bgr_resize = cv2.resize(self.image_bgr, self.new_size, interpolation=cv2.INTER_AREA)
           self.image_rgb = cv2.cvtColor(self.image_bgr_resize,
                                         cv2.COLOR_BGR2RGB)  # Since imread is BGR, it is converted to RGB

           # self.image_rgb = cv2.cvtColor(self.image_bgr, cv2.COLOR_BGR2RGB) #Since imread is BGR, it is converted to RGB
           self.image_PIL = Image.fromarray(self.image_rgb)  # Convert from RGB to PIL format
           self.image_tk = ImageTk.PhotoImage(self.image_PIL)  # Convert to ImageTk format
           self.canvas1.create_image(150, 150, image=self.image_tk)


           pass

       except:


           pass

       pass




   def detect_number(self):


       if self.image_shape > 0:

           #messagebox.showinfo("shape", str(self.filename))

           if self.main_program_txt.get() == "Select":

               messagebox.showerror("Alert", "Select Detection program !")

               pass

           else:

               detection_method = self.main_program_txt.get()

               ##############################################

               self.detected_license_number, self.detected_license_plate = main_function(image_name=self.filename,detection_method=detection_method)


               # setting canvas


               self.detected_license_plate = cv2.resize(self.detected_license_plate, (270, 70),
                                                        interpolation=cv2.INTER_AREA)
               self.detected_license_plate = cv2.cvtColor(self.detected_license_plate,
                                                          cv2.COLOR_BGR2RGB)  # Since imread is BGR, it is converted to RGB

               # self.image_rgb = cv2.cvtColor(self.image_bgr, cv2.COLOR_BGR2RGB) #Since imread is BGR, it is converted to RGB
               self.detected_license_plate = Image.fromarray(
                   self.detected_license_plate)  # Convert from RGB to PIL format
               self.detected_license_plate = ImageTk.PhotoImage(
                   self.detected_license_plate)  # Convert to ImageTk format
               self.canvas2.create_image(135, 35, image=self.detected_license_plate)



               ####################################


               license_number = self.detected_license_number

               numbers_list = []

               for single_character in license_number:

                   if single_character.isalnum():
                       numbers_list.append(single_character)

                       pass

                   pass

               correct_license_number = ''.join(numbers_list)

               messagebox.showinfo("Detected Number is = ", str(correct_license_number))

               text = str(correct_license_number)

               self.text_field.delete(0, END)
               self.text_field.insert(0, text)

               pass



           pass



       pass

   def get_record(self):

       try:
           connection = pymysql.connect(host="localhost",
                                        user="root",
                                        password="",
                                        database="test",
                                        port=3306
                                        )

           cursor = connection.cursor()

           if self.text_field.get() != "":

               cursor.execute(query="SELECT * FROM car_detail WHERE Registration_No = %s",
                              args=(self.text_field.get()))

               rows = cursor.fetchone()

               #print(rows)

               self.tree.insert("", tkinter.END, values=rows[1:])


               pass



           connection.close()

           pass

       except Exception as exp:

           messagebox.showerror("Alert",str(exp))


           pass


       pass






   pass

def license_plate_main_program():

    root = Tk()
    license_plate_object = Register(root)
    root = mainloop()

    number = license_plate_object.return_value

    if number == 1:

        from Arsalan_MCS.dashboard import main_program

        main_program()


        pass


    pass

#license_plate_main_program()