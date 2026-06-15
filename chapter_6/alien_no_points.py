alien = {'color': 'green', 'points': 5}

#print(alien['speed']) # ERROR (KeyError)

speed = alien.get('speed', 'FAST')
print(speed)