motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

# Modifies Element 
motorcyles[0] = 'ducati'
print(motorcyles)

# Appends Element to the end
motorcyles.append('honda') # Adds element to the end of the list
print(motorcyles)

# Inserts Element at Position 
motorcyles.insert(2, 'toyota')
print(motorcyles)

# Delete Element at Position
del motorcyles[2]
print(motorcyles)

# Popped Element from List
popped_motorcycle = motorcyles.pop(-1)
print(popped_motorcycle)


# Delete by Value
motorcyles.remove('suzuki')
print(motorcyles)