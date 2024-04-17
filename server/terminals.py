import subprocess

def main():
    while True:
        # Get user input
        command = input("$ ")

        # Exit if user inputs 'exit'
        if command.lower() == 'exit':
            break

        # Execute the command and capture output
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            print(output.decode())  # Print the output
        except subprocess.CalledProcessError as e:
            print("Error:", e.output.decode())  # Print any errors

if __name__ == "__main__":
    main()
