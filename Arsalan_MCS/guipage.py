from tkinter import *
import tkinter.messagebox as tkMessageBox

TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)


#=====================================LABEL WIDGETS=============================
lbl_title = Label(TitleFrame, text="IT SOURCECODE - Register Form", font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
lbl_username.grid(row=1)
lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
lbl_password.grid(row=2)
lbl_firstname = Label(RegisterFrame, text="Name:", font=('arial', 18), bd=18)
lbl_firstname.grid(row=3)
lbl_lastname = Label(RegisterFrame, text="Address:", font=('arial', 18), bd=18)
lbl_lastname.grid(row=4)
lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=5, columnspan=2)


#=======================================ENTRY WIDGETS===========================
user = Entry(RegisterFrame, font=('arial', 20), textvariable=USER, width=15)
user.grid(row=1, column=1)
pass1 = Entry(RegisterFrame, font=('arial', 20), textvariable=PASS, width=15, show="*")
pass1.grid(row=2, column=1)
name = Entry(RegisterFrame, font=('arial', 20), textvariable=NAME, width=15)
name.grid(row=3, column=1)
address = Entry(RegisterFrame, font=('arial', 20), textvariable=ADDRESS, width=15)
address.grid(row=4, column=1)
#========================================BUTTON WIDGETS=========================
btn_register=Button(RegisterFrame, font=('arial', 20), text="Register", command=Register)
btn_register.grid(row=6, columnspan=2)
#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)