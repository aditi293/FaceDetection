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
    username = username_entry.get()
    password = password_entry.get()
    if username == "myusername" and password == "mypassword":
        message_label.config(text="Login successful")
    else:
        message_label.config(text="Incorrect username or password")

root = tk.Tk()
root.geometry("800x670")
root.title("Login")

tk.Label(root, text="Login Form", font=("Times New Roman", 25)).place(x=250, y=50)

username_label = tk.Label(root, text="Username:", font=("Times New Roman", 23))
username_label.place(x=100,y=150)

username_entry = tk.Entry(root)
username_entry.place(x=280,y=150)

password_label = tk.Label(root, text="Password:", font=("Times New Roman", 23))
password_label.place(x=100,y=200)

password_entry = tk.Entry(root, show="*")
password_entry.place(x=280,y=200)

login_button = tk.Button(root, text="Login", command=verify_login, font=("Times New Roman", 20), width=10,height=1)
login_button.place(x=250,y=280)

message_label = tk.Label(root, text="", font=("Times New Roman", 20))
message_label.pack()

root.mainloop()
