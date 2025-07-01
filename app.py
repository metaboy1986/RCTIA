
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("data/advisories.json", "r") as f:
        advisories = json.load(f)
    with open("data/iocs.json", "r") as f:
        iocs = json.load(f)
    return render_template("index.html", advisories=advisories, iocs=iocs)

@app.route("/advisory/<int:advisory_id>")
def advisory_detail(advisory_id):
    with open("data/advisories.json", "r") as f:
        advisories = json.load(f)
    with open("data/iocs.json", "r") as f:
        iocs = json.load(f)
    advisory = advisories[advisory_id]
    return render_template("advisory.html", advisory=advisory, iocs=iocs)

if __name__ == "__main__":
    app.run(debug=True)
