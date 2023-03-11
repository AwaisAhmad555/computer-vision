from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
#import pymysql
class Register:
   def __init__ (self,root):
       self.root = root
       self.root.title("registeration on window")
       self.root.geometry("1350x700+0+0")

       #self BG image
       self.bg = ImageTk.PhotoImage(file = "pic 1.jpg.jpg")
       bg = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       #front image
       #self.left = ImageTk.PhotoImage(file="pic4.png")
       #left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

       #RIGESTER FRAME
       frame1 = Frame(self.root,bg="Aliceblue")
       frame1.place(x=800,y=90,width=350,height=500)
       title = Label(frame1,text="Log In Here",font=("time new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

       user_name = Label(frame1, text="User Name", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=70,y=90)
       self.txt_username=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_username.place(x=70,y=130,width=200)

       #l_name = Label(frame1, text="Last Name", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=100)
       #self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       #self.txt_lname.place(x=370, y=130, width=250)

       #...........
       #contect = Label(frame1, text="Contect NO", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=50,y=170)
       #self.txt_contect=Entry(frame1,font=("times new roman",15),bg="lightgray")
       #self.txt_contect.place(x=50,y=200,width=250)

       #email = Label(frame1, text="E_Mail", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=170)
       #self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       #self.txt_email.place(x=370, y=200, width=250)


       #...........
       #question = Label(frame1, text="security Question", font=("time new roman", 15, "bold"), fg="gray").place(x=50,y=240)
       #self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
       #self.cmb_quest['values']=("select","your first city name","your mother name"," your favorite teacher name")
       #self.cmb_quest.place(x=50,y=270,width=250)
       #self.cmb_quest.current(0)
       #answer = Label(frame1, text="Answer", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=240)
       #self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       #self.txt_answer.place(x=370, y=270, width=250)
       #...........


       password = Label(frame1, text="password", font=("time new roman", 15, "bold"), bg="white", fg="black").place(x=70,y=200)
       self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_password.place(x=70,y=240,width=200)

       #confirm = Label(frame1, text="Confirm password", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=310)
       #self.txt_confirm = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       #self.txt_confirm.place(x=370, y=340, width=250)


       #.....terms and condition......
       #self.var_chk=IntVar()
       #chk=Checkbutton(frame1,text="I agree terms and conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
       #self.btn_image=ImageTk.PhotoImage(file="images.png")
       #btn=Button(frame1,image=self.btn_image,bd=0,cursor="hand2",command=self.register_data).place(x=350,y=370)
       btn_login = Button(self.root,text="Log In",font=("times new roman",20),bd=0, cursor="hand2",command=self.integrity_constraint()).place(x=890,y=500,width=150)
       forget_password_login = Button(self.root, text="Forget Password", font=("times new roman", 15), bd=0, cursor="hand2").place(x=870,y=400,width=200)

   def integrity_constraint(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","Enter Username and password both",parent=self.root)

        pass



   def register_data(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","Enter password and E-Mail both",parent=self.root)
        #elif self.txt_password.get() != self.txt_confirm.get():
            #messagebox.showerror("Error", "password is not confirm", parent=self.root)
        #elif self.var_chk.get()==0:
            #messagebox.showerror("Error", "please accept our term and conditions", parent=self.root)
        #else:
            #messagebox.showinfo("success","registeration is successful",parent=self.root)



   pass

root = Tk()
obj = Register(root)
root = mainloop()
