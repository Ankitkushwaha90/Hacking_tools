import subprocess
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form['command']
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        result = e.output
    return result

@app.route('/search', methods=['POST'])
def search_files():
    query = request.form['query']
    files = []
    media_path = '/media'
    for root, dirs, filenames in os.walk(media_path):
        for filename in filenames:
            if query in filename:
                files.append(os.path.relpath(os.path.join(root, filename), media_path))
    return render_template('search_results.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
