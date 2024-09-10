class Customer:
    def __init__(self, name):
        self.name = name
        self.order_history = [] 
    def create_order(self, coffee, price):
        coffee.add_customer(self)  
        coffee.record_order(price) 
        self.order_history.append((coffee, price))
        return Order(coffee, price)

    def coffees(self):
        
        return [(order[0].name, order[1]) for order in self.order_history]


class Coffee:
    def __init__(self, name):
        self.name = name
        self.customer_list = []   
        self.total_price = 0    
        self.total_orders = 0     

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