# Defining a Tuple

dimensions = (200, 50)

# Accessing Elements
print(dimensions[1])
print(dimensions[0])

# ERROR -> dimensions[0] = 100 
print(dimensions[0])

# Looping through Tuple
for dimension in dimensions:
    print(dimension)
