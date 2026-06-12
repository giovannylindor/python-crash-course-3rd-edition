bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # Prints list w/ square brackets 

# Accessing elements 
print(bicycles[0]) # Prints 1st element
print(bicycles[2].title()) # Prints 3rd element w/ .title method
print(bicycles[-1]) # Prints last element from the list
print(bicycles[-2]) # Prints second-to-last element from the list

message = f"My first Bike was a {bicycles[1].title()}."
print(message)