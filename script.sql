CREATE TABLE restaurants (
    /*restaurant_number INTEGER PRIMARY KEY, */
    restaurant_name TEXT NOT NULL,
    restaurant_address TEXT NOT NULL UNIQUE,
    restaurant_label TEXT NOT NULL,
    restaurnt_price INTEGER,
    restaurant_rating INTEGER
);
