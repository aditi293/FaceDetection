import tkinter as tk
import cv2
from PIL import Image, ImageTk


class CameraCapture:
    def __init__(self, window):
        self.window = window
        self.window.title("Camera Capture")

        self.vid = cv2.VideoCapture(0)

        # Create a canvas to display the captured image
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Create a button to capture an image
        self.btn_capture = tk.Button(window, text="Capture", command=self.capture)
        self.btn_capture.pack(pady=10)

    def capture(self):
        # Capture an image from the camera
        ret, frame = self.vid.read()

        # Convert the captured frame to an ImageTk object
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        # Update the canvas with the captured image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.image = img

        # Call the capture function again after 100ms
        self.window.after(10, self.capture)


if __name__ == "__main__":
    window = tk.Tk()
    app = CameraCapture(window)
    window.mainloop()
