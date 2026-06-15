player = {
    'firstName': "Nick",
    'lastName': 'Van Exel', 
    'teams': ['Los Angeles Lakers', 'Golden State Warriors', 'Denver Nuggets', 'Dallas Mavericks', 'Portland Trail Blazers', 'San Antonio Spurs']
}

print("Player Stats: ")

for stat, desc in player.items():
    if stat == 'teams':
        break
    else:
        print(f"{stat}: {desc}")
    

print("\nTeams Played: ")
for team in player['teams']:
    print(f"{team}")