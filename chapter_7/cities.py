prompt = '\nEnter a name of your city'
prompt += '\nEnter "Quit" when done: '

cities = []

while True: 
    city = input(prompt)
    if city.lower() == 'quit':
        break
    else:
        cities.append(city)
        print(f"WOW! You've been to {city.title()}")


if not cities:
    print("You've been Nowhere? BUMMER !")
else:
    for city in cities:
        print(f"{city.title()}")