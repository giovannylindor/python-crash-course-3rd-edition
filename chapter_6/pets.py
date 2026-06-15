dog = {
    'breed': 'german shepard',
    'owner': 'mark'
}

cat = {
    'breed': 'siamese',
    'owner': 'carlos'
}

wolf = {
    'breed': 'husky',
    'owner': 'joe'
}

pets = [dog, cat, wolf]

for pet in pets:
    print(f"\n{pet['breed'].title()} -> {pet['owner'].title()}")
    if pet == dog:
        print('this is a big dog')
    elif pet == cat:
        print('this cat loves food')
    elif pet == wolf:
        print('this is a dangerous wolf')