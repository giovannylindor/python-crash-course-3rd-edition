cities = {
    'new york city': {
        'country': 'USA',
        'population': 4_000_000,
        'fact': 'Knicks in Five!'
    },
    'boston': {
        'country': 'USA',
        'population': 2_500_000,
        'fact': 'Celtics Suck!'
    },
    'miami': {
        'country': 'USA',
        'population': 3_200_000,
        'fact': 'lebron took his talents to south beach'
    }
}

print("Here is info on the following cities:")
for city, info in cities.items():
    print(f"\n{city}: ")
    print(f"Country: {info['country'].upper()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact'].capitalize()}")