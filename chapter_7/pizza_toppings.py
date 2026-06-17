prompt = 'Enter a Pizza topping: '
toppings = []
while True:
    message = input(prompt)
    if message.lower() == 'quit':
        break
    else:
        toppings.append(message)
        print(f"Adding {message}")
    

if not toppings:
    print("Making a regular Cheese Pizza")
else: 
    print("\nAdding the following toppings on your pizza: ")
    for topping in toppings:
        print(f"{topping}")