users = {
    'gi3vnny': {
        'firstName': 'giovanny',
        'lastName': 'lindor',
        'location': 'brooklyn, ny'
    },

    'thaddaholics': {
        'firstName': 'thadd',
        'lastName': 'allonce',
        'location': 'brooklyn, ny'
    },
    
    'brickscamecheap': {
        'firstName': 'giovanny',
        'lastName': 'lindor',
        'location': 'brooklyn, ny'
    }
}

# looping
for username, info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{info['firstName'].title()} {info['lastName'].title()}"
    location = info['location'].title()

    print(f"Name: {full_name}")
    print(f"Location: {location}")