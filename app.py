import tkinter as tk
from tkinter import*
root =tk.Tk
root = Tk()
root.title("Registration")
root.geometry("800x670")
root.resizable(False,False)
frame = tk.Frame(root, bg='gray')
frame.configure(bg='light blue')
frame.pack(fill=tk.BOTH, expand=True)



def register():
    print("registered")


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

firstEntry=Entry(root,textvariable=firstValue,width=30,bd=2,font=20)
lastEntry=Entry(root,textvariable=lastValue,width=30,bd=2,font=20)
genderEntry=Entry(root,textvariable=GenderValue,width=30,bd=2,font=20)
phoneEntry=Entry(root,textvariable=PhoneValue,width=30,bd=2,font=20)
emailEntry=Entry(root,textvariable=EmailValue,width=30,bd=2,font=20)
ageEntry=Entry(root,textvariable=AgeValue,width=30,bd=2,font=20)
passwordEntry=Entry(root,textvariable=PasswordValue,width=30,bd=2,font=20)
confirmpasswordEntry=Entry(root,textvariable=ConfirmpasswordValue,width=30,bd=2,font=20)

firstEntry.place(x=280,y=150)
lastEntry.place(x=280,y=200)
genderEntry.place(x=280,y=250)
phoneEntry.place(x=280,y=300)
emailEntry.place(x=280,y=350)
ageEntry.place(x=280,y=400)
passwordEntry.place(x=280,y=450)
confirmpasswordEntry.place(x=280,y=500)

firstEntry = firstValue.get()
lastEntry= lastValue.get()


checkValue=IntVar
checkbtn=Checkbutton(text="remember me?",variable=checkValue)
checkbtn.place(x=290,y=550)

Button(text="Register",font=20,width=15,height=1,command=register).place(x=360,y=580)

root.mainloop()
