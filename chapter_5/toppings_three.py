# Checking for Special Items 
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == requested_toppings[1]:
        print(f"Sorry, we're out of {requested_toppings[1]}")
    else:
        print(f"Adding {requested_topping}")

print("Finished Making your Pizza!")


# Checking That A LIST isn't empty
requested_toppings = []

if requested_toppings: # Checks if List contains at least 1 item -> Empty List == False
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("Finished!")
else:
    print("\nMaking Cheese Pizza!")