sandwich_orders = ['blt', 'pastrami', 'bacon egg & cheese','pastrami', 'everything bagel', 
                   'egg & cheese', 'chopped cheese', 'pastrami']

finished_sandwiches = []

print("Note: The Deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders: 
    order = sandwich_orders.pop()
    print(f"Making a {order.title()}")
    finished_sandwiches.append(order.title())

print("\nHere are all the sandwiches that were made: ")
for sandwich in finished_sandwiches: 
    print(f"{sandwich}")