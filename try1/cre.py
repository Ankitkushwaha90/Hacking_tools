from flask import Flask, request
import csv

app = Flask(__name__)

def write_to_csv(data):
    with open('user_info.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([data])

@app.route('/')
def index():
    user_agent = request.user_agent.string
    write_to_csv(user_agent)
    return 'User information saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
