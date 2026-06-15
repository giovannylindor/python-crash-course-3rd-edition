d = {
    'SGA': 'converse',
    'LeBron': 'nike',
    'Luka': 'jordan'
}

print(f"The following brands have been mentioned: ")
for brand in set(d.values()):
    print(f"{brand.title()}")