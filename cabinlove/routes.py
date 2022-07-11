from flask import render_template
from cabinlove import app, db
from cabinlove.models import Location, Cabin, User


@app.route("/")
def home():
    return render_template("base.html")