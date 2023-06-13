from flask import Blueprint, render_template, redirect, url_for
from main import run

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    with open("text.txt", "r") as fh:
        stuff = fh.read()
    return render_template("index.html", f_action="/l", b_text="Click here to start listening", txtstuff=stuff)
@views.route("/l")
def l():
    return render_template("index2.html", f_action="/listening/", b_text="Click here to stop listening")
@views.route("/listening/")
def listening():
    run(testing=False)
    with open("text.txt", "r") as fh:
        stuff = fh.read()
    return redirect(url_for("views.home"))
