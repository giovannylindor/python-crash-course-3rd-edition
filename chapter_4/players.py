players = ['kobe', 'lebron', 'jordan', "o'neal"]

# Slicing
print(players[0:2]) # Grabs elements from 0-1 (2 elements)
print(players[1:3]) # Grabs elements from 1-2 (2 elements)

print(players[:2]) # Grabs elements from the beginning to 1 (2 elements)
print(players[-3:]) # Grabs from the 3rd-to-last to the end of the list (Last 3 elements)

# Looping through a slice
cars = ['Hellcat SRT', 
        'TrackHawk', 
        'Corvette C8', 
        'Maybach S-Class', 
        'GNX',
        "87 Monte Carlo SS"]

print("\n\nMy favorite cars are: ")

for car in cars:
    print(car)

print("\nBut if I had to limit it, I'd go for:")

for car in cars[1:5]: # Loops through the 1-5 elements in the list
    print(car)
