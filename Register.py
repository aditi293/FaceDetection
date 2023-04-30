import tkinter as tk
from tkinter import*
from tkinter import messagebox

import subprocess

def open_login():
    subprocess.Popen(["python", "C:\\Users\\Hp\\PycharmProjects\\Frontend\\FaceDetection\\Login.py"])


# Button(text="Submit", command=open_new_page).pack()




def register():
    first = firstValue.get()
    last = lastValue.get()
    gender = genderValue.get()
    phone = PhoneValue.get()
    email = EmailValue.get()
    age = AgeValue.get()
    password = PasswordValue.get()
    confirm_password = ConfirmpasswordValue.get()

    if not (first and last and gender and phone and email and age and password and confirm_password):
        messagebox.showerror("Error", "All fields are required!")
    else:
        open_login()



root =tk.Tk
root = Tk()
root.title("Registration")
root.geometry("800x670")
root.resizable(False,False)
frame = tk.Frame(root, bg='gray')
frame.configure(bg='light blue')
frame.pack(fill=tk.BOTH, expand=True)



Label(root,text="Registration Form",font="arial 25").place(x=250,y=50)
Label(text="First Name",font=23).place(x=100,y=150)
Label(text="Last Name",font=23).place(x=100,y=200)
Label(text="Gender",font=23).place(x=100,y=250)
Label(text="PhoneNumber",font=23).place(x=100,y=300)
Label(text="Email",font=23).place(x=100,y=350)
Label(text="Age",font=23).place(x=100,y=400)
Label(text="Password",font=23).place(x=100,y=450)
Label(text="Confirm Password",font=23).place(x=100,y=500)

firstValue=StringVar()
lastValue=StringVar()
GenderValue=StringVar()
PhoneValue=StringVar()
EmailValue=StringVar()
AgeValue=StringVar()
PasswordValue=StringVar()
ConfirmpasswordValue=StringVar()

entries = []

firstEntry=Entry(root,textvariable=firstValue,width=30,bd=2,font=20)
firstEntry.place(x=280,y=150)
entries.append(firstEntry)
lastEntry=Entry(root,textvariable=lastValue,width=30,bd=2,font=20)
lastEntry.place(x=280,y=200)
entries.append(lastEntry)
genderOptions = ["Male", "Female", "Other"]
genderValue = StringVar()
genderValue.set("Choose your Gender")
genderMenu = OptionMenu(root, genderValue, *genderOptions)
genderMenu.config(width=27, font=20)
genderMenu.place(x=280, y=250)
entries.append(genderMenu)
phoneEntry=Entry(root,textvariable=PhoneValue,width=30,bd=2,font=20)
phoneEntry.place(x=280,y=300)
entries.append(phoneEntry)
emailEntry=Entry(root,textvariable=EmailValue,width=30,bd=2,font=20)
emailEntry.place(x=280,y=350)
entries.append(emailEntry)
ageEntry=Entry(root,textvariable=AgeValue,width=30,bd=2,font=20)
ageEntry.place(x=280,y=400)
entries.append(ageEntry)
passwordEntry=Entry(root,textvariable=PasswordValue,width=30,bd=2,font=20)
passwordEntry.place(x=280,y=450)
entries.append(passwordEntry)
confirmpasswordEntry=Entry(root,textvariable=ConfirmpasswordValue,width=30,bd=2,font=20)
confirmpasswordEntry.place(x=280,y=500)
entries.append(confirmpasswordEntry)

firstEntry.place(x=280,y=150)
lastEntry.place(x=280,y=200)
# genderEntry.place(x=280,y=250)
phoneEntry.place(x=280,y=300)
emailEntry.place(x=280,y=350)
ageEntry.place(x=280,y=400)
passwordEntry.place(x=280,y=450)
confirmpasswordEntry.place(x=280,y=500)

checkValue=IntVar
checkbtn=Checkbutton(text="remember me?",variable=checkValue)
checkbtn.place(x=290,y=550)

Button(text="Register",font=20,width=15,height=1,command=register).place(x=360,y=580)
def register():
    first = firstValue.get()
    last = lastValue.get()
    gender = genderValue.get()
    phone = PhoneValue.get()
    email = EmailValue.get()
    age = AgeValue.get()
    password = PasswordValue.get()
    confirm_password = ConfirmpasswordValue.get()

    if not (first and last and gender and phone and email and age and password and confirm_password):
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    else:
        # Perform registration logic here
        # If successful, show success message and open login page
        # Otherwise, show error message
        messagebox.showinfo("Success", "Registration successful!")
        open_login()


# Button(text="Register",font=20,width=15,height=1,command=open_login).place(x=360,y=580)


root.mainloop()
