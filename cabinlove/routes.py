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


@app.route("/add_cabin", methods=["GET", "POST"])
def add_cabin():
    locations = list(Location.query.order_by(Location.location_name).all())
    if request.method == "POST":
        cabin = Cabin(
            cabin_name = request.form.get("cabin_name"),
            photo = request.form.get("photo_url"),
            cabin_description = request.form.get("cabin_description"),
            pet_friendly = bool(True if request.form.get("pet_friendly") else False),
            wifi_included = bool(True if request.form.get("wifi_included") else False),
            kids_allowed = bool(True if request.form.get("kids_allowed") else False),
            max_adults = request.form.get("max_adults"),
            price_per_night = request.form.get("price_per_night"),
            location_id = request.form.get("location_id"),
            created_by = request.form.get("created_by"),
        )
        db.session.add(cabin)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_cabin.html", locations=locations)