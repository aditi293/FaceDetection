# import tkinter as tk
# from tkinter import*
# root =tk.Tk
# root = Tk()
# root.title("Login")
# root.geometry("800x670")
# root.resizable(False,False)
# frame = tk.Frame(root, bg='white')
# frame.configure(bg='light blue')
# frame.pack(fill=tk.BOTH, expand=True)
import tkinter as tk

def verify_login():
    PhoneNumber = PhoneNumber_entry.get()
    password = password_entry.get()
    if PhoneNumber == "myPhoneNumber" and password == "mypassword":
        message_label.config(text="Login successful")
    else:
        message_label.config(text="Incorrect PhoneNumber or password")

root = tk.Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Login")

tk.Label(root, text="Login Here!", fg="blue",font=("Times New Roman", 25)).place(x=400, y=70)

PhoneNumber_label = tk.Label(root, text="PhoneNumber:", font=("Times New Roman", 20))
PhoneNumber_label.place(x=100,y=150)

PhoneNumber_entry = tk.Entry(root,width=25,bd=2,font=("Times New Roman", 20))
PhoneNumber_entry.place(x=300,y=150)

password_label = tk.Label(root, text="Password:", font=("Times New Roman", 20))
password_label.place(x=100,y=200)

password_entry = tk.Entry(root, show="*",font=("Times New Roman", 20),width=25,bd=2)
password_entry.place(x=300,y=200)

login_button = tk.Button(root, text="LOGIN", command=verify_login, bg="light gray",font=("Times New Roman Bold", 15), width=15,height=1,bd=1)
login_button.place(x=400,y=250)

message_label = tk.Label(root, text="", font=("Times New Roman", 20))
message_label.pack()

root.mainloop()
