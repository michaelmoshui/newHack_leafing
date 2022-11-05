"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file
"""

from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

################# DB Set up starts
# change to name of your database; add path if necessary
DB_NAME = "restaurant.db"

# sets the url of the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_NAME

# TODO Find out what this does
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# this variable, db, will be used for all SQLAlchemy commands
DB = SQLAlchemy(app)
############ DB set up ends


class Restaurants(DB.Model):
    """
    initializes the database
    """

    restaurant_id = DB.Column(DB.Integer, primary_key=True)
    restaurant_name = DB.Column(DB.String(100), nullable=False)
    address = DB.Column(DB.String(200), nullable=False)
    label = DB.Column(DB.String(150), nullable=False)
    price = DB.Column(DB.Integer, nullable=False)
    rating = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
@app.route("/")
def testdb():
    try:
        DB.session.query(text("1")).from_statement(text("SELECT 1")).all()
        return render_template("index.html")
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = "<h1>Something is broken.</h1>"
        return hed + error_text


@app.route("/add", methods=["POST"])
def add_entry():
    if request.method == "POST":
        restaurant_name = request.form["restaurant_name"]
        address = request.form["address"]
        label = request.form["label"]
        price = float(request.form["price"])
        rating = float(request.form["rating"])
        # print("DATA\n\n\n\n\n\n\n")
        print(restaurant_name, address, label, price, rating)
        # print("DATA\n\n\n\n\n\n\n")
        text = "<h1>" + str(restaurant_name) + "</h1>"
        text += "<h1>" + str(address) + "</h1>"
        text += "<h1>" + str(label) + "</h1>"
        text += "<h1>" + str(price) + "</h1>"
        text += "<h1>" + str(rating) + "</h1>"
        return text
    if request.method == "GET":
        error_text = "<h1>Hello</h1>"
        return error_text


if __name__ == "__main__":
    try:
        with app.app_context():
            DB.create_all()
        print("Works")
    except:
        print("Doesn't works")
    app.run(debug=True)
