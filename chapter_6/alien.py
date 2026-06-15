# Simple Dict
alien_0 = {'color': 'green',
            'points': 5 }


# Accessing Vals 
print(alien_0['color'])
print(alien_0['points'])


# Adding New Key-Val Pairs
alien_0['x-pos'] = 35.2
alien_0['y-pos'] = 99.42


# Starting w/ Empty Dictionary 
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 1848
alien_1['x-pos'] = 22.9
alien_1['y-pos'] = -45.2

print(alien_1)

# Modifying Vals

alien_1['color'] = 'white'
print(alien_1)


# Deeper Example
alien_2 = {'x-positon': 0, 'y-position': 25,
            'speed': 'medium'}

print(f"OG Position: {alien_2['x-positon']}")

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else: 
    x_increment = 3

alien_2['x-positon'] += x_increment
print(f"New Position: {alien_2['x-positon']}")

# Removing Key-Value Pairs
alien_3 = {'color': 'indigo', 'points': 2_354_423}
print(f"\nAlien_3: {alien_3}")

del alien_3['points']
print(f"New Alien_3: {alien_3}")