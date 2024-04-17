from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.user_agent
    browser = user_agent.browser
    os = user_agent.platform

    with open('user_info.csv', 'a', newline='') as csvfile:
        fieldnames = ['Browser', 'OS']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty, if so, write the header
        csvfile.seek(0)
        first_char = csvfile.read(1)
        if not first_char:
            writer.writeheader()

        writer.writerow({'Browser': browser, 'OS': os})

    return 'User information saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
