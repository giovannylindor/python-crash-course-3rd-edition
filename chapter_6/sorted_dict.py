shoes = {
    'sga': 'converse', 
    'lebron': 'nike',
    'luka': 'jordan',
    'jokic': '361'
}

for player in sorted(shoes.keys()):
    if player == 'sga':
        print(f"\n{player.upper()} is a {shoes[player]} signature athlete")
    else:
        print(f"\n{player.title()} is a {shoes[player]} signature athlete")