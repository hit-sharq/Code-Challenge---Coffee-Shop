from entities import Coffee, Customer
coffee1 = Coffee("french coffee")
coffee2 = Coffee("Mako")

customer1 = Customer("Lee")
customer2 = Customer("Joshua")

order1 = customer1.create_order(coffee1, 4.5)
order2 = customer2.create_order(coffee1, 4.5)
order3 = customer1.create_order(coffee2, 5.0)
order4 = customer2.create_order(coffee2, 5.0)

print("Coffee customers:", coffee1.customers())

print("Customer coffees (with prices):")
for coffee, price in customer1.coffees():
    print(f"{customer1.name} ordered {coffee} for ${price}")

for coffee, price in customer2.coffees():
    print(f"{customer2.name} ordered {coffee} for ${price}")

for coffee in [coffee1, coffee2]:
    print(f"{coffee.name} - Total Orders: {coffee.total_orders}, Average Price: ${coffee.average_price():.2f}")
