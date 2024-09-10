# Code-Challenge---Coffee-Shop
## Description
The Coffee Shop Application is an Object-Oriented Programming (OOP) project that simulates the operations of a coffee shop. It models three main classes: **Coffee**, **Customer**, and **Order**, allowing customers to place orders for different types of coffee. The application keeps track of the orders, prices, and customer details, exemplifying relationships between the classes with a many-to-many relationship between **Coffee** and **Customer**.

## Features
- Customers can create orders for specific coffees.
- Each order is associated with a price.
- The application tracks all orders for each coffee and customer.
- Provides methods to calculate the total number of orders and average prices for each coffee.

## Technologies Used
- Python 3.8.13

## Getting Started
Instructions:

This assessment is designed to evaluate your understanding of Object Oriented Programming using Python.
You are required to complete the tasks outlined below within the specified time frame.
Ensure your code adheres to Python syntax and best practices.
Write comments to explain your code where necessary.
Create a well-written README file providing instructions on repository setup and running the application in the terminal.
Create a new PRIVATE repository, and push your solutions to it.
 

More Instructions:

Create a new folder for your project:
Create the relevant subfolders and files needed to kickstart your project
Create a virtual environment
Activate the virtual environment and install the relevant dependencies
 

🚀 You are now good to go, Focus on the deliverables below 🚀

For this assignment, we'll be working with a Coffee shop-style domain.

We have three models: Coffee, Customer, and Order.

For our purposes, a Coffee has many Orders, a Customer has many Orders, and an Order belongs to a Customer and to a Coffee.

Coffee - Customer is a many-to-many relationship.

Note: You should draw your domain on paper or on a whiteboard before you start coding. Remember to identify a single source of truth for your data.

Topics:

Classes and Instances
Class and Instance Methods
Variable Scope
Object Relationships
lists and list Methods

Deliverables:

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

Initializers and Properties:

Customer:

Customer __init__(self, name)
Customer is initialized with a name
Customer property name
Returns customer's name
Names must be of type str
Names must be between 1 and 15 characters, inclusive
Should be able to change after the customer is instantiated

Coffee:

Coffee __init__(self, name)
Coffee is initialized with a name
Coffee property name
Returns the coffee's name
Names must be of type str
Names length must be greater or equal to 3 characters
Should not be able to change after the coffee is instantiated
hint: hasattr()

Order:

Order __init__(self, customer, coffee, price)
Order is initialized with a Customer instance, a Coffee instance, and a price
Order property price
Returns the price for the order
Prices must be of type float
Price must be a number between 1.0 and 10.0, inclusive
Should not be able to change after the order is instantiated
hint: hasattr()
Object Relationship Methods and Properties

Order:

Order property customer
Returns the customer object for that order
Must be of type Customer
Order property coffee
Returns the coffee object for that order
Must be of type Coffee

Coffee:

Coffee orders()
Returns a list of all orders for that coffee
Orders must be of type Order
Coffee customers()
Returns a unique list of all customers who have ordered a particular coffee.
Customers must be of type Customer
Customer
Customer orders()
Returns a list of all orders for that customer
Orders must be of type Order
Customer coffees()
Returns a unique list of all coffees a customer has ordered
Coffees must be of type Coffee
Aggregate and Association Methods

Customer:

Customer create_order(coffee, price)
Receives a coffee object and a price number as arguments
Creates and returns a new Order instance and associates it with that customer and the coffee object provided.

Coffee:

Coffee num_orders()
Returns the total number of times a coffee has been ordered
Returns 0 if the coffee has never been ordered
Coffee average_price()
Returns the average price for a coffee based on its orders
Returns 0 if the coffee has never been ordered
Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders
Bonus: Aggregate and Association Method
Customer classmethod most_aficionado(coffee)
Receives a coffee object argument
Returns the Customer instance that has spent the most money on the coffee instance provided as argument.
Returns None if there are no customers for the coffee instance provided.
hint: will need a way to remember all Customer objects
Uncomment lines 137-147 in the customer_test file

### Prerequisites
Before running the application, ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
You can clone this repository to your local machine.

## LICENSE
MIT License

Copyright (c) 2024 joshua mwendwa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
