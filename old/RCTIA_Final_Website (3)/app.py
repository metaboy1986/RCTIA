from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/iocs')
def get_iocs():
    with open(os.path.join('data', 'iocs.json')) as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/advisories')
def get_advisories():
    with open(os.path.join('data', 'advisories.json')) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
