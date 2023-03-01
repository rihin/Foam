import tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Submit:
    def __init__(self, root):
        self.root = root
        self.root.title("Admission Foam")
        self.root.geometry("1599x800+150+150")
        #self.root.resizable(False, False)
         
        #Submit Frame
        Frame_Submit = Frame(self.root, bg="brown")
        Frame_Submit.place(x=350, y=100, width=800, height=700)
        
        #Title & Subtitle
        title = Label(Frame_Submit, text="Fill Foam", font=("impact", 35, "bold"), fg="#6162FF", bg="white").place(x=300, y=30)
        subtitle = Label(Frame_Submit, text="Student Registration Foam", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=300, y=100)
        
        # Name
        lbl_name = Label(Frame_Submit, text="Name", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=145)
        self.name = Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.name.place(x=160, y=145, width=250, height=27)
        
        # Father's Name
        lbl_fathername = Label(Frame_Submit, text="Father's Name", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=190)
        self.fathername = Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.fathername.place(x=160, y=190, width=250, height=27)
        
        # Mother's Name
        lbl_mothername = Label(Frame_Submit, text="Mother's Name", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=225)
        self.mothername = Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.mothername.place(x=160, y=225, width=250, height=27)
        
        # Date of birth
        lbl_dateofbirth = Label(Frame_Submit, text="Date of birth", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=260)
        self.dateofbirth= Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.dateofbirth.place(x=160, y=260, width=250, height=27)
        
        # Email
        lbl_email = Label(Frame_Submit, text="Email", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=295)
        self.email = Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.email.place(x=160, y=295, width=250, height=27)
        
        # Mobile number
        lbl_Phone = Label(Frame_Submit, text="Phone Number", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=330)
        self.phone = Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.phone.place(x=160, y=330, width=250, height=27)
        
        # Address
        lbl_Address = Label(Frame_Submit, text="Address", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=365)
        self.Address = Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.Address.place(x=160, y=365, width=500, height=27)
        
        # Gender
        lbl_Gender = Label(Frame_Submit, text="Gender", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=20, y=400)
        self.gender = Entry(Frame_Submit, font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        self.gender.place(x=160, y=400, width=250, height=27)
        
        # Button
        Submit = Button(Frame_Submit, command=self.check_function,  text="Submit", font=("Goudy old style", 16, "bold"), bg="#1d1d1d", fg="red").place(x=300, y=450)
        
    def check_function(self):
            if self.name.get()=="" or self.fathername.get()=="" or self.mothername.get()=="" or self.dateofbirth.get()=="" or self.email.get()=="" or self.phone.get()=="" or self.Address.get()=="" or self.gender.get()=="":
                messagebox.showerror("Error", "All fields required", parent=self.root)
            else:
                messagebox.showinfo("welcome", f"welcome {self.name.get()}")
                
        
        
root = Tk()       
obj = Submit(root)
root.mainloop()