import cv2
import tkinter as tk
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Open the first webcam connected to the computer
        self.cap = cv2.VideoCapture(0)

        # Create a canvas to display the webcam feed
        self.canvas = tk.Canvas(window, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Button to capture an image from the webcam
        self.btn_capture = tk.Button(window, text="Capture", width=50, command=self.capture)
        self.btn_capture.pack(anchor=tk.CENTER, expand=True)

        # Button to close the application
        self.btn_close = tk.Button(window, text="Close", width=50, command=self.close)
        self.btn_close.pack(anchor=tk.CENTER, expand=True)

        # Update the webcam feed display
        self.update()

        self.window.mainloop()

    def update(self):
        # Read a frame from the webcam
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to an ImageTk object
            self.img = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))

            # Update the canvas with the new frame
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        # Call the update function after 15 milliseconds
        self.window.after(15, self.update)

    def capture(self):
        # Read a frame from the webcam
        ret, frame = self.cap.read()
        if ret:
            # Save the captured frame to a file
            cv2.imwrite("captured_image.png", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def close(self):
        # Release the webcam and close the window
        self.cap.release()
        self.window.destroy()

# Create a Tkinter window
window = tk.Tk()
app = WebcamApp(window, "Webcam App")

