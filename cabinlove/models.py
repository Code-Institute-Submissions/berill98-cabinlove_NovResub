from cabinlove import db


class Location(db.Model):
    # schema for the Location model
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(25), unique=True, nullable=False)
    cabins = db.relationship(
        "Cabin", backref="location", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.location_name


class Cabin(db.Model):
    # schema for the Cabin model
    id = db.Column(db.Integer, primary_key=True)
    cabin_name = db.Column(db.String(60), unique=True, nullable=False)
    photo = db.Column(db.String(200), unique=True, nullable=False)
    cabin_description = db.Column(db.Text, nullable=False)
    pet_friendly = db.Column(db.Boolean, default=False, nullable=False)
    wifi_included = db.Column(db.Boolean, default=True, nullable=False)
    kids_allowed = db.Column(db.Boolean, default=True, nullable=False)
    max_adults = db.Column(db.Integer)
    price_per_night = db.Column(db.Integer)
    location_id = db.Column(db.Integer, db.ForeignKey(
        "location.id", ondelete="CASCADE"), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Cabin: {1} | Price: {2}".format(
            self.id, self.cabin_name, self.price_per_night
        )


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    cabins = db.relationship(
        "Cabin", backref="owner", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name
