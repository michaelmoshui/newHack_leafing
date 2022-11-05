"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file
"""

from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlite3

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

# conn_ = sqlite3.connect("""restaurant.db""")
# cur_ = conn_.cursor()
############ DB set up ends
def add_restaurant(DB, restaurant_name, address, label, price, rating):
    """
    Create a new task
    :param conn:
    :param task:
    :param lable: string separated by space that has all the labels
    :return:
    """
    # new_add = Restaurants(
    #     # restaurant_id=number,
    #     restaurant_name=restaurant_name,
    #     address=address,
    #     label=label,
    #     price=price,
    #     rating=rating,
    # )
    query = 'INSERT INTO restaurants(restaurant_name, address, label, price, rating) values("{res_name}", "{addr}", "{lab}", {pricing}, {rate})'.format(
        res_name=restaurant_name, addr=address, lab=label, pricing=price, rate=rating,
    )
    with app.app_context():
        DB.session.execute(query)
        DB.session.commit()


# class Restaurant_Entry(DB.Model):
#     def __init__(self, number, restaurant_name, address, label, price, rating):
#         self.number = number
#         self.restaurant_name = restaurant_name
#         self.address = address
#         self.label = label
#         self.price = price
#         self.rating = rating


class Restaurants(DB.Model):
    """
    initializes the database
    """

    # # DB.Column("restaurant_id", DB.Integer, nullable=False, primary_key=True)
    # DB.Column("restaurant_name", DB.String(100), nullable=False)
    # DB.Column("address", DB.String(200), nullable=False)
    # DB.Column("label", DB.String(150), nullable=False)
    # DB.Column("price", DB.Integer, nullable=False)
    # DB.Column("rating", DB.Integer, nullable=False)

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
        # extract data from the html form
        restaurant_name = request.form["restaurant_name"]
        address = request.form["address"]
        label = request.form["label"]
        price = float(request.form["price"])
        rating = float(request.form["rating"])

        # assume that the data at this point is fine to insert to the database

        # TODO return error if not good
        # michael said he will take care of it

        ### debug stuff
        # print("DATA\n\n\n\n\n\n\n")
        # print(restaurant_name, address, label, price, rating)
        # print("DATA\n\n\n\n\n\n\n")
        return render_template("index.html", restaurant_name=restaurant_name)
    if request.method == "GET":
        error_text = "<h1>Hello</h1>"
        return error_text


if __name__ == "__main__":
    with app.app_context():
        DB.create_all()
        # add_restaurant(
        #     DB, "restaurant_name", "address", "label", "price", "rating",
        # )
        # add_restaurant(
        #     DB,
        #     restaurant_name="york",
        #     address="Hello",
        #     label="test",
        #     price=10,
        #     rating=2,
        # )
        # print("Works")

    app.run()
    # app.run(debug=True)
