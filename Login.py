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

root = tk.Tk()

# Set the window size
root.geometry("800x600")

# Set the background image
bg_image = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


button1 = tk.Button(root, text="Button 1")
button1.place(relx=0.3, rely=0.5,x=50,y=50)

button2 = tk.Button(root, text="Button 2")
button2.place(relx=0.7, rely=0.5,x=100,y=100)

# Add widgets here

root.mainloop()
