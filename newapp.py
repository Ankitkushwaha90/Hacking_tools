import os
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class VideoPlayer(tk.Tk):
    def __init__(self, video_folder):
        super().__init__()
        self.title("Luxury Video Player")

        self.video_folder = video_folder
        self.video_files = [f for f in os.listdir(self.video_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]
        self.current_video_index = 0

        self.video_frame = tk.Label(self)
        self.video_frame.pack()

        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(pady=10)

        self.prev_button = ttk.Button(self.controls_frame, text="Previous", command=self.prev_video)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = ttk.Button(self.controls_frame, text="Next", command=self.next_video)
        self.next_button.pack(side=tk.LEFT)

        self.play_video()

    def play_video(self):
        video_path = os.path.join(self.video_folder, self.video_files[self.current_video_index])
        video_capture = cv2.VideoCapture(video_path)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(frame)

            self.video_frame.configure(image=frame)
            self.video_frame.image = frame

            if cv2.waitKey(28) & 0xFF == ord("q"):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def prev_video(self):
        self.current_video_index -= 1
        if self.current_video_index < 0:
            self.current_video_index = len(self.video_files) - 1
        self.play_video()

    def next_video(self):
        self.current_video_index += 1
        if self.current_video_index >= len(self.video_files):
            self.current_video_index = 0
        self.play_video()

if __name__ == "__main__":
    app = VideoPlayer("./hello/")
    app.mainloop()

