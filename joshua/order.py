from customers import Customer
from coffee import Coffee
class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Must be a valid Customer")
        if not isinstance(coffee, Coffee):
            raise ValueError("Must be a valid Coffee")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
    
    @property
    def customer(self):
        """Return the customer associated with this order"""
        return self._customer

    def coffee(self):
        """Return the coffee associated with this order"""
        return self._coffee

    def price(self):
        """Return the price of this order"""
        return self._price
