# -*- coding: utf-8 -*-
"""Used Car Marketplace Dummy Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bWm3QgSBxab3h91kColxip4RZEvRbcTR

# Used Car Marketplace
"""

# Instalasi library Faker
!pip install Faker
!pip install tabulate

from google.colab import drive
drive.mount('/content/drive')

# Import Library yang akan digunakan
from faker import Faker
from tabulate import tabulate
import random
from datetime import datetime, timedelta
import csv
import pandas as pd
import re

# Definisikan bahwa data yang digunakan menggunakan format Indonesia
fake = Faker('id_ID')

"""## Membuat dummy data

### Dummy data yang dibuat adalah tabel-tabel berikut:

* libraries
* users
* publishers
* authors
* categories
* books
* book at library
* loan
* hold


"""

cars = pd.read_csv("/content/drive/MyDrive/Pacmann/SQL/vehicles.csv")
cars = cars[['id', 'price', 'year', 'manufacturer', 'model']]
cars = cars.dropna()

cars.isna().sum()

def generate_users_data(num=5):
    """
    Generate user data.

    Args:
        num (int, optional): Number of user records to generate. Defaults to 5.

    Returns:
        pandas.DataFrame: DataFrame containing user data with columns:
            - user_id (int): Unique identifier for each user.
            - username (str): Username generated based on first name, last name, and phone number.
            - first_name (str): User's first name.
            - last_name (str): User's last name.
            - email (str): User's email address.
            - password (str): User's password.
            - contact_number (str): User's contact phone number.
    """

    first_name_list = []
    last_name_list = []
    phone_number_list = []
    password_list = []
    username_list = []
    email_list = []
    address_list = [fake.address() for i in range(num)]
    street_name_list = [fake.street() for i in range(num)]
    state_list = [fake.administrative_unit() for i in range(num)]
    city_list = [fake.city_name() for i in range(num)]
    postal_code_list = [fake.postcode() for i in range(num)]
    longitude_list = [float(fake.longitude()) for i in range(num)]
    latitude_list = [float(fake.latitude()) for i in range(num)]
    is_seller_list = [fake.boolean(chance_of_getting_true = 60) for i in range(num)]

    for i in range(num):
      first_name = fake.first_name()
      last_name = fake.last_name()
      phone_number = fake.phone_number()
      password = fake.password()
      username = f"{first_name.lower()}_{last_name.lower()}{phone_number[-2:-1]}"
      email = f"{first_name.lower()}.{last_name.lower()}@usermail.com"

      first_name_list.append(first_name)
      last_name_list.append(last_name)
      phone_number_list.append(phone_number)
      password_list.append(password)
      username_list.append(username)
      email_list.append(email)

    users = {"user_id": [i+1 for i in range(num)],
              "username": username_list,
              "first_name": first_name_list,
              "last_name": last_name_list,
              "email": email_list,
              "password": password_list,
              "contact_number": phone_number_list,
              "address": address_list,
              "street_name": street_name_list,
              "state": state_list,
              "city": city_list,
              "postal_code": postal_code_list,
              "longitude": longitude_list,
              "latitude": latitude_list,
              "is_seller": is_seller_list
             }

    df = pd.DataFrame(users)
    return df

df_users = pd.DataFrame(generate_users_data(num=200))
df_users.head()

def generate_cars_data(num, body_type, fuel_type, transmission, color, cars):
    """
    Generate author data.

    Args:
        num (int): Number of author records to generate.
        books_metadata (pandas.DataFrame): DataFrame containing book metadata.

    Returns:
        pandas.DataFrame: DataFrame containing author data with columns:
            - author_id (int): Unique identifier for each author.
            - name (str): Author's name.
            - email (str): Author's email address (generated based on name).
            - contact_number (str): Author's contact phone number (generated).

    """

    car = {"car_id": [i+1 for i in range(num)],
               "brand": [cars['manufacturer'].iloc[i+1] for i in range(num)],
               "model": [cars['model'].iloc[i+1] for i in range(num)],
               "body_type": [random.choice(body_type) for i in range(num)],
               "manufacturing_year": [int(cars['year'].iloc[i+1]) for i in range(num)],
               "color": [random.choice(color) for i in range(num)],
               "mileage_km":[fake.pyint(min_value = 1000, step = 500) for i in range(num)] ,
               "machine_CC":[fake.pyint(min_value = 850, step = 10) for i in range(num)],
               "fuel_type":[random.choice(fuel_type) for i in range(num)],
               "transmission": [random.choice(transmission) for i in range(num)]

              }

    df = pd.DataFrame(car)
    return df

