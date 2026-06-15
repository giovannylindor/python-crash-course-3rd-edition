alien_0 = {'color': 'red', "pts": 5}
alien_1 = {'color': 'green', "pts": 15}
alien_2 = {'color': 'blue', "pts": 105}


# List of Aliens
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print()


aliens = []

for alien_num in range(30):
    new_alien = {'color': 'green', 'pts': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for a in aliens[:5]:
    print(a)