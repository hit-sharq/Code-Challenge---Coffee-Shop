from entities import Order
class Customers:
    all_customers = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Customer names must be between 1 and 15 characters long")
        self.name = name
        Customers.all_customers.append(self)

    @property
    def name(self):
        """Return the name of the customer"""
        return self._name

    @name.setter
    def name(self, current_name):
        if not isinstance(current_name, str) or len(current_name) < 1 or len(current_name) > 15:
            raise ValueError("Customer names must be between 1 and 15 characters long")
        self._name = current_name
    def create_order(self,name,coffee,price):
        order = order(self,name,price)
        self._order.append(order)
        coffee.add_order(order)
        return order
    def orders(self):
        """Return a list of orders made by this customer"""
        return self._order
    def coffees(self):
        """Return a list of coffees ordered by this customer"""
        return [order.coffee for order in self._order]
    @classmethod
    def most_spent(cls, coffee):
        """Return the customer instance who has spent the most on a given coffee"""
        if not coffee.orders():  # If there are no orders, return None
            return None
        highest_spender = None
        max_spent = 0
        
        # Check each customer for total spent on the given coffee
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:  # Update highest spender
                max_spent = total_spent
                highest_spender = customer
                
        return highest_spender  # Return the customer who spent the most
    
                
    
        

