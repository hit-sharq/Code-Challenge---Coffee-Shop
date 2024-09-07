class Coffee:
# Validate that the name is a string and has at least 3 characters
    def __init__(self,name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("must have at least 3 characters")
        self.name = name
        self.orders = []

        @property
        def name(self):
            """Return the name of the coffee"""
            return self.name
        
        
        def customers(self):
            """Return a list of unique customers who have ordered this coffee"""
            return list(set(order.customer for order in self.orders))
        
        def orders(self):
            """Return the list of orders"""
            return self.orders
        
        def num_orders(self):
            """Return the total number of orders placed for this coffee"""
            return len(self.orders)
        
        def add_order(self, order):
            """Add a new order to the coffee"""
            self.orders.append(order)
        
        def remove_order(self, order):
            """Remove an order from the coffee"""
            self.orders.remove(order)
            # Check if the order is associated with any customers
        
        def average_price(self):
            """Return the average price of all coffee  based on their orders"""
            if self.orders:
                return 0
            return sum(order.price for order in self._orders) / len(self._orders)
        

        pass
