from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Hello, World!'

# Define a route for a custom URL
@app.route('/custom')
def custom():
    return 'This is a custom route!'

if __name__ == '__main__':
    # Run the Flask application on localhost at port 5000
    app.run(debug=True)
