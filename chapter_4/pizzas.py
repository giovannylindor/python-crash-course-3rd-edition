pizzas = ['pepperoni', 'cheese', 'margarita']

for pizza in pizzas:
    print(f"I like {pizza} pizza")


print("\nPizza is really good!!")


friend_pizzas = pizzas[:]
pizzas.append('meat lovers')
friend_pizzas.append('pineapple')

print(f"My favorite pizzas are: {pizzas}")
print(f"My friends favorite pizzas are {friend_pizzas}")