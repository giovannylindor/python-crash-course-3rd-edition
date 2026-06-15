favorite_languages = {
    'jen': 'python', 
    'sarah': 'c',
    'eddie':'rust',
    'phil': 'python'
}

take_poll = ['carlos', 'benny', 'alvin', 'jen', 'eddie', 'johnny', 'sarah', 'sara']

for person in take_poll:
    if person in favorite_languages:
        print(f"{person.title()}, thanks for taking the poll!")
    else:
        print(f"{person.title()}, please take the poll!")