import tkinter as tk
import subprocess

class TerminalApp:
    def __init__(self, master):
        self.master = master
        master.title("Windows Terminal-like GUI")

        self.text = tk.Text(master, wrap="word", undo=True, width=60, height=20)
        self.text.pack(expand=True, fill="both")

        self.input_entry = tk.Entry(master)
        self.input_entry.pack(fill="x")
        self.input_entry.bind("<Return>", self.run_command)

    def run_command(self, event):
        command = self.input_entry.get()
        self.input_entry.delete(0, tk.END)  # Clear the input entry
        self.text.insert(tk.END, f"$ {command}\n")  # Display command in the text widget

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            self.text.insert(tk.END, result.stdout)
            self.text.insert(tk.END, result.stderr)
        except Exception as e:
            self.text.insert(tk.END, f"Error: {e}\n")

root = tk.Tk()
app = TerminalApp(root)
root.mainloop()
