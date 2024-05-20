# Used-Car-Marketplace-Database-Management-System
SQL database implementation of used car marketplace

# Objective
Transportation is a tool that can move goods or people from one place to another. With technological advancements, transportation methods are evolving, such as electric cars capable of self-driving, which have recently boomed. Many people are rushing to buy the latest car models. However, the prices offered by automotive companies are often unaffordable for those who do not have enough money to buy a new car. Used cars have become one solution for those who cannot afford a new car. The used car application serves as a solution for those looking for a used car within their desired price range and with guaranteed quality.The development of this application begins with defining business requirements and designing the database. As a database administrator, we are responsible for designing a relational database for this used car marketplace, including ensuring that relationships between tables are well-established. To ensure that our database design is optimal, we need to create dummy data for each table that has been created. This will help us test and validate the database design before implementing it in the actual application. To check if the database can function properly, we will generate dummy data and import it into the database. Furthermore, we will perform simple queries and analysis on the imported data.

# Features and Limitation 
* Each application user can offer more than one used car product.
* Before selling a car product, the user must first complete their personal data, such as name, contact information, and residential location.
* Users advertise their products through ads displayed on the website.
* These ads include a title, detailed information about the product being offered, and the seller's contact information.
* Some information that must be included in the ad is as follows:
  * Car brand: Toyota, Daihatsu, Honda, etc.
  * Model: Toyota Camry, Toyota Corolla Altis, Toyota Vios, Toyota Camry Hybrid, etc.
  * Car body type: MPV, SUV, Van, Sedan, Hatchback, etc.
  * Car type: manual or automatic
  * Year of car manufacture: 2005, 2010, 2011, 2020
  * Other descriptions, such as color, mileage, etc., can be added as needed.
* Each user can search for offered cars based on the seller's location, car brand, and car body type.
* If a potential buyer is interested in a car, they can bid on the product price if the seller allows bidding.
* The purchase transaction is conducted outside the application scope.

# Design Process
* Explaining the mission statement
* Creating table structure
* Defining relationships between tables
* Defining business rules and constraints

# Mission Statement 
* Users can advertise their used cars on the website.
* Buyers can make offers for the available used cars on the website.

# Creating Table Structure
1. Users Table
* Desc : store about user profile (seller and buyer)
* Column name dan data type
  
| Nama kolom | Tipe Data | Key |
| --- | --- | --- |
| user_id | int | CK → PK |
| username | varchar(100) | CK → AK |
| first_name | varchar(100) |
| last_name | varchar(20) |
| email | varchar(100) | 
| password | varchar(50) |
| contact_number | varchar(50) |
| address | varchar(500) |
| street_name | varchar(100) |
| state | varchar(100) |
| city | varchar(100) |
| postal_code | varchar(20) |
| longitude | float |
| latitude | float |
| is_seller | boolean |

# Defining Relationship between Tables
* A user can have multiple cars (1:N relationship between Users and Cars).
* A user can post multiple ads (1:N relationship between Users and Ads).
* An ad is associated with one car (1:N relationship between Cars and Ads).
* A user can place multiple bids on different ads (1:N relationship between Users and Bids).
* An ad can have multiple bids from different users (1:N relationship between Ads and Bids).

# Defining Business Rules and Constraint
1. Users Table:
  * Primary key user_id is auto-incremental.
  * All fields must be complete (Not Null constraint on all fields except user_id which is auto-incremental).
  * username is unique.
2. Cars Table:
  * Primary key car_id is auto-incremental.
  * All fields must be complete (Not Null constraint on all fields except car_id which is auto-incremental).
3. Ads Table:
  * Primary key ads_id is auto-incremental.
  * price must be greater than or equal to 0.
  * All fields must be complete (Not Null constraint on all fields except ads_id which is auto-incremental).
4. Bids Table:
  * Primary key bid_id is auto-incremental.
  * bid_price must be greater than or equal to 0.
  * All fields must be complete (Not Null constraint on all fields except bid_id which is auto-incremental).

# ERD
![used_car_marketplace](https://github.com/andrewwcp/Used-Car-Marketplace-Database-Management-System/assets/64004958/cc6ddea7-f557-4015-8069-7a7dd61e9c63)

