"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file

TODO
1. weighted average
2. print to webpage
"""

from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlite3
import pandas as pd

# debugging
import pprint

pp = pprint.PrettyPrinter(indent=4)

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
############ Filter starts
# return a list of dictionary with the restaurant's information that contains the name
def filter_name(name, data):
    food = []
    for index, row in data.iterrows():
        if name == row["restaurant_name"]:
            res = {
                "name": row["restaurant_name"],
                "city": row["city"],
                "address": row["address"],
                "label": row["label"],
                "price": row["price"],
                "rating": row["rating"],
            }
            food.insert(0, res)
        elif name in row["restaurant_name"]:
            res = {
                "name": row["restaurant_name"],
                "city": row["city"],
                "address": row["address"],
                "label": row["label"],
                "price": row["price"],
                "rating": row["rating"],
            }
            food.append(res)
    return food


# filter_name(user_name)

# user_address = input("Enter a address")

# return a list of dictionary with the restaurant's information that contains the address
def filter_address(address, data):
    food = []
    for index, row in data.items():
        if address == row["address"]:
            res = {
                "name": row["restaurant_name"],
                "city": row["city"],
                "address": row["address"],
                "label": row["label"],
                "price": row["price"],
                "rating": row["rating"],
            }
            food.insert(0, res)
        elif address in row["address"]:
            res = {
                "name": row["restaurant_name"],
                "city": row["city"],
                "address": row["address"],
                "label": row["label"],
                "price": row["price"],
                "rating": row["rating"],
            }
            food.append(res)
    return food


# filter_address(user_address)


def filter_city(city, data):
    # pp.pprint(city)
    # pp.pprint(data)
    # print("\n\n\n\\n\n\n\n\n\n\n\n")
    # print(data)
    # print("\n\n\n\\n\n\n\n\n\n\n\n")
    food = []
    for index, row in data.items():
        # print(city.lower())
        # print(row["city"].lower())
        if city.lower() == row["city"].lower():
            # print(row)
            res = {
                "name": row["restaurant_name"],
                "city": row["city"],
                "address": row["address"],
                "label": row["label"],
                "price": row["price"],
                "rating": row["rating"],
            }
            food.append(res)
        elif city.lower() in row["city"].lower():
            res = {
                "name": row["restaurant_name"],
                "city": row["city"],
                "address": row["address"],
                "label": row["label"],
                "price": row["price"],
                "rating": row["rating"],
            }
            food.append(res)
    return food


# filter_city(user_city)

# user_min = int(input("Enter a min price"))
# user_max = int(input("Enter a max price"))

# return a list of dictionary with the restaurant's information that contains the address
def filter_price(price_min, price_max, dupl):
    food = []

    if price_min == "":
        price_min = 1
    if price_max == "":
        price_max = 5

    for item in dupl:
        if (int(price_min) <= item["price"]) and (item["price"] <= int(price_max)):
            res = {
                "name": item["name"],
                "city": item["city"],
                "address": item["address"],
                "label": item["label"],
                "price": item["price"],
                "rating": item["rating"],
            }
            food.append(res)
    return food

    # for index, row in data.items():
    #     # print("TYPE:")
    #     # print(type(price_min), type(row["price"]))
    #     if (int(price_min) <= row["price"]) and (row["price"] <= int(price_max)):
    #         res = {
    #             "name": row["restaurant_name"],
    #             "city": row["city"],
    #             "address": row["address"],
    #             "label": row["label"],
    #             "price": row["price"],
    #             "rating": row["rating"],
    #         }
    #         food.append(res)
    # return food


# filter_price(user_min, user_max)

# user_label = [0, 1, 1, 0] #[vegan, vegetarian, gluten-free, halal]

# return a list of dictionary with the restaurant's information that contains the address
def filter_label(label, dupl):
    print(label)
    food = []
    if sum(label) == 0:
        return []
    else:
        for idx in range(len(dupl)):
            temp_data = dupl[idx]
            print(temp_data)
            if label[0] == 1:
                if "vegetarian" in temp_data["label"]:
                    food.append(temp_data)
                    continue
            if label[1] == 1:
                if "vegan" in temp_data["label"]:
                    food.append(temp_data)
                    continue
            if label[2] == 1:
                if "glutenfree" in temp_data["label"]:
                    food.append(temp_data)
                    continue
            if label[3] == 1:
                if "halal" in temp_data["label"]:
                    food.append(temp_data)
                    continue
        return food
        # for index, row in temp_data.items():
        #     if label[i] and row["label"][i]:
        #         res = {
        #             "name": row["restaurant_name"],
        #             "city": row["city"],
        #             "address": row["address"],
        #             "label": row["label"],
        #             "price": row["price"],
        #             "rating": row["rating"],
        #         }
        #         food.append(res)
    # if sum(label) == 0:
    #     for index, row in data.items():
    #         res = {
    #             "name": row["restaurant_name"],
    #             "city": row["city"],
    #             "address": row["address"],
    #             "label": row["label"],
    #             "price": row["price"],
    #             "rating": row["rating"],
    #         }
    #         food.append(res)
    # for i in range(4):
    #     for index, row in data.items():
    #         if label[i] and row["label"][i]:
    #             res = {
    #                 "name": row["restaurant_name"],
    #                 "city": row["city"],
    #                 "address": row["address"],
    #                 "label": row["label"],
    #                 "price": row["price"],
    #                 "rating": row["rating"],
    #             }
    #             food.append(res)
    #             print("LABELLLL")
    #             pp.pprint(food)
    return food


# filter_address(user_label)

# user_rating = int(input("Enter a min rating"))

# return a list of dictionary with the restaurant's information that contains the address
def filter_rating(rating, dupl):
    food = []

    if rating == "":
        rating = 0.0

    for item in dupl:
        if float(rating) <= item["rating"]:
            res = {
                "name": item["name"],
                "city": item["city"],
                "address": item["address"],
                "label": item["label"],
                "price": item["price"],
                "rating": item["rating"],
            }
            food.append(res)
    return food

    # for index, row in data.items():
    #     # print(type(rating), type(row["rating"]))
    #     if float(rating) <= row["rating"]:
    #         res = {
    #             "name": row["restaurant_name"],
    #             "city": row["city"],
    #             "address": row["address"],
    #             "label": row["label"],
    #             "price": row["price"],
    #             "rating": row["rating"],
    #         }
    #         food.append(res)
    # return food


# filter_price(user_rating)


def filter_restaurants(user_input, data):  # user_input is a dictionary
    # print(user_input)
    # pp.pprint(data)
    # data is a dictionary of dictionaries with restaurant_id
    result = []
    duplicates = []
    if user_input["city"] != "":
        # print("USERINPUT", user_input["city"])
        city = filter_city(user_input["city"], data)
        # pp.pprint(city)
        for entry in city:
            duplicates.append(entry)
            # pp.pprint(duplicates)
    print("\n\n\n")
    pp.pprint(duplicates)
    if user_input["restaurant_name"] != "":
        name = filter_name(user_input["restaurant_name"], data)
        for entry in name:
            duplicates.append(entry)
    print("\n\n\n")
    pp.pprint(duplicates)
    if user_input["address"] != "":
        address = filter_address(user_input["address"], data)
        for entry in address:
            duplicates.append(entry)
    print("\n\n\n")
    pp.pprint(duplicates)
    label = filter_label(user_input["label"], duplicates)
    # print("LABBBBELLLL")
    # pp.pprint(label)
    for entry in label:
        duplicates.append(entry)
    print("\n\n\nLABEL")
    pp.pprint(duplicates)
    if user_input["max_price"] is not None and user_input["min_price"] is not None:
        price = filter_price(
            user_input["min_price"], user_input["max_price"], duplicates
        )
        for entry in price:
            duplicates.append(entry)
    print("\n\n\n")
    pp.pprint(duplicates)
    if user_input["rating"] is not None:
        rating = filter_rating(user_input["rating"], duplicates)
        for entry in rating:
            duplicates.append(entry)
    print("\n\n\n")
    pp.pprint(duplicates)

    ret = []

    for dictionary in duplicates:
        if dictionary not in ret:
            ret.append(dictionary)

    return ret


#     new_list = []
# for dictionary in list_of_dictionariesif dictionary not in new_list:
#         new_list.append(dictionary)

############ Filter ends


def add_restaurant(DB, city, restaurant_name, address, label, price, rating):
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
    query = 'INSERT INTO restaurants(city, restaurant_name, address, label, price, rating) values("{res_name}", "{region}", "{addr}", "{lab}", {pricing}, {rate})'.format(
        region=city.lower(),
        res_name=restaurant_name.lower(),
        addr=address.lower(),
        lab=label.lower(),
        pricing=price,
        rate=rating,
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
    city = DB.Column(DB.String(50), nullable=False)
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
def index():
    """
    index
    """
    return render_template("index.html")


# def testdb():
#     try:
#         DB.session.query(text("1")).from_statement(text("SELECT 1")).all()
#         return render_template("index.html")
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = "<h1>Something is broken.</h1>"
#         return hed + error_text


# @app.route("/list", methods=["GET"])
@app.route("/list", methods=["POST", "GET"])
def filter():
    if request.method == "POST":
        result = DB.session.execute("SELECT * FROM restaurants")
        result = result.fetchall()
        data = {}
        for l in result:
            data[l[0]] = {
                "city": l[1],
                "restaurant_name": l[2],
                "address": l[3],
                "label": l[4],
                "price": l[5],
                "rating": l[6],
            }

        filter_dict = {}

        restaurant_name = request.form["restaurant_name"]
        address = request.form["address"]
        #### vegetarian categories START
        is_vegetarian = request.form.get("vegetarian")
        # print("Debug is_vegetarian:", is_vegetarian)
        if is_vegetarian == "on":
            is_vegetarian = 1
        else:
            is_vegetarian = 0

        is_vegan = request.form.get("vegan")
        if is_vegan == "on":
            is_vegan = 1
        else:
            is_vegan = 0

        is_gluten_free = request.form.get("gluten-free")
        if is_gluten_free == "on":
            is_gluten_free = 1
        else:
            is_gluten_free = 0

        is_halal = request.form.get("halal")
        if is_halal == "on":
            is_halal = 1
        else:
            is_halal = 0
            #### vegetarian categories END
        min_price = request.form["min-price"]  # 1-5
        if min_price != "":
            min_price = int(min_price)
            # TODO ask michael if integer value is guaranteed

        max_price = request.form["max-price"]  # 1-5
        if max_price != "":
            max_price = int(max_price)

        rating = request.form["rating"]  # 1-10
        if rating != "":
            rating = int(rating)

        city = request.form["city"]
        # label = request.form["label"]

        filter_dict["restaurant_name"] = restaurant_name
        filter_dict["address"] = address
        filter_dict["label"] = [is_vegan, is_vegetarian, is_gluten_free, is_halal]
        filter_dict["min_price"] = min_price
        filter_dict["max_price"] = max_price
        filter_dict["rating"] = rating
        filter_dict["city"] = city
        # print("\n\n\n\n\n\n\n\n\n\n")
        # print(filter_dict)

        # print("\n\n\n\n\n\n\nn\n\n\\n")
        # pp.pprint(filter_dict)

        # pp.pprint(data)
        # print("FILTER QUERY")
        # pp.pprint(filter_dict)
        filter_result = filter_restaurants(filter_dict, data)
        for result in filter_result:
            print("QUERY RESULT: ", result)
        # print("FILTER RESULT")
        # for result in filter_result:
        #     pp.pprint(result)
        # list of dictionaries
        # print(filter_result)
        # for result in filter_result:
        #     print("RESULT:", result)
        # print("FILTER RESULT:", end="")
        # pp.pprint(filter_result)
        # for result in filter_result:
        #     print("Result:", result)
        # print("\n\n\n\n\n\n\nn\n\n\\n")
        return "<h1>hello</h1>"
    elif request.method == "GET":
        return render_template("list.html")


# TODO use anna's filter function

#       <p><input type = "text" name = "restaurant_name" /></p>
# <p><input type = "text" name = "address" /></p>
# <p><input type="checkbox"  name="vegetarian"></p>
# <p><input type="checkbox"  name="vegan"></p>
# <p><input type="checkbox"  name="gluten-free"></p>
# <p><input type="checkbox"  name="halal"></p>
# <p><input type = "number" name = "min-price" min = "1" max = "5"/></p>
# <p><input type = "number" name = "max-price" min = "1" max = "5"/></p>
# <p><input type = "number" name = "rating" min = "1" max = "10"/></p>
# <p><input type = "string" name = "city" /></p>
# <p><input type = "submit" value = "submit" /></p>


@app.route("/addPlaces", methods=["POST"])
def add_entry():
    if request.method == "POST":
        # extract data from the html form
        restaurant_name = request.form["restaurant_name"]
        city = request.form["city"]
        address = request.form["address"]
        label = request.form["label"]
        price = float(request.form["price"])
        rating = float(request.form["rating"])

        # assume that the data at this point is fine to insert to the database
        # adds restaurant to the database
        add_restaurant(
            DB,
            city=city,
            restaurant_name=restaurant_name,
            address=address,
            label=label,
            price=price,
            rating=rating,
        )

        # result = DB.session.execute("SELECT * FROM restaurants")
        # for row in result:
        #     print(row)

        # TODO return error if not good

        ### debug stuff
        # print("DATA\n\n\n\n\n\n\n")
        # print(restaurant_name, address, label, price, rating)
        # print("DATA\n\n\n\n\n\n\n")
        # return render_template("index.html", restaurant_name=restaurant_name)
    if request.method == "GET":
        error_text = "<h1>Error</h1>"
        return error_text


if __name__ == "__main__":
    with app.app_context():
        DB.create_all()
        # add_restaurant(
        #     DB, "restaurant_name", "address", "label", "price", "rating",
        # )
        # add_restaurant(
        #     DB,
        #     city="Toronto",
        #     restaurant_name="niceeat",
        #     address="123 Bay",
        #     label="Vegan",
        #     price=10,
        #     rating=2,
        # )
        # result = DB.session.execute("SELECT * FROM restaurants")
        # result = result.fetchall()
        # for l in result:
        #     print(l)
        # # results of everything
        # data = {}
        # for l in result:
        #     data[l[0]] = {
        #         "city": l[1],
        #         "restaurant_name": l[2],
        #         "address": l[3],
        #         "label": l[4],
        #         "price": l[5],
        #         "rating": l[6],
        #     }

        # pp.pprint(data)

        # data = pd.DataFrame(result.fetchall())
        # print(data)
        # [print(x[0]) for x in result.keys()]
        # data.columns = [x[0] for x in result.keys()]
        # for row in result:
        #     print(row)
        print("Works")

    # app.run()
    app.run(debug=True)
