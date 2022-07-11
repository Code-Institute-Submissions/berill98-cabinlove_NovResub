from flask import render_template, request, redirect, url_for
from cabinlove import app, db
from cabinlove.models import Location, Cabin, User


@app.route("/")
def home():
    return render_template("cabins.html")


@app.route("/locations")
def locations():
    locations = list(Location.query.order_by(Location.location_name).all())
    return render_template("locations.html", locations=locations)


@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        location = Location(location_name=request.form.get("location_name"))
        db.session.add(location)
        db.session.commit()
        return redirect(url_for("locations"))
    return render_template("add_location.html")