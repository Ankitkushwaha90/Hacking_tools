import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from moviepy.editor import VideoFileClip
import pygame
from threading import Thread

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

        self.replay_button = ttk.Button(self.controls_frame, text="Replay", command=self.replay_video)
        self.replay_button.pack(side=tk.LEFT)

        self.player_thread = None
        self.play_video()

    def play_video(self):
        if self.player_thread and self.player_thread.is_alive():
            self.player_thread.join()

        self.player_thread = Thread(target=self._play_video)
        self.player_thread.daemon = True
        self.player_thread.start()

    def _play_video(self):
        video_path = os.path.join(self.video_folder, self.video_files[self.current_video_index])

        pygame.init()
        pygame.mixer.init()

        video_clip = VideoFileClip(video_path)
        audio_file = video_clip.audio
        audio_file.write_audiofile("temp_audio.mp3")

        pygame.mixer.music.load("temp_audio.mp3")
        pygame.mixer.music.play()

        for frame in video_clip.iter_frames():
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)

            self.video_frame.configure(image=img)
            self.video_frame.image = img

            self.controls_frame.update_idletasks()

        pygame.mixer.music.stop()
        pygame.quit()

        os.remove("temp_audio.mp3")

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

    def replay_video(self):
        self.play_video()

if __name__ == "__main__":
    app = VideoPlayer("./hello/")
    app.mainloop()
