vacation = {} 
active = True

while active: 
    name = input("Enter your name (type \"Quit\" to Quit): ")

    if name.lower() == 'quit':
        active = False
    else:
        place = input("If you could visit one place in the world,"
                " what would it be? \nPlace: ")
        vacation[name] = place


if not vacation:
    exit()
else:
    print("\nOutput:")
    for name, place in vacation.items():
        print(f"{name.title()} would love to go to {place.title()}")

# NOTE: FLAGS ONLY STOP THE NEXT ITERATION FROM HAPPENING