# A List inside a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "w/ the following: ")

# Looping through the list thats within the dictionary 
for topping in pizza['toppings']:
    print(f"\t{topping}")