from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import cv2 as opencv
import pymysql
import tkinter
import cv2
from Arsalan_MCS.license_plate_detection import main_function
from Arsalan_MCS.Hand_digit_system import main_program


class Register:
    def __init__(self, root):

        self.root = root
        self.root.title("Take a photo or select an image")
        self.root.geometry("1350x700+0+0")

        # self BG image
        self.bg = ImageTk.PhotoImage(file="assets\\pic3.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="Welcome To HandWritten Digits Classification System",
                      font=("Comic Sans MS", 18, "bold"), bd=10, bg="silver",
                      fg="MediumSeaGreen").place(x=90, y=30)

        # MAIN FRAME
        frame1 = Frame(self.root, bg="Aliceblue")
        frame1.place(x=100, y=120, width=1150, height=500)
        title = Label(frame1, text="Please Select Image !", font=("Comic Sans MS", 18, "bold"), bd=10, bg="Lavender",
                      fg="#F96167").place(x=30, y=30)

        background_image = opencv.imread("assets\\camera2.jpg")

        background_image = opencv.resize(background_image, (225, 100))

        opencv.imwrite("assets\\btn_bgd.jpg", img=background_image)

        self.btn_cam = ImageTk.PhotoImage(file="assets\\btn_bgd.jpg")

        image = Image.open('assets\\upload.jpg')
        # The (450, 350) is (height, width)
        image = image.resize((35, 35), Image.ANTIALIAS)

        self.button_bg = ImageTk.PhotoImage(image)

        background_image = opencv.imread("assets\\upload.jpg")
        # self.btn_cam = image.resize((350, 350), Image.ANTIALIAS)

        photo = PhotoImage(file="assets\\ocr (1).png")


        self.return_value = 0
        # back navigation image

        # self.back_image = ImageTk.PhotoImage(file="back.png")
        self.back_image = Image.open("back.png")
        self.new_back_image = self.back_image.resize((30, 30))
        self.back_image = ImageTk.PhotoImage(self.new_back_image)

        back_btn = Button(self.root, image=self.back_image, bd=0, cursor="hand2", command=self.back_function).place(
            x=20, y=20, width=30, height=30)




        self.image_shape = 0

        # btn= Button(self.root,image=self.btn_cam, bd=0, cursor="hand2").place(x=870, y=240)

        btn_license_plate_detection = Button(frame1, text="Select Image", font=("Comic Sans MS", 15), bg="#008CBA",
                                             bd=0, command=self.loadImage,
                                             cursor="hand2").place(x=30, y=440)

        btn_clear = Button(frame1, text="Clear", font=("Comic Sans MS", 15), bg="#4CAF50", bd=0,
                           command=self.clear_canvas,
                           cursor="hand2").place(x=270, y=440)

        btn_ocr = Button(frame1, text="Detect", font=("Comic Sans MS", 15), bg="#f44336", bd=0,
                         command=self.detect_number,
                         cursor="hand2")

        # btn_ocr.pack()

        btn_ocr.place(x=180, y=440)

        # Canvas

        self.canvas1 = tkinter.Canvas(frame1)
        self.canvas1.configure(width=300, height=300, bg='#FCE77D')
        # self.canvas1.create_rectangle(0, 0, 120, 70, fill='green')
        self.canvas1.grid(column=1, row=0)
        self.canvas1.grid(padx=20, pady=20)
        self.canvas1.place(x=30, y=110)


        # Canvas 2

        self.canvas2 = tkinter.Canvas(frame1)
        self.canvas2.configure(width=300, height=300, bg='#FCE77D')
        # self.canvas1.create_rectangle(0, 0, 120, 70, fill='green')
        self.canvas2.grid(column=1, row=0)
        self.canvas2.grid(padx=20, pady=20)
        self.canvas2.place(x=410, y=110)

        # Canvas 3

        self.canvas3 = tkinter.Canvas(frame1)
        self.canvas3.configure(width=300, height=300, bg='#FCE77D')
        # self.canvas1.create_rectangle(0, 0, 120, 70, fill='green')
        self.canvas3.grid(column=1, row=0)
        self.canvas3.grid(padx=20, pady=20)
        self.canvas3.place(x=785, y=110)






        #################

        self.text_field = Entry(frame1, font=("Comic Sans MS", 12), bg="lightgray")
        self.text_field.place(x=375, y=455, width=250)

        """btn_get_record = Button(frame1, text="Fetch Record", font=("Comic Sans MS", 15), bg="#317773", bd=0,
                                command=self.get_record,
                                cursor="hand2").place(x=660, y=440)"""

        #self.check_variable = 0

        self.check_variable = IntVar()

        self.checkbox = Checkbutton(frame1, text="Invert color check (Only check if background is white)",
                                    variable=self.check_variable, onvalue=1, offvalue=2, bg="Lavender",
                                    font=("Comic Sans MS", 12))
        self.checkbox.place(x=635, y=450)


    def back_function(self):

        self.root.destroy()

        self.return_value = 1

        pass

        # Event Call Back

    def clear_canvas(self):

        self.image_shape = 0
        self.canvas1.delete("all")
        self.text_field.delete(0, END)



        # self.text_field.insert(0, text)

        pass

    def loadImage(self):

        self.filename = filedialog.askopenfilename()

        # print(self.filename)

        self.image_bgr = cv2.imread(self.filename)

        try:

            self.orignal_image = self.image_bgr.copy()

            self.image_shape = self.orignal_image.shape[0]

            self.height, self.width = self.image_bgr.shape[:2]
            # print(self.height, self.width)

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

        #messagebox.showinfo("variable",self.check_variable.get())

        if self.image_shape > 0:

            #messagebox.showinfo("shape", str(self.filename))

            #self.detected_license_number = main_function(image_name=self.filename)

            self.complete_number, self.canny_image, self.bounding_box_image = main_program(file_name=self.filename,color_check=self.check_variable.get())


            #canvas 2
            self.canny_image_resize = cv2.resize(self.canny_image, self.new_size, interpolation=cv2.INTER_AREA)
            self.canny_image = cv2.cvtColor(self.canny_image_resize,
                                          cv2.COLOR_BGR2RGB)

            self.image_PIL_canny = Image.fromarray(self.canny_image)  # Convert from RGB to PIL format
            self.image_tk_canny = ImageTk.PhotoImage(self.image_PIL_canny)  # Convert to ImageTk format
            self.canvas2.create_image(150, 150, image=self.image_tk_canny)

            # Canvas 3

            self.bounding_box_image_resize = cv2.resize(self.bounding_box_image, self.new_size, interpolation=cv2.INTER_AREA)
            self.bounding_box_image = cv2.cvtColor(self.bounding_box_image_resize,
                                          cv2.COLOR_BGR2RGB)

            self.image_PIL_bounding_box = Image.fromarray(self.bounding_box_image)  # Convert from RGB to PIL format
            self.image_tk_bounding_box = ImageTk.PhotoImage(self.image_PIL_bounding_box)  # Convert to ImageTk format
            self.canvas3.create_image(150, 150, image=self.image_tk_bounding_box)


            complete_number = self.complete_number

            numbers_list = []

            for single_character in complete_number:

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

                # print(rows)

                #self.tree.insert("", tkinter.END, values=rows)

                pass

            connection.close()

            pass

        except Exception as exp:

            messagebox.showerror("Alert", str(exp))

            pass

        pass

    def return_function(self):


        return self.return_value
        pass

    pass


def digit_recognition_main_program():

    root = Tk()
    digit_recognition_object = Register(root)
    root = mainloop()

    number = digit_recognition_object.return_function()

    if number == 1:

        from Arsalan_MCS.dashboard import main_program

        main_program()


        pass



    pass


digit_recognition_main_program()
