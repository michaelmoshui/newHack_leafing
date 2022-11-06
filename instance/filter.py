import sqlite3
import pandas as pd

conn = sqlite3.connect('''restaurant.db''')
cur = conn.cursor()
cur.execute("SELECT * FROM restaurants;")
data = pd.DataFrame(cur.fetchall())
data.columns = [x[0] for x in cur.description]

#user_name = input("Enter a restaurant name: ")

# return a list of dictionary with the restaurant's information that contains the name
def filter_name(name):
    food = []
    for index, row in data.iterrows():
        if(name == row["restaurant_name"]):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.insert(0, res)
        elif(name in row["restaurant_name"]):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.append(res)
    return food

#filter_name(user_name)

#user_address = input("Enter a address")

# return a list of dictionary with the restaurant's information that contains the address
def filter_address(address):
    food = []
    for index, row in data.iterrows():
        if(address == row["address"]):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.insert(0, res)
        elif(address in row["address"]):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.append(res)
    return food

#filter_address(user_address)

def filter_city(city):
    food = []
    for index, row in data.iterrows():
        if(city == row["city"]):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.insert(0, res)
        elif(city in row["city"]):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.append(res)
    return food

#filter_city(user_city)

# user_min = int(input("Enter a min price"))
# user_max = int(input("Enter a max price"))

# return a list of dictionary with the restaurant's information that contains the address
def filter_price(min, max):
    food = []
    for index, row in data.iterrows():
        if((min <= row["price"]) and (row["price"] <= max)):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.append(res)
    return food

# filter_price(user_min, user_max)

# user_label = [0, 1, 1, 0] #[vegan, vegetarian, gluten-free, halal]

# return a list of dictionary with the restaurant's information that contains the address
def filter_label(label):
    food = []
    if(sum(label) == 0):
        for index, row in data.iterrows():
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.append(res)
    for i in range(4):
        for index, row in data.iterrows():
            if(label[i] and row["label"][i]):
                res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
                food.append(res)
    return food

# filter_address(user_label)

# user_rating = int(input("Enter a min rating"))

# return a list of dictionary with the restaurant's information that contains the address
def filter_rating(rating):
    food = []
    for index, row in data.iterrows():
        if(rating <= row["price"]):
            res = {"name": row["restaurant_name"], "city": row["city"], "address": row["address"], "label" : row["label"], "price": row["price"], "rating":row["rating"]}
            food.append(res)
    return food

# filter_price(user_rating)

def filter(user_input): #user_input is a dictionary
    result = []
    duplicates = []
    if(user_input["city"] != ""):
        city = filter_city(user_input["city"])
        duplicates.append(city)
    if(user_input["restaurant_name"]!= ""):
        name = filter_name(user_input["restaurant_name"])
        duplicates.append(name)
    if(user_input["address"] != ""):
        address = filter_address(user_input["address"])
        duplicates.append(address)
    label = filter_label(user_input["label"])
    duplicates.append(label)
    if(user_input["price_max"] is not None and user_input["price_min"] is not None):
        price = filter_price(user_input["price_min"], user_input["price_max"])
        duplicates.append(price)
    if(user_input["rating"] is not None):
        rating = filter_rating(user_input["rating"])
        duplicates.append(price)
        
    for i in range(len(duplicates)): #This algorithmn could be improved cuz it only work with relatively small database
        for j in range(len(duplicates[i])):
            res = duplicates[i][j]
            for x in range(i+1, len(duplicates)):
                compare = duplicates[x]
                if(res in compare):
                    break
                else:
                    result.append(res)
    
    return result
