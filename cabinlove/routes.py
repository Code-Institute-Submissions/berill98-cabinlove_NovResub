from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from cabinlove import app, db
from cabinlove.models import Location, Cabin, User


@app.route("/")
def home():
    all_data = []
    cabins = list(Cabin.query.order_by(Cabin.cabin_name).all())
    for cabin in cabins:
        cabin_data = {
            "cabin_id": cabin.id,
            "cabin_name": cabin.cabin_name,
            "photo": cabin.photo,
            "cabin_description": cabin.cabin_description,
            "pet_friendly": cabin.pet_friendly,
            "wifi_included": cabin.wifi_included,
            "kids_allowed": cabin.kids_allowed,
            "max_adults": cabin.max_adults,
            "price_per_night": cabin.price_per_night,
            "owner": User.query.filter(User.id == cabin.created_by).first(),
            "location": Location.query.filter(
                Location.id == cabin.location_id).first(),
        }
        all_data.append(cabin_data)
    return render_template("cabins.html", cabins=all_data)


@app.route("/locations")
def locations():
    locations = list(Location.query.order_by(Location.location_name).all())
    return render_template("locations.html", locations=locations)


@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage locations!")
        return redirect(url_for("locations"))

    if request.method == "POST":
        location = Location(location_name=request.form.get("location_name"))
        db.session.add(location)
        db.session.commit()
        return redirect(url_for("locations"))
    return render_template("add_location.html")


@app.route("/edit_location/<int:location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage locations!")
        return redirect(url_for("locations"))
    
    location = Location.query.get_or_404(location_id)
    if request.method == "POST":
        location.location_name = request.form.get("location_name")
        db.session.commit()
        return redirect(url_for("locations"))
    return render_template("edit_location.html", location=location)


@app.route("/delete_location/<int:location_id>")
def delete_location(location_id):
    if session["user"] != "admin":
        flash("You must be admin to manage locations!")
        return redirect(url_for("locations"))

    location = Location.query.get_or_404(location_id)
    db.session.delete(location)
    db.session.commit()
    return redirect(url_for("locations"))


@app.route("/add_cabin", methods=["GET", "POST"])
def add_cabin():
    if "user" not in session:
        flash("You need to be logged in to add a cabin")
        return redirect(url_for("home"))

    user = User.query.filter(
            User.user_name == session["user"].lower()).first()
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
            created_by = session["user_id"],
        )
        db.session.add(cabin)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_cabin.html", locations=locations)


@app.route("/edit_cabin/<int:cabin_id>", methods=["GET", "POST"])
def edit_cabin(cabin_id):
    if "user" not in session or session["user"] != "owner":
        flash("You must be the owner of the cabin to manage it!")
        return redirect(url_for("cabin"))
    
    cabin = Cabin.query.get_or_404(cabin_id)
    if request.method == "POST":
        cabin.cabin_name = request.form.get("cabin_name")
        cabin.photo = request.form.get("photo_url"),
        cabin.cabin_description = request.form.get("cabin_description"),
        cabin.pet_friendly = bool(True if request.form.get("pet_friendly") else False),
        cabin.wifi_included = bool(True if request.form.get("wifi_included") else False),
        cabin.kids_allowed = bool(True if request.form.get("kids_allowed") else False),
        cabin.max_adults = request.form.get("max_adults"),
        cabin.price_per_night = request.form.get("price_per_night"),
        cabin.location_id = request.form.get("location_id"),
        cabin.created_by = session["user_id"],
        db.session.commit()
        return redirect(url_for("cabins"))
    return render_template("edit_cabin.html", cabin=cabin)


@app.route("/delete_cabin/<int:cabin_id>")
def delete_cabin(cabin_id):
    if "user" not in session or session["user"] != "owner":
        flash("You must be the owner to manage the cabin!")
        return redirect(url_for("cabins"))

    cabin = Cabin.query.get_or_404(cabin_id)
    db.session.delete(cabin)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter(
            User.user_name == request.form.get("username").lower()).first()
        
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
        session["user_id"] = user.id
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = User.query.filter(
            User.user_name == request.form.get("username").lower()).first()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user.password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        session["user_id"] = existing_user.id
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
    session.clear()
    return redirect(url_for("login"))


@app.route("/cabins_at_locations/<int:location_id>")
def cabins_at_locations(location_id):
    cabins_at_locations = list(Cabin.query.get(Cabin.cabin_name).all())
    return render_template("locations.html", locations=locations)