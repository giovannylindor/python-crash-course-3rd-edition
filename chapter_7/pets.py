pets = ['dog', 'cat', 'sheep', 'dog', 'cat', 'rabbit', 3, 'goldfish', 'jackrabbit', 'cow', 343.2332]

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(f"\nNew List: {pets}")