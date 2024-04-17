import os

def run_command(command):
    """Execute a system command."""
    return os.system(command)

def main():
    while True:
        # Display prompt
        user_input = input("$ ")

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print("Exiting...")
            break

        # Execute the command
        output = run_command(user_input)
        print(output)

if __name__ == "__main__":
    main()
