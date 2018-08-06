from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["apple", "banana", "cainito"]
    return render_template("index.html", items = items)
