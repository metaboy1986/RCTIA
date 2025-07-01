from flask import Flask, render_template

app = Flask(__name__)

# Sample Data
top_advisories = [
    "CISA Warns on MOVEit Exploits",
    "OpenSSH Backdoor Found",
    "Android Malware Campaigns Rise",
    "Microsoft Patch Tuesday Zero-Day",
    "Supply Chain Trojan Detected"
]

ioc_summary = {
    "Virus": 25,
    "Worm": 50,
    "Trojan": 10,
    "Ransomware": 50,
    "Other": 135
}

ioc_details = {
    "virus": {
        "IPs": ["1.1.1.1", "2.2.2.2"],
        "Hashes": ["abcd1234efgh5678", "ijkl9101mnop1121"],
        "Domains": ["badvirus.com", "infected.xyz"],
        "URLs": ["http://malicious.com/virus", "https://evil.com/v"]
    }
}

@app.route("/")
def index():
    return render_template("index.html", top_advisories=top_advisories, ioc_summary=ioc_summary)

@app.route("/ctia")
def all_ctia():
    return "<h2>All CTIA Advisories</h2>" + "<br>".join(top_advisories)

@app.route("/ioc/<ioc_type>")
def show_iocs(ioc_type):
    details = ioc_details.get(ioc_type.lower(), {})
    html = f"<h2>{ioc_type.title()} IOCs</h2>"
    for category, values in details.items():
        html += f"<h4>{category}</h4><ul>"
        for v in values:
            html += f"<li>{v}</li>"
        html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
