import random
from twilio.rest import Client
import tkinter as tk

# Twilio API credentials
account_sid = 'ACe38dfbc68ed60de80bbe8386b1029b20'
auth_token = 'a2cb639b458b64d353fc11896e519ca0'
client = Client(account_sid, auth_token)

# Generate a random 6-digit OTP
otp = random.randint(100000, 999999)

# Define a function to send the OTP via SMS
def send_otp():
    phone_number = phone_number_entry.get()
    message = f"Your OTP is: {otp}"
    message = client.messages.create(to=phone_number, from_='+16203901221', body=message)
    message_label.config(text="OTP sent")

# Define a function to verify the OTP entered by the user
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

# Create an entry for the phone number
phone_number_entry = tk.Entry(root, width=15, font=("Arial", 24))
phone_number_entry.pack(pady=20)

# Create a button to send the OTP via SMS
send_otp_button = tk.Button(root, text="Send OTP", command=send_otp)
send_otp_button.pack(pady=10)

# Create an entry for the user to enter the OTP
otp_entry = tk.Entry(root, width=10, font=("Arial", 24))
otp_entry.pack(pady=20)

# Create a button to verify the OTP
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=10)

# Create a label to display the message
message_label = tk.Label(root, text="")
message_label.pack()

# Run the Tkinter main loop
root.mainloop()
