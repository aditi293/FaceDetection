import random
import tkinter as tk

# Define a function to generate a random 6-digit OTP
def generate_otp():
    global otp
    otp = random.randint(100000, 999999)
    otp_label.config(text=f"OTP: {otp}")

# Define a function to check the OTP entered by the user
def verify_otp():
    user_otp = otp_entry.get()
    if user_otp == str(otp):
        message_label.config(text="OTP verified")
    else:
        message_label.config(text="Incorrect OTP")

# Create a Tkinter window
root = tk.Tk()
root.geometry("500x300")
root.title("OTP Verification")

# Create a label for the OTP
otp_label = tk.Label(root, text="", font=("Arial", 24))
otp_label.pack(pady=20)

# Create a button to generate a new OTP
generate_button = tk.Button(root, text="Generate OTP", command=generate_otp)
generate_button.pack(pady=10)

# Create an entry for the user to enter the OTP
otp_entry = tk.Entry(root, width=10, font=("Arial", 24))
otp_entry.pack(pady=20)

# Create a button to verify the OTP
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=10)

# Create a label to display the verification message
message_label = tk.Label(root, text="")
message_label.pack()

# Run the Tkinter main loop
root.mainloop()
