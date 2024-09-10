class Customer:
    def __init__(self, name):
        self.name = name
        self.order_history = []  # Keep track of coffees ordered and their prices

    def create_order(self, coffee, price):
        coffee.add_customer(self)  # Add customer to coffee's customer list
        coffee.record_order(price)  # Record the price of the order in the coffee class
        self.order_history.append((coffee, price))  # Track the order
        return Order(coffee, price)

    def coffees(self):
        # Returns a list of coffee names and their prices that this customer has ordered
        return [(order[0].name, order[1]) for order in self.order_history]


class Coffee:
    def __init__(self, name):
        self.name = name
        self.customer_list = []   # Hold customers who ordered this coffee
        self.total_price = 0      # Total sum of orders for this coffee
        self.total_orders = 0     # Total number of orders for this coffee

    def add_customer(self, customer):
        # Add this customer to the coffee's customer list
        self.customer_list.append(customer)

    def record_order(self, price):
        # Update total price and number of orders
        self.total_price += price
        self.total_orders += 1

    def average_price(self):
        # Calculate the average price of this coffee
        return self.total_price / self.total_orders if self.total_orders > 0 else 0

    def customers(self):
        # Return a list of customer names
        return [customer.name for customer in self.customer_list]


class Order:
    def __init__(self, coffee, price):
        self.coffee = coffee
        self.price = price