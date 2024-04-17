import subprocess

def open_terminal():
    # Open a terminal window
    subprocess.call(["x-terminal-emulator", "-e"])

def execute_command(command):
    # Execute the provided command in the terminal
    subprocess.call(["x-terminal-emulator", "-e", command])

if __name__ == "__main__":
    open_terminal()
    ip_address = input("Enter IP address: ")
    if ip_address:
        command = f"ssh {ip_address}"  # Example command to SSH into the provided IP address
        execute_command(command)
