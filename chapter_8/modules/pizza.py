def makePizza(size, *toppings):
    print(f"Making a {size}-inch pizza w/ the following: ")
    for topping in toppings:
        print(f"- {topping.title()}")