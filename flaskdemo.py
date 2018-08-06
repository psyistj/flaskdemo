from flask import Flask, render_template, request, session
from flask_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def hello():
    items = ["apple", "banana", "cainito"]
    return render_template("index.html", items = items)

@app.route("/mainpage",methods=["GET","POST"])
def mainpage():
    if session.get("fruits") is None:
        session["fruits"] = []
    if request.method == "POST":
        fruit = request.form.get("fruit")
        session["fruits"].append(fruit)

    return render_template("mainpage.html", fruits = session["fruits"])
