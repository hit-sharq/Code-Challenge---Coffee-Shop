from customers import Customer
from coffee import Coffee
# Import Order for future use
from order import Order

# Example usage
if __name__ == "__main__":
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    coffee1 = Coffee("percolator")
    coffee2 = Coffee("moka")

    order1 = customer1.create_order(coffee1, 4.5)
    order2 = customer2.create_order(coffee1, 3.5)
    order3 = customer1.create_order(coffee2, 2.0)

    print("Coffee customers:", coffee1.customers())
    print("Customer coffees:", customer1.coffees())
    print("most_spent for mako:", Customer.most_spent(coffee2).name)
