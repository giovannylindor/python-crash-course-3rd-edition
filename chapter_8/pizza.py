def make_pizza(*toppings):
    """Print a list of toppings"""
    
    print("\nMake a pizza w/ the following: ")
    for topping in toppings:
        print(f"- {topping}")    

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza2(size, *toppings): 
    """Summarize the pizza"""
    print(f"\nMaking a {size}-inch pizza w/ the following: ")
    for topping in toppings: 
        print(f"- {topping}")

print()
make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'green peppers', 'extra cheese')