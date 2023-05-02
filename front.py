import tkinter as tk
import subprocess

root = tk.Tk()

def open_register():
    subprocess.Popen(["python", "C:\\Users\\Hp\\PycharmProjects\\Frontend\\FaceDetection\\Register.py"])

def open_login():
        subprocess.Popen(["python", "C:\\Users\\Hp\\PycharmProjects\\Frontend\\FaceDetection\\Login.py"])

# Set the window size
root.geometry("1024x1024")

# Set the background image
bg_image = tk.PhotoImage(file="bb.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


button1 = tk.Button(root, text="REGISTER",font=("Times New Roman Bold",10), width=20, height=2,command=open_register)
button1.place(relx=0.1, rely=0.5, anchor='w')

button2 = tk.Button(root, text="LOGIN",font=("Times New Roman Bold",10), width=20,height=2, command=open_login)
button2.place(relx=0.1, rely=0.65, anchor='w')

# Button(text="Register",font=20,width=15,height=1,command=open_login).place(x=360,y=580)

# Add widgets here

root.mainloop()
