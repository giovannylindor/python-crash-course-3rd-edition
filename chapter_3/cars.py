cars = ['bmw', 'toyota', 'honda', 'audi']
cars.sort() 
print(cars) # Prints alphabetically sorted version of List

cars.sort(reverse=True) # Sorts in reverse-alphabetical order
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"List: {cars}")
print(f"List using the Sorted Function: {sorted(cars)}") # Temp sorts the list



new_cars = ['ferarri', 'mercedes-benz', 'dodge', 'jeep']
new_cars.reverse() # Reverses the list (Doesn't sort backwards!)
print(f"\n{new_cars}")


print(f"There are {len(cars)} elements in the \"cars\" list. \nThere are {len(new_cars)} elements in the \"new_cars\" list")
