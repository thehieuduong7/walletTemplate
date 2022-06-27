from __init__ import app
from flask import render_template, url_for, redirect


@app.route("/login", methods=["Get"])
def login():
    return render_template("views/login.html")


@app.route("/", methods=["Get"])
def home():
    return render_template("views/home.html")


@app.route("/createMore", methods=["Get"])
def createMore():
    return render_template("views/moreWallet.html")


@app.route("/beautyNumber", methods=["Get"])
def beautyNumber():
    return render_template("views/beautyNumber.html")


@app.route("/myWallet", methods=["Get"])
def myWallet():
    return render_template("views/myWallet.html")


if(__name__ == "__main__"):
    with app.app_context():
        app.run(debug=1)
