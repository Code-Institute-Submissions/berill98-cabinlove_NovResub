from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter(User.user_name == \
                                           request.form.get("username").lower()).all()
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        user = User(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = User.query.filter(User.user_name == \
                                           request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
        
    if "user" in session:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))