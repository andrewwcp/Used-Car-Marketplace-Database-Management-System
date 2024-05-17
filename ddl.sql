-- Users Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    contact_number VARCHAR(50) NOT NULL,
    address VARCHAR(500) NOT NULL,
    street_name VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    longitude float not NULL,
    latitude float not null,
    is_seller BOOLEAN NOT NULL
);

-- Cars Table
CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    brand VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    body_type VARCHAR(100) NOT NULL,
    manufacturing_year INT NOT NULL,
    color VARCHAR(100) NOT NULL,
    mileage_km INT NOT NULL,
    machine_CC INT NOT NULL,
    fuel_type VARCHAR(100) NOT NULL,
    transmission VARCHAR(100) NOT NULL
);

-- Ads Table
CREATE TABLE ads (
    ads_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description VARCHAR(500) NOT NULL,
    car_id INT NOT NULL,
    user_id INT NOT NULL,
    price DOUBLE PRECISION CHECK (price >= 0) NOT NULL,
    bid_allowed BOOLEAN NOT NULL,
    constraint ads_cars FOREIGN KEY (car_id) REFERENCES cars(car_id),
    constraint ads_users FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Bids Table
CREATE TABLE bids (
    bid_id SERIAL PRIMARY KEY,
    ads_id INT NOT NULL,
    user_id INT NOT NULL,
    bid_price DOUBLE PRECISION CHECK (bid_price >= 0) NOT NULL,
    bid_date TIMESTAMP NOT NULL,
    bid_status VARCHAR(50) NOT NULL,
    constraint bids_ads FOREIGN KEY (ads_id) REFERENCES ads(ads_id),
    constraint bids_users FOREIGN KEY (user_id) REFERENCES users(user_id)
);