transmission = ["Automatic", "Manual"]
body_type = ["SUV", "MPV", "Sport", "Convertible", "Station Wagon", "Pick Up", "Electric", "Off Road", "Hybrid", "LCGC", "Hatchback", "Crossover", "Coupe"]
fuel_type = ["Gasoline", "Diesel", "Electric Batteries"]
color = ["Grey", "Black", "Silver", "White", "Yellow", "Red"]
df_cars = pd.DataFrame(generate_cars_data(300, body_type, fuel_type, transmission, color, cars))
df_cars.head()

def generate_ads_data(num, df_cars, df_users):
    """
    Generate publisher data.

    Args:
        num (int): Number of publisher records to generate.
        books_metadata (pandas.DataFrame): DataFrame containing book metadata.

    Returns:
        pandas.DataFrame: DataFrame containing publisher data with columns:
            - publisher_id (int): Unique identifier for each publisher.
            - name (str): Publisher's name.
            - address (str): Publisher's address.
            - email (str): Publisher's email address (generated based on name).
            - contact_number (str): Publisher's contact phone number (generated).

    """
    ads = {"ads_id": [i+1 for i in range(num)],
               "title": [f"{df_cars['model'].iloc[i]} - {df_cars['manufacturing_year'].iloc[i]}" for i in range(num)],
               "description": [f"Brand: {df_cars['brand'].iloc[i]}, Color: {df_cars['color'].iloc[i]}, Body_type: {df_cars['body_type'].iloc[i]}" for i in range(num)],
               "price": [float(fake.pyint(min_value = 50_000_000, step = 5_000_000, max_value = 800_000_000)) for i in range(num)] ,
               "bid_allowed": [fake.boolean(chance_of_getting_true = 70) for i in range(num)],
               "user_id": [random.choice(df_users['user_id']) for _ in range(num)],
               "car_id": [random.choice(df_cars['car_id']) for _ in range(num)],
              }

    df = pd.DataFrame(ads)
    return df

df_ads = pd.DataFrame(generate_ads_data(70, df_cars, df_users))
df_ads.head()

def generate_bids_data(num, df_users, df_ads):
    """
    Generate category data.

    Args:
        num (int): Number of category records to generate.
        cat_name (list): List of category names.

    Returns:
        pandas.DataFrame: DataFrame containing category data with columns:
            - category_id (int): Unique identifier for each category.
            - category_name (str): Name of the category.

    """
    bids = {"bid_id": [i+1 for i in range(num)],
               "bid_price": [float(fake.pyint(min_value = 40_000_000, step = 3_000_000, max_value = 800_000_000)) for i in range(num)],
               "bid_date": [fake.date_time_between(start_date=datetime(2024, 1, 1), end_date=datetime.now()) for i in range(num)],
               "bid_status": [random.choice(['Sent', 'Failed']) for _ in range(num)],
               "user_id": [random.choice(df_users['user_id']) for _ in range(num)],
               "ads_id": [random.choice(df_ads['ads_id']) for _ in range(num)],
              }

    df = pd.DataFrame(bids)
    return df

category_name = ["Mystery", "Thriller", "Science Fiction", "Fantasy", "Romance", "Non-Fiction", "Biography"]
df_bids = pd.DataFrame(generate_bids_data(200, df_users, df_ads))
df_bids

# Save to CSV
df_users.to_csv('users.csv', index=False)
df_cars.to_csv('cars.csv', index=False)
df_bids.to_csv('bids.csv', index=False)
df_ads.to_csv('ads.csv', index=False)