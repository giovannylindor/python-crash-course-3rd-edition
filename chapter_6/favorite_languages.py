favorite_languages = {
    'jen': 'python', 
    'sarah': 'c',
    'eddie':'rust',
    'phil': 'python'
}

# Looping through dict (Key AND Value)
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print()
print()
print()

# Looping through dict (KEYS ONLY)
print("People: ")
for name in favorite_languages:
    print(f"{name}")
# for name in favorite_languages.keys() is the same syntax as the code above ^

shoes = {
    'nike': 'kobe',
    'jordan': 'zion',
    'converse': 'shai'
}

brands = ['nike', 'converse']

for brand in shoes.keys():
    if brand in brands:
        print(f"{brand.title()}'s Signature Athlete is {shoes[brand].title()}")
    else:
        print(f"{brand}")