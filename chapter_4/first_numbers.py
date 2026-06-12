for value in range(1, 5):  
    print(value) # Prints from 1-4

# Similar to for(int i = 0; i < 5; i++){}

print()
for value in range(1, 6):
    print(value) # Prints 1-5


print()
for value in range(6): 
    print(value) # Prints 0-5

# Using range() to make list

# uses list function & range function to create a list of nums from 1-10
numbers = list(range(1, 11))
print(numbers)